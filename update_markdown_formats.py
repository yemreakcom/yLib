"""Markdown link ve buton düzenleyici
Markdowndaki static bağlantıları dinamik bağlantıya, 
butonlar için yapılmış code formatını kbd'ye çeviri
"""

import os
from urllib.parse import quote

# TODO
# CTRL
# <kbd>CTRL</kbd>
# Ve tüm harfler `T` gibi
button_names = ['CTRL', 'TAB', 'ALT', 'SHIFT',
                'WİNDOWS TUŞU (SUPER)', 'SUPER', 'ENTER', 'F!', 'F2', 'F3', 'F4', 'F5', 'F6']
# [name](link) Belki atlarız
links = []


def fix_file(file_path):

    def fix_line(line):
        # TODO Buton var mı kontrol edilecek
        return line

    with open(file_path, 'r', encoding='utf-8') as file:
        lines = []
        for line in file:
            line = fix_line(line)
            lines.append(line)

    with open(file_path, 'w', encoding='utf-8') as file:
        file.writelines(lines)


def generate_file_path(pattern):
    dir_paths = os.listdir()
    for dir_path in dir_paths:
        if os.path.isdir(dir_path):
            file_paths = os.listdir(dir_path)
            for file_path in file_paths:
                if pattern in file_path:
                    yield f'{dir_path}/{file_path}'


def main():
    exit()
    for file_path in generate_file_path('md'):
        fix_file(file_path)
        break


main()
