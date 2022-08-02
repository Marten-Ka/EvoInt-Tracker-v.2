
from bs4 import BeautifulSoup
from urllib.request import urlopen

from Downloader import process_publication

URLS = ['https://digital.ecai2020.eu/accepted-papers-main-conference/',
        'https://digital.ecai2020.eu/accepted-papers-pais/']


def ecai_iterator_process_all_publications():

    for url in URLS:

        print(f'[2020] - Processing publications from: {url}')

        response = urlopen(url)
        page_source = response.read()
        soup = BeautifulSoup(page_source, 'html.parser')

        link_tags = get_all_valid_link_tags(url)

        for link in link_tags:
            yield process_single_publication(link)


def process_all_publications():

    for url in URLS:

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


def get_all_valid_link_tags(url):

    link_tags = []

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
