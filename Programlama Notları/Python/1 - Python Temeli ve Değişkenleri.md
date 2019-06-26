# Python Temeli ve Değişkenleri <!-- omit in toc -->

<!-- TODO: Immutabble mutable kavramını açıkla -->

- Ek başlangıç yazısı için [buraya][python türkçe başlangıç] bakabilirsin
- Kod yeteneklerini test etmek için [buraya][python hackerrank] bakabilirsin

## İçerikler <!-- omit in toc -->

- [Python ile Programlamaya Hazırlanma](#Python-ile-Programlamaya-Haz%C4%B1rlanma)
  - [Yazım Kuralları](#Yaz%C4%B1m-Kurallar%C4%B1)
  - [Modül Dökümantasyon Örneği](#Mod%C3%BCl-D%C3%B6k%C3%BCmantasyon-%C3%96rne%C4%9Fi)
  - [Çok Satırlı Kod Yazma](#%C3%87ok-Sat%C4%B1rl%C4%B1-Kod-Yazma)
  - [Dökümantasyon PyDoc](#D%C3%B6k%C3%BCmantasyon-PyDoc)
- [Anahtar Kelimeler (Keywords)](#Anahtar-Kelimeler-Keywords)
  - [Fonksyion Oluşturma Anahtar Kelimeleri](#Fonksyion-Olu%C5%9Fturma-Anahtar-Kelimeleri)
    - [Fonksiyon Anahtar Kelimeleri](#Fonksiyon-Anahtar-Kelimeleri)
- [Değişkenler](#De%C4%9Fi%C5%9Fkenler)
  - [Değişkenlere Hızlı Bakış](#De%C4%9Fi%C5%9Fkenlere-H%C4%B1zl%C4%B1-Bak%C4%B1%C5%9F)
  - [List](#List)
  - [Set](#Set)
  - [Dictionary](#Dictionary)
  - [Değersiz Değişken Tanımlama](#De%C4%9Fersiz-De%C4%9Fi%C5%9Fken-Tan%C4%B1mlama)
  - [Sabit Değerler (Constants)](#Sabit-De%C4%9Ferler-Constants)
  - [Değişkenler Arası Dönüşüm (Casting)](#De%C4%9Fi%C5%9Fkenler-Aras%C4%B1-D%C3%B6n%C3%BC%C5%9F%C3%BCm-Casting)
    - [Eval Fonksiyonu ile Dönüştürme](#Eval-Fonksiyonu-ile-D%C3%B6n%C3%BC%C5%9Ft%C3%BCrme)
    - [İleri Seviye Değişken Dönüştürme](#%C4%B0leri-Seviye-De%C4%9Fi%C5%9Fken-D%C3%B6n%C3%BC%C5%9Ft%C3%BCrme)
  - [Değişken Tipleri için Ek Kaynak](#De%C4%9Fi%C5%9Fken-Tipleri-i%C3%A7in-Ek-Kaynak)
  - [Değişken ve Sabitlerde Gizlilik](#De%C4%9Fi%C5%9Fken-ve-Sabitlerde-Gizlilik)
  - [Değişkenin Tanımlı Olduğunu Kontrol Etme](#De%C4%9Fi%C5%9Fkenin-Tan%C4%B1ml%C4%B1-Oldu%C4%9Funu-Kontrol-Etme)
- [Programı Sonlandırma](#Program%C4%B1-Sonland%C4%B1rma)

## Python ile Programlamaya Hazırlanma

Python ve Javascript en popüler diller arasındadır.

- Python kodlarının uzatıları `.py` şeklindedir.
- Windows için `.pyw` uzantılı python dosyaları `start` (veya `pythonw`) komutu ile çalıştırılabilmekte
- Python komutunu ve pip ile indiklerinizi terminal üzerinden görebilmek için aşağıdakileri ortam değişkenlerine kaydetmeniz gerekmekte
  - `python.exe`'nin yolunu
  - `pip` ile indirilen terminal üzerinden derlenebilir komutlar için de _Scripts_ yolunu
  - `pip install` komutu ile indirilen script'ler scripts dizinine gider
  - Python'ı `exe` yapmak için [auto-py-exe](https://github.com/brentvollebregt/auto-py-to-exe) aracını kullanabiilirsin

> Aralarındaki kıyaslama için [buraya][python vs javascript] bakabilirisin.

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

### Modül Dökümantasyon Örneği

```py
'''
Xenotix Python Keylogger for Windows
====================================
Coded By: Ajin Abraham <ajin25@gmail.com>
Website: http://opensecurity.in/xenotix-python-keylogger-for-windows/
GitHub: https://github.com/ajinabraham/Xenotix-Python-Keylogger

FEATURES
========
1.STORE LOGS LOCALLY
2.SEND LOGS TO GOOGLE FORMS
3.SEND LOGS TO EMAIL
4.SEND LOGS TO FTP

MINIMUM REQUIREMENTS
===================
Python 2.7: http://www.python.org/getit/
pyHook Module: http://sourceforge.net/projects/pyhook/
pyrhoncom Module: http://sourceforge.net/projects/pywin32/
pyHook Module -
Unofficial Windows Binaries for Python Extension Packages: http://www.lfd.uci.edu/~gohlke/pythonlibs/

NOTE: YOU ARE FREE TO COPY,MODIFY,REUSE THE SOURCE CODE FOR EDUCATIONAL PURPOSE ONLY.
'''
```

### Çok Satırlı Kod Yazma

Çok satırlı kod yazmak için `\` karakterini koyup <kbd>ENTER</kbd>'a basarak alt satırdan devam edebilirsin

- Alttaki iki komut birbirine eşdeğerdir

```py
python 'train.py' \
      --train_dir="/{MODELIN_CIKTI_DIZINI_YOLU}" \
      --pipeline_config_path="/{YAPILANDIRMA_DOSYASI_YOLU}" \
      {'--logtostderr' if logdir else ''}

python 'train.py' --train_dir="/{MODELIN_CIKTI_DIZINI_YOLU}" --pipeline_config_path="/{YAPILANDIRMA_DOSYASI_YOLU}" {'--logtostderr' if logdir else ''}
```

### Dökümantasyon PyDoc

- `'''` ile fonksiyonların üstüne dökümantasyon (açıklama) eklenir
- `#` ile koda yorum eklenir

```py
def func(a):
  """ 1 Değeri döndürür """
  return 1 # Döndürme keywordu
```

> [PyDoc videosu](https://www.youtube.com/watch?v=Y6TgbyfKCNM)

## Anahtar Kelimeler (Keywords)

Harici link için [buraya](https://www.programiz.com/python-programming/keyword-list) tıklayabilirsin.

| Anahtar | Anlamı                          |
| ------- | ------------------------------- |
| `is`    | Adres eşitliği (==)             |
| `in`    | İçerisindeki elemanlar          |
| `pass`  | Boş                             |
| `None`  | Tanımsız (null)                 |
| `with`  | Açık olduğu sürece anlamı taşır |

> Döngü veya metotların _içleri doldurulana_ kadar yer kaplayıcı olarak `pass` kullanılır.

### Fonksyion Oluşturma Anahtar Kelimeleri

| Anahtar  | Oluştuma                   | Erişim        |
| -------- | -------------------------- | ------------- |
| Lambda   | `m_lambda = lambda x: x*2` | `m_lambda(2)` |
| Function | `def m_func(param):`       | `m_func(5)`   |

#### Fonksiyon Anahtar Kelimeleri

| Anahtar  | Anlamı             |
| -------- | ------------------ |
| `return` | Veri döndürme      |
| `yield`  | Her çağırılmada te |

## Değişkenler

### Değişkenlere Hızlı Bakış

| Tip          | Açıklama                           | Örnek                 |
| ------------ | ---------------------------------- | --------------------- |
| bool         | 2'li değer, bit                    | `True`                |
| int          | Sayı                               | `1`                   |
| float        | Virgüllü sayı                      | `1.2`                 |
| complex      | Karmaşık sayılar                   | `2+3j`                |
| str          | String, metin                      | `"Hello"` / `'Hello'` |
| [List]       | `liste = [1, 2]`                   | `liste[index]`        |
| [Set]        | `kume = {1.0, "Hello", (1, 2, 3)}` | `kume.add(1)`         |
| [Dictionary] | `site = {"adi":"yemreak"}`         | `site['adi']`         |
| [Tuple]      | `konum = (1, 2)`                   | `x, y = konum`        |

> Değişkenin daha önceden tanımlandığını kontorl etme için [buraya][değişkenin daha önceden tanımlandığını kontrol etme] bakabilirsin.

### List

Birden fazla veriyi saklamak için kullanılan değişkendir. (array)

- Birbirinden farklı değişkenleri tutabilir
- Aynı değişken birden fazla tekrar edebilir
- Hızlıca göz atmak için [buraya][list] buraya bakabilirsin

| List Metodları               | Açıklama                                                    |
| ---------------------------- | ----------------------------------------------------------- |
| `len(list)`                  | Karakter sayısı                                             |
| `list.append(<value>)`       | Eleman ekleme                                               |
| `list[i]` veya `list.get(i)` | `i`. karakter                                               |
| `list[-i]`                   | `len-i`. karakter                                           |
| `list[i:]`                   | `i`. eleman ve sonrasındakiler                              |
| `list[:i]`                   | `i`. elemana kadar (`i` dahil değil) olanlar                |
| `list[i:j]`                  | `i`. eleman ve `j`. elemana kadar (`j` dahil değil) olanlar |

- `[<değişken> for <değişken> in <dizi_veya_liste> if <koşul>` İstenen koşullardaki elemanların listesini verir
  - Örn: `[x for x in a if x != 20]`

### Set

Küme işlemleri için kullanılır, temel küme özelliklerini taşır.

- Set'in kendine özgü bir yerleştirme yapısı (_hash_) vardır.
  - Bu yapı sayesinde veriler, en hızlı olacak şekilde, **karmaşık** olarak dizilir
  - List'ten daha **hızlıdır**
  - Kaynak için [buraya][set mi yoksa list mi daha hızlı] bakabilirsin
- Birbirinden farklı değişkenleri tutabilir
- Aynı değişken birden fazla **yazılamaz** (küme özelliği)
- Tüm değerlerin _inmutable_ (değiştirilemez) olması gerekmektedir
  - `myset = {[1, 2, 3]}` komutunda `[1, 2, 3]` list öğesi _mutable_ olduğundan değiştirilebilir (ekleme çıkarma olabilir)
- _Indexing_ (indekslenme) ve _slicing, subscription_ (kesme, parçalama) işlemlerini desteklemez
  - `myset[0]` çalışmaz

| Set Metodları                | Açıklama                  |
| ---------------------------- | ------------------------- |
| `add(<immutable>)`           | Eleman ekleme             |
| `for <isim> in <set>`        | Elemanları döngü ile alma |
| `<isim> = next(iter(<set>))` | Elemanları sıra ile alma  |

- `<immutable>` Herhangi değiştirilemez değer
  - Örn: `1`, `"yemreak"`, `tuple`, `str`, `int` vs
- `<isim>` Elemena verilecek isim
  - Örn: `i`, `e` vs

> **Ek bağlantılar:**
>
> - [Hızlıca set açıklaması][set]
> - [Detaylı set açıklaması][set detaylı]

### Dictionary

> Alttaki işlemlerin her biri `dict` objesinin alt işlemidir.

| İşlem                        | Açıklama                                        |
| ---------------------------- | ----------------------------------------------- |
| `dict[<key>]` & `get(<key>)` | Anahtar ile veri alma, veri yoksa hata fırlatır |
| `dict[<key>] = <değer>`      | Belirli anahtara değer atama                    |
| `<key> in dict`              | Anahtar `dict`'e var mı kontrolü                |
| `json.dumps(dict)`           | `dict`'i `str`'a çevirme                        |

- [`Dict`'i `str`'a çevirme][dict'i str'a çevirme]
- [`Dict`'ten hızlı bir yöntem var mı][dict'ten hızlı var mı]

### Değersiz Değişken Tanımlama

```py
degersiz = None
```

### Sabit Değerler (Constants)

Python'da _constant_'lar yoktur. Sabit değerler büyük harfler ile belirtilir.

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

### Değişkenler Arası Dönüşüm (Casting)

Değişkenin tipi öğrenmek için `type(<değişken>)` komutu kullanılır.

```py
ondalikli = 5.8
type(ondalikli) #  <class 'float'>

tam = int(5.8) # 5 atanır
type(tam) # <class 'int'>

sonuc = int(7/3.5) # 2 atanır
sonuc = int(7/3) # 2 atanır
sonuc = float(7 / 3.5) # 2.0 atanır
sonuc = 7 / 3 # 2.33 atanır

value = "False"
print(bool(value)) # True verir, bool'a takılama string içeriğine bakmaz.
print(bool("")) # False
```

#### Eval Fonksiyonu ile Dönüştürme

```py
value = "5"
print(type(value)) # <class 'str'>
print(type(eval(value))) # <class 'int'>
print(type(value)) # <class 'str'>
```

#### İleri Seviye Değişken Dönüştürme

```py
value1 = "5"
value2 = 3

print(type(value1)) # <class 'str'>
print(type(value2)) # <class 'int'>

value3 = type(value2)(value1) # Value1'i value2'nin tipine dönüştürme

print(value3) # 5
print(type(value3)) # <class 'int'>
```

### Değişken Tipleri için Ek Kaynak

- [Basic Data Types in Python](https://realpython.com/python-data-types/)

### Değişken ve Sabitlerde Gizlilik

- `__` ile gizli anlamında gelmektedir.
  - Dışarıdan sadece `_<class>.__<değişken>` şeklinde erişilebilir

> Detaylar için [buraya](https://www.bogotobogo.com/python/python_private_attributes_methods.php) bakabilirsin.

### Değişkenin Tanımlı Olduğunu Kontrol Etme

```py
if 'myVar' in locals():
  # myVar exists.
if 'myVar' in globals():
  # myVar exists.
if hasattr(obj, 'attr_name'):
  # obj.attr_name exists.
```

> Kaynak için [buraya](https://stackoverflow.com/a/843293) bakabilirsin.

## Programı Sonlandırma

Alttaki metodlarla programı sonlandırabilirsin.

- `exit(<mesaj>)`
- `quit(<mesaj>)`
- `sys.exit(<mesaj>)`

<!-- ## Harici Bağlantılar -->

[python vs javascript]: https://www.educba.com/python-vs-javascript/
[list]: https://www.programiz.com/python-programming/list
[set]: https://www.programiz.com/python-programming/set
[set detaylı]: https://www.datacamp.com/community/tutorials/sets-in-python
[tuple]: https://www.programiz.com/python-programming/tuple
[dictionary]: https://www.programiz.com/python-programming/dictionary
[dict'ten hızlı var mı]: https://stackoverflow.com/a/40694623/9770490
[dict'i str'a çevirme]: https://stackoverflow.com/a/4547331/9770490
[set mi yoksa list mi daha hızlı]: https://stackoverflow.com/a/7717046/9770490
[değişkenin daha önceden tanımlandığını kontrol etme]: https://stackoverflow.com/questions/843277/how-do-i-check-if-a-variable-exists
[python türkçe başlangıç]: https://github.com/fuatbeser/python-notlarim/blob/master/python_turkce_baslangic.ipynb
[python hackerrank]: https://www.hackerrank.com/domains/python
