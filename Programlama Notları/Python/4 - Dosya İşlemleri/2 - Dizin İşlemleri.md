# 🗂 Dizin İşlemleri (Dir)

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

## OS Modülü

| Metod                         | Açıklama                                                   |
| ----------------------------- | ---------------------------------------------------------- |
| `os.path.dirname(<path>)`     | Bulunduğu dizinin adını alma                               |
| `os.path.basename(<path>)`    | Dosya (uzantı ile) veya dizin adını alma                   |
| `os.path.normpath(<path>)`    | OS'lar için farklılık gösteren `/`, `\\` sorununu düzeltme |
| `os.path.join(<path>, <str>)` | Path birleştirme (tanımlama)                               |
| `os.path.relpath(<path>)`     | Relative path'e çevirir (`.` `..` ile )                    |
| `os.path.realpath(<path>)`    | Tam path değerini verir                                    |
| `os.mkdir(<path>)`            | Dizin oluşturma                                            |
| `os.walk(<path>)`             | Verilen path üzerinden ilerleme                            |
| `os.path.splittext(<path>)`   | Adı ve uzantısına göre ayırma                              |

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

### Dizinleri Tree Yapısında Listeleme

```py
def list_files(startpath):
    for root, dirs, files in os.walk(startpath):
        level = root.replace(startpath, '').count(os.sep)
        indent = ' ' * 4 * (level)
        print('{}{}/'.format(indent, os.path.basename(root)))
        subindent = ' ' * 4 * (level + 1)
        for f in files:
            print('{}{}'.format(subindent, f))
```

#### Gizli Dosyaları Atlayarak Listeleme

```py
for root, dirs, files in os.walk(path):
    print root

    dirs[:] = [d for d in dirs if not d.startswith('.')]

    for dir in dirs:
        print os.path.join(root, dir)
    for file in files:
        print os.path.join(root, file)
```

#### İstenen Dizinleri Atlayarak Listeleme

```py
for root, dirs, files in os.walk(path):
    if root in ignore_list:
        dirs[:] = []
        files[:] = []
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

