
from bs4 import BeautifulSoup
from urllib.request import urlopen

def download():
    
    url = 'https://digital.ecai2020.eu/accepted-papers-main-conference/'
    
    response = urlopen(url)
    page_source = response.read()
    soup = BeautifulSoup(page_source, 'html.parser')
    sum = 0
    
    for link in soup.find_all('a'):
        pdf_link = link.get('href') # e.g. /papers/11_paper.pdf
        
        if(pdf_link == None):
            continue
        if(not pdf_link.startswith('/papers/')):
            continue
        
        pdf_link = f'http://ecai2020.eu{pdf_link}'
        sum += 1
        print(pdf_link)
        
        table_node = link.find_parent('td').find_parent('tr')
        tr_nodes = table_node.contents
        title = tr_nodes[1].string
        author = tr_nodes[2].string
        print(author)
        print(title)
        
download()