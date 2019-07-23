# 6 - Python Dosya İşlemleri <!-- omit in toc -->

## İçerikler <!-- omit in toc -->

- [Dosyaya Erişim](#dosyaya-eri%c5%9fim)
- [Dosya İşlemi Örnekleri](#dosya-%c4%b0%c5%9flemi-%c3%96rnekleri)
- [Dosya Erişim Modları](#dosya-eri%c5%9fim-modlar%c4%b1)
- [Dosyada İşlem Metodları](#dosyada-%c4%b0%c5%9flem-metodlar%c4%b1)
- [Dosyayı Kapatmadan Yazma İşlemleri](#dosyay%c4%b1-kapatmadan-yazma-%c4%b0%c5%9flemleri)
- [Dizin (Dir) İşlemleri](#dizin-dir-%c4%b0%c5%9flemleri)
  - [Dizin veya Dosya Yolları Listesi Döndürme](#dizin-veya-dosya-yollar%c4%b1-listesi-d%c3%b6nd%c3%bcrme)
  - [Python System Dizinlerine Erişme (System Enviroment)](#python-system-dizinlerine-eri%c5%9fme-system-enviroment)
  - [Python Kullanıcı Dizinlerine Erişme](#python-kullan%c4%b1c%c4%b1-dizinlerine-eri%c5%9fme)
- [Dosya Yolu (Path) İşlemleri](#dosya-yolu-path-%c4%b0%c5%9flemleri)
- [Raporlama İşlemleri (Logging)](#raporlama-%c4%b0%c5%9flemleri-logging)
- [EXE'ye çevirme](#exeye-%c3%a7evirme)

## Dosyaya Erişim

Python üzerinde dosya işlemleri oldukça kolaydır.

- Temel okuma metodu `open(<dosya_ismi>, <erişim_modu>, encoding=<kodlama>)` şeklindedir
  - `<dosya_ismi>` Dosya yolu veya ismi
    - _Örn: "text.txt"_
  - `<erişim_modu>` Okuma, yazma veya ekleme
    - _Örn: 'a', 'w', 'r', 'r+' ..._
  - `<kodlama>` Dosya kodlama formatı
    - _Örn: 'utf-8'_
- Dosya bulunamazsa `IOError` hatası verir

<details>
<summary>Obje ile dosya okuma</summary>

```python
f = open('./data/sample.txt', 'r')
data = f.read()
f.close()

print(data)
print(f)
```

```bash
Hello!
Congratulations!
You've read in data from a file.
<_io.TextIOWrapper name='./data/sample.txt' mode='r' encoding='UTF-8'>
```

</details>

<details>
<summary>Context manager ile dosya okume</summary>

Döngüden çıkıldığından dosya otomatik olarak kapatılır (`f.close`)

```python
with open('./data/sample.txt', 'r') as f:
    print(f.read())

print(f)
```

```bash
Hello!
Congratulations!
You've read in data from a file.
<_io.TextIOWrapper name='./data/sample.txt' mode='r' encoding='UTF-8'>
```

</details>

## Dosya İşlemi Örnekleri

<details>
<summary>Tek satır okuma</summary>

```python
with open('./data/sample.txt', 'r') as f:
    print(f.readline())
```

```bash
Hello!
```

</details>

<details>
<summary>Tüm satırları okuma</summary>

```python
with open('./data/sample.txt', 'r') as f:
    print(f.readlines())
```

```bash
['Hello!\n', 'Congratulations!\n', "You've read in data from a file."]
```

</details>

<details>
<summary>Diğer erişim örnekleri</summary>

```python
file_str = ""
with open("README.md", "r", encoding="utf-8") as file:
    file_str = "".join(file.readlines())

```

```python
file_str = ""
with open("README.md", "r", encoding="utf-8") as file:
    for line in file:
        file_str += line

```

```python
with open(xml_path) as fp:
        for row, line in enumerate(fp):
            pass
```

```python
with open("README.md", "r", encoding="utf-8") as file:
    lines = list(file) # Tüm satırları liste olarak döndürür
    line = file.readline() # Tek bir satırı string olarak döndürür
    lines = file.readlines() # Tüm satırları liste olarak döndürür

```

</details>

## Dosya Erişim Modları

| Mod          | Anlamı           | Açıklama                                                |
| ------------ | ---------------- | ------------------------------------------------------- |
| `r`          | Read (Okuma)     | Dosya varsa okumak için açar yoksa hata verir           |
| `w`          | Write (Yazma)    | Dosyayı sıfırdan yazmak için oluşturma (verileri siler) |
| `a`          | Append (Ekleme)  | Dosyayı üzerine eklemek için açar, yoksa oluşturur      |
| `wb, rb, ab` | Binary işlemleri | Sıkıştırılmış dosyada işlemler                          |

> Ek bilgiler için [buraya][dosya erişim modları] bakabilirsin.

## Dosyada İşlem Metodları

| Mod              | Açıklama                                     |
| ---------------- | -------------------------------------------- |
| `read()`         | Dosyayı komple okuma                         |
| `readline()`     | Dosyadaki 1 satırı okuma                     |
| `readlines()`    | Dosyadaki tüm satırları `list` objesine alma |
| `write(<metin>)` | Dosyaya metin yazma                          |

## Dosyayı Kapatmadan Yazma İşlemleri

Sürekli açık olan bir dosya için:

- `flush()` metodu ile değişikliklerinizi kaydetmelisiniz
- Dosyayı kapatmak için `close()` metodunu kullanın

```python
DOSYA_YOLU = "README.md"
DOSYA_MODU = "w+" # w, a, r, w+ ...
ENCODING = "utf-8" # Özel karakterleri aktif etmek için

file = open(DOSYA_YOLU, DOSYA_MODU, encoding=ENCODING)
file.flush() # Dosyaya yapılan işlemleri kaydetme
file.close() # Dosyayı kapatır
```

## Dizin (Dir) İşlemleri

Dizin işlemleri için `os` veya `glob` paketi kullanılır.

| Paket  | Fonksiyon                      | Açıklama                                         |
| ------ | ------------------------------ | ------------------------------------------------ |
| `os`   | `listdir(<yol>)`               | Dizinin içindekileri listeler                    |
| `os`   | `rename(<eski_ad>, <yeni_ad>)` | Dosya veya dizin adlandırma                      |
| `glob` | `glob(<yol_şablonu>)`          | Dosya ve dizinleri döndürür                      |
| `glob` | `iglob(<yol_şablonu>)`         | Dosya ve dizinleri generator yapısı ile döndürür |

- `<yol_şablonu>` Özel dizin sorguları
  - _Örn: `_.txt`,`../help`\*

### Dizin veya Dosya Yolları Listesi Döndürme

```python
def listfolderpaths(path=os.getcwd()):
        folderlist = []
        for name in os.listdir(path):
            pathname = os.path.join(path, name)
            if not is_private(name) and os.path.isdir(pathname):
                folderlist.append(pathname)
        return folderlist

def listfolderpaths(path=os.getcwd()):
    return [os.path.join(path, name) for name in os.listdir(path) if (not is_private(name) and os.path.isdir(os.path.join(path, name)))]

def listfilepaths(path=os.getcwd()):
    return [os.path.join(path, name) for name in os.listdir(path) if (not is_private(name) and os.path.isfile(os.path.join(path, name)))]

def list_files(image_dir, pattern):
    return [image for image in glob.glob(osp.join(image_dir, pattern))]

list_images(r"C\Users\Picture", ".jpg")
```

### Python System Dizinlerine Erişme (System Enviroment)

```python
import os, sys, site
ENVIROMENT_VAR = "WINDIR" # Sistem değişkeni isimleri

pythonpath = os.path.dirname(sys.executable) # Python.exe yolu
pythondir = os.path.dirname(sys.exec_prefix) # python.exe dizini
varname = os.environ[ENVIROMENT_VAR] # Sistem değişkenini değeri
userpath = site.getuserbase() # Kullanıcı seviyesindeki python yolu
modul_init_path = os.__file__ # Os modülünün init dosyasının yolu
```

### Python Kullanıcı Dizinlerine Erişme

Herhangi bir kullanıcı modülü (_`pip install` ile indirilenler_) vasıtasıyla erişebiliriz.

```python
import module # Herhangi bir pip ile indirilen modülü temsil eder, örn: pynput

path = module.__file__
site_packages_path = os.path.join(path, "..", "..")
```

path = module

## Dosya Yolu (Path) İşlemleri

Dosya yolu işlemleri için `os.path` modülü kullanılır.

| Metod                       | Açıklama                                           |
| --------------------------- | -------------------------------------------------- |
| `isfile(<yol>)`             | Dosya mı kontrolü                                  |
| `isdir(<yol>)`              | Dizin mi kontrolü                                  |
| `join(<yol1>, <dosya_adı>)` | Dizinleri birleştirme                              |
| `basename(<yol>)`           | Dosyanın adını ve uzantısını bulma                 |
| `splitext(<dosya_adı>)`     | Dosyanın yolunu ve uzantısını döndürür (path, ext) |

- `<yol>` Path, dosya yolu
  - _Örn: C:\Users\Username\help.txt_
- `<dosya_adı>` Dosyanın uzantısıyla birlikteki adı
  - _Örn: help.txt_

[dosya erişim modları]: https://stackoverflow.com/a/1466036/9770490

## Raporlama İşlemleri (Logging)

Raporlama işlemleri için `logging` modülü kullanılır

```python
import logging

message = "Raporlanacak"
LOG_DIR = "dosya/dizini"
LOG_FILE = "dosya.log"
FLAG = "w" # a+, r
ENCODING = "utf-8"

# Rapolamayı tanımlama
logging.basicConfig(handlers=[logging.FileHandler(LOG_DIR + LOG_FILE, FLAG, ENCODING)], level=logging.DEBUG, format='%(asctime)s: %(message)s')

logging.info("mesaj") # Raporu yazma

```

## EXE'ye çevirme

> [Exe'ye çevirme işlemi](https://nitratine.net/blog/post/convert-py-to-exe/)
