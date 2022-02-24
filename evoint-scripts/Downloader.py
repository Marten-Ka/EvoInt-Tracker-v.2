from Publication import publications, Publication, get_keywords_from_csv
from Vikus_writer import create_data_csv, read_data_csv
from Year import years, Year
from urllib.request import urlopen
import urllib.parse
from urllib.parse import urlparse
import os
from bs4 import BeautifulSoup
from pathlib import Path

from pdf2image import convert_from_path
from urllib.error import HTTPError
import sys


def parse_title(title):
    title = title.replace('\n', ' ')
    title = title.replace('\t', ' ')
    title = title.replace('  ', ' ')
    title = title.strip()
    return title


def next_pub_id():
    ids = [int(pub_id) for pub_id in publications.keys()]
    ids.sort()
    result = str(ids[-1] + 1) if len(ids) > 0 else '0'
    return result.zfill(4)


def download(pubs=None):
    if pubs is None:
        pubs = publications
    total = len(pubs.values())
    for key, pub in pubs.items():
        # check if file is already downloaded
        if Path(pub.path_to_pdf).is_file():
            continue
        try:
            print(f'{str(round((float(key)/total) * 100, 2))}% ({key}/{total}) - Downloading Publication "{pub.title}" \n\tfrom {pub.origin_path}\n')
            response = urlopen(pub.origin_path)
            # TODO: path_to_pdf has to start at data/..., so add vikus-viewer/ here
            os.makedirs(pub.path_to_pdf[:-8], exist_ok=True)
            file = open(pub.path_to_pdf, 'wb')
            file.write(response.read())
            file.close()
        except HTTPError:
            print("error writing file: " + pub.origin_path)
            continue
        except TimeoutError:
            print("TimeoutError")
            continue


def is_link_to_volume(link: str):
    year = link.split("/")[-1]
    if not year:
        year = link.split("/")[-2]
    print(year)
    return year[:4].isdigit()


def get_available_volumes(index_page_url=None):
    result = set()
    if index_page_url is None:
        index_page_url = "https://www.ijcai.org/past_proceedings/"
    response = urlopen(index_page_url)
    page_source = response.read()
    soup = BeautifulSoup(page_source, 'html.parser')
    content = soup.find('div', 'content')
    for link in content.find_all('a'):
        current_link = link.get('href')
        if current_link.split("/")[-1] == "2017":
            current_link = current_link + "/"
        if is_link_to_volume(current_link):
            # if index_page_url not in current_link:
            #     current_link = urllib.parse.urljoin(index_page_url, current_link)
            if current_link not in result:
                result.add(current_link)
    return sorted(result, reverse=True)


def download_from_single_volume_years():

    base_pdf_path = '../vikus-viewer/data/fulltext/pdf/'
    base_url = "https://www.ijcai.org/past_proceedings/"

    available_volumes = get_available_volumes(base_url)
    print('\n'.join(available_volumes))

    for volume_link in available_volumes:
        year = volume_link.split("/")[-1][:4]
        if not year:
            year = volume_link.split("/")[-2][:4]
        Year(year)
        os.makedirs(base_pdf_path + year, exist_ok=True)

        visited_links = []
        # year_url = urllib.parse.urljoin(base_url, year)
        response = urlopen(volume_link)  # opens the URL
        page_source = response.read()
        soup = BeautifulSoup(page_source, 'html.parser')
        for link in soup.find_all('a'):
            current_link = link.get('href')
            if volume_link not in current_link:
                current_link = urllib.parse.urljoin(volume_link, current_link)
            if current_link.endswith('.pdf') and current_link not in visited_links:
                visited_links.append(urllib.parse.urljoin(volume_link, current_link))

                if not urlparse(current_link).scheme:
                    current_link = 'https://' + current_link

                pub_id = next_pub_id()
                title = parse_title(link.text)
                if title == "here":
                    continue

                authors = ""

                # TODO: Following lines in own Method. Check if link is actually a publication.
                if title == "PDF":  # TODO: missing for years 2015, 2016
                    if int(year) >= 2017:
                        paper_wrapper = link.find_parent("div", "paper_wrapper")
                        title = paper_wrapper.find("div", "title")
                        title = parse_title(title.text)
                        authors = paper_wrapper.find("div", "authors").text

                path_to_pdf = base_pdf_path + str(year) + '/' + str(pub_id) + '.pdf'
                print(f'{year}:')
                print(f'Creating Publication_Object "{title}"')
                publication = Publication(pub_id=pub_id,
                                          title=title,
                                          authors=authors,
                                          year=year,
                                          origin_path=current_link,
                                          path_to_pdf=path_to_pdf)

                download(publication)

                # TODO: new Method 'add_to_data_csv(publication)'
                create_data_csv(publications)


# TODO: actually use var output_path on save
def pdf_to_thumbnail(dct):
    for publication in dct.values():
        path = Path(publication.path_to_pdf)
        output_path = Path('data/thumbnails/' + str(publication.id) + '.png')
        if path.is_file() and not output_path.is_file():
            print(f'{publication.id} - Creating Thumbnail for Publication "{publication.title}"')
            page = convert_from_path(path, 200, first_page=1, last_page=1)
            page[0].save('data/thumbnails/' + str(publication.id) + '.png', 'PNG')


def create_vikus_textures_and_sprites():
    # for pub in publications.values():
    #     os.system(f'node ../vikus-viewer-script/bin/textures "data/thumbnails/{pub.id}.png" --output "../vikus-viewer/data/images"')
    # os.system("ulimit -n 16100; node ../vikus-viewer-script/bin/textures 'data/thumbnails/*.png' --output '../vikus-viewer/data/images'")
    os.system("vikus-viewer-script 'data/thumbnails/*.png' --output '../vikus-viewer/data/images' --spriteSize 90")


# download_from_single_volume_years()

read_data_csv()
# download()
# create_data_csv(publications)
# pdf_to_thumbnail(publications)
# create_vikus_textures_and_sprites()

# get_keywords_from_csv()
for publication in publications.values():
    print(publication.id)
    fulltext = publication.fulltext()
    publication.set_keywords(fulltext)
create_data_csv(publications)
