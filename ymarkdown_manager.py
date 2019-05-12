"""Markdown Yöneticisi

README.md dosyasına indeksleri ekleme
Linkleri dynamic yapma

Author:
    Yunus Emre Ak

TODO: Options'lara bağlı olanlar Options metdolarında olsun
TODO: Aranan options yoksa default değer döndürsün
TODO: ToC oluştur
TODO: Header'lar için dinamik link oluştur [Baslik]: #baslik
TODO: Belki vscode eklentisi yapabilirsin
TODO: index="md" şeklinde veri alımı yap, stringlerdeki boşluk siliniyor

Yapısal işlem Notları:
    TODO: list, private gibi işlemler en dışta olacak
    TODO: Cfg yapısına dinamik link oluşturma gibi ek scriptler eklenebilir olacak

Belki yapılır:
    TODO: Vscode extension yapabilirsin
"""

import os
from enum import Enum, unique
from urllib.parse import quote

# Yapılandırma dosyası ayarları
CONFIG_FILE = "ymm.cfg"
README_FILE = "README.md"
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


# TODO: option.add_argument(...) ile ayar ekleme olanağı sun
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
    "INDEX_FOR_PAGE": Option(
        False,
        "Github sayfası (gh-pages) için indeksleme"
    ),
    "INSERT_INDICATOR": Option(
        "<!--Index-->",
        "İndexlenmesinin ekleneceği dosya aralığının başlangıç ve bitiş belirteci"
    ),
    "MAKE_LINKS_DYNAMIC": Option(
        False,
        "Statik linkleri dinamik linklere çevirme"
    )
}

# Görmezden gelinen dosya veya dizinler ('set' olma sebebi tekrarlı verileri engellemektir)
PRIVATES = {".git", ".vscode", "temp", "phpoffice"}


def load_cfg():
    """Yapılandırma dosyasındaki bilgileri programa yükleme
    """

    def cfg_exist() -> bool:
        """Yapılandırma dosyası kontrolü

        Returns:
            bool -- Dosya varsa `True`, yoksa `False`
        """
        return CONFIG_FILE in os.listdir()

    def read_cfg() -> None:
        """Yapılandırma dosyasındaki verileri değişkenlere kaydetme
        """

        @unique
        class Sections(Enum):
            """Dosya bölge indeksleri
            """
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

        def reg_option(name: str, value):
            """Verilen ayarı `OPTIONS` içerisine kaydetme

            Args:
                name (str): Ayar ismi
                value: Ayarın değeri
            """

            def cast_value(name, value):
                if type(OPTIONS[name].value) is not str:
                    return eval(value)
                return value

            if name in OPTIONS:
                OPTIONS[name].value = cast_value(name, value)

        def reg_privates(value):
            """Gizli dosya ve dizinleri `PRIVATES` değişkenine kaydetme

            Args:
                value : Dosya veya dizin ismi
            """
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
        """Yapılandırma dosyasını oluşturma
        """

        def headerstr(string: str) -> str:
            """Başlık metnini oluşturma

            Args:
                string (str): Başlık ismi

            Returns:
                str: Başlık metni
            """
            return f"{string}\n\n"

        def configstr() -> str:
            """Yapılandırma metnini oluşturma

            Returns:
                str: Oluşturulan metin
            """

            def optionstr() -> str:
                """Ayar metnini oluşturma

                Returns:
                    str: Oluşturulan metin
                """
                filestr = ""
                for option in OPTIONS:
                    filestr += f"# {OPTIONS[option].description}\n"
                    filestr += f"{option} = {OPTIONS[option].value}\n"
                filestr += "\n"
                return filestr

            filestr = headerstr(CONFIG_HEADER)
            filestr += optionstr()
            return filestr

        def privatestr() -> str:
            """Gizli dosya ve dizinlerin metnini oluşturma

            Returns:
                str: Oluşturulan metin
            """

            filestr = headerstr(PRIVATE_HEADER)
            for private in PRIVATES:
                filestr += f"{private}\n"
            filestr += "\n"
            return filestr

        with open(CONFIG_FILE, "w") as file:
            file.write(configstr())
            file.write(privatestr())

    if cfg_exist():
        read_cfg()
    else:
        create_cfg()
        read_cfg()


