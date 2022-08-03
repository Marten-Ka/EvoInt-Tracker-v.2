
import os
from pathlib import Path
from urllib.parse import urlparse, urljoin
from urllib.request import urlopen

from bs4 import BeautifulSoup
from Downloader import process_publication, clean_text, VIKUS_VIEWER_DATA_FULLTEXT_PDF_PATH

IJCAI_URL = "https://www.ijcai.org/past_proceedings/"


def get_supported_ijcai_years() -> list[str]:
    return ["2021", "2020", "2019", "2018", "2017", "2016", "2015", "2013", "2011", "2009", "2007", "2005", "2003", "1999", "1997", "1995", "1993"]


def ijcai_iterator_process_all_publications():
    for year in get_supported_ijcai_years():
        iterator = ijcai_iterator_process_publications_for_year(year)
        for publication in iterator:
            yield publication


def ijcai_iterator_process_publications_for_year(year):

    year = str(year)
    os.makedirs(VIKUS_VIEWER_DATA_FULLTEXT_PDF_PATH + year, exist_ok=True)

    volume_links = get_available_volumes_per_year()[year]
    visited_links = []

    for volume_link in volume_links:
        response = urlopen(volume_link)  # opens the URL
        page_source = response.read()
        soup = BeautifulSoup(page_source, 'html.parser')
        print(f'[{year}] - Processing publications from: {volume_link}')

        for link in soup.find_all('a'):
            current_link = link.get('href')

            if volume_link not in current_link:
                current_link = urljoin(volume_link, current_link)
            if current_link.endswith('.pdf') and current_link not in visited_links:
                visited_links.append(
                    urljoin(volume_link, current_link))

                if not urlparse(current_link).scheme:
                    current_link = 'https://' + current_link

                #
                # This listed publication contains an
                # a-Tag with the wrong link to the PDF.
                #
                if current_link == 'https://www.ijcai.org/proceedings/Papers/IJCAI07-107.pdf':
                    current_link = 'https://www.ijcai.org/Proceedings/09/Papers/107.pdf'

                title = clean_text(link.text)
                if title == "here" or current_link == f'https://www.ijcai.org/proceedings/{year}/preface.pdf':
                    continue

                valid_publication, title, authors = get_pdf_information(
                    int(year), link, title)

                if valid_publication:
                    yield process_publication(title, authors, year, current_link)

#
# Parses every available year in the given URL.
# Returns a sorted set (starting with "newest" year)
#


def get_available_volumes():

    result = set()

    response = urlopen(IJCAI_URL)
    page_source = response.read()
    soup = BeautifulSoup(page_source, 'html.parser')
    content = soup.find('div', 'content')

    for link in content.find_all('a'):
        current_link = link.get('href')
        if current_link.split("/")[-1] == "2017":
            current_link = current_link + "/"

        #
        # Ignore the year 2001, because the site
        # does not provide any information?
        # Visit: https://www.ijcai.org/proceedings/2001-1
        #   and: https://www.ijcai.org/proceedings/2001-2
        #
        if current_link.split("/")[-1] == "2001-1" or current_link.split("/")[-1] == "2001-2":
            continue
        if is_link_to_volume(current_link):
            if current_link not in result:
                result.add(current_link)

    return sorted(result, reverse=True)


def get_available_volumes_per_year():

    result = dict()

    response = urlopen(IJCAI_URL)
    page_source = response.read()
    soup = BeautifulSoup(page_source, 'html.parser')
    content = soup.find('div', 'content')

    for link in content.find_all('a'):
        current_link = link.get('href')
        if current_link.split("/")[-1] == "2017":
            current_link = current_link + "/"

        #
        # Ignore the year 2001, because the site
        # does not provide any information?
        # Visit: https://www.ijcai.org/proceedings/2001-1
        #   and: https://www.ijcai.org/proceedings/2001-2
        #
        if current_link.split("/")[-1] == "2001-1" or current_link.split("/")[-1] == "2001-2":
            continue
        if is_link_to_volume(current_link):
            if current_link not in result:
                year = volume_link_to_year(current_link)
                if year in result.keys():
                    result[year].append(current_link)
                else:
                    result[year] = [current_link]

    return result


def is_link_to_volume(link: str) -> bool:
    year = link.split("/")[-1]
    if not year:
        year = link.split("/")[-2]
    return year[:4].isdigit()


def volume_link_to_year(volume_link):
    year = volume_link.split("/")[-1][:4]  # example: 2021
    if not year:
        year = volume_link.split("/")[-2][:4]
    return year


