"""README dosyasını yeni dosya değişikliği durumunda güncelleme

Author:
    Yunus Emre Ak
"""

import os
import re
from urllib.parse import quote

# TODO Git modülü ile branch'lara özgü otomatik README oluştur
# TODO Github dosyanda çalıştırdığında tüm git projelerini güncellesin
# TODO Dosyayı CLI parametresi olarak alsın (yoksa bulunduğu dizindeki klasörleri ele alsın)

############    private.cfg     ############
# # VsCode dosyaları
# .vscode
#
#############################################

# Yaplandırma dosyası
CONFIG_FILE = "readme.cfg"
CONFIG_DEFAULT = r"""[Config]

# Sıralı indeksleme
SORTED_INDEX = True
# Sadece bu veriyi barındıranları indeksleme (hepsi için boş bırakın)
INDEX_FILTER =
# İndekslemeye dosya uzantısını da ekleme
INDEX_WITH_EXT = True
# Gizli dosyaları atlama
SKIP_PRIVATE_FOLDER = True

[Private]
.git
res
images
.vscode
Windows10 Kaynakları
"""

# Gizli dizinlerin bilgileri
PRIVATES = []


def load_cfg():

    config_section = False
    private_section = False

    def remove_comments(line):
        return line[:line.find("#")]

    def parse_value(line):
        try:
            return line.split("=")[1].strip()
        except:
            return ''

    def find_section(line: str) -> bool:
        """Başlık alanı bulucu

        Arguments:
            line {str} -- Dosya satırı

        Returns:
            bool -- Başlık alanı ise True
        """
        nonlocal config_section, private_section
        if '[Config]' in line:
            config_section = True
            private_section = False
            return True
        elif '[Private]' in line:
            config_section = False
            private_section = True
            return True
        else:
            return False

    def reg_configs(line):
        if config_section:
            # Değeri oluşturma
            value = parse_value(line)
            global SORTED_INDEX, INDEX_FILTER, INDEX_WITH_EXT, SKIP_PRIVATE_FOLDER
            if 'SORTED_INDEX' in line:
                SORTED_INDEX = value == 'True'
            elif 'INDEX_FILTER' in line:
                INDEX_FILTER = value
            elif 'INDEX_WITH_EXT' in line:
                INDEX_WITH_EXT = value == 'True'

            elif 'SKIP_PRIVATE_FOLDER' in line:
                SKIP_PRIVATE_FOLDER = value == 'True'

    def reg_privates(line):
        if private_section:
            global PRIVATES
            PRIVATES.append(line)

    def read_file():
        with open(CONFIG_FILE, 'r') as file:
            for line in file:
                line = remove_comments(line)

                if not find_section(line):
                    reg_configs(line)
                    reg_privates(line)

    def create_file():
        with open(CONFIG_FILE, "w") as file:
            file.write(CONFIG_DEFAULT)

    try:
        read_file()
    except FileNotFoundError:
        create_file()


def check_dir_if_wanted(dir_name: str) -> bool:
    """Aranan dizin mi kontrolü

    Arguments:
        dir_name {str} -- Dizin ismi

    Returns:
        bool -- Aranan dizinse true
    """

    def isPrivate(dir_name) -> bool:
        global PRIVATES
        for folder_name in PRIVATES:
            if dir_name == folder_name:
                return True

    return not any([
        SKIP_PRIVATE_FOLDER and isPrivate(dir_name),
        not os.path.isdir(dir_name)
    ])


def list_files(path):
    list = [i for i in os.listdir(path) if os.path.isfile("/".join([path, i]))]

    if SORTED_INDEX:
        list.sort()

    return list


def list_wanted_dir():
    list = [i for i in os.listdir() if check_dir_if_wanted(i)]

    if SORTED_INDEX:
        list.sort()

    return list


def insert_indexes(dir_names):

    def create_header(dir_name):
        return r"## " + dir_name + "\n\n"

    def create_link(dir_name, filename):
        return "- [" + filename.split(".")[0] + "](" + quote(f"{dir_name}/{filename}") + ")\n"

    def create_indexes(dir_names):
        str = ""

        for dir_name in dir_names:
            # Başlık oluşturma
            str += create_header(dir_name)

            # Dizindeki dosya isimlerini alma ve sıralama
            filenames = list_files(dir_name)

            # Verileri sıralama ve işleme
            for filename in filenames:
                # Markdown dosyası ise bağlantı oluşturma
                if INDEX_FILTER in filename:
                    filename, ext = os.path.splitext(filename)
                    str += create_link(
                        dir_name, filename + (ext if INDEX_WITH_EXT else '')
                    )

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
    load_cfg()
    update()
