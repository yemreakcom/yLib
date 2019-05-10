# 6 - Python Dosya İşlemleri <!-- omit in toc -->

## İçerikler <!-- omit in toc -->

- [Dosya Açma](#dosya-a%C3%A7ma)
  - [Dosya Erişim Modları](#dosya-eri%C5%9Fim-modlar%C4%B1)
- [Dosya Okuma](#dosya-okuma)
- [Dizin (Dir) İşlemleri](#dizin-dir-i%CC%87%C5%9Flemleri)
  - [Dizin veya Dosya Yolları Listesi Döndürme](#dizin-veya-dosya-yollar%C4%B1-listesi-d%C3%B6nd%C3%BCrme)
- [Dosya Yolu (Path) İşlemleri](#dosya-yolu-path-i%CC%87%C5%9Flemleri)

## Dosya Açma

Python üzerinde dosya işlemleri oldukça kolaydır ve `context manager` ile halledilir.

```py
with open(<dosya_ismi>, <erişim_modu>, encoding=<kodlama>) as file:
    # İşlemler
    pass
```

- `<dosya_ismi>` Dosya yolu veya ismi
  - *Örn: "text.txt"*
- `<erişim_modu>` Okuma, yazma veya ekleme
  - *Örn: 'a', 'w', 'r', 'r+' ...*
- `<kodlama>` Dosya kodlama formatı
  - *Örn: 'utf-8'*

### Dosya Erişim Modları

| Mod | Anlamı          | Açıklama                                                |
| --- | --------------- | ------------------------------------------------------- |
| `r` | Read (Okuma)    | Dosya varsa okumak için açar yoksa hata verir           |
| `w` | Write (Yazma)   | Dosyayı sıfırdan yazmak için oluşturma (verileri siler) |
| `a` | Append (Ekleme) | Dosyayı üzerine eklemek için açar, yoksa oluşturur      |

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
  - *Örn: `*.txt`, `../help`*

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
| `splittext(<dosya_adı>)`    | Dosyanın yolunu ve uzantısını döndürür (path, ext) |

- `<yol>` Path, dosya yolu
  - *Örn: C:\Users\Username\help.txt*
- `<dosya_adı>` Dosyanın uzantısıyla birlikteki adı
  - *Örn: help.txt*