def get_pdf_information(year, link_tag, origin_title):

    try:

        paper_wrapper = None
        title = None
        authors = ''

        if year >= 2015:

            if origin_title != 'PDF':
                return False, origin_title, []

        else:

            if origin_title == "Abstract":
                return False, origin_title, []

        if year >= 2017:
            paper_wrapper = link_tag.find_parent("div", "paper_wrapper")
        else:
            paper_wrapper = link_tag.find_parent("p")

        if year >= 2017:

            title = paper_wrapper.find("div", "title")
            title = clean_text(title.text)
            authors = paper_wrapper.find("div", "authors").text

        elif year == 2016 or year == 2015:

            title = paper_wrapper.text.split(
                "\n")[0]  # example: Preface / xxxiii
            title = title.rsplit(' / ', 1)[0]  # example: Preface
            title = clean_text(title)

            author_container = None

            if year == 2016:
                author_container = paper_wrapper.find("i")
            elif year == 2015:
                author_container = paper_wrapper.find("em")

            authors = author_container.text

        elif year == 2013 or year == 2011 or year == 2009 or year == 2007:

            #
            # Some headlines contain a-Tags.
            # We need to ignore those.
            #
            if paper_wrapper == None:
                return False, origin_title, []

            a_tags = paper_wrapper.find_all('a')

            if len(a_tags) >= 2:

                abstract_a_tag = None
                title_a_tag = None

                if year == 2013 or year == 2011:
                    abstract_a_tag = a_tags[1]
                    title_a_tag = a_tags[0]
                elif year == 2009 or year == 2007:
                    abstract_a_tag = a_tags[0]
                    title_a_tag = a_tags[1]

                #
                # If the wrapper has a link to an abstract
                # we assume it is a publication.
                #
                if "Abstract" in abstract_a_tag.text:

                    title = clean_text(title_a_tag.text)
                    authors = paper_wrapper.find("i").text

        elif year == 2005:

            title = clean_text(link_tag.text)

            title_wrapper = link_tag.find_parent('p', class_='doctitle')
            author_wrapper = title_wrapper.find_next_sibling()
            authors = author_wrapper.text

        elif year == 2003:

            title = clean_text(link_tag.text)

            title_wrapper = link_tag.find_parent('p')
            author_wrapper = title_wrapper.find_next_sibling()

            if author_wrapper == None:
                return False, title, []
            authors = author_wrapper.text

        elif year == 1999 or year == 1997 or year == 1995:

            #
            # The year 1999 has two seperate sites:
            # https://www.ijcai.org/proceedings/1999-1 and
            # https://www.ijcai.org/proceedings/1999-2
            #
            # They both are not exactly structured the same.
            # The first site has a b-Tag around the text, whereas
            # the second site not.
            # Therefore we need to make a few checks.
            #

            title = clean_text(link_tag.text)

            link_parent = link_tag.find_parent('b')
            title_wrapper = None

            if link_parent == None:
                title_wrapper = link_tag.find_parent('p')
            else:

                #
                # Some publications have a b-Tag as a
                # "grandparent". We need to check if one
                # child has a a-Tag.
                #

                if len(link_parent.contents) >= 1:
                    title_wrapper = link_tag.find_parent('p')
                else:
                    title_wrapper = link_parent.find_parent('p')

            author_wrapper = title_wrapper.find_next_sibling()

            if author_wrapper == None:
                return False, title, []

            b_author_tag = author_wrapper.find('b')

            if b_author_tag == None:
                authors = author_wrapper.text
            else:
                authors = b_author_tag.text

            #
            # The text inside the author wrapper
            # contains a digits and dots at the end.
            #
            authors = remove_dots_and_numbers_at_end(authors)

        elif year == 1993:

            title = clean_text(link_tag.text)

            #
            # This author tag is an a-Tag.
            # Therefore the program thinks it is a publication.
            #
            if(title == 'Henri Be ringer and Bruno de Backer.'):
                return False, title, []

            current_tag = link_tag.find_parent('p')

            #
            # This publication has a different layout:
            #
            # <p>
            #   <a href="https://www.ijcai.org/Proceedings/93-1/Papers/024.pdf">Situation Recognition: Representation and Algorithms</a>
            #   Christophe Dousson, Paul Gaborit and Malik Ghallab..166
            # </p>
            #
            if(title == 'Situation Recognition: Representation and Algorithms'):

                authors = clean_text(current_tag.text.replace(
                    'Situation Recognition: Representation and Algorithms', ''))
                authors = remove_dots_and_numbers_at_end(authors)

            else:

                #
                # Authors sometimes are seperated into two or more p-Tags
                # Example for a structure:
                #
                #   <p>
                #       <a href="...">TITLE</a>
                #   </p>
                #
                #   <p>AUTHOR1, AUTHOR2</p>
                #   <p>and AUTHOR3..52</p>
                #
                # We use the ".." plus a number (we don't know what the number is for)
                # to identify if it is still a p-Tag with author information
                # or whether it is the next section.
                #

                raw_authors = ''
                while(len(raw_authors) == 0 or not string_ends_with_dots_or_numbers(raw_authors)):

                    author_wrapper = current_tag.find_next_sibling()
                    current_tag = author_wrapper

                    author_text = clean_text(author_wrapper.text)
                    raw_authors += author_text
                    authors += remove_dots_and_numbers_at_end(
                        author_text) + ' '

        else:
            raise Exception(f'Year {year} not implemented!')

        valid_publication = True

        if title == None or authors == None:
            valid_publication = False

        return valid_publication, title, normalize_authors_string(authors)

    except Exception as e:
        print(f'Error while retrieving information: {e}')
        return False, title, authors


def authors_string_to_array(authors) -> list[str]:
    authors = clean_text(authors)

    #
    # We can't just replace the word 'and' with a comma,
    # because then names like 'Alexander' would be
    # changed to 'Alex,er'. We need to check if the
    # and is inside a name.
    #

    words = authors.split(' ')
    new_words = []

    for i in range(len(words)):

        if(words[i] == 'and' or words[i] == ',and' or words[i] == 'and,'):
            continue

        if((i + 1) < len(words) and words[i + 1].lower() == 'and'):
            word = words[i] + ',' if(words[i][-1] != ',') else words[i]
            new_words.append(word)
        else:
            new_words.append(words[i])

    return new_words


def normalize_authors_string(authors) -> str:
    return ' '.join(authors_string_to_array(authors))


def remove_dots_and_numbers_at_end(text) -> str:

    while(text[-1].isdigit() or text[-1] == '.' or text[-1] == ' '):
        text = text[0:-1]

    return text


def string_ends_with_dots_or_numbers(text) -> bool:
    text = text.strip()
    return text[-1].isdigit() or text[-1] == '.'