def is_private(name: str) -> bool:
    """İsmi verilen gizli mi kontrolü

    Args:
        name (str): Dosya ismi

    Returns:
        bool: Gizli ise `True` değilse `False`
    """

    for private in PRIVATES:
        if name == private:
            return True
    return False


def listfolderpaths(path: str = os.getcwd(), sort: bool = False) -> list:
    """Dizinleri listeleme

    Args:
        path (str, optional): Dizinleri listelenecek dizin. Defaults to os.getcwd().

    Returns:
        list: Listenelenen dizinler
    """

    folderlist = []
    for name in os.listdir(path):
        pathname = os.path.join(path, name)
        if os.path.isdir(pathname) and not is_private(name):
            folderlist.append(pathname)

    if sort:
        folderlist.sort()

    return folderlist


def listfilepaths(path: str = os.getcwd(), sort: bool = False) -> list:
    """Dosyaları listeleme

    Args:
        path (str, optional): Dosyaları listelenecek dizin. Defaults to os.getcwd().

    Returns:
        list: Listenelenen dosyalar
    """

    filelist = []
    for name in os.listdir(path):
        pathname = os.path.join(path, name)
        if os.path.isfile(pathname) and not is_private(name):
            filelist.append(pathname)

    if sort:
        filelist.sort()

    return filelist


def apply_all_files(func, path: str = os.getcwd(), sort: bool = False):
    for filepath in listfilepaths(path, sort):
        filepath = os.path.join(path, filepath)
        func(filepath)

    for folderpath in listfolderpaths(path, sort):
        folderpath = os.path.join(path, folderpath)
        apply_all_files(func, path=folderpath, sort=sort)


def apply_all_folders(func, path: str = os.getcwd(), sort: bool = False):
    for folderpath in listfolderpaths(path, sort):
        folderpath = os.path.join(path, folderpath)
        func(folderpath)
        apply_all_folders(func, path=folderpath, sort=sort)


def indexstr(pathname: str = os.getcwd(), headerlvl: int = 2, privates: set = set(), sort=True, remove_md=True, indexfilter="") -> str:
    """Indekslenmiş metin oluşturma

    Args:
        pathname (str, optional): İndekslerin oluşturulacağı dizin. Defaults to os.getcwd().
        headerlvl (int, optional): Markdown header seviyesi. Defaults to 2.
        privates (set, optional): Gizli dosya veya dizinler. Defaults to set().
        sort (bool, optional): İndeksleri sıralama. Defaults to True.
        remove_md (bool, optional): Markdown (.md) uzantısını kaldırma. Defaults to True.
        indexfilter (str, optional): İndeks filtresi. Defaults to "".

    Returns:
        str: Oluşturulan metin
    """

    def headerstr(folderpath: str, headerlvl: int) -> str:
        """Dizin için markdown header'ı oluşturma

        Args:
            folderpath (str): Dizin yolu
            headerlvl (int): # sayısı

        Returns:
            str: Oluşturulan metin
        """

        header = ""
        for i in range(0, headerlvl):
            header += "#"

        foldername = os.path.basename(folderpath)
        header += f" {foldername}\n\n"

        return header

    def linkstr(folderpath: str) -> str:
        """Dizin için markdown linklerini oluşturma

        Args:
            folderpath (str): Dizin yolu
            headerlvl (int): # sayısı

        Returns:
            str: Oluşturulan metin
        """

        def barename(filepath: str) -> str:
            """Dosya yolundan, yol ve uzantıyı temizleme

            Args:
                filepath (str): Dosya yolu

            Returns:
                str: Sadece dosya ismi
            """

            filename = os.path.basename(filepath)
            filename = remove_extension(filename)

            return filename

        def remove_extension(filepath: str) -> str:
            """Dosya uzantısını kaldırma

            Args:
                filepath (str): Dosya yolu

            Returns:
                str: Uzantsız dosya yolu
            """

            filepath, _ = os.path.splitext(filepath)
            return filepath

        def get_ext(filepath: str) -> str:
            """Dosya uzantısını alma

            Args:
                filepath (str): Dosya yolu

            Returns:
                str: Uzantı `.ext`
            """

            _, ext = os.path.splitext(filepath)
            return ext

        def encoded_realtivepath(pathname: str) -> str:
            """Verilen yola uygun kodlanmış markdown linki oluşturma

            Args:
                pathname (str): Yol

            Returns:
                str: Oluşturulan link metni
            """

            def modifypath(pathname: str) -> str:
                """Yol verisini düzenleme

                Uzantıyı koşula bağlı kaldırma veya kaldırmama

                Args:
                    pathname (str): Yol

                Returns:
                    str: Düzenlenen yol
                """

                if remove_md and ("md" in pathname):
                    pathname = remove_extension(pathname)
                return pathname

            def relativepath(pathname: str) -> str:
                """Statik yol verisini dinamik yol verisine dönüştürme

                Args:
                    pathname (str): Yol ismi

                Returns:
                    str: Dönüştürülen metin
                """

                return pathname.replace(os.getcwd(), '.')

            def encodedpath(pathname: str) -> str:
                """Verilen yolu url formatında kodlama

                Args:
                    pathname (str): Yol ismi

                Returns:
                    str: Kodlanmış metin
                """
                return quote(pathname)

            pathname = modifypath(pathname)
            pathname = relativepath(pathname)
            pathname = encodedpath(pathname)
            return pathname

        def create_link(filepath: str) -> str:
            """Markdown linki oluşturma

            Args:
                filepath (str): Dosya yolu

            Returns:
                str: Oluşturulan link
            """

            filename = barename(filepath)
            link = f"- [{filename}]({encoded_realtivepath(filepath)})\n"
            return link

        linkstr = ""
        filepaths = listfilepaths(folderpath, sort=sort)
        for filepath in filepaths:
            linkstr += create_link(filepath)

        # Link varsa satır atlatma, link yoksa gereksiz satır oluşturulmasını engelliyor
        if len(linkstr) > 0:
            linkstr += "\n"

        return linkstr

    filestr = ""
    folderpaths = listfolderpaths(pathname, sort=sort)
    for folderpath in folderpaths:
        filestr += headerstr(folderpath, headerlvl)
        filestr += linkstr(folderpath)
        filestr += indexstr(folderpath, headerlvl + 1,
                            privates, sort, remove_md, indexfilter)

    return filestr


