from pathlib import Path
from colorama import Fore, Style, init
from time import sleep

init(autoreset=True)

sys_msg = Fore.CYAN+Style.BRIGHT
gr_msg = Fore.YELLOW+Style.BRIGHT
suc_msg = Fore.LIGHTGREEN_EX+Style.BRIGHT
bd_msg = Fore.LIGHTRED_EX+Style.BRIGHT
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
    print(sys_msg + "Это сортировщик файлов в папке")
    sleep(1)
    print(bd_msg +"Не сортируй системные файлы, это может вызвать ошибки")
    sleep(1)
    print(sys_msg +"Хотите отсортировать файлы?")
    if choose():
        take_uri()

def choose():
    print(Style.BRIGHT + "1 - Да")
    print(Style.BRIGHT + "2 - Нет")
    chosen = input("Введите цифру: ")
    while chosen != "1" and chosen != "2":
        chosen = input("Введите корректную цифру: ")
    if chosen == "1":
        return True
    else:
        input("Нажмите Enter чтобы выйти")

def take_uri():
    print(sys_msg + "Отправь путь на сортируемую папку в формате: 'C:/users/username/Downloads'")
    uri = input("Путь: ")
    while Path(uri).is_dir() == False:
        print(bd_msg + "Не корректная ссылка")
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
                flag = 0
                for value in sort_checker[key]:
                    if value == file.suffix:
                        print(gr_msg + f"{file.name} - {key}")
                        flag = 1
                        sleep(0.2)
                        break
                    if flag != 0:
                        break
    print(sys_msg + "Начать сортировку?")
    if choose():
        file_sort(uri)

def file_sort(uri):
    dir_count = 0
    file_count = 0
    for file in uri.iterdir():
        for key in sort_checker:
            for value in sort_checker[key]:
                if file.suffix == value:
                    old_file = uri / file.name
                    new_dir = uri / key
                    new_file = new_dir / file.name
                    if new_dir.exists() == False:
                        print(bd_msg + f"Директории {key} не существует")
                        sleep(0.2)
                        print(suc_msg + "Создание директории")
                        sleep(0.2)
                        new_dir.mkdir()
                        dir_count += 1

                    while new_file.exists():
                        print(bd_msg + f"Файл {file.name} уже существует в директории {key}")
                        sleep(0.4)
                        print(sys_msg + f"Не забывайте про суффикс. Пример: 'Букварь.txt'")
                        new_file_name = input("Введите новое имя файла: ")
                        new_file = new_dir / new_file_name
                    old_file.rename(new_file)
                    print(suc_msg + f"{new_file.name} успешно перемещен")
                    sleep(0.2)
                    file_count += 1
    print(sys_msg + f"Успешно создано {dir_count} директорий")
    print(sys_msg + f"Успешно отсортировано {file_count} файлов")
    print("Желаете ещё раз ")
    if choose():
        take_uri()
start()