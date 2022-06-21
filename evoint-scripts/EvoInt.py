from __future__ import print_function, unicode_literals
from PyInquirer import prompt, print_json, Separator

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
                'Exit'
            ]
        }
    ]

    answers = prompt(questions, style=custom_style_2)

    if answers['action'] == 'Start downloading':
        download()
    elif answers['action'] == 'Delete data':
        pass
    elif answers['action'] == 'Exit':
        exit()


def download():
    answers = prompt({
        'type': 'list',
        'name': 'source',
        'message': 'Which data source?',
        'choices': [
            'IJCAI',
            'ECAI',
            Separator(),
            'Back',
            'Exit'
        ]
    }, style=custom_style_2)

    if answers['source'] == 'Back':
        main()
        return
    elif answers['source'] == 'Exit':
        exit()

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
