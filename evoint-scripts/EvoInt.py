from __future__ import print_function, unicode_literals
from PyInquirer import prompt, print_json, Separator

import time
import progressbar
from alive_progress import alive_bar

from examples import custom_style_2

from Downloader_ECAI import iterator_process_all_publications

def main():
    
    questions = [
        {
            'type': 'list',
            'name': 'action',
            'message': 'What do you want to do?',
            'choices': [
                'Start downloading',
                'Delete data',
                Separator(),
            ]
        }
    ]

    answers = prompt(questions, style=custom_style_2)
    print(answers)
    
    if answers['action'] == 'Start downloading':
        download()
        
def download():
    answers = prompt({
        'type': 'list',
        'name': 'source',
        'message': 'Which data source?',
        'choices': [
            'IJCAI',
            'ECAI',
        ]        
    }, style=custom_style_2)
    
    iterator = None
    
    if answers['source'] == 'ECAI':
        iterator = iterator_process_all_publications()
    
    publication = next(iterator)
        
    with alive_bar(iterator.max_length, dual_line=True, title='Processing data from ECAI', ctrl_c=True) as bar:
        for publication in iterator:
            bar.text(f'Processing publication: {publication.title}')
            bar()
        bar.title('Processed data from ECAI')

if __name__ == '__main__':
    main()