from __future__ import print_function, unicode_literals
from PyInquirer import prompt, Separator

from alive_progress import alive_bar

from examples import custom_style_2

from Downloader_IJCAI import iterator_download_publications_for_year, get_available_volumes_per_year, get_supported_years
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

    if answers['source'] == 'IJCAI':

        yearAnswer = askIJCAIYear()

        if yearAnswer == 'Back':
            download()
        else:
            iterator = iterator_download_publications_for_year(yearAnswer)
            with alive_bar(dual_line=True, title='Processing data from IJCAI') as bar:
                for publication in iterator:
                    bar.text(f'Processing publication: {publication.title}')
                    bar()
                bar.title('Processed data from IJCAI')

    elif answers['source'] == 'ECAI':
        iterator = iterator_process_all_publications()

        with alive_bar(iterator.max_length, dual_line=True, title='Processing data from ECAI') as bar:
            for publication in iterator:
                bar.text(f'Processing publication: {publication.title}')
                bar()
            bar.title('Processed data from ECAI')

    download()


def askIJCAIYear():
    answers = prompt({
        'type': 'list',
        'name': 'year',
        'message': 'Select a year you want to download:',
        'choices': get_supported_years() + [Separator(), 'Back']
    }, style=custom_style_2)
    return answers['year']


def create_year_choices():
    choices = []
    for year in get_supported_years():
        choices.append(year)
    return choices


if __name__ == '__main__':
    main()
