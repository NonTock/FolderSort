from pathlib import Path
from colorama import Fore, Style, init
from time import sleep

init(autoreset=True)

sort_checker = {
    "Images": [".jpg", ".jpeg", ".png", ".gif"],
    "Documents": [".pdf", ".doc", ".docx", ".odt", ".txt", ".xlsx"],
    "Videos": [".mp4", ".avi", ".mkv"],
    "Archives": [".zip", ".rar", ".tar.gz", ".7z", ".tar.xz"],
    "Executables": [".exe", ".msi", ".dmg"],
    "Others": [],
}
def start():
    print("Это сортировщик файлов в папке")
    sleep(1)
    print("Не сортируй системные файлы, это может вызвать ошибки")
    print("Отправь ссылку на сортируемую папку в формате: 'C:/users/userName/Downloads'")
    uri = input("URI: ")
    while Path(uri).exists() == False:
        print("Не корректная ссылка")
        uri = input("URI: ")
start()