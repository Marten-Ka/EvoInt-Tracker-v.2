# /usr/bin/python3

import os
import csv
import pandas as pd
from pathlib import Path

from Publication import publications, Publication

csv.field_size_limit(10000000)

csv_file = None
csv_file_reader = None
csv_dataframe = None

CSV_PATH = '../vikus-viewer/data/data.csv'


def get_csv_dataframe() -> pd.DataFrame:
    global csv_dataframe
    if csv_dataframe is None:
        try:
            csv_dataframe = pd.read_csv(get_data_csv_path())
        except:
            csv_dataframe = pd.DataFrame({'keywords': [], 'year': [], 'id': [], '_title': [], '_authors': [], '_abstract': [
            ], '_origin_path': [], '_display_path_to_pdf': [], '_path_to_pdf': [], '_fulltext': []})
    return csv_dataframe


def get_data_csv_path() -> str:

    create_csv_file()

    global CSV_PATH
    return CSV_PATH


def create_csv_file():
    global CSV_PATH
    if not Path(CSV_PATH).is_file():
        with open(CSV_PATH, 'w') as f:
            pass


def check_file_empty(path_of_file) -> bool:
    # Checking if file exist and it is empty
    return os.path.exists(path_of_file) and os.stat(path_of_file).st_size == 0


def check_file_exists_and_has_content(path_of_file) -> bool:
    return os.path.exists(path_of_file) and os.stat(path_of_file).st_size > 0


def filter_empty_pdf_files(paths) -> list[bool]:

    result = []
    for path in paths:
        result.append(check_file_exists_and_has_content(path))
    return result


def clean_data_csv():

    csv_file_path = get_data_csv_path()

    csv_file_size_before_filter = os.stat(csv_file_path).st_size
    df = pd.read_csv(csv_file_path, index_col=2)
    df = df[filter_empty_pdf_files(df._path_to_pdf)]
    df.to_csv(csv_file_path)

    remove_duplicate_entries_in_csv()

    csv_file_size_after_filter = os.stat(csv_file_path).st_size

    if csv_file_size_before_filter == csv_file_size_after_filter:
        print("There was nothing to clean in the data.csv-file.")
    elif csv_file_size_before_filter < csv_file_size_after_filter:
        print(
            f'Oops! The file is now {csv_file_size_after_filter - csv_file_size_before_filter} bytes bigger than before. Something went wrong!')
    else:
        print(
            f"The file is now {csv_file_size_before_filter - csv_file_size_after_filter} bytes smaller.")


def open_csv_file_reader():

    global csv_file
    global csv_file_reader

    if csv_file == None:
        csv_file = open(get_data_csv_path(), 'r', encoding="utf-8")
        csv_file_reader = csv.reader(csv_file)
    else:
        csv_file.seek(0, 0)  # reset read and write position


def close_csv_file_reader():
    global csv_file
    csv_file.close()


def get_csv_file_reader():
    global csv_file_reader
    open_csv_file_reader()
    return csv_file_reader


def write_data_csv_header(csv_writer):

    if check_file_empty(get_data_csv_path()):
        csv_writer.writerow(['keywords'] +
                            ['year'] +
                            ['id'] +
                            ['_title'] +
                            ['_authors'] +
                            ['_abstract'] +
                            ['_origin_path'] +
                            ['_display_path_to_pdf'] +
                            ['_path_to_pdf'] +
                            ['_fulltext'])


def write_data_csv_row(csv_writer, publication: Publication):

    if not csv_contains(publication.id):
        add_row_to_dataframe(publication)
        csv_writer.writerow(publication.to_csv_row())


def add_row_to_dataframe(publication: Publication):
    create_csv_file()
    global csv_dataframe
    csv_dataframe = pd.concat(
        [get_csv_dataframe(), publication.to_series().to_frame().T])


def csv_contains(id) -> bool:

    try:
        df = get_csv_dataframe()
        result = df[df['id'] == id]
        return not result.empty
    except:
        return False


# Returns how many rows were deleted
def remove_duplicate_entries_in_csv() -> int:

    try:
        df = pd.read_csv(get_data_csv_path())
        row_count = df.shape[0]
        df = df.drop_duplicates(subset=['id'])
        df.to_csv(get_data_csv_path(), index=False)
        return (row_count - df.shape[0])
    except Exception as e:
        print(e)


def add_to_data_csv(publication):

    with open(get_data_csv_path(), 'a+', newline='', encoding="utf-8") as csvfile:

        csv_writer = csv.writer(csvfile, delimiter=',',
                                quotechar='"', quoting=csv.QUOTE_MINIMAL)
        write_data_csv_header(csv_writer)

        write_data_csv_row(csv_writer, publication)


def create_data_csv():
    with open(get_data_csv_path(), 'w', newline='', encoding="utf-8") as csvfile:
        csv_writer = csv.writer(csvfile, delimiter=',',
                                quotechar='"', quoting=csv.QUOTE_MINIMAL)
        write_data_csv_header(csv_writer)

        for publication in list(publications):
            write_data_csv_row(csv_writer, publication)


if __name__ == "__main__":
    if False:
        try:
            df = pd.read_csv(get_data_csv_path())
            print(df.columns)
            row_count = df.shape[0]
            df = df.loc[:, df.dtypes == str]
            print(row_count, df.shape[0])
        except Exception as e:
            print("Error:", e)
