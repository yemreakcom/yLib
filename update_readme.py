"""README dosyasını yeni dosya değişikliği durumunda güncelleme

Returns:
    None -- [description]
"""

import os
import re
from urllib.parse import quote

# Indexlenmeyecek dosya isimleri
PRIVATE_FOLDERS = ['.git', 'images', 'pdfs', '.vscode', 'Windows10 Kaynakları']


def isPrivate(dir_name) -> bool:
    for folder_name in PRIVATE_FOLDERS:
        if dir_name == folder_name:
            return True
    return False


def print_dirs_contents(dir_names):
    str = ""

    for dir_name in dir_names:
        if not isPrivate(dir_name) and os.path.isdir(dir_name):
            # Başlık oluşturma
            str += r"## " + dir_name + "\n\n"

            for file_name in os.listdir(dir_name):
                # Markdown dosyası ise bağlantı oluşturma
                if '.md' in file_name:
                    str += "- [" + file_name.split(".")[0] + \
                        "](" + quote(f"{dir_name}/{file_name}") + ")\n"
            str += "\n"
    return str


def update() -> None:
    """README'de indeksleme oluşturucu
    README dosyasında `<!-- Index -->` adlı kısmın içerisine indekslemeyi iliştirir.
    """

    dir_names = os.listdir()

    # Dizinleri sıralayıp işleme (her defasında aynı gelsin)
    dir_names.sort()
    file_str = print_dirs_contents(dir_names)

    # README'yi okuma
    file_str = ""
    save_to_file = True
    with open("README.md", "r", encoding="utf-8") as file:
        for line in file:
            if "<!-- Index -->" in line:
                if save_to_file:
                    # Yeni index satırına kadar dosyaya kaydetmeyi devre dışı bırakma
                    save_to_file = False

                    # Dosyaların indekslerini oluşturup ekleme
                    file_str += "<!-- Index -->" + "\n\n"
                    file_str += print_dirs_contents(dir_names)
                else:
                    # İkinci index için okuma modunu aktif etme
                    save_to_file = True

                    # Indeks satırını ekleme
                    file_str += "<!-- Index -->" + "\n"
            else:
                # Okuma izni varsa dosyayı değişkene aktarma
                if save_to_file:
                    file_str += line

    # Yeni metni dosyaya yazma
    with open("README.md", "w", encoding="utf-8") as file:
        file.writelines(file_str)

    print("Updated! ~YEmreAk")


if __name__ == "__main__":
    update()
