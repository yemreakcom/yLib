# 🚩 Yol İşlemleri (Path)

Yol işlemleri için `os.path` modülü kullanılır.

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

## Dizin veya Dosya Yolunu Bulma

### Dosyanın Gerçek Yolu

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
