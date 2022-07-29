from __future__ import print_function, unicode_literals
from InquirerPy import prompt
from InquirerPy.base.control import Choice
from InquirerPy.separator import Separator

import os
from pathlib import Path
from alive_progress import alive_bar

from Downloader import delete_year as downloader_remove_year, delete_all_thumbnails, get_thumbnail_count, get_years_with_downloaded_pdf_data
from Downloader_IJCAI import iterator_download_publications_for_year, iterator_download_all_publications, get_supported_ijcai_years
from Downloader_ECAI import ecai_iterator_process_all_publications
from Downloader_AAAI import aaai_iterator_process_publications, get_supported_aaai_years
from VikusWriter import clean_data_csv


def main():

    questions = [
        {
            'type': 'list',
            'name': 'action',
            'message': 'What do you want to do?',
            'choices': [
                'Start downloading',
                'Delete data',
                'Clean CSV file',
                Separator(),
                'Exit'
            ]
        }
    ]

    answers = prompt(questions)

    if answers['action'] == 'Start downloading':
        prompt_download()
    elif answers['action'] == 'Delete data':
        prompt_delete_options()
    elif answers['action'] == 'Clean CSV file':
        prompt_clean_csv()
    elif answers['action'] == 'Exit':
        exit()


def prompt_clean_csv():
    print('This action will delete entries of publications, if the associated PDF file does not exist anymore.')
    answers = prompt({
        'type': 'confirm',
        'name': 'clean',
        'message': f'Do you really want to clean the data.csv-file?'
    })
    if answers['clean'] == True:
        clean_data_csv()


def prompt_delete_options():

    choices = []

    csv_file_option_name = 'CSV file'
    if not Path('../vikus-viewer/data/data.csv').exists():
        csv_file_option_name += ' (does not exist)'

    # TODO: disabled does not work

    choices.append(Choice('CSV file', csv_file_option_name,
                   Path('../vikus-viewer/data/data.csv').exists()))

    choices.append(
        Choice('Thumbnails', f'Thumbnails ({get_thumbnail_count()}x)'))

    choices.extend(["PDF files", "Sprites", Separator(), "Back"])

    questions = {
        'type': 'list',
        'name': 'action',
        'message': 'What data do you want to remove?',
        'choices': choices
    }
    answers = prompt(questions)

    if answers['action'] == 'CSV file':
        if Path('../vikus-viewer/data/data.csv').exists():
            prompt_delete_csv_file()
        else:
            print("No data.csv file was found!")
            prompt_delete_options()
    elif answers['action'] == 'PDF files':
        prompt_delete_year()
    elif answers['action'] == 'Thumbnails':
        prompt_delete_thumbnails()
    elif answers['action'] == 'Sprites':
        pass
    elif answers['action'] == 'Back':
        main()


def prompt_delete_thumbnails():

    thumbnail_count = get_thumbnail_count()

    if thumbnail_count > 0:
        answers = prompt({
            'type': 'confirm',
            'name': 'delete',
            'message': f'Do you really want to delete {get_thumbnail_count()} thumbnails?'
        })

        if answers['delete'] == True:
            delete_all_thumbnails()
    else:
        print('No thumbnails found!')

    prompt_delete_options()


def prompt_delete_csv_file():

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

    prompt_delete_options()


def prompt_delete_year():

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
    year = answers['year']

    if year == 'Back':
        prompt_delete_options()
        return

    pdf_count = get_years_with_downloaded_pdf_data()[year]

    confirm = prompt({
        'type': 'confirm',
        'name': 'delete',
        'message': f'Do you really want to delete {pdf_count} PDF files of year {year}?'
    })

    if confirm['delete'] == True:
        downloader_remove_year(year)
        print(
            f'Successfully deleted {pdf_count} PDFs from year {year}!')

    prompt_delete_options()


def prompt_download():
    answers = prompt({
        'type': 'list',
        'name': 'source',
        'message': 'Which data source?',
        'choices': [
            'IJCAI',
            'ECAI',
            'AAAI',
            Separator(),
            'Back'
        ]
    })

    source = answers['source']
    if source == 'Back':
        main()
        return

    iterator = None
    max_iterations = None

    if source == 'IJCAI':

        year_answer = prompt_year(get_supported_ijcai_years())

        if year_answer == 'Back':
            prompt_download()
            return
        else:

            if year_answer == 'All':
                iterator = iterator_download_all_publications()
            else:
                iterator = iterator_download_publications_for_year(year_answer)

    elif source == 'ECAI':
        iterator = ecai_iterator_process_all_publications()
        max_iterations = iterator.max_length

    elif source == 'AAAI':
        year_answer = prompt_year(get_supported_aaai_years())

        if year_answer == 'Back':
            prompt_download()
            return
        else:
            iterator = aaai_iterator_process_publications(year_answer)

    with alive_bar(total=max_iterations, dual_line=True, title=f'Processing data from {source}') as bar:
        for publication in iterator:
            bar.text(
                f'Processing publication: {publication.title}')
            bar()
        bar.title(f'Processed data from {source}')

    prompt_download()


def prompt_year(years):
    answers = prompt({
        'type': 'list',
        'name': 'year',
        'message': 'Select a year you want to download:',
        'choices': years + ['All', Separator(), 'Back']
    })
    return answers['year']


def create_year_choices():
    choices = []
    for year in get_supported_ijcai_years():
        choices.append(year)
    return choices


if __name__ == '__main__':
    main()
