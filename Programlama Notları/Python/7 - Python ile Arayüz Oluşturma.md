# Python CLI GUI <!-- omit in toc -->

## İçerikler <!-- omit in toc -->

- [Komut İsteminden Python (CLI)](#komut-i%CC%87steminden-python-cli)
  - [Argparse Modülü Detayları](#argparse-mod%C3%BCl%C3%BC-detaylar%C4%B1)
  - [Argüman Ekleme](#arg%C3%BCman-ekleme)
  - [Argüman Action Özelliği](#arg%C3%BCman-action-%C3%B6zelli%C4%9Fi)
  - [Örnek CLI Kodu](#%C3%B6rnek-cli-kodu)
- [Python Görsel Programlama (GUI)](#python-g%C3%B6rsel-programlama-gui)
- [PyQT5](#pyqt5)
  - [PyQt5 Kurulumu](#pyqt5-kurulumu)
  - [Basit GUI Yapımı](#basit-gui-yap%C4%B1m%C4%B1)
  - [PyQt Widgets](#pyqt-widgets)
- [PyInstaller ile Executable Dosya Oluşturma](#pyinstaller-ile-executable-dosya-olu%C5%9Fturma)

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

Python görsel programlama araçları:

- PyQt5
- Tkintrer (zaten yüklü olarak gelir)
- WxPython
- Kivy (opensource)
- PyForms

## PyQT5

Python görsel programlama **PyQt API**'ı ile yapılmaktadır.

- Bu yazıyı oluştururken yararlandığım kaynak için [buraya](https://build-system.fman.io/pyqt5-tutorial) bakabilirsin.
- Türkçe eğitim serisi için [buraya](https://www.youtube.com/playlist?list=PLOl6SW8nLgJx9guRvfylVwrMXIginZhin) bakabilirsin.
- Hızlıca göz atmak için [buraya](https://www.youtube.com/watch?v=GLqrzLIIW2E) bakabilirsin

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
