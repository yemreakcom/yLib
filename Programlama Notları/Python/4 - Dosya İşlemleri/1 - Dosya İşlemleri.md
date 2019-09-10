# 📂 Dosya İşlemleri (File)

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

## Dosya Erişim Modları

| Mod          | Anlamı           | Açıklama                                                |
| ------------ | ---------------- | ------------------------------------------------------- |
| `r`          | Read (Okuma)     | Dosya varsa okumak için açar yoksa hata verir           |
| `w`          | Write (Yazma)    | Dosyayı sıfırdan yazmak için oluşturma (verileri siler) |
| `a`          | Append (Ekleme)  | Dosyayı üzerine eklemek için açar, yoksa oluşturur      |
| `wb, rb, ab` | Binary işlemleri | Sıkıştırılmış dosyada işlemler                          |

> Ek bilgiler için [buraya](https://stackoverflow.com/a/1466036/9770490) bakabilirsin.

## Dosyada İşlem Metodları

| Mod              | Açıklama                                             |
| ---------------- | ---------------------------------------------------- |
| `read()`         | Dosyayı komple okuma                                 |
| `readline()`     | Dosyadaki 1 satırı okuma                             |
| `readlines()`    | Dosyadaki tüm satırları `list` objesine alma         |
| `write(<metin>)` | Dosyaya metin yazma                                  |
| `close()`        | Dosyayı kapatma (context manager için gerekli değil) |


## Obje ile Dosya Okuma

```python
f = open('./data/sample.txt', 'r', encoding="utf-8")
data = f.read()
f.close()

print(data)
print(f)
```

```txt
Hello!
Congratulations!
You've read in data from a file.
<_io.TextIOWrapper name='./data/sample.txt' mode='r' encoding='UTF-8'>
```

## Context Manager ile Dosya Okuma

Döngüden çıkıldığından dosya otomatik olarak kapatılır (`f.close`)

```python
with open('./data/sample.txt', 'r', encoding="utf-8") as f:
    print(f.read())

print(f)
```

```txt
Hello!
Congratulations!
You've read in data from a file.
<_io.TextIOWrapper name='./data/sample.txt' mode='r' encoding='UTF-8'>
```

## Dosya İşlemleri Örnekleri

### Tek Satır Okuma

```python
with open('./data/sample.txt', 'r') as f:
    print(f.readline())
```

```bash
Hello!
```

### Tüm Satırları Okuma

```python
with open('./data/sample.txt', 'r') as f:
    print(f.readlines())
```

```bash
['Hello!\n', 'Congratulations!\n', "You've read in data from a file."]
```

### Diğer Erişim Örnekleri

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

## Encoding

| Komut                                      | Açıklama                                                                                               |
| ------------------------------------------ | ------------------------------------------------------------------------------------------------------ |
| `sys.stdout.reconfigure(encoding='utf-8')` | 🚀 Emoji gibi farklı formattaki metinler üzerinde çalışırken kullanılır (Terminal bunları algılayamaz) |

> [How to set sys.stdout encoding in Python 3?](https://stackoverflow.com/a/52372390/9770490)
