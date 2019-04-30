# Python <!-- omit in toc -->

- Bir başka faydalı kaynak olarak [buradaki][Fuatbeser Python Notları] *repo*'ya bakabilirsin.
- Python örnekleri için [buraya](https://pythonprogramming.net/) bakabilirsin.
- Mobile dev için Kiv çok iyidir, çoklu dokunma desteği sağlar.

> Ek kaynak için [harici kaynaklara](#harici-kaynaklar) bakmayı unutma

## İçerik <!-- omit in toc -->

> `HOME` tuşu ile yukarı yönlenebilrsiniz.

- [Kurulum ve Kullanım](#kurulum-ve-kullan%C4%B1m)
  - [VsCode Üzerinde Python](#vscode-%C3%BCzerinde-python)
    - [Python Kodlarını Formatlama](#python-kodlar%C4%B1n%C4%B1-formatlama)
    - [VsCode Debug Yapılandırması](#vscode-debug-yap%C4%B1land%C4%B1rmas%C4%B1)
    - [VsCode Jupyter Desteği](#vscode-jupyter-deste%C4%9Fi)
    - [VsCode Python Ortamı Ayarlama](#vscode-python-ortam%C4%B1-ayarlama)
    - [VsCode Ek Python Ayarları](#vscode-ek-python-ayarlar%C4%B1)
    - [VsCode Python Eklentileri](#vscode-python-eklentileri)
    - [Anaconda üzerindeki Python'ı Desteklemeyen Eklentiler](#anaconda-%C3%BCzerindeki-python%C4%B1-desteklemeyen-eklentiler)
    - [VsCode Python Kısayolları](#vscode-python-k%C4%B1sayollar%C4%B1)
    - [VsCode Python Ortam Değişkenleri](#vscode-python-ortam-de%C4%9Fi%C5%9Fkenleri)
  - [Faydalı Soru & Cevaplar](#faydal%C4%B1-soru--cevaplar)
- [Python ile Programlamaya Hazırlanma](#python-ile-programlamaya-haz%C4%B1rlanma)
  - [Yazım Kuralları](#yaz%C4%B1m-kurallar%C4%B1)
  - [Dökümantasyon PyDoc](#d%C3%B6k%C3%BCmantasyon-pydoc)
- [Temel Python](#temel-python)
  - [Anahtar Kelimeler (Keywords)](#anahtar-kelimeler-keywords)
    - [Fonksyion Oluşturma Anahtar Kelimeleri](#fonksyion-olu%C5%9Fturma-anahtar-kelimeleri)
      - [Fonksiyon Anahtar Kelimeleri](#fonksiyon-anahtar-kelimeleri)
  - [Değişkenler](#de%C4%9Fi%C5%9Fkenler)
    - [Ana Değişkenler](#ana-de%C4%9Fi%C5%9Fkenler)
    - [Ek Değişkenler](#ek-de%C4%9Fi%C5%9Fkenler)
    - [Değersiz Değişken Tanımalma](#de%C4%9Fersiz-de%C4%9Fi%C5%9Fken-tan%C4%B1malma)
    - [Sabit Değerler (Constants)](#sabit-de%C4%9Ferler-constants)
    - [Değişkenler Arası Takılama (Casting)](#de%C4%9Fi%C5%9Fkenler-aras%C4%B1-tak%C4%B1lama-casting)
    - [Değişken Tipleri için Ek Kaynak](#de%C4%9Fi%C5%9Fken-tipleri-i%C3%A7in-ek-kaynak)
    - [Değişken ve Sabitlerde Gizlilik](#de%C4%9Fi%C5%9Fken-ve-sabitlerde-gizlilik)
  - [Operatörler](#operat%C3%B6rler)
    - [Aritmatik Operatörler](#aritmatik-operat%C3%B6rler)
      - [Ek Aritmatik Operatörler](#ek-aritmatik-operat%C3%B6rler)
    - [Karşılaştırma Operatörleri](#kar%C5%9F%C4%B1la%C5%9Ft%C4%B1rma-operat%C3%B6rleri)
    - [Mantıksal Operatörler](#mant%C4%B1ksal-operat%C3%B6rler)
    - [Bit Düzeyinde Operatörler](#bit-d%C3%BCzeyinde-operat%C3%B6rler)
    - [Kimlik Belirleme Operatörleri](#kimlik-belirleme-operat%C3%B6rleri)
      - [Kimlik Belirleme Operatörleri Örneği](#kimlik-belirleme-operat%C3%B6rleri-%C3%B6rne%C4%9Fi)
    - [Üyelik Operatörleri](#%C3%BCyelik-operat%C3%B6rleri)
      - [Üyelik Operatörleri Örneği](#%C3%BCyelik-operat%C3%B6rleri-%C3%B6rne%C4%9Fi)
  - [If / Else Koşul (Constraints) Yapısı](#if--else-ko%C5%9Ful-constraints-yap%C4%B1s%C4%B1)
    - [Tek satır (üçlü) If / Else Yapısı](#tek-sat%C4%B1r-%C3%BC%C3%A7l%C3%BC-if--else-yap%C4%B1s%C4%B1)
  - [Döngüler (Loop)](#d%C3%B6ng%C3%BCler-loop)
    - [For Döngüsü](#for-d%C3%B6ng%C3%BCs%C3%BC)
      - [Değişken içinde For Döngüsü](#de%C4%9Fi%C5%9Fken-i%C3%A7inde-for-d%C3%B6ng%C3%BCs%C3%BC)
      - [İki Liste Üzerinde Paralel For Döngüsü](#i%CC%87ki-liste-%C3%BCzerinde-paralel-for-d%C3%B6ng%C3%BCs%C3%BC)
    - [While Döngüsü](#while-d%C3%B6ng%C3%BCs%C3%BC)
    - [Range Fonksiyonu](#range-fonksiyonu)
  - [Break / Continue](#break--continue)
  - [Fonksiyonlar](#fonksiyonlar)
    - [Dahili Fonksiyon Kullanımları](#dahili-fonksiyon-kullan%C4%B1mlar%C4%B1)
      - [Ekrana Yazma / Print İşlemleri](#ekrana-yazma--print-i%CC%87%C5%9Flemleri)
      - [String İşlemleri](#string-i%CC%87%C5%9Flemleri)
    - [Harici Fonksiyon Kullanımları](#harici-fonksiyon-kullan%C4%B1mlar%C4%B1)
      - [Harici String İşlemleri](#harici-string-i%CC%87%C5%9Flemleri)
      - [Dizin ve Yol İşlemleri](#dizin-ve-yol-i%CC%87%C5%9Flemleri)
    - [Fonksiyon Oluşturma](#fonksiyon-olu%C5%9Fturma)
      - [Fonksiyon İskeleti](#fonksiyon-i%CC%87skeleti)
      - [Fonksiyon Örneği](#fonksiyon-%C3%B6rne%C4%9Fi)
      - [Fonksyion Dökümantasyonu](#fonksyion-d%C3%B6k%C3%BCmantasyonu)
      - [Fonksyion Varsayılan Parametreler](#fonksyion-varsay%C4%B1lan-parametreler)
      - [Fonksiyonlarda Keyfi Parametreler](#fonksiyonlarda-keyfi-parametreler)
      - [Özyineleyen Fonksiyonlar](#%C3%B6zyineleyen-fonksiyonlar)
        - [Özyineleyen Fonksiyonların Avantajları](#%C3%B6zyineleyen-fonksiyonlar%C4%B1n-avantajlar%C4%B1)
        - [Özyineleyen Fonksiyonların Zararları](#%C3%B6zyineleyen-fonksiyonlar%C4%B1n-zararlar%C4%B1)
    - [Lambda Fonksiyonlar](#lambda-fonksiyonlar)
      - [Filter ile Lambda Kullanımı](#filter-ile-lambda-kullan%C4%B1m%C4%B1)
      - [Map ile Lambda Kullanımı](#map-ile-lambda-kullan%C4%B1m%C4%B1)
  - [Global, Local ve Nonlocal Kavramları](#global-local-ve-nonlocal-kavramlar%C4%B1)
    - [Global, Local ve Nonlocal Kavramlarına Örnek](#global-local-ve-nonlocal-kavramlar%C4%B1na-%C3%B6rnek)
    - [Global Kullanımına Örnek](#global-kullan%C4%B1m%C4%B1na-%C3%B6rnek)
  - [Modüller](#mod%C3%BCller)
    - [Modül Kullanım Örnekleri](#mod%C3%BCl-kullan%C4%B1m-%C3%B6rnekleri)
    - [Python Modül Dosyaları](#python-mod%C3%BCl-dosyalar%C4%B1)
      - [Sistemin Python Modüllerine Bakma](#sistemin-python-mod%C3%BCllerine-bakma)
    - [Modül İçinde Tanımlanan İsimleri Alma](#mod%C3%BCl-i%CC%87%C3%A7inde-tan%C4%B1mlanan-i%CC%87simleri-alma)
  - [Paketler (Package)](#paketler-package)
    - [Paketten ve Modül Örnekleri](#paketten-ve-mod%C3%BCl-%C3%B6rnekleri)
    - [Sık Kullanılan Paketler](#s%C4%B1k-kullan%C4%B1lan-paketler)
      - [Windows Paketleri](#windows-paketleri)
      - [Görüntü İşleme Paketleri](#g%C3%B6r%C3%BCnt%C3%BC-i%CC%87%C5%9Fleme-paketleri)
      - [Giriş Çıkış (I/O) Kontrol Paketleri](#giri%C5%9F-%C3%A7%C4%B1k%C4%B1%C5%9F-io-kontrol-paketleri)
    - [Paketler için Harici Bağlantıları](#paketler-i%C3%A7in-harici-ba%C4%9Flant%C4%B1lar%C4%B1)
  - [Sayılar, Sayılar Arası Dönüşüm ve Matematik](#say%C4%B1lar-say%C4%B1lar-aras%C4%B1-d%C3%B6n%C3%BC%C5%9F%C3%BCm-ve-matematik)
    - [Tabanlı Sayılar](#tabanl%C4%B1-say%C4%B1lar)
    - [Ondalıklı Sayılar (Decimals / Floats)](#ondal%C4%B1kl%C4%B1-say%C4%B1lar-decimals--floats)
      - [Decimal Float Kullanımları ve Farkı](#decimal-float-kullan%C4%B1mlar%C4%B1-ve-fark%C4%B1)
    - [Kesirli Sayılar (Fractions)](#kesirli-say%C4%B1lar-fractions)
      - [Kesirli Sayılarla İşlemler](#kesirli-say%C4%B1larla-i%CC%87%C5%9Flemler)
    - [Matematik İşlemleri](#matematik-i%CC%87%C5%9Flemleri)
      - [Matematikte Rastgelelik](#matematikte-rastgelelik)
  - [Class](#class)
    - [Class Anahtar Kelimeleri](#class-anahtar-kelimeleri)
    - [Basit Class Örneği](#basit-class-%C3%B6rne%C4%9Fi)
    - [Metodlu Class Örneği](#metodlu-class-%C3%B6rne%C4%9Fi)
      - [Obje Özelliği Silme](#obje-%C3%B6zelli%C4%9Fi-silme)
      - [Class Silme](#class-silme)
    - [Scopes and Namespaces](#scopes-and-namespaces)
    - [Enumeration](#enumeration)
      - [Basit Kullanım](#basit-kullan%C4%B1m)
      - [Enum Özellikleri](#enum-%C3%B6zellikleri)
        - [Benzersin Enum Tanımlaması](#benzersin-enum-tan%C4%B1mlamas%C4%B1)
- [Komut İsteminden Python (CLI)](#komut-i%CC%87steminden-python-cli)
  - [Argparse Modülü Detayları](#argparse-mod%C3%BCl%C3%BC-detaylar%C4%B1)
  - [Argüman Ekleme](#arg%C3%BCman-ekleme)
  - [Argüman Action Özelliği](#arg%C3%BCman-action-%C3%B6zelli%C4%9Fi)
  - [Örnek CLI Kodu](#%C3%B6rnek-cli-kodu)
- [Python Görsel Programlama (GUI)](#python-g%C3%B6rsel-programlama-gui)
  - [PyQt5 Kurulumu](#pyqt5-kurulumu)
  - [Basit GUI Yapımı](#basit-gui-yap%C4%B1m%C4%B1)
  - [PyQt Widgets](#pyqt-widgets)
- [PyInstaller ile Executable Dosya Oluşturma](#pyinstaller-ile-executable-dosya-olu%C5%9Fturma)
- [İleri Seviye Python](#i%CC%87leri-seviye-python)
  - [Assertion (Kural Koyma)](#assertion-kural-koyma)
    - [Assertion Örnekleri](#assertion-%C3%B6rnekleri)
  - [Try / Except Yapısı](#try--except-yap%C4%B1s%C4%B1)
  - [Dosya İşlemleri](#dosya-i%CC%87%C5%9Flemleri)
    - [Dosya Okuma](#dosya-okuma)
  - [Thread](#thread)
    - [Basit Thread Yapısı](#basit-thread-yap%C4%B1s%C4%B1)
    - [Zamanlayıcı Yapısı (Timer)](#zamanlay%C4%B1c%C4%B1-yap%C4%B1s%C4%B1-timer)
    - [Bir Plana göre Fonksiyon Çalıştırma](#bir-plana-g%C3%B6re-fonksiyon-%C3%A7al%C4%B1%C5%9Ft%C4%B1rma)
  - [Paralel İşlemler (Multiprocessing)](#paralel-i%CC%87%C5%9Flemler-multiprocessing)
    - [Multiprocessing Örneği](#multiprocessing-%C3%B6rne%C4%9Fi)
  - [Kod Parçaları (Code Snippet)](#kod-par%C3%A7alar%C4%B1-code-snippet)
    - [Ekran Görünüsünü Alma ve Kaydetme](#ekran-g%C3%B6r%C3%BCn%C3%BCs%C3%BCn%C3%BC-alma-ve-kaydetme)
    - [Kısayol ile Ekran Alanı Seçme](#k%C4%B1sayol-ile-ekran-alan%C4%B1-se%C3%A7me)
    - [Url Encode İşlemi](#url-encode-i%CC%87%C5%9Flemi)
- [Google Colabrotory Üzerinden Python](#google-colabrotory-%C3%BCzerinden-python)
  - [IPython Operatorleri](#ipython-operatorleri)
  - [Python Değişkenlerinin Bash Üzerinde Kullanımı](#python-de%C4%9Fi%C5%9Fkenlerinin-bash-%C3%BCzerinde-kullan%C4%B1m%C4%B1)
- [Ortam Değişkenleri](#ortam-de%C4%9Fi%C5%9Fkenleri)
  - [PyCharm Uygulmasında Ortam Değişkeni Tanımlama](#pycharm-uygulmas%C4%B1nda-ortam-de%C4%9Fi%C5%9Fkeni-tan%C4%B1mlama)
- [Yapılacaklar](#yap%C4%B1lacaklar)
- [Harici Kaynaklar](#harici-kaynaklar)

## Kurulum ve Kullanım

- Temel python kurulumunu, resmi sitesinden [buraya](https://www.python.org/downloads/) tıklayarak tamamlayabilirsin.
  - **pip** paket yöneticisini kullanır
  - `pip install` komutu ile modül yüklemesi yapılır
- **Makine öğrenimi** ve **veri bilimi** gibi işlemlerle uğaşacak isen, bu iş için geliştirilmiş olan [Anaconda](https://www.anaconda.com/distribution/#download-section) veya [MiniConda](https://docs.conda.io/en/latest/miniconda.html) yazılımı tavsiye edilir
  - Resmi paket yönetici **conda** olmasına rağmen **pip** üzerinden de kuruluma izin verir
  - `conda install` komutu ile modül yüklemesi yapılır
  - Temel yükleme yapısı '*Conda ile yüklenemezse pip kullan*' idir
  - Anaconda, MiniConda ve VirtualEnv farkı kullanımı için [buraya](http://deeplearning.lipingyang.org/2018/12/23/anaconda-vs-miniconda-vs-virtualenv/) bakabilirsin

> Anaconda ile alakalı bilgiler [burada](../Uygulama%20Notlar%C4%B1/Anaconda.md) derlenmektedir.

### VsCode Üzerinde Python

Başlangıç dökümanı için [buraya](https://code.visualstudio.com/docs/python/python-tutorial) bakabilirsin.

#### Python Kodlarını Formatlama

- `CTRL` + `SHIFT` + `P` yapın
- Çıkan alana `Python: Select Linter` yazın
- `pylint` düzenleyicisini seçin
  - `pylint` aynı dizindeki modulleri bulamamakta, bu hatananın çözümü için `.pylintrc` dosyasını düzenlemek gerekmekte
  - <!-- TODO echolu koda çevir -->
  - `pylint --generate-rcfile .pylintrc` komutunu çalışma dizininde yazdıktan sonra, içini açıp `#init-hook` satırını `init-hook='import sys; system.path.append("${workspaceFolder}")'` ile değiştirin. (Yorum satırı olmaktan kaldırın)
  - Eğer girintiyi <kbd>TAB</kbd> ile yapıyorsanız `pylint`'de *bug*'a sebebiyet vermekte, <kbd>SPACE</kbd> kullanın
- Python derleyicinize `autopep8` paketini aşağıdaki komutlarla veya vscode arayüzü ile yükleyin
  - pip install autopep8
  - conda install autopep8
- Artık `SHIFT` + `ALT` + `F` ile kodları düzenleyebilirsiniz.
- Dosyaya sağ tıklayarak derleyebilirsiniz.

#### VsCode Debug Yapılandırması

Detaylar için [buraya](https://code.visualstudio.com/docs/python/debugging) bakabilirsin.

- `CTRL` + `SHIFT` + `D` ile debug ekranını açın
- Sol üstte açılan ekrandan `ayarlar butonuna` tıklayın
- `Python` kısmını seçin

#### VsCode Jupyter Desteği

Detaylar için [buraya](https://code.visualstudio.com/docs/python/jupyter-support) bakabilirsin.

- Kod alanının üstüne `#%%` yazarak olutşurabilirsiniz.

#### VsCode Python Derleyicisi Ayarlama

Aktif olan derleyici ortamı, en altta bulunan durum çubuğunun solunda gösterilmektedir. Değiştirmek için:

- `CTRL` + `SHIFT` + `P` tuş kombinasyonuna basın
- Çıkan alana `Python: Select Interpreter` yazınız
- Çıkan ekrandan istediğiniz derleyiciyi seçiniz

#### VsCode PYTHONPATH Oluşturma

- Çalışma dizininde `.env` dosyası oluşturun
- `.env` dosyasının içerisine `PYTHONPATH=` satırını ekleyin
  - Örnek için bir alttaki başlığa bakınız
- Vscode ayarlarına `"python.envFile": "${workspaceFolder}/.env"` satırını ekleyin
- Vscode'u yeniden başlatın

> Kaynak için [buraya](https://github.com/Microsoft/vscode-python/issues/3840#issuecomment-463789294) bakabilirsin. Ek olarak [buraya](https://stackoverflow.com/a/54083402/9770490) bakmanda da fayda var.

#### Vscode PYTHONPATH Örneği

Resmi döküman için [buraya](https://code.visualstudio.com/docs/python/environments#_environment-variable-definitions-file) bakabilirsin.

- VsCode birden fazla satıra sahip değişken değerlerini kabul etmez
- Ortam değişklenleri oluşturmak için proje ayarlarından **env file** seçmemiz gerekmekte
- Ardından içine değişkenlerimizi tanımlamamız gerkemekte

```json
"python.envFile": "${workspaceFolder}/prod.env"
```

```sh
# prod.env
# Python kaynak dizinleri
RESEARCH_FOLDER=C:/Users/YEmre/Documents/Tensorflow/models/research
OBJECT_FOLDER=C:/Users/YEmre/Documents/Tensorflow/models/research/object_detection
SLIM_FOLDER=C:/Users/YEmre/Documents/Tensorflow/models/research/slim
SCRIPT_FOLDER=C:/Users/YEmre/Documents/Tensorflow/scripts

# Python modül yolu
PYTHONPATH=${RESEARCH_FOLDER}:${OBJECT_FOLDER}:${SLIM_FOLDER}:${SCRIPT_FOLDER}
```

```sh
PYTHONPATH=./src:${PYTHONPATH}
```

> Kaynak için [buraya](https://code.visualstudio.com/docs/python/environments#_use-of-the-pythonpath-variable) bakabilirsin.

#### VsCode Ek Python Ayarları

Ek python ayarları için [buradaki](https://code.visualstudio.com/docs/python/settings-reference) resmi dökümana bakabilirsin.

#### VsCode Python Eklentileri

| Eklenti                                                                                                                               | Açıklama                                                   |
| ------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------- |
| [Python](https://marketplace.visualstudio.com/items?itemName=ms-python.python)                                                        | Dil desteği                                                |
| [Visual Studio IntelliCode - **Preview**](https://marketplace.visualstudio.com/items?itemName=VisualStudioExptTeam.vscodeintellicode) | Sık kullanılan kod önerileri (**eksik öneriler olabilir**) |
| [autoDocstring](https://marketplace.visualstudio.com/items?itemName=njpwerner.autodocstring)                                          | Dökümantasyon parçaları sağlayan eklenti                   |
| [Better Comment](https://marketplace.visualstudio.com/items?itemName=aaron-bond.better-comments)                                      | Yorum satırı renklediricisi                                |
| [Trailing Space](https://marketplace.visualstudio.com/items?itemName=shardulm94.trailing-spaces)                                      | Gereksiz boşlukları hızlıca silmek için aydınlatır         |

#### Anaconda üzerindeki Python'ı Desteklemeyen Eklentiler

| Eklenti                                                                                      | Açıklama                 |
| -------------------------------------------------------------------------------------------- | ------------------------ |
| [AREPL for python](https://marketplace.visualstudio.com/items?itemName=almenon.arepl)        | Anlık çıktıları gösterme |
| [Code Runner](https://marketplace.visualstudio.com/items?itemName=formulahendry.code-runner) | Kod koşturucusu          |

#### VsCode Python Kısayolları

Alttaki kısayollar `keybindings.json` dosyası içerisinde bulunmalıdır.

```json
// Place your key bindings in this file to override the defaultsauto[]
[
  {
    // Kod parçasını metoda çevirme
    "key": "ctrl+shift+m ctrl+shift+m",
    "command": "python.refactorExtractMethod"
  },
  {
    // Kod parçasını metoda taşıma
    "key": "ctrl+shift+v ctrl+shift+v",
    "command": "python.refactorExtractVariable"
  },
  {
    // İmport'ları sıralama
    "key": "ctrl+shift+s ctrl+shift+s",
    "command": "python.sortImports"
  },
  {
    "key": "shift+f10",
    "command": "python.execInTerminal"
  }
]
```

### Faydalı Soru & Cevaplar

- [What's the difference between a pip install and conda install?](https://www.quora.com/Whats-the-difference-between-a-pip-install-and-conda-install)
- [Module Package Library Meaning](https://knowpapa.com/modpaclib-py/)

## Python ile Programlamaya Hazırlanma

### Yazım Kuralları

Orjinal dökümantasyon için [buraya](https://www.python.org/dev/peps/pep-0008/) bakabilirsin.

- Her python dosyasına **modül** denir
  - `import` ile dahil edilirler
  - `.` ile içlerine erişilir
- Class isimleri için **camel case** yazım kuralı geçerlidir
  - Boşluk karakteri **harfi büyüterek** temsil edilir
  - `camelCase`
- Geri kalanlar için **snake case** yazım kuralı geçerlidir
  - Boşluk karakteri `_` ile temsil edilir
  - `snake_case`
- Girintiler (`\t` karakteri) `{}` işlevi görür
- `:` karakteri ile yeni bir scope (alt alan) açılır
  - `for`, `def` gibi döngü veya metod işlemlerinde kullanırlır
- Metotlar arasında 2 satır bırakılır
- Metodların en son satırları boş olmalıdır (return için)
- Kodun en son satırı boş olmalıdır (End of File)

> Daha fazla bilgi için harici linklerdeki [Should I use underscores or camel case for Python?](https://www.quora.com/Should-I-use-underscores-or-camel-case-for-Python) bağlantısına tıklayabilirsin.

### Dökümantasyon PyDoc

- `'''` ile fonksiyonların üstüne dökümantasyon (açıklama) eklenir
- `#` ile koda yorum eklenir

```py
def func(a):
  """ 1 Değeri döndürür """
  return 1 # Döndürme keywordu
```

> [PyDoc videosu](https://www.youtube.com/watch?v=Y6TgbyfKCNM)

## Temel Python

### Anahtar Kelimeler (Keywords)

Harici link için [buraya](https://www.programiz.com/python-programming/keyword-list) tıklayabilirsin.

| Anahtar | Anlamı                          |
| ------- | ------------------------------- |
| `pass`  | Tanımsız (null)                 |
| `is`    | Eşitlik (==)                    |
| `in`    | İçerisindeki elemanlar          |
| `with`  | Açık olduğu sürece anlamı taşır |

> Döngü veya metotların *içleri doldurulana* kadar yer kaplayıcı olarak `pass` kullanılır.

#### Fonksyion Oluşturma Anahtar Kelimeleri

| Anahtar  | Oluştuma                   | Erişim        |
| -------- | -------------------------- | ------------- |
| Lambda   | `m_lambda = lambda x: x*2` | `m_lambda(2)` |
| Function | `def m_func(param):`       | `m_func(5)`   |

##### Fonksiyon Anahtar Kelimeleri

| Anahtar  | Anlamı                                            |
| -------- | ------------------------------------------------- |
| `return` | Veri döndürme                                     |
| `yield`  | Her çağırılmada tek bir veri döndürme (generator) |

### Değişkenler

#### Ana Değişkenler

| Tip     | Açıklama         | Örnek                 |
| ------- | ---------------- | --------------------- |
| bool    | 2'li değer, bit  | `True`                |
| int     | Sayı             | `1`                   |
| float   | Virgüllü sayı    | `1.2`                 |
| complex | Karmaşık sayılar | `2+3j`                |
| str     | String, metin    | `"Hello"` / `'Hello'` |

#### Ek Değişkenler

| Tip                                                                   | Oluştuma                           | Erişim         |
| --------------------------------------------------------------------- | ---------------------------------- | -------------- |
| [List](https://www.programiz.com/python-programming/list)             | `liste = [1, 2]`                   | `liste[index]` |
| [Set](https://www.programiz.com/python-programming/set)               | `kume = {1.0, "Hello", (1, 2, 3)}` | `kume.add(1)`  |
| [Dictionary](https://www.programiz.com/python-programming/dictionary) | `site = {"adi":"yemreak"}`         | `site['adi']`  |
| [Tuple](https://www.programiz.com/python-programming/tuple)           | `konum = (1, 2)`                   | `x, y = konum` |

- `[<değişken> for <değişken> in <dizi_veya_liste> if <koşul>` İstenen koşullardaki elemanların listesini verir
  - Örn: `[x for x in a if x != 20]`

#### Değersiz Değişken Tanımalma

```py
degersiz = None
```

#### Sabit Değerler (Constants)

Python'da *constant*'lar yoktur. Sabit değerler büyük harfler ile belirtilir.

> Aynı dosya içerisinde büyük harflerle yazılsa bile değiştirilebilir.

**`sabitler.py` dosyası**

```py
PI = 3.14
YER_CEKIMI = 9.8
```

**`main.py` dosyası**

```py
import sabitler

print(sabitler.PI) # 3.14
print(sabitler.GRAVITY) # 9.8
```

#### Değişkenler Arası Takılama (Casting)

```py
ondalikli = 5.8
tam = int(5.8) # 5 atanır
sonuc = int(7/3.5) # 2 atanır
sonuc = int(7/3) # 2 atanır
sonuc = float(7 / 3.5) # 2.0 atanır
sonuc = 7 / 3 # 2.33 atanır
```

#### Değişken Tipleri için Ek Kaynak

- [Basic Data Types in Python](https://realpython.com/python-data-types/)

#### Değişken ve Sabitlerde Gizlilik

- `__` ile gizli anlamında gelmektedir.
  - Dışarıdan sadece `_<class>.__<değişken>` şeklinde erişilebilir

> Detaylar için [buraya](https://www.bogotobogo.com/python/python_private_attributes_methods.php) bakabilirsin.

### Operatörler

| Operatör | Açıklama                       |
| -------- | ------------------------------ |
| `\`      | Satır atlatmayı geçersiz kılma |

#### Aritmatik Operatörler

| Operatör         | Açıklama                                |
| ---------------- | --------------------------------------- |
| `+, -, /, *`     | 4 işlem                                 |
| `=`              | Atama işlemi                            |
| `a, b = c, d`    | Tek satırda çoklu atama                 |
| `+=, -=, /=, *=` | Kendisiyle işleme sokup kendisine atama |
| `<operatör>=`    | Kendisiyle işleme sokup kendisine atama |
| `( )`            | Parantej ile öncelik belirleme          |

> `<operatör>` herhangi bir operatörü temsil eder.

##### Ek Aritmatik Operatörler

| Operatör | Açıklama             | Örnek     | Çıktı |
| -------- | -------------------- | --------- | ----- |
| `%`      | Mod alma işlemi      | `6 % 2`   | `0`   |
| `**`     | Kuvvet alma          | `6 ** 2`  | `36`  |
| `//`     | Kalansız bölümü alma | `13 // 2` | `6`   |

#### Karşılaştırma Operatörleri

| Operatör | Açıklama   | Örnek    | Çıktı   |
| -------- | ---------- | -------- | ------- |
| `>`      | Büyük      | `3 > 2`  | `True`  |
| `<`      | Küçük      | `3 < 2`  | `False` |
| `==`     | Eşit       | `3 == 3` | `True`  |
| `!=`     | Eşit değil | `2 != 2` | `False` |
| `>=`     | Büyük eşit | `2 >= 5` | `False` |
| `<=`     | Küçük eşit | `2 <= 2` | `True`  |

#### Mantıksal Operatörler

| Operatör | Açıklama    | Örnek            | Çıktı   |
| -------- | ----------- | ---------------- | ------- |
| `and`    | Ve işlemi   | `True and False` | `False` |
| `or`     | Veya işlemi | `False or True`  | `True`  |
| `not`    | Değili      | `not False`      | `True`  |

#### Bit Düzeyinde Operatörler

| Operatör | Açıklama      | Örnek                     |
| -------- | ------------- | ------------------------- |
| `&`      | Ve            | `x & y = 0 (0000 0000)`   |
| `|`      | Veya          | `x | y = 14 (0000 1110)`  |
| `~`      | Değili        | `~ x = -11 (1111 0101)`   |
| `^`      | XOR           | `x ^ y = 14 (0000 1110)`  |
| `>>`     | Sağa kaydırma | `x >> 2 = 2 (0000 0010)`  |
| `<<`     | Sola kaydırma | `x << 2 = 40 (0010 1000)` |

#### Kimlik Belirleme Operatörleri

| Operatör | Açıklama                  | Örnek                     | Çıktı   |
| -------- | ------------------------- | ------------------------- | ------- |
| `is`     | Aynı objeye işaret etme   | `[1, 2, 3] and [1, 2, 3]` | `False` |
| `is not` | Farklı objeye işaret etme | `1  is not 1`             | `False` |

> Ek değişkenlerde objelerin adresleri farklı olduğunda ilk çıktı `False` olur.

##### Kimlik Belirleme Operatörleri Örneği

```py
x1 = 5
y1 = 5
x2 = 'Hello'
y2 = 'Hello'
x3 = [1,2,3]
y3 = [1,2,3]

# Output: False
print(x1 is not y1)

# Output: True
print(x2 is y2)

# Output: False
print(x3 is y3)
 ```

#### Üyelik Operatörleri

| Operatör | Açıklama    | Örnek        | Çıktı   |
| -------- | ----------- | ------------ | ------- |
| `in`     | Anahtar var | `5 in x`     | `False` |
| `not in` | Anahtar yok | `1 not in x` | `False` |

> `x = [1, 2, 3, 4]`

##### Üyelik Operatörleri Örneği

```py
x = 'Hello world'
y = {1:'a',2:'b'}

print('H' in x) # True
print('hello' not in x) # True (h'si büyük değil)
print(1 in y) # True
print('a' in y) # False ('a' bir değerdir anahtar değildir)
```

### If / Else Koşul (Constraints) Yapısı

- `:` ile if / else satırı sonlandırılır
- `Tab` kadar boşluk atılırsa if scope*'u içerisinde olur

```py
num = float(input("Sayı giriniz: "))
if num >= 0:
    if num == 0:
        print("Sıfır")
    elif num == 1:
        print("Bir")
    else:
        print("Pozitif sayı")
else:
    print("Negatif sayı")
```

#### Tek satır (üçlü) If / Else Yapısı

```py
fruit = 'Apple'
isApple = True if fruit == 'Apple' else False
```

### Döngüler (Loop)

#### For Döngüsü

```py
sayilar = [6, 5, 3, 8, 4, 2, 5, 4, 11]
toplam = 0 # Toplam değeri tutacak değişken

for sayi in sayilar: # Liste üzerinde döngü ile ilerleme
  toplam = toplam + sayi

print("Toplam değer:", sum) # Toplam Değer: 48
```

##### Değişken içinde For Döngüsü

```py
values = [item.value for item in Fruit]  # [4, 5, 6]
values = set(item.value for item in Fruit)  # {4, 5, 6}
```

##### İki Liste Üzerinde Paralel For Döngüsü

```py
for num, cheese, color in zip([1,2,3], ['manchego', 'stilton', 'brie'],
                              ['red', 'blue', 'green']):
    print('{} {} {}'.format(num, color, cheese))
```

```sh
1 red manchego
2 blue stilton
3 green brie
```

#### While Döngüsü

```py
sayac = 0

while sayac < 3:
    print("Döngü içinde")
    sayac = sayac + 1
else:
    print("Döngü dışında")
```

```out
Döngü içinde
Döngü içinde
Döngü içinde
Döngü dışında
```

#### Range Fonksiyonu

```py
print(range(10)) # range(0, 10)
print(list(range(10))) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(list(range(2, 8))) # [2, 3, 4, 5, 6, 7]
print(list(range(2, 20, 3))) #  [2, 5, 8, 11, 14, 17]
```

### Break / Continue

```py
for deger in "string":
    if deger == "i":
        break # Döngüyü sonlandırır
    if deger == "t"
        continue # Döngüdeki adımı sonlandırır
    print(deger)

print("Son")
```

```out
s
r
Son
```

### Fonksiyonlar

#### Dahili Fonksiyon Kullanımları

##### Ekrana Yazma / Print İşlemleri

| Fonksiyon                      | Açıklama              | Örnek                      | Çıktı        |
| ------------------------------ | --------------------- | -------------------------- | ------------ |
| `print(<string>)`              | Ekrana yazma          | `print(f"X: {a}, Y: {2}")` | `X: 1, Y: 2` |
| `print(f'...{<python_kodu>}')` | Ekrana formatlı yazma | `print(f"X: {a}, Y: {2}")` | `X: 1, Y: 2` |

##### String İşlemleri

Çok önemli ve ileride kullanılacak bir konudur. 🌟

<!-- TODO linkleri ekle -->

| Link    | Metot                   | Açıklama                | Örnek                                  | Çıktı                  |
| ------- | ----------------------- | ----------------------- | -------------------------------------- | ---------------------- |
|         | `len`                   | Uzunluk                 | `len("yemreak")`                       | 7                      |
|         | `format`                | Formatlama              | `"X: {}, Y: {}".format(1, 2)`          | `'X: 1, Y: 2'`         |
|         | `%`                     | Operatör ile formatlama | `'new(%s %d)' % ('help', 5)`           | `'new(help 5)'`        |
|         | `f`                     | Format string ön eki    | `f'X: {a}'`                            | `'X: 2'`               |
|         | `r`                     | Raw String ön eki       | `r"C:\Users"`                          | `C:\\Users`            |
|         | `"""`                   | Çok satırlı string      |
|         | `split`                 | Parçalama               | `"ye mre ak".split(" ")`               | `['ye', 'mre', 'ak']`  |
| [Slice] | `[<başlangıç>:<bitiş>]` | Kesme                   | `"yemreak".[2:5]`, `"yemreak".[-3:-1]` | `"mre"`, `"ea"`        |
|         | `join`                  | Birleştirme             | `','.join(['do', 're', 'mi'])`         | `'do,re,mi'`           |
|         | `split & join`          | Yeniden formatlama      | `arr.split("\t").join("|")`            | `'İsim|Soyisim|Numara` |
|         | `replace`               | Metin değiştirme        | `"yemreak".replace("ak", "")`          | `'yemre'`              |
|         | `strip`                 | Metin düzeltme          | `' abc '.strip()`                      | `'abc'`                |
|         | `ltrip`                 | Metnin solunu düzeltme  | `' abc '.ltrip()`                      | `'abc '`               |
|         | `rtrip`                 | Metnin sağını düzeltme  | `' abc '.rtrip()`                      | `' abc'`               |
|         | `sort`                  | Metni sıralama          | `['n', 'a', 'i']`                      | `['a', 'i', 'n']`      |

> Daha fazla bilgi için [buraya](https://www.programiz.com/python-programming/methods/string) ve [buraya](https://stackoverflow.com/questions/10660435/pythonic-way-to-create-a-long-multi-line-string) bakabilirsin.

#### Harici Fonksiyon Kullanımları

- Fonksiyonları kullanmadan önce `import <paket>` ile paketi dahil etmeniz lazım
- Fonksiyonların kullanımı `<paket>.<fonksiyon>` şeklindedir

##### Harici String İşlemleri

| Paket | Fonksiyon                                | Açıklama                              |
| ----- | ---------------------------------------- | ------------------------------------- |
| `re`  | `split(<ayırıcı_karakterler>, <string>)` | Birden fazla karaktere göre parçalama |

- `<ayırıcı_karakterler>` Metni hangi karakterlere göre böleceğimizi ifade eder
  - Birden fazla olacaksa `|` ile birbirinden ayrılır
  - Ayırma sırasında `boşluk karakteri`nin kullanılması sorun oluşturur
  - *Örn:* `'\n|\t|\*'`
- `<string>` Ayrıştırılacak metin
  - *Örn:* `'yemreak.com'`

##### Dizin ve Yol İşlemleri

| Paket     | Fonksiyon                      | Açıklama                                                                         |
| --------- | ------------------------------ | -------------------------------------------------------------------------------- |
| `os`      | `listdir(<yol>)`               | Yolu verilen dizinin içindekileri döndürür                                       |
| `os`      | `rename(<eski_ad>, <yeni_ad>)` | Dosya veya dizin adlandırma                                                      |
| `os.path` | `isfile(<yol>)`                | Dosya mı kontrolü                                                                |
| `os.path` | `join(<yol1>, <dosya_adı>)`    | Dizinleri birleştirme                                                            |
| `os.path` | `basename(<yol>)`              | Yolu verilen dosyanın salt adını ve uzantısını bulma                             |
| `os.path` | `splittext(<dosya_adı>)`       | Dosyanın başlığını ve uzantısını döndürür (title, ext)                           |
| `glob`    | `glob(<yol_şablonu>)`          | Verilen sorguya veya yola uygun dosya ve dizinleri döndürür                      |
| `glob`    | `iglob(<yol_şablonu>)`         | Verilen sorguya veya yola uygun dosya ve dizinleri generator yapısı ile döndürür |

- `<yol>` Path, dosya yolu
  - *Örn: C:\Users\Username\help.txt*
- `<dosya_adı>` Dosyanın uzantısıyla birlikteki adı
  - *Örn: help.txt*
- `<yol_şablonu>` Özel dizin sorguları
  - *Örn: `*.txt`, `../help`*

#### Fonksiyon Oluşturma

##### Fonksiyon İskeleti

```py
def function_name(parameters):
  """docstring"""
  statement(s)
```

##### Fonksiyon Örneği

```py
def greet(name):
  """This function greets to
  the person passed in as
  parameter"""
  print("Hello, " + name + ". Good morning!")
```

##### Fonksyion Dökümantasyonu

```cmd
>>> print(greet.__doc__)
This function greets to
  the person passed into the
  name paramete
```

##### Fonksyion Varsayılan Parametreler

```py
def greet(name, msg = "Good morning!"):
   """
   This function greets to
   the person with the
   provided message.

   If message is not provided,
   it defaults to "Good
   morning!"
   """

   print("Hello",name + ', ' + msg)

greet("Kate") # Varsayılan parametreyi kullanma
greet("Bruce","How do you do?") # Sıralı parametre verme
greet("Bruce", msg="Naber") # İşaretleyerek paremetre verme
```

##### Fonksiyonlarda Keyfi Parametreler

```py
def greet(*names):
   """This function greets all
   the person in the names tuple."""

   # names is a tuple with arguments
   for name in names:
       print("Hello",name)

greet("Monica","Luke","Steve","John")
```

> `*` ön eki ile ile kaç tane isim gelirse o kadar kullanıyoruz.

##### Özyineleyen Fonksiyonlar

```py
def calc_factorial(x):
    """This is a recursive function
    to find the factorial of an integer"""

    if x == 1:
        return 1
    else:
        return (x * calc_factorial(x-1))

num = 4
print("The factorial of", num, "is", calc_factorial(num))
```

```out
calc_factorial(4)              # 1st call with 4
4 * calc_factorial(3)          # 2nd call with 3
4 * 3 * calc_factorial(2)      # 3rd call with 2
4 * 3 * 2 * calc_factorial(1)  # 4th call with 1
4 * 3 * 2 * 1                  # return from 4th call as number=1
4 * 3 * 2                      # return from 3rd call
4 * 6                          # return from 2nd call
24                             # return from 1st call
```

###### Özyineleyen Fonksiyonların Avantajları

- Özyineleyen fonksiyonlar kodun daha temiz ve zarif gözükmesini sağlar
- Karmaşık bir görev alt görevlere ayrılarak rahat çözülebilir
- İç içe döngülere göre daha iyidir

###### Özyineleyen Fonksiyonların Zararları

- Bazı durumlarda anlaşılabilmesi zordur
- Uzun tekrarlarda çok fazla vakit ve zaman harcarlar
- Hata ayıklama oldukça zordur

#### Lambda Fonksiyonlar

```py
double = lambda x: x * 2 # lambda fonksiyon


def double(x): # Fonksiyon
   return x * 2
```

##### Filter ile Lambda Kullanımı

Sadece koşulu sağlayan değerleri döndürür.

```py
listem = [1, 5, 4, 6, 8, 11, 3, 12]

cift_listem = list(filter(lambda x: (x%2 == 0) , listem))
print(cift_listem) # [4, 6, 8, 12]
```

##### Map ile Lambda Kullanımı

Her eleman için işlem yapar.

```py
listem = [1, 5, 4, 6, 8, 11, 3, 12]

katlanmis_listem = list(map(lambda x: x * 2 , listem))
print(katlanmis_listem) # Output: [2, 10, 8, 12, 16, 22, 6, 24]
```

### Global, Local ve Nonlocal Kavramları

| Kavram     | Açıklama                                                                                    |
| ---------- | ------------------------------------------------------------------------------------------- |
| `global`   | Tüm modülde geçerli değişkenler                                                             |
| `local`    | Fonksiyonların içerisindeki yerel değişkenler                                               |
| `nonlocal` | Modül ile fonksiyon arasında kalan, genellikle iç içe fonksiyonlarda kullanılan değişkenler |

#### Global, Local ve Nonlocal Kavramlarına Örnek

```py
x = 5 # Global

def fonksiyonum():
  x = 3 # Nonlocal

  def degisitirici():
    x = 1 # Local
```

#### Global Kullanımına Örnek

```py
x = 5
  # Yerel x değişkenine 3 değeri atanır, evrensel x değişmez.
  def xDegistir():
    x = 3

  # Evrensel x değişir
  def globalXDegistir():
    global x
    x = 4
```

### Modüller

Her python dosyasına modül denir.

- `import` ile dahil edilirler
- `.` ile içlerindekilere erişilir

#### Modül Kullanım Örnekleri

- Python aynı modülü birden fazla kez `import` etmez
  - Kullanıcı birden fazla `import` işlemi yaparsa tepki vermez
- Baştan `import` edilmek istenirse `imp.reload(modül)` şeklinde kullanılır

```py
import math # Doğrudan öodülü alma
print("Pi: ", math.pi) # Pi: 3.141592653589793
```

```py
import math as m # Modülü özel isimlendirme
print("Pi: ", m.pi) # Pi: 3.141592653589793
```

```py
from math import pi # Modül içinden özel değeri alma
print("Pi: ", pi) # Pi: 3.141592653589793
```

```py
from math import * # Modül içindeki her şeyi alma
print("Pi: ", pi) # Pi: 3.141592653589793
```

#### Python Modül Dosyaları

Modül dosyalarının aranma yerleri:

- Çalışılan dizin
- Ortam değişkenlerindeki `PYTHONPATH` değişkeni değeri
- Kuruluma bağlı varsayılan dizin

##### Sistemin Python Modüllerine Bakma

```py
>>> import sys
>>> sys.path
['',
'C:\\Python33\\Lib\\idlelib',
'C:\\Windows\\system32\\python33.zip',
'C:\\Python33\\DLLs',
'C:\\Python33\\lib',
'C:\\Python33',
'C:\\Python33\\lib\\site-packages']
```

#### Modül İçinde Tanımlanan İsimleri Alma

```py
>>> dir(example)
['__builtins__',
'__cached__',
'__doc__',
'__file__',
'__initializing__',
'__loader__',
'__name__',
'__package__',
'add']
```

```py
>>> import example
>>> example.__name__
'example'
```

```py
>>> a = 1 # Modül değişkenlerine ekleniyor
>>> b = "hello" # Modül değişkenlerine ekleniyor
>>> import math # Modül değişkenlerine ekleniyor
>>> dir()
['__builtins__', '__doc__', '__name__', 'a', 'b', 'math', 'pyscripter']
```

### Paketler (Package)

- Birden fazla modülü içinde barındırır
- `.` ile modüllere erişilir
  - Tekrar `.` atılırsa modülün içindekilere erişilir

#### Paketten ve Modül Örnekleri

```py
import Game.Level.start
```

```py
from Game.Level import start
```

```py
from Game.Level.start import select_difficulty
```

#### Sık Kullanılan Paketler

| Modül                                                                                          | Odaklantığı İşlemler |
| ---------------------------------------------------------------------------------------------- | -------------------- |
| [os](https://www.pythonforbeginners.com/os/pythons-os-module)                                  | İşletim sistemi      |
| time                                                                                           | Zaman                |
| [datetime](https://www.pythonforbeginners.com/basics/python-datetime-timedelta)                | Tarih                |
| [numpy](https://s3.amazonaws.com/assets.datacamp.com/blog_assets/Numpy_Python_Cheat_Sheet.pdf) | Matematiksel         |
| [openCV](https://docs.opencv.org/3.0-last-rst/opencv_cheatsheet.pdf)                           | Görüntü              |
| [pillow](https://pillow.readthedocs.io/en/stable/)                                             | Resim                |
| Tensorflow                                                                                     | Makine öğrenimi      |

##### Windows Paketleri

| Modül       | Odaklandığı İşlemler                                                | Dökümanlar                                                                                                                                                                                       |
| ----------- | ------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| pywinauto ☆ | Önplanda olmasalar dahi windows uygulamaları (pywin32'i barındırır) | [🌐](https://pywinauto.readthedocs.io/en/latest/index.html) [📺](https://www.youtube.com/watch?v=mhNIHgJPP3g) [📥](https://pywinauto.readthedocs.io/en/latest/#installation)                     |
| pygetwindow | Windows pencereleri (basit)                                         | [🌐](https://github.com/asweigart/PyGetWindow)                                                                                                                                                   |
| pywin32     | Resmi windows API (pencere dahil)                                   | [🌐](http://timgolden.me.uk/pywin32-docs/contents.html) [📺]([https://www.youtube.com/watch?v=o-k6l6ea3Lg](https://www.youtube.com/watch?v=o-k6l6ea3Lg)) [📥](https://pypi.org/project/pywin32/) |
| pyautogui   | Arayüz, fare, klavye ...                                            | [📃](https://media.readthedocs.org/pdf/pyautogui/latest/pyautogui.pdf) [📺](https://www.youtube.com/watch?v=xOfBezEDZ24)                                                                         |

##### Görüntü İşleme Paketleri

| Modül       | Açılkama                 | Dökümanlar                                                       |
| ----------- | ------------------------ | ---------------------------------------------------------------- |
| pillow      | Python resim kütüphanesi |                                                                  |
| opencv      | Görüntü işleme           | [📃](https://docs.opencv.org/3.0-last-rst/opencv_cheatsheet.pdf) |
| pytesseract | Görüntüdeki yazıyı bulma | [🌐](https://pypi.org/project/pytesseract/)                      |

##### Giriş Çıkış (I/O) Kontrol Paketleri

| Paket  | Odaklanığı İşlemler | Dökümanlar                                                                                                                                                                  |
| ------ | ------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| pynput | Fare, klavye vs...  | [🌐](https://pynput.readthedocs.io/en/latest/index.html) [📃](https://media.readthedocs.org/pdf/pynput/latest/pynput.pdf) [📺](https://www.youtube.com/watch?v=kJshtCfqCsY) |

#### Paketler için Harici Bağlantıları

- [Python Kütüphaneleri](https://docs.python.org/3/library/)
- [Argparse Tutorial](https://docs.python.org/3/howto/argparse.html)
- [PyAutoGUI vs Pywinauto](https://www.reddit.com/r/Python/comments/8bymeo/pyautogui_vs_pywinauto/)

### Sayılar, Sayılar Arası Dönüşüm ve Matematik

#### Tabanlı Sayılar

| Taban  | Ön ek           | Örnek                | Çıktı         |
| ------ | --------------- | -------------------- | ------------- |
| 2'lik  | `0b` ya da `0B` | `print(0b1101011)`   | 107           |
| 8'lik  | `0o` ya da `0O` | `print(0xFB + 0b10)` | 253 (251 + 2) |
| 16'lık | `0x` ya da `0X` | `print(0o15)`        | 13            |

#### Ondalıklı Sayılar (Decimals / Floats)

```py
>>> (1.1 + 2.2) == 3.3
False
>>> 1.1 + 2.2
3.3000000000000003
```

```py
import decimal

print(0.1) # 0.1
print(decimal.Decimal(0.1)) # Decimal('0.1000000000000000055511151231257827021181583404541015625')
```

```py
from decimal import Decimal as D

print(D('1.1') + D('2.2')) #  Decimal('3.3')
print(D('1.2') * D('2.50')) # Decimal('3.000')
```

##### Decimal Float Kullanımları ve Farkı

- Decimal daha fazla bellek kaplar
- Finansal işlemlerde decimal tercih edilir

#### Kesirli Sayılar (Fractions)

```py
import fractions

print(fractions.Fraction(1.5)) # 3/2
print(fractions.Fraction(5)) # 5
print(fractions.Fraction(1,3)) # 1/3
```

```py
import fractions

# Floatlar virgülden sonra da sayı barındırdığından dolayı farklı sonuç verir
print(fractions.Fraction(1.1)) # 2476979795053773/2251799813685248
print(fractions.Fraction('1.1')) # 11/10
```

##### Kesirli Sayılarla İşlemler

```py
from fractions import Fraction as F

print(F(1,3) + F(1,3)) # 2/3
print(1 / F(5,6)) # 6/5
print(F(-3,10) > 0) # False
print(F(-3,10) < 0) # True
```

#### Matematik İşlemleri

```py
import math

print(math.pi) # 3.141592653589793
print(math.cos(math.pi)) # -1.0
print(math.exp(10)) # 22026.465794806718
print(math.log10(1000)) # .0
print(math.sinh(1)) # 1.1752011936438014
print(math.factorial(6)) # 720
```

##### Matematikte Rastgelelik

```py
import random

x = ['a', 'b', 'c', 'd', 'e']

print(random.randrange(10,20)) # Rastgele 10, 20 arasında sayı yazdırma
print(random.choice(x)) # Rastgele seçim yapma
random.shuffle(x) # Karıştrma
print(x) # Karışım sonucunu yazma
print(random.random()) # Rastgele eleman yazma
```

### Class

#### Class Anahtar Kelimeleri

| Anhatar                | Açıklama                               | Örnek                                                   |
| ---------------------- | -------------------------------------- | ------------------------------------------------------- |
| `self`                 | Diğer dillerdeki `this` anlamına gelir | [Basit Class Örneği](#basit-class-%C3%B6rne%C4%9Fi)     |
| `__init__`             | Constructer fonksiyonudur              | [Basit Class Örneği](#basit-class-%C3%B6rne%C4%9Fi)     |
| `def function(param):` | Fonksiyon tanımalama                   | [Metodlu Class Örneği](#metodlu-class-%C3%B6rne%C4%9Fi) |

#### Basit Class Örneği

```py
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("John", 36)

print(p1.name)
print(p1.age)
```

```cmd
John
36
```

#### Metodlu Class Örneği

```py
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("Hello my name is " + self.name)

p1 = Person("John", 36)
p1.myfunc()
```

```cmd
Hello my name is John
```

##### Obje Özelliği Silme

```py
del p1.age
```

##### Class Silme

```py
del p1
```

#### Scopes and Namespaces

```py
def scope_test():
    def do_local():
        spam = "local spam"

    def do_nonlocal():
        nonlocal spam
        spam = "nonlocal spam"

    def do_global():
        global spam
        spam = "global spam"

    spam = "test spam"
    do_local()
    print("After local assignment:", spam)
    do_nonlocal()
    print("After nonlocal assignment:", spam)
    do_global()
    print("After global assignment:", spam)

scope_test()
print("In global scope:", spam)
```

```txt
After local assignment: test spam
After nonlocal assignment: nonlocal spam
After global assignment: nonlocal spam
In global scope: global spa
```

#### Enumeration

Resmi dökümantasyon için [buraya](https://docs.python.org/3/library/enum.html) bakabilirsin.

- Sıralı ve sabit veriler oluşturmak için kullanılır
- `from enum import Enum` ile projeye dahil edilir

##### Basit Kullanım

```py
from enum import Enum

class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3

# Erişim şekli
Color.RED # 1
Color.RED.name # RED
type(Color.RED) # <enum 'Color'>
Color(1) # <Color.RED: 1>
Color(3) # <Color.BLUE: 3>
isinstance(Color.GREEN, Color) # True

# Obje olarka kullanımı
color = Color.RED
color.value # 1
color.name # RED
```

##### Enum Özellikleri

Aynı özelliklere sahip objeler oluşturulamaz

```py
# Oluşturulmaz!
class Shape(Enum):
    SQUARE = 2
    SQUARE = 3

# Oluşturabilir
class Shape(Enum):
    SQUARE = 2
    DIAMOND = 1
    CIRCLE = 3
    ALIAS_FOR_SQUARE = 2

Shape.SQUARE # <Shape.SQUARE: 2>
Shape.ALIAS_FOR_SQUARE # <Shape.SQUARE: 2>
Shape(2) # <Shape.SQUARE: 2>
```

###### Benzersin Enum Tanımlaması

`@unique` etiketi ile tanımlama yapılır

```py
from enum import Enum, unique
@unique
class Mistake(Enum):
    ONE = 1
    TWO = 2
    THREE = 3
    FOUR = 3

# Traceback (most recent call last):
# ValueError: duplicate values found in <enum 'Mistake'>: FOUR -> THREE
```

## Komut İsteminden Python (CLI)

- Komut isteminden gelen argümanları **argparse** adlı modül ile yönetmekteyiz
- Otomatik kod tamamlaması için [buraya](https://stackoverflow.com/a/15289025/9770490) bakmanda fayda var.
- Kullanıcı cmd üzerinden `python <dosya_adı> <argümanlar>` gibi komutlarla programımızı kullanabilir

### Argparse Modülü Detayları

- Argüman ekleme işlemi `parser = argparse.ArgumentParser(...)` ile yapılmaktadır.
- Parametrelerin kullanımı `argparse.ArgumentParser(description='yok')` şeklindedir.

| Parametre     | Açıklama                               |
| ------------- | -------------------------------------- |
| `description` | Uygulama ile alakalı açıklama metnidir |

### Argüman Ekleme

- Argüman ekleme işlemi `parser.add_argument(...)` ile yapılmaktadır.

| Parametre    | Açıklama                                    |
| ------------ | ------------------------------------------- |
| 1. parametre | Kısa kullanım komutunu içerir               |
| 2. Parametre | Orjinal kullanım komutunu içerir            |
| `help`       | `-h` yazıldığında çıkacak olan yardım metni |
| `action`     | Davranışı belirler                          |
| `type`       | Tip bilgisini içerir (int, string ...)      |
| `default`    | Varsayılan değer                            |

### Argüman Action Özelliği

| Parametre      | Açıklama                                                               |
| -------------- | ---------------------------------------------------------------------- |
| `'store_true'` | Flag* değeri olur ve komutta içerilirse `True` değeri alır (`-h` gibi) |
| `count`        | Kaç kere yazıldığı bilgisini tutar (-vvv için 3)                       |

```py
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("--verbose", help="increase output verbosity",
                    action="store_true")
args = parser.parse_args()
if args.verbose:
    print("verbosity turned on")
```

**Çıktısı:**

```sh
$ python3 prog.py --verbose
verbosity turned on

$ python3 prog.py --verbose 1
usage: prog.py [-h] [--verbose]
prog.py: error: unrecognized arguments: 1

$ python3 prog.py --help
usage: prog.py [-h] [--verbose]

optional arguments:
  -h, --help  show this help message and exit
  --verbose   increase output verbosity
```

### Örnek CLI Kodu

```py
import argparse

def main():
    # Initiate argument parser
    parser = argparse.ArgumentParser(
        description="Sample TensorFlow XML-to-CSV converter")
    parser.add_argument("-i",
                        "--inputDir",
                        help="Path to the folder where the input .xml files are stored",
                        type=str)
    parser.add_argument("-o",
                        "--outputFile",
                        help="Name of output .csv file (including path)", type=str)
    args = parser.parse_args()

    if args.inputDir is None:
        args.inputDir = os.getcwd()

    if args.outputFile is None:
        args.outputFile = args.inputDir + "/labels.csv"

    assert (os.path.isdir(args.inputDir))

    xml_df = xml_to_csv(args.inputDir)
    xml_df.to_csv(
        args.outputFile, index=None)
    print('Successfully converted xml to csv.')

if __name__ == '__main__':
    main()
```

## Python Görsel Programlama (GUI)

Python görsel programlama **PyQt API**'ı ile yapılmaktadır.

- Bu yazıyı oluştururken yararlandığım kaynak için [buraya](https://build-system.fman.io/pyqt5-tutorial) bakabilirsin.
- Türkçe eğitim serisi için [buraya](https://www.youtube.com/playlist?list=PLOl6SW8nLgJx9guRvfylVwrMXIginZhin) bakabilirsin.

### PyQt5 Kurulumu

GUI için *cross development* desteği olan **pyqt** kullanılmaktadır.

- `pip install pyqt5`
- `conda install pyqt`

> 💡 *Cross development*: Birden çok işletiim sisteminde çalışabilen yazılım geliştirmesi: PC, Mac, linux vs..

### Basit GUI Yapımı

GUI oluşturma yardımcı olan **QTDesigner** oldukça faydalı olacaktır. (💡 Çek-bırak mantığında çalışır. )

```py
from PyQt5.QtWidgets import QApplication, QLabel

# Uygulamayı tanımlama
# - [] objesi içine aktarılacak argümanları ifade eder
app = QApplication([])

# Pencernein içine yazı yazma ve görünür kılma
label = QLabel('~ YEmreAk')
label.show()

# Uygulamayı kullanıcı kapatana kadar çalıştırma (exec olursa arkaplanda da çalışır)
app.exec_()
```

### PyQt Widgets

PyQt deki her bir obje widget olarak adlandırılmakta

![pyqt_widgets](../images/pyqt_widgets.png)

Yukarıdan-aşağı, soldan-sağa olmak üzere sırayla:

- [QLabel](http://doc.qt.io/qt-5/qlabel.html)
- [QComboBox](http://doc.qt.io/qt-5/qcombobox.html)
- [QCheckBox](http://doc.qt.io/qt-5/qcheckbox.html)
- [QRadioButton](http://doc.qt.io/qt-5/qradiobutton.html)
- [QPushButton](http://doc.qt.io/qt-5/qpushbutton.html)
- [QTableWidget](http://doc.qt.io/qt-5/qtablewidget.html)
- [QLineEdit](http://doc.qt.io/qt-5/qlineedit.html)
- [QSlider](http://doc.qt.io/qt-5/qslider.html)
- [QProgressBar](http://doc.qt.io/qt-5/qprogressbar.html)

> Ekran görüntüsündeki kodu [buraya](https://build-system.fman.io/static/public/files/widgets_example.py) tıklayarak indirebilirsin.

## PyInstaller ile Executable Dosya Oluşturma

Video açıklaması için [buraya](https://youtu.be/lOIJIk_maO4) bakabilirsin.

## İleri Seviye Python

### Assertion (Kural Koyma)

Boolean değeri sağlanmazsa hata verir ve programı kapatır.

```py
assertion(<bool>, <açıklama>)
```

- `<bool>` Kontrol değişkeni
  - *Örn: 0 > 5*
- `<açıklama>` Hatanın neden verildiğine dair metin
  - *Örn: Küçük bir değer girildi*

#### Assertion Örnekleri

```py
def KelvinToFahrenheit(Temperature):
   assert (Temperature >= 0),"Colder than absolute zero!"
   return ((Temperature-273)*1.8)+32

print (int(KelvinToFahrenheit(505.78)))
print (KelvinToFahrenheit(-5))
```

```sh
451
Traceback (most recent call last):
  File "test.py", line 9, in <module>
    print KelvinToFahrenheit(-5)
  File "test.py", line 4, in KelvinToFahrenheit
    assert (Temperature >= 0),"Colder than absolute zero!"
AssertionError: Colder than absolute zero!
```

### Try / Except Yapısı

Olası hatalarda programın kapanmasını engelleyerek hata kontrolü sağlar.

```py
try:
    a = float("Ben sayı değilim")
except ValueError:
    print("Bu sayı değil")
```

### Dosya İşlemleri

Python üzerinde dosya işlemleri oldukça kolaydır ve `context manager` ile halledilir.

```py
with open(<dosya_ismi>, <erişim_modu>, encoding=<kodlama>) as file:
    # İşlemler
    pass
```

- `<dosya_ismi>` Dosya yolu veya ism
  - *Örn: "text.txt"*
- `<erişim_modu>` Okuma, yazma veya ekleme
  - *Örn: 'a', 'w', 'r', 'r+' ...*
- `<kodlama>` Dosya kodlama formatı
  - *Örn: 'utf-8'*

#### Dosya Okuma

```py
file_str = ""
with open("README.md", "r", encoding="utf-8") as file:
    file_str = "".join(file.readlines())

```

```py
file_str = ""
with open("README.md", "r", encoding="utf-8") as file:
    for line in file:
        file_str += line

```

```py
with open(xml_path) as fp:
        for row, line in enumerate(fp):
            pass
```

```py
with open("README.md", "r", encoding="utf-8") as file:
    lines = list(file) # Tüm satırları liste olarak döndürür
    line = file.readline() # Tek bir satırı string olarak döndürür
    lines = file.readlines() # Tüm satırları liste olarak döndürür
```

### Thread

Thread modülü ile satır satır ilerleyen kod yerine karma ilerleyen kodlar yazılabilir.

- `threading` modülü kullanılır
- Eş zamanlı işlemler için [multiprocessing](#paralel-i%CC%87%C5%9Flemler-multiprocessing) tercih edilir

| Class     | Açıklama                                  |
| --------- | ----------------------------------------- |
| Thread    | Sırasız olarak bir fonksiyonu çalıştırma  |
| Timer     | Belirli saniyelerde fonksiyonu çalıştırma |
| Scheduler | Bir plana göre fonksiyonu çalıştırma      |

#### Basit Thread Yapısı

```py
from time import sleep
from threading import Thread

def tekrarla(ne, bekleme):
    while True:
        print ne
        sleep(bekleme)

if __name__ == '__main__':
    dum = Thread(target = tekrarla, args = ("dum",1))
    tis = Thread(target = tekrarla, args = ("tis",0.5))
    ah = Thread(target = tekrarla, args = ("ah",3))

    dum.start()
    tis.start()
    ah.start()
```

```sh
dum
tis
ah

tis
dumtis

tis
dumtis

tis
ah
tisdum
```

#### Zamanlayıcı Yapısı (Timer)

```py
import threading


def run_check():
    print("Fonksiyon çalıştı.")
    threading.Timer(5.0, run_check).start()


run_check()
```

#### Bir Plana göre Fonksiyon Çalıştırma

```py
import sched, time
s = sched.scheduler(time.time, time.sleep)
def do_something(sc):
    print "Doing stuff..."
    # do your stuff
    s.enter(60, 1, do_something, (sc,))

s.enter(60, 1, do_something, (s,))
s.run()
```

### Paralel İşlemler (Multiprocessing)

Python'da eş zamanlı işler `thread` ile yapılamaz

> Kaynak için [buraya](https://stackoverflow.com/a/7207336/9770490) bakabilirsin.

#### Multiprocessing Örneği

```py
from multiprocessing import Process


def func1():
    print('func1: starting')
    for i in range(10000000):
        pass
    print('func1: finishing')


def func2():
    print ('func2: starting')
    for i in range(10000000):
        pass
    print ('func2: finishing')


if __name__ == '__main__':
    p1 = Process(target=func1)
    p1.start()
    p2 = Process(target=func2)
    p2.start()
    p1.join() # Threadi çalıştırma (gecikmesini engellemek için)
    p2.join()

# func1: starting
# func2: starting
# func2: finishing
# func1: finishing
```

### Kod Parçaları (Code Snippet)

#### PYTHONPATH Ayarlama

```py
# Tek başına çalışmak isterse
if __name__ == "__main__":
    import os
    import sys
    sys.path.append(os.getcwd())
```

#### Ekran Görünüsünü Alma ve Kaydetme

```py
from PIL import ImageGrab as ig

import numpy as np
import time
import cv2

# Hata ayıklama ve bilgilendirme notlarını aktif edery
DEBUG = True

# Çıktı kaydını aktif etme
KEEP = False

# Yakalanacak ekranın konum bilgileri (x0, y0, x1, y1)
CAPTURE_AREA = (80, 101, 1111, 923)

# Yakalanan ekranın gösterilme boyutu (Varsayılan için 0 yapın)
WIDTH = 0
HEIGHT = 0

# FPS sayacını tanımlama
if DEBUG:
    frame_count = 0
    last_time = time.time()

out = cv2.VideoWriter(
    'output.avi',
    cv2.VideoWriter_fourcc(*'XVID'),
    5.0,
    (CAPTURE_AREA[2] - CAPTURE_AREA[0], CAPTURE_AREA[3] - CAPTURE_AREA[1])
) if KEEP else None

while True:
    screen = ig.grab(bbox=CAPTURE_AREA)
    screen_np = np.array(screen)

    # BGR tipindeki görüntüyü RGB yapıyoruz
    screen_np_RGB = cv2.cvtColor(screen_np, cv2.COLOR_BGR2RGB)

    # Gösterilecek ekranın boyutunu ayarlama
    screen_width = WIDTH if WIDTH != 0 else CAPTURE_AREA[2] - CAPTURE_AREA[0]
    screen_height = HEIGHT if WIDTH != 0 else CAPTURE_AREA[3] - CAPTURE_AREA[1]

    # Kaydedilen ekranı uygun boyutta görüntüleme
    cv2.imshow(
        'Ekran görüntüsü',
        cv2.resize(
            screen_np_RGB,
            (
                screen_width,
                screen_height
            )
        )
    )

    # Dosyaya yazma
    out.write(screen_np_RGB) if KEEP else None

    # 'q' tuşuna basıldığında çıkma işlemi
    if cv2.waitKey(25) & 0xFF == ord('q'):
        out.release() if KEEP else None
        cv2.destroyAllWindows()
        break

    # FPS bilgilerini hesaplama ve ekrana basma
    if DEBUG:
        frame_count += 1
        if time.time() - last_time >= 1:
            print('FPS: {}'.format(frame_count))
            frame_count = 0
            last_time = time.time()

```

#### Kısayol ile Ekran Alanı Seçme

```py
def draw_dimension(hotkey="ctrl_l") -> tuple:
    """Ekrandan seçilen alanın koordinatlarını verir

    Keyword Arguments:
        hotkey {string} -- Klavye kısayolu (default: {None})

    Returns:
        tuple -- Seçilen alanın koordinatları `(x0, y0, x1, y1)`
    """

    # Farenin başlangıç ve bitiş konumları
    start_position, end_position = (0, 0)

    def listen_keyboard():
        with keyboard.Listener(on_press=on_press, on_release=on_release) as keyboard_listener:
            keyboard_listener.join()

    def on_press(key):
        # Başlangıç koordinatlarını oluşturma
        if key == keyboard.Key[hotkey]:
            nonlocal start_position
            start_position = mouse.Controller().position

    def on_release(key):
        # Bitiş koordinatlarını başlangıca ekleme
        if key == keyboard.Key[hotkey]:
            nonlocal end_position
            end_position = mouse.Controller().position

            # Dinleyiciyi kapatma
            return False

    print(
        f"Seçmek istediğiniz alanın başlangıç noktasına farenizi getirin ve {hotkey} tuşuna basılı tutarak farenizi alanın bitiş noktasına götürün.")

    listen_keyboard()
    return start_position + end_position

print(draw_dimension())
```

#### Url Encode İşlemi

- TODO

## Google Colabrotory Üzerinden Python

Google Colabrotory `IPython` modülünü kullanmaktadır.

> Detaylı bilgileri içeren google colabrotory notum için [buraya](../Yaz%C4%B1l%C4%B1m%20Notlar%C4%B1/Google%20Colabrotory.md) tıklayabilirsin.

### IPython Operatorleri

| Operator | Açıklama               |
| -------- | ---------------------- |
| `!`      | Bash komutları ön eki  |
| `%`      | Bash dizini ön eki (?) |

### Python Değişkenlerinin Bash Üzerinde Kullanımı

| Operatör         | Açıklama                        | Örnek                   | Çıktı  |
| ---------------- | ------------------------------- | ----------------------- | ------ |
| `$<değişken>`    | Tek değişkenler için kullanılır | `!echo $filename`       | test   |
| `{<pyton_kodu>}` | Python kodu için kullanılır     | `{"{}.test".format(1)}` | 1.test |

## Ortam Değişkenleri

- `PYTHONPATH` Python modülleri yollarını barındıran değişkendir.
  - `import` ile verilen yollardaki dizinlerden script dahil edilir

> Windows için cmd ortam değişkeni ayarlama yapısı `set name=value;value` şeklindedir.

### PyCharm Uygulmasında Ortam Değişkeni Tanımlama

- Üst sekmeden `Run` kısmına gelin
- `Edit Configuration` yazısına tıklaıyn
- Yapılandırma ayarınızı seçin
  - Yoksa `+` ile yeni bir tane oluşturun
- `Environment Variables` kısmında en sağdaki dosya simgesine tıklayın
- `+` ile yeni ortam değişkeninizi ekletin

> Windows için cmd ortam değişkeni ayarlama yapısı `set name=value;value` şeklindedir.

## Yapılacaklar

- [x] Thread ve Timer eklenecek
  - [Link1](http://ysar.net/python/threading.html), [Link2](https://stackoverflow.com/questions/474528/what-is-the-best-way-to-repeatedly-execute-a-function-every-x-seconds-in-python), [Link3](https://stackoverflow.com/questions/33473899/how-set-a-loop-that-repeats-at-a-certain-interval-in-python), [Link4](https://daanlenaerts.com/blog/2015/07/04/python-3-4-execute-function-every-five-seconds/)
- [ ] Alttaki yapı eklenecek
  - `t2 = Thread(target={time.sleep(3)})`
  - {} ile fonksiyon
  - return olursa değeri çıkarır

## Harici Kaynaklar

- [String işlemleri](https://sites.google.com/site/egitimbilgileri/home/a---python---twisted---qt/03---string-islemleri)
- [Learn Python Programming](https://www.programiz.com/python-programming)
- [Python Türkçe Başlangıç](https://github.com/fuatbeser/python-notlarim/blob/master/python_turkce_baslangic.ipynb)
- [Should I use underscores or camel case for Python?](https://www.quora.com/Should-I-use-underscores-or-camel-case-for-Python)
- [Top 10 Python Libs 2017](https://tryolabs.com/blog/2017/12/19/top-10-python-libraries-of-2017/)
- [Tensorflow Object Detection API](https://buildmedia.readthedocs.org/media/pdf/tensorflow-object-detection-api-tutorial/latest/tensorflow-object-detection-api-tutorial.pdf)
- [Dosyadak Belli Satırı Değiştirme](https://stackoverflow.com/a/2081880/9770490)
- [How do I list all files of a directory](https://stackoverflow.com/questions/3207219/how-do-i-list-all-files-of-a-directory)
- [Replace single backslash with double backslash](https://stackoverflow.com/questions/17327202/python-replace-single-backslash-with-double-backslash)
- [What does `if __name__ == '__main__':` do?](https://stackoverflow.com/questions/419163/what-does-if-name-main-do)
- [Gitignore yapılandırması](https://github.com/martinohanlon/flightlight/issues/1)
- [Ekranın Video Görüntüsünü Yakalama](https://stackoverflow.com/a/51643195/9770490)
- [Putting a simple if-then-else statement on one line](https://stackoverflow.com/a/2802748/9770490)
- [Can python get the screen shot of a specific window?](https://stackoverflow.com/a/48669645/9770490)
- [Get window position & size with python](https://stackoverflow.com/a/7142360/9770490)
- [Python inactive screen capture](https://stackoverflow.com/a/52314641/9770490)
- [Computer Screen Recording using Python & OpenCV](https://www.youtube.com/watch?v=GWdrL8dt1xQ)
- [How can I code OpenCV to use GPU using Python?](https://www.quora.com/How-can-I-code-OpenCV-to-use-GPU-using-Python)
- [Google Keep to Text](https://github.com/HardFork/KeepToText)
- [Python ile QuickDraw Projesi][Quick Draw]
- [7 Top Python GUI Frameworks][7 Top Python GUI Frameworks]
- [Python __init__.py Dosyası][Python __init__.py Dosyası]

[Python __init__.py Dosyası]: https://stackoverflow.com/questions/448271/what-is-init-py-for
[Fuatbeser Python Notları]: https://github.com/fuatbeser/python-notlarim
[Quick Draw]: https://github.com/vietnguyen91/QuickDraw
[7 Top Python GUI Frameworks]: https://insights.dice.com/2017/08/07/7-top-python-gui-frameworks/
[Slice]: https://www.webucator.com/how-to/how-slice-strings-python.cfm