def insertfile(filename: str, string: str, indicator: str):

    def create_filestr():
        # Dosya metni
        filestr = ""

        # Kontrol flagları
        inserted = False
        save = True

        def indicatorstr() -> str:
            filestr = "\n"
            filestr += string
            filestr += indicator
            filestr += "\n"
            return filestr

        with open(filename, "r") as file:
            for line in file:
                if save:
                    filestr += line

                if indicator in line:
                    if not inserted:
                        filestr += indicatorstr()
                        inserted = True

                    save = not save

        return filestr

    filestr = create_filestr()
    # Hatalı işlemleri dosyanın silinmesini engeller
    if len(filestr) > 0:
        with open(filename, "w") as file:
            file.write(filestr)
    else:
        print("Dosya okumada hata meydana geldi :(")


def replace_static_links_from_file(filepath) -> str:
    # Markdownlar için çalışacak
    if '.md' not in filepath:
        return

    DELIMS = ('[', ']', '(', ')')
    NOT_FOUND = -1
    LINKS = []

    def init_indexes() -> list:
        nonlocal DELIMS
        return [-1 for i in range(len(DELIMS))]

    def reset_indexes(indexlist: list, start: int = 0) -> list:
        """İndeksleri sıfırlama

        Args:
            indexlist (list): İndex listesi
            start (int, optional): Başlangıç indeksi. Defaults to 0.

        Returns:
            list: Değiştirilen indeksler
        """

        nonlocal NOT_FOUND
        for i in range(start, len(indexlist)):
            indexlist[i] = NOT_FOUND

        return indexlist

    def grablink(line: str, indexes: list) -> str:
        """Verilen satırdaki linki alma

        Args:
            line (str): Satır
            indexes (list): Ayıraçların indeksleri

        Returns:
            str: Link metni
        """
        return line[indexes[2] + 1:indexes[3]]

    def replace_line(line: str, link: str, index: int) -> (str, int):
        """Satırdaki linki dinamikleştirme

        Args:
            line (str): Satır
            link (str): Link metni
            link_index (int): Link indeksi

        Returns:
            ((str, int)): Yeni satır ve yeni indeks değeri
        """

        def reg_link(linkstr: str) -> int:
            """Link kayıtlı değil koşula göre kayıt altına alma

            Args:
                linkstr (str): Link metni
                condition (str, optional): Koşul metni. Defaults to "".

            Returns:
                int: Kayıt altına alınan linkin indeksi
            """
            nonlocal LINKS

            link_index = len(LINKS)
            found = False
            for i, link in enumerate(LINKS):
                if link == linkstr:
                    link_index = i
                    found = True
                    break

            # Link yoksa ekleme
            if not found:
                LINKS.append(linkstr)

            return link_index

        # Anchor linkleri atlama
        if len(link) > 0 and link[0] != "#":
            link_index = reg_link(link)

            line = line.replace(f"({link})", f"[{link_index}]")
            index -= len(link) - len(str(link_index))

        return line, index

    def append_header(filestr: str) -> str:
        if len(LINKS) > 0:
            if filestr[len(filestr) - 1] != "\n":
                filestr += "\n"

            filestr += "\n<!--DynamicLinks-->\n"

        return filestr

    def append_links(filestr: str):
        if len(LINKS) > 0:
            filestr += "\n"

            for i, link in enumerate(LINKS):
                filestr += f"[{i}]: {link}\n"

        return filestr

    filestr = ""
    with open(filepath, "r") as file:

        for line in file:
            # Her ayıracın konum indeksini tanımlama
            delim_indexes = init_indexes()

            # Satırları satır indeksiyle okuma
            index = 0
            for char in line:
                # Karakter '[' ise indeksini alma
                if char == DELIMS[0]:
                    delim_indexes[0] = index

                    # Diğer indeksleri sıfırlama
                    delim_indexes = reset_indexes(delim_indexes, 1)

                # "[" karakteri bulunduysa diğer karakterleri arama
                elif delim_indexes[0] != NOT_FOUND:
                    # "]" karakteri ise indeksini alma
                    if char == DELIMS[1]:
                        delim_indexes[1] = index

                    # "]" karakteri alındıysa diğer karakterleri arama
                    elif delim_indexes[1] != NOT_FOUND:
                        # Karakter ')' ise ve ']' dan hemen sonra geliyorsa indeksini alma
                        if char == DELIMS[2] and index == delim_indexes[1] + 1:
                            delim_indexes[2] = index

                        # '(' bulundusya diğer karakterleri arama
                        elif delim_indexes[2] != NOT_FOUND:
                            # Karakter ")" ise indeksini alma ve ek işlemler
                            if char == DELIMS[3]:
                                delim_indexes[3] = index

                                # Linkleri ayrıştırma ve gerekli dizilere ekleme
                                linkstr = grablink(line, delim_indexes)

                                # Parantezleri ve aradaki linki dinamikleştirme, indeksi yenileme
                                line, index = replace_line(
                                    line, linkstr, index)

                                # İndeksleri sıfırlama (yenisi için hazırlama)
                                delim_indexes = reset_indexes(delim_indexes)

                            # Boşluk karakteri link yapısını bozduğundan yeni link için hazırlama
                            elif char == ' ':
                                delim_indexes = reset_indexes(delim_indexes)

                # Yeni karaktere geçmeden önce indeksi ayarlama
                index += 1
            filestr += line

    filestr = append_header(filestr)
    filestr = append_links(filestr)

    with open(filepath, "w") as file:
        file.write(filestr)


def update():
    """README'de indeksleme oluşturucu
README dosyasında '<!--Index-->' adlı kısmın içerisine indekslemeyi iliştirir.
"""

    load_cfg()
    # TODO: Veriler bulunamazsa default değer veren bir metod ekle
    global OPTIONS, PRIVATES, README_FILE
    sort = OPTIONS['SORTED_INDEX'].value
    remove_md = OPTIONS['INDEX_FOR_PAGE'].value
    indicator = OPTIONS['INSERT_INDICATOR'].value
    indexfilter = OPTIONS['INDEX_FILTER'].value
    dynamic_link = OPTIONS['MAKE_LINKS_DYNAMIC'].value

    string = indexstr(privates=PRIVATES, sort=sort,
                      remove_md=remove_md, indexfilter=indexfilter)
    insertfile(README_FILE, string, indicator)

    if dynamic_link:
        apply_all_files(replace_static_links_from_file, sort=True)

    print("Updated! ~YEmreAk")


update()
