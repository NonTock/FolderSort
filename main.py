from pathlib import Path
from colorama import Fore, Style, init
from time import sleep

init(autoreset=True)

sort_checker = {
    "Images": [".jpg", ".jpeg", ".png", ".gif"],
    "Documents": [".pdf", ".doc", ".docx", ".odt", ".txt", ".xlsx"],
    "Videos": [".mp4", ".avi", ".mkv"],
    "Archives": [".zip", ".rar", ".tar.gz", ".7z", ".tar.xz", ".deb"],
    "Executables": [".exe", ".msi", ".dmg"],
    "Torrents": [".torrent"],
    "Programming": [".py"],
    "Others": [".a"],
}


def start():
    print("Это сортировщик файлов в папке")
    sleep(1)
    print("Не сортируй системные файлы, это может вызвать ошибки")
    print("Отправь путь на сортируемую папку в формате: 'C:/users/username/Downloads'")
    uri = input("Путь: ")
    while Path(uri).is_dir() == False:
        print("Не корректная ссылка")
        uri = input("Путь: ")
    sorted_list(uri)

def available_check(file):
    for value in sort_checker.values():
        if file in value:
            break
    else:
        sort_checker["Others"].append(file)


def sorted_list(uri):
    uri = Path(uri)
    files_uri = uri.iterdir()
    for file in files_uri:
        if file.is_file():
            available_check(file.suffix)
            for key in sort_checker:
                for value in sort_checker[key]:
                    if value == file.suffix:
                        flag = 1
                        print(f"{file.name} - {key}")
                        break
start()