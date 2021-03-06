
import re

from bs4 import BeautifulSoup
from urllib.request import urlopen

from Downloader import process_publication, clean_text

YEARS = [13, 14, 15, 17, 18]  # retrieved by testing the URLs


def get_supported_aaai_years():
    return [f'20{year}' for year in YEARS]


def normalize_year(year):
    if(len(str(year)) == 4):
        year = year[-2:]

    if isinstance(year, int) or year.isdigit():
        return int(year)
    else:
        return None


def process_single_publication(year, link):

    year = normalize_year(year)

    if(not link.text == 'PDF'):
        return None

    pdf_link = link.get('href')
    # directly getting the PDF link
    pdf_link = pdf_link.replace('view', 'viewFile')

    if(pdf_link == None):
        return None

    table_node = link.find_parent('td').find_parent('tr').find_parent('table')
    # print(table_node)
    tr_nodes = table_node.find_all('tr')
    # print(tr_nodes)
    title = tr_nodes[0].find('a').string

    # filter out generic organization PDFs
    if(title in [f'HCOMP-{year} Organization', 'Sponsors', 'Preface']):
        return None

    authors = clean_text(tr_nodes[1].find('td').string)
    return process_publication(title, authors, year, pdf_link)


def aaai_iterator_process_all_publications():
    for year in get_supported_aaai_years():
        iterator = aaai_iterator_process_publications(year)
        for publication in iterator:
            yield publication


def aaai_iterator_process_publications(year):

    year = normalize_year(year)
    url = get_available_volumes_per_year()[year]

    print(f'Processing publications from: {url}')

    response = urlopen(url)
    page_source = response.read()
    soup = BeautifulSoup(page_source, 'html.parser')

    for link in soup.find_all('a'):

        publication = process_single_publication(year, link)

        if not publication == None:
            yield publication


def get_available_volumes_per_year():
    urls = dict()
    for year in YEARS:
        urls[year] = f'https://www.aaai.org/ocs/index.php/HCOMP/HCOMP{year}/schedConf/presentations'
    return urls


def get_year_from_url(url):
    match = re.search(r'HCOMP[0-9][0-9]', url)

    if match == None:
        return None

    string = match.group()
    year_string = string[-2:]  # last two chars

    if year_string.isdigit():
        return int(year_string)
    else:
        return None
