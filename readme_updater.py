"""Readme dosyasına indeksleri ekleme

TODO: ToC oluştur
TODO: Header'lar için dinamik link oluştur [Baslik]: #baslik
TODO: Belki vscode eklentisi yapabilirsin
"""

import os
from enum import Enum, unique
from urllib.parse import quote

# Yapılandırma dosyası ayarları
CONFIG_FILE = "readme.cfg"
COMMENT_DELIM = "#"
VARIABLE_DELIM = "="
CONFIG_HEADER = "[Config]"
PRIVATE_HEADER = "[Private]"
WHITESPACES = {"\n", " "}


# Program aylarındaki indeks bilgileri
class Option():
    def __init__(self, value, description):
        self.value = value
        self.description = description


# Program ayarları
OPTIONS = {
    "SORTED_INDEX": Option(
        True,
        "Sıralı indeksleme"
    ),
    "INDEX_FILTER": Option(
        "",
        "Sadece bu veriyi barındıranları indeksleme (hepsi için boş bırakın)"
    ),
    "INDEX_WITH_EXT": Option(
        True,
        "İndekslemeye dosya uzantısını da ekleme"
    ),
    "SKIP_PRIVATE_FOLDER": Option(
        True,
        "Gizli dosyaları atlama"
    )
}

# Görmezden gelinen dosya veya dizinler ('set' olma sebebi tekrarlı verileri engellemektir)
PRIVATES = {".git", ".vscode"}


def load_cfg():

    def check_cfg():
        return CONFIG_FILE in os.listdir()

    def read_cfg():

        @unique
        class Sections(Enum):
            Config = 0
            Private = 1

        # İşlemler için belirleyici (flag)
        SECTION = Sections.Config

        def trim_line(line: str) -> str:
            """Satırdaki gereksiz karakterleri temizler

            Arguments:
                line {str} -- Satır

            Returns:
                str -- Temizlenmiş satır
            """

            def remove_comment(line: str) -> str:
                """Satırdaki yorumların kaldırılrması

                Arguments:
                    line {str} -- Satır

                Returns:
                    str -- Yorum alanları kaldırılmış satır
                """

                # Yorum satırının başlangıç indeksi
                index = line.find(COMMENT_DELIM)
                if index > -1:
                    return line[:index]
                return line

            def remove_whitespaces(line: str) -> str:
                """Satır sonu karakterini kaldırma

                Arguments:
                    line {str} -- Satır

                Returns:
                    str -- Satır sonu karakteri kaldırılmış satır
                """

                for whitespace in WHITESPACES:
                    line = line.replace(whitespace, "")
                return line

            line = remove_comment(line)
            line = remove_whitespaces(line)

            return line

        def update_section(line: str) -> bool:
            """Bölüm değişkenini günceller

            Arguments:
                line {str} -- Satır

            Returns:
                bool -- Güncelleme olduysa `True`
            """

            nonlocal SECTION
            if CONFIG_HEADER in line:
                SECTION = Sections.Config
                return True
            elif PRIVATE_HEADER in line:
                SECTION = Sections.Private
                return True

            # Güncelleme olmadığını belirtme
            return False

        def parse_line(line: str) -> tuple:
            """Satırdaki değişken ismini ve değerini ayrıştırma

            Arguments:
                line {str} -- Satır

            Returns:
                tuple -- Değşiken ismi, değeri
            """

            datas = line.split(VARIABLE_DELIM)
            return datas[0], datas[1]

        def reg_option(name, value):

            def cast_value(name, value):
                if type(OPTIONS[name].value) is not str:
                    return eval(value)
                return value

            if name in OPTIONS:
                OPTIONS[name].value = cast_value(name, value)

        def reg_privates(value):
            if value not in PRIVATES:
                PRIVATES.add(value)

        with open(CONFIG_FILE, "r") as file:
            for line in file:
                # Gereksiz karakterleri kaldırma
                line = trim_line(line)

                # Satırda veri kaldıysa işleme
                if len(line) > 0:
                    try:
                        # Veri bölümünü güncelleme, güncelleme varsa sonraki veriye geçme
                        if not update_section(line):
                            if SECTION is Sections.Config:
                                name, value = parse_line(line)
                                reg_option(name, value)
                            elif SECTION is Sections.Private:
                                reg_privates(line)
                    except:
                        continue

    def create_cfg():

        def create_header_filestr(string: str) -> str:
            return f"{string}\n\n"

        def get_config_filestr():

            def get_options_filestr() -> str:
                filestr = ""
                for option in OPTIONS:
                    filestr += f"# {OPTIONS[option].description}\n"
                    filestr += f"{option} = {OPTIONS[option].value}\n"
                filestr += "\n"
                return filestr

            filestr = create_header_filestr(CONFIG_HEADER)
            filestr += get_options_filestr()
            return filestr

        def get_privates_filestr():

            def get_privates_filestr():
                filestr = ""
                for private in PRIVATES:
                    filestr += f"{private}\n"
                filestr += "\n"
                return filestr

            filestr = create_header_filestr(PRIVATE_HEADER)
            filestr += get_privates_filestr()
            return filestr

        with open(CONFIG_FILE, "w") as file:
            file.write(get_config_filestr())
            file.write(get_privates_filestr())

    # TODO Dosya varsa okuma moduna al
    try:
        read_cfg()
    except:
        create_cfg()
        read_cfg()


