
from bs4 import BeautifulSoup
from urllib.request import urlopen

from Downloader import process_publication


def process_all_publications():

    url = 'https://digital.ecai2020.eu/accepted-papers-main-conference/'

    response = urlopen(url)
    page_source = response.read()
    soup = BeautifulSoup(page_source, 'html.parser')

    for link in soup.find_all('a'):
        process_single_publication(link)


def process_single_publication(link):

    pdf_link = link.get('href')  # e.g. /papers/11_paper.pdf

    if(pdf_link == None):
        return None
    if(not pdf_link.startswith('/papers/')):
        return None

    pdf_link = f'http://ecai2020.eu{pdf_link}'

    table_node = link.find_parent('td').find_parent('tr')
    tr_nodes = table_node.contents
    title = tr_nodes[1].string
    authors = tr_nodes[2].string

    return process_publication(title, authors, 2020, pdf_link)


def iterator_process_all_publications():

    link_tags = get_all_valid_link_tags()
    return ECAIPublicationIterator(link_tags)


def get_all_valid_link_tags():

    link_tags = []
    url = 'https://digital.ecai2020.eu/accepted-papers-main-conference/'

    response = urlopen(url)
    page_source = response.read()
    soup = BeautifulSoup(page_source, 'html.parser')

    for link in soup.find_all('a'):

        pdf_link = link.get('href')  # e.g. /papers/11_paper.pdf

        if(pdf_link == None):
            continue
        if(not pdf_link.startswith('/papers/')):
            continue

        link_tags.append(link)

    return link_tags


class ECAIPublicationIterator:
    def __init__(self, link_tags):
        self.data = link_tags
        self.max_length = len(self.data)
        self.count = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.count < self.max_length:
            self.count = self.count + 1
            return process_single_publication(self.data[self.count - 1])
        else:
            return None


if __name__ == '__main__':
    pass
