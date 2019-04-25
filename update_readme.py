"""README dosyasını yeni dosya değişikliği durumunda güncelleme

Returns:
    None -- [description]
Author:
    Yunus Emre Ak
"""

import os
import re
from urllib.parse import quote


# Sıralı indeksleme
SORTED_INDEX = True
# Sadece bu veriyi barındıranları indeksleme (hepsi için '')
INDEXED_FILE_EXT = ''

# Gizli dosyaları atlama
SKIP_PRIVATE_FOLDER = True
# Indexlenmeyecek dosya isimleri
PRIVATE_FOLDERS = ['.git', 'images', 'pdfs', '.vscode', 'Windows10 Kaynakları']


def check_dir_if_wanted(dir_name: str) -> bool:
    """Aranan dizin mi kontrolü

    Arguments:
        dir_name {str} -- Dizin ismi

    Returns:
        bool -- Aranan dizinse true
    """

    def isPrivate(dir_name) -> bool:
        for folder_name in PRIVATE_FOLDERS:
            if dir_name == folder_name:
                return True

    return not any([
        SKIP_PRIVATE_FOLDER and isPrivate(dir_name),
        not os.path.isdir(dir_name)
    ])


def list_wanted_dir():
    list = [i for i in os.listdir() if check_dir_if_wanted(i)]
    if SORTED_INDEX:
        list.sort()

    return list


def insert_indexes(dir_names):

    def create_header(dir_name):
        return r"## " + dir_name + "\n\n"

    def create_link(dir_name, filename):
        return "- [" + filename.split(".")[0] + \
            "](" + quote(f"{dir_name}/{filename}") + ")\n"

    def create_indexes(dir_names):
        str = ""

        for dir_name in dir_names:
            # Başlık oluşturma
            str += create_header(dir_name)

            # Dizindeki dosya isimlerini alma ve sıralama
            filenames = os.listdir(dir_name)
            filenames.sort()

            # Verileri sıralama ve işleme
            for filename in filenames:
                # Markdown dosyası ise bağlantı oluşturma
                if INDEXED_FILE_EXT in filename:
                    filename, _ = os.path.splitext(filename)
                    str += create_link(dir_name, filename + INDEXED_FILE_EXT)

            # Yeni alt başlık için boş satır oluşturma
            str += "\n"

        return str

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
                    file_str += create_indexes(dir_names)
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


def update() -> None:
    """README'de indeksleme oluşturucu
    README dosyasında `<!-- Index -->` adlı kısmın içerisine indekslemeyi iliştirir.
    """

    # Dizinleri sıralı olarak alma
    dir_names = list_wanted_dir()

    # İndeksleri dosya arasına yerleştirme
    insert_indexes(dir_names)

    print("Updated! ~YEmreAk")


if __name__ == "__main__":
    update()
