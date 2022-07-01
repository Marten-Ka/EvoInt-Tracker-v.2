
import re

from bs4 import BeautifulSoup
from urllib.request import urlopen

from Downloader import process_publication, clean_text

YEARS = [13, 14, 15, 17, 18]  # retrieved by testing the URLs
URLS = list(map(
    lambda year: f'https://www.aaai.org/ocs/index.php/HCOMP/HCOMP{year}/schedConf/presentations', YEARS))


def process_single_publication(year, link):

    if(not link.text == 'PDF'):
        return None

    pdf_link = link.get('href')

    if(pdf_link == None):
        return None

    if(link.text in [f'HCOMP-{year} Organization', 'Sponsors', 'Preface']):
        return None

    table_node = link.find_parent('td').find_parent('tr')
    print(table_node)
    tr_nodes = table_node.contents
    title = tr_nodes[0].find('a').string
    authors = clean_text(tr_nodes[1].find('td').string)

    return process_publication(title, authors, year, pdf_link)


def aaai_iterator_process_all_publications():

    link_tags = get_all_valid_link_tags()
    return AAAIPublicationIterator(link_tags)


def get_year_from_url(url):
    print(f'URL: {url}')
    return int(re.findall(r'HCOMP[0-9][0-9]', url))


def get_all_valid_link_tags():

    link_tags = []

    for url in URLS:
        response = urlopen(url)
        page_source = response.read()
        soup = BeautifulSoup(page_source, 'html.parser')

        for link in soup.find_all('a'):

            if(not link.text == 'PDF'):
                continue

            pdf_link = link.get('href')  # e.g. /papers/11_paper.pdf

            if(pdf_link == None):
                continue

            year = get_year_from_url(url)
            if(link.text in [f'HCOMP-{year} Organization', 'Sponsors', 'Preface']):
                continue

            link_tags.append(link)

    return link_tags


class AAAIPublicationIterator:
    def __init__(self, link_tags):
        self.data = link_tags
        self.max_length = len(self.data)
        self.count = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.count < self.max_length:
            publication = process_single_publication(self.data[self.count])
            self.count = self.count + 1
            return publication
        else:
            raise StopIteration
