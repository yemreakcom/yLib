# 6 - Python Dosya İşlemleri <!-- omit in toc -->

## İçerikler <!-- omit in toc -->

- [Dosya Açma](#Dosya-A%C3%A7ma)
  - [Dosya Erişim Modları](#Dosya-Eri%C5%9Fim-Modlar%C4%B1)
- [Dosya Okuma](#Dosya-Okuma)
- [Dizin (Dir) İşlemleri](#Dizin-Dir-%C4%B0%C5%9Flemleri)
  - [Dizin veya Dosya Yolları Listesi Döndürme](#Dizin-veya-Dosya-Yollar%C4%B1-Listesi-D%C3%B6nd%C3%BCrme)
- [Dosya Yolu (Path) İşlemleri](#Dosya-Yolu-Path-%C4%B0%C5%9Flemleri)
- [Raporlama İşlemleri (Logging)](#Raporlama-%C4%B0%C5%9Flemleri-Logging)
- [EXE'ye çevirme](#EXEye-%C3%A7evirme)

## Dosya Açma

Python üzerinde dosya işlemleri oldukça kolaydır ve `context manager` ile halledilir.

```py
with open(<dosya_ismi>, <erişim_modu>, encoding=<kodlama>) as file:
    # İşlemler
    pass
```

- `<dosya_ismi>` Dosya yolu veya ismi
  - _Örn: "text.txt"_
- `<erişim_modu>` Okuma, yazma veya ekleme
  - _Örn: 'a', 'w', 'r', 'r+' ..._
- `<kodlama>` Dosya kodlama formatı
  - _Örn: 'utf-8'_

### Dosya Erişim Modları

| Mod | Anlamı          | Açıklama                                                |
| --- | --------------- | ------------------------------------------------------- |
| `r` | Read (Okuma)    | Dosya varsa okumak için açar yoksa hata verir           |
| `w` | Write (Yazma)   | Dosyayı sıfırdan yazmak için oluşturma (verileri siler) |
| `a` | Append (Ekleme) | Dosyayı üzerine eklemek için açar, yoksa oluşturur      |

> Ek bilgiler için [buraya][dosya erişim modları] bakabilirsin.

## Dosya Okuma

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

```py
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
```

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

```py
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
