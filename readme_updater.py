"""Readme dosyasına indeksleri ekleme
"""

from enum import Enum, unique

# Yapılandırma dosyası ayarları
CONFIG_FILE = "readme.cfg"
COMMENT_DELIM = "#"
VARIABLE_DELIM = "="
CONFIG_HEADER = "[Config]"
PRIVATE_HEADER = "[Private]"
WHITESPACES = ["\n", " "]


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

# Görmezden gelinen dosya veya dizinler
PRIVATES = [".git", ".vscode"]


def update():
    """README'de indeksleme oluşturucu
README dosyasında `<!-- Index -->` adlı kısmın içerisine indekslemeyi iliştirir.
"""

    load_cfg()


def load_cfg():

    def read_file():

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
                return type(OPTIONS[name].value)(value)

            for option in OPTIONS:
                if name in OPTIONS:
                    OPTIONS[name].value = cast_value(name, value)

        def reg_privates(value):
            if value not in PRIVATES:
                PRIVATES.append(value)

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

    def create_file():

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
        read_file()
    except:
        create_file()
        read_file()


load_cfg()
