from __future__ import print_function, unicode_literals
from InquirerPy import prompt
from InquirerPy.base.control import Choice
from InquirerPy.separator import Separator

import os
from pathlib import Path
from alive_progress import alive_bar

from Downloader import get_supported_years, get_years_with_downloaded_pdf_data
from Downloader_IJCAI import iterator_download_publications_for_year, get_available_volumes_per_year, get_supported_ijcai_years
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
                'Rebuild CSV file',
                Separator(),
                'Exit'
            ]
        }
    ]

    answers = prompt(questions)

    if answers['action'] == 'Start downloading':
        download()
    elif answers['action'] == 'Delete data':
        delete_options()
    elif answers['action'] == 'Exit':
        exit()


def delete_options():

    choices = []

    csv_file_option_name = 'CSV file'
    if not Path('../vikus-viewer/data/data.csv').exists():
        csv_file_option_name += ' (does not exist)'

    # TODO: disabled does not work
    choices.append({
        "name": csv_file_option_name,
        "value": 'CSV file',
        "disabled": not Path('../vikus-viewer/data/data.csv').exists()
    })

    choices.extend(["PDF files", "Thumbnails", "Sprites", Separator(), "Back"])

    questions = {
        'type': 'list',
        'name': 'action',
        'message': 'What data do you want to remove?',
        'choices': choices
    }
    answers = prompt(questions)

    if answers['action'] == 'CSV file':
        delete_csv_file()
    elif answers['action'] == 'PDF files':
        delete_year()
    elif answers['action'] == 'Thumbnails':
        pass
    elif answers['action'] == 'Sprites':
        pass
    elif answers['action'] == 'Back':
        main()


def delete_csv_file():

    print("If you delete the CSV file, the Vikus Viewer will not have any data.")
    print("Therefore no data can be displayed and you need to create a new CSV file.")
    answers = prompt({
        'type': 'confirm',
        'name': 'delete',
        'message': 'Do you really want to delete the CSV file?'
    })

    if answers['delete'] == True:
        if Path('../vikus-viewer/data/data.csv').exists():
            os.remove('../vikus-viewer/data/data.csv')
            print('Successfully deleted data.csv file!')
        else:
            print('No data.csv file was found!')


def delete_year():

    choices = []
    for _, (year, count) in enumerate(get_years_with_downloaded_pdf_data().items()):
        choices.append({
            "name": f'{year} ({count} PDFs)',
            "value": year
        })
    choices.extend([Separator(), 'Back'])

    questions = {
        'type': 'list',
        'name': 'year',
        'message': 'Which year data do you want to remove?',
        'choices': choices
    }

    answers = prompt(questions)

    if answers['year'] == 'Back':
        delete_options()


def download():
    answers = prompt({
        'type': 'list',
        'name': 'source',
        'message': 'Which data source?',
        'choices': [
            'IJCAI',
            'ECAI',
            Separator(),
            'Back'
        ]
    })

    if answers['source'] == 'Back':
        main()
        return

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
        'choices': get_supported_ijcai_years() + [Separator(), 'Back']
    })
    return answers['year']


def create_year_choices():
    choices = []
    for year in get_supported_ijcai_years():
        choices.append(year)
    return choices


if __name__ == '__main__':
    main()
