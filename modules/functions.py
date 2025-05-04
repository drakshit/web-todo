import csv
import webbrowser
import shutil
from zipfile import ZipFile

SEARCH_URL = "https://www.google.com/search?q="
READ_MODE = "r"
WRITE_MODE = "w"

def file_operation(mode, write_todo=None, filename='todos.txt', r_w_option='line'):
    """ Read and Write to-do items from the todos file.
    The default file is todos.txt, but it can be anything else.
    Read / Write operation depends on mods passes while calling the function."""
    match mode.upper():
        case 'R':
            with open(filename, READ_MODE) as _file:
                if r_w_option == 'line':
                    content = _file.readlines()
                else:
                    content = _file.read()
                return content
        case 'W':
            with open(filename, WRITE_MODE) as _file:
                if r_w_option == 'line':
                    _file.writelines(write_todo)
                else:
                    _file.write(write_todo)
                _file.close()
        case _:
            pass

def read_weather(file_path):
    with open(file_path) as file:
        file_data = list(csv.reader(file))
    return file_data

def get_or_open_web_search(search, content=[]):
    search_city_str = search['city'].strip()
    search_item = search['search_item'].strip()
    if len(content) > 0:
        for row in content[1:]:
            if row[0].lower() == search_city_str.lower():
                match search_item.lower():
                    case 'temperature':
                        return row[1]
                    case 'time':
                        return row[2]
        webbrowser.open(SEARCH_URL + search_city_str + '+' + search_item)
        return f"File doesn't contain {search_item} of city {search_city_str}"
    else:
        return "File is empty"

def create_zip(base_name = "files", file_format="zip", root_dir="files"):
    shutil.make_archive(base_name,file_format,root_dir)
    print(f"files.zip successfully created")

def extract_zip(source, destination):
    with ZipFile(source, 'r') as archive:
        archive.extractall(destination)
if __name__ == "__main__":
    print("Calling from functions.py!")
    extract_zip("../files.zip", "/Users/DRAKSHIT/WORK/Python/Udemy/mython-mega/todo_app/dist")