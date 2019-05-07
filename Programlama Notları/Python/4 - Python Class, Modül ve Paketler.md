# Python Class, Modül ve Paketler <!-- omit in toc -->

## İçerikler <!-- omit in toc -->

- [Class](#class)
  - [Class Anahtar Kelimeleri](#class-anahtar-kelimeleri)
  - [Basit Class Örneği](#basit-class-%C3%B6rne%C4%9Fi)
  - [Metodlu Class Örneği](#metodlu-class-%C3%B6rne%C4%9Fi)
    - [Obje Özelliği Silme](#obje-%C3%B6zelli%C4%9Fi-silme)
    - [Class Silme](#class-silme)
  - [Enumeration](#enumeration)
    - [Basit Kullanım](#basit-kullan%C4%B1m)
    - [Fonksiyon API ile Kullanım](#fonksiyon-api-ile-kullan%C4%B1m)
    - [Enum Özellikleri](#enum-%C3%B6zellikleri)
      - [Benzersin Enum Tanımlaması](#benzersin-enum-tan%C4%B1mlamas%C4%B1)
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

## Class

### Class Anahtar Kelimeleri

| Anhatar                | Açıklama                               | Örnek                                                   |
| ---------------------- | -------------------------------------- | ------------------------------------------------------- |
| `self`                 | Diğer dillerdeki `this` anlamına gelir | [Basit Class Örneği](#basit-class-%C3%B6rne%C4%9Fi)     |
| `__init__`             | Constructer fonksiyonudur              | [Basit Class Örneği](#basit-class-%C3%B6rne%C4%9Fi)     |
| `def function(param):` | Fonksiyon tanımalama                   | [Metodlu Class Örneği](#metodlu-class-%C3%B6rne%C4%9Fi) |

### Basit Class Örneği

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

### Metodlu Class Örneği

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

#### Obje Özelliği Silme

```py
del p1.age
```

#### Class Silme

```py
del p1
```

### Enumeration

Resmi dökümantasyon için [buraya](https://docs.python.org/3/library/enum.html) bakabilirsin.

- Sıralı ve sabit veriler oluşturmak için kullanılır
- `from enum import Enum` ile projeye dahil edilir

#### Basit Kullanım

```py
from enum import Enum

class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3

# Erişim şekli
Color # <enum 'Color'>
Color.RED.value # 1
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

#### Fonksiyon API ile Kullanım

```py
ornek = Enum('Color', 'ANT BEE CAT DOG')
print(ornek) # <enum 'Color'>
```

#### Enum Özellikleri

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

##### Benzersin Enum Tanımlaması

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

## Modüller

Her python dosyasına modül denir.

- `import` ile dahil edilirler
- `.` ile içlerindekilere erişilir

### Modül Kullanım Örnekleri

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

### Python Modül Dosyaları

Modül dosyalarının aranma yerleri:

- Çalışılan dizin
- Ortam değişkenlerindeki `PYTHONPATH` değişkeni değeri
- Kuruluma bağlı varsayılan dizin

#### Sistemin Python Modüllerine Bakma

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

### Modül İçinde Tanımlanan İsimleri Alma

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

## Paketler (Package)

- Birden fazla modülü içinde barındırır
- `.` ile modüllere erişilir
  - Tekrar `.` atılırsa modülün içindekilere erişilir

### Paketten ve Modül Örnekleri

```py
import Game.Level.start
```

```py
from Game.Level import start
```

```py
from Game.Level.start import select_difficulty
```

### Sık Kullanılan Paketler

| Modül                                                                                          | Odaklantığı İşlemler |
| ---------------------------------------------------------------------------------------------- | -------------------- |
| [os](https://www.pythonforbeginners.com/os/pythons-os-module)                                  | İşletim sistemi      |
| time                                                                                           | Zaman                |
| [datetime](https://www.pythonforbeginners.com/basics/python-datetime-timedelta)                | Tarih                |
| [numpy](https://s3.amazonaws.com/assets.datacamp.com/blog_assets/Numpy_Python_Cheat_Sheet.pdf) | Matematiksel         |
| [openCV](https://docs.opencv.org/3.0-last-rst/opencv_cheatsheet.pdf)                           | Görüntü              |
| [pillow](https://pillow.readthedocs.io/en/stable/)                                             | Resim                |
| Tensorflow                                                                                     | Makine öğrenimi      |

#### Windows Paketleri

| Modül       | Odaklandığı İşlemler                                                | Dökümanlar                                                                                                                                                                                       |
| ----------- | ------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| pywinauto ☆ | Önplanda olmasalar dahi windows uygulamaları (pywin32'i barındırır) | [🌐](https://pywinauto.readthedocs.io/en/latest/index.html) [📺](https://www.youtube.com/watch?v=mhNIHgJPP3g) [📥](https://pywinauto.readthedocs.io/en/latest/#installation)                     |
| pygetwindow | Windows pencereleri (basit)                                         | [🌐](https://github.com/asweigart/PyGetWindow)                                                                                                                                                   |
| pywin32     | Resmi windows API (pencere dahil)                                   | [🌐](http://timgolden.me.uk/pywin32-docs/contents.html) [📺]([https://www.youtube.com/watch?v=o-k6l6ea3Lg](https://www.youtube.com/watch?v=o-k6l6ea3Lg)) [📥](https://pypi.org/project/pywin32/) |
| pyautogui   | Arayüz, fare, klavye ...                                            | [📃](https://media.readthedocs.org/pdf/pyautogui/latest/pyautogui.pdf) [📺](https://www.youtube.com/watch?v=xOfBezEDZ24)                                                                         |

#### Görüntü İşleme Paketleri

| Modül       | Açılkama                 | Dökümanlar                                                       |
| ----------- | ------------------------ | ---------------------------------------------------------------- |
| pillow      | Python resim kütüphanesi |                                                                  |
| opencv      | Görüntü işleme           | [📃](https://docs.opencv.org/3.0-last-rst/opencv_cheatsheet.pdf) |
| pytesseract | Görüntüdeki yazıyı bulma | [🌐](https://pypi.org/project/pytesseract/)                      |

#### Giriş Çıkış (I/O) Kontrol Paketleri

| Paket  | Odaklanığı İşlemler | Dökümanlar                                                                                                                                                                  |
| ------ | ------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| pynput | Fare, klavye vs...  | [🌐](https://pynput.readthedocs.io/en/latest/index.html) [📃](https://media.readthedocs.org/pdf/pynput/latest/pynput.pdf) [📺](https://www.youtube.com/watch?v=kJshtCfqCsY) |

### Paketler için Harici Bağlantıları

- [Python Kütüphaneleri](https://docs.python.org/3/library/)
- [Argparse Tutorial](https://docs.python.org/3/howto/argparse.html)
- [PyAutoGUI vs Pywinauto](https://www.reddit.com/r/Python/comments/8bymeo/pyautogui_vs_pywinauto/)