def update():
    """README'de indeksleme oluşturucu
README dosyasında `<!-- Index -->` adlı kısmın içerisine indekslemeyi iliştirir.
"""

    load_cfg()


def insert_indexes():

    def is_private(filename):
        global PRIVATES
        for private in PRIVATES:
            if filename == private:
                return True
        return False

    def listfolderpaths(path: str = os.getcwd()) -> str:
        folderlist = []
        for name in os.listdir(path):
            pathname = os.path.join(path, name)
            if not is_private(name) and os.path.isdir(pathname):
                folderlist.append(pathname)
        return folderlist

    def listfilepaths(path: str = os.getcwd()) -> str:
        filelist = []
        for name in os.listdir(path):
            pathname = os.path.join(path, name)
            if not is_private(name) and os.path.isfile(pathname):
                filelist.append(pathname)
        return filelist

    def headerstr(folderpath: str, headerlvl: int, withext=True) -> str:
        header = ""
        for i in range(0, headerlvl):
            header += "#"

        foldername = os.path.basename(folderpath)
        header += f" {foldername}\n\n"

        return header

    def linkstr(folderpath: str):

        def barename(filepath: str):
            filename = os.path.basename(filepath)
            filename = remove_extension(filename)

            return filename

        def remove_extension(filepath: str) -> str:
            filepath, _ = os.path.splitext(filepath)
            return filepath

        def encoded_realtivepath(pathname: str) -> str:

            def modifypath(pathname: str):
                if not OPTIONS['INDEX_WITH_EXT'].value:
                    pathname = remove_extension(pathname)
                return pathname

            def relativepath(pathname: str):
                return pathname.replace(os.getcwd(), '.')

            def encodedpath(pathname: str):
                return quote(pathname)

            pathname = modifypath(pathname)
            pathname = relativepath(pathname)
            pathname = encodedpath(pathname)
            return pathname

        def create_link(filepath: str):
            filename = barename(filepath)
            link = f"- [{filename}]({encoded_realtivepath(filepath)})\n"
            return link

        linkstr = ""
        filepaths = listfilepaths(folderpath)
        for filepath in filepaths:
            linkstr += create_link(filepath)
        linkstr += "\n"

        return linkstr

    def indexstr(pathname: str = os.getcwd(), headerlvl: int = 2):
        filestr = ""
        folderpaths = listfolderpaths(pathname)
        for folderpath in folderpaths:
            filestr += headerstr(folderpath, headerlvl)
            filestr += linkstr(folderpath)
            filestr += indexstr(folderpath, headerlvl + 1)

        return filestr

    indexstr()
    print(indexstr())


load_cfg()
insert_indexes()
