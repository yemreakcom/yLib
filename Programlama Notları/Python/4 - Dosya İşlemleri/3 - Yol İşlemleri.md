# 🚩 Yol İşlemleri (Path)

## 👨‍🏫 Önemli Hususlar

Yol işlemleri için `os.path` modülü kullanılır.

- İşletim sistemlerindeki farklılıkları engellemek için `os.path.normpath` metodunu kullan
- Yolları birleştirmek için `\` veya `/` **kullanma**, işletim sistemlerine göre değişen `os.path.join` metodunu kullan
- Yolun doğruluğu `os.path.exists` ile kontrol etmeden işlem yapma


## 🌟 Sık Kullanılan Metodlar

> Metodların kulalnımı `os.path.<metod>` şeklindedir

| Metod                       | Açıklama                                            |
| --------------------------- | --------------------------------------------------- |
| `exists(<yol>)`             | Yolun doğruluğu kontrol etme                        |
| `isfile(<yol>)`             | Dosya mı kontrolü                                   |
| `isdir(<yol>)`              | Dizin mi kontrolü                                   |
| `join(<yol1>, <dosya_adı>)` | Yolları birleştirme                                 |
| `normpath<yol>`             | Yoldaki fazladan `\` `/` gibi karakterleri kaldırma |
| `basename(<yol>)`           | Dosyanın adını ve uzantısını bulma                  |
| `splitext(<dosya_adı>)`     | Dosyanın yolunu ve uzantısını döndürür (path, ext)  |

- `<yol>` Path, dosya yolu
  - _Örn: C:\Users\Username\help.txt_
- `<dosya_adı>` Dosyanın uzantısıyla birlikteki adı
  - _Örn: help.txt_

## 🗂 Dizin veya Dosya Yolunu Bulma

### Dosyanın Gerçek Yolu3

```py
filepath = os.path.realpath(__file__)
```

### Script Dosyasının Gerçek Dizini

```py
import os 
dir_path = os.path.dirname(os.path.realpath(__file__))
```

### Çalışma Dizini Yolu
```py
import os
cwd = os.getcwd()
```
