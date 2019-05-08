# Python Giriş <!-- omit in toc -->

## İçerikler <!-- omit in toc -->

- [Python ile Programlamaya Hazırlanma](#python-ile-programlamaya-haz%C4%B1rlanma)
  - [Yazım Kuralları](#yaz%C4%B1m-kurallar%C4%B1)
  - [Dökümantasyon PyDoc](#d%C3%B6k%C3%BCmantasyon-pydoc)
- [Anahtar Kelimeler (Keywords)](#anahtar-kelimeler-keywords)
  - [Fonksyion Oluşturma Anahtar Kelimeleri](#fonksyion-olu%C5%9Fturma-anahtar-kelimeleri)
    - [Fonksiyon Anahtar Kelimeleri](#fonksiyon-anahtar-kelimeleri)
- [Değişkenler](#de%C4%9Fi%C5%9Fkenler)
  - [Ana Değişkenler](#ana-de%C4%9Fi%C5%9Fkenler)
  - [Ek Değişkenler](#ek-de%C4%9Fi%C5%9Fkenler)
  - [Dictionary](#dictionary)
- [Değersiz Değişken Tanımlama](#de%C4%9Fersiz-de%C4%9Fi%C5%9Fken-tan%C4%B1mlama)
  - [Sabit Değerler (Constants)](#sabit-de%C4%9Ferler-constants)
  - [Değişkenler Arası Dönüşüm (Casting)](#de%C4%9Fi%C5%9Fkenler-aras%C4%B1-d%C3%B6n%C3%BC%C5%9F%C3%BCm-casting)
    - [Eval Fonksiyonu ile Dönüştürme](#eval-fonksiyonu-ile-d%C3%B6n%C3%BC%C5%9Ft%C3%BCrme)
    - [İleri Seviye Değişken Dönüştürme](#i%CC%87leri-seviye-de%C4%9Fi%C5%9Fken-d%C3%B6n%C3%BC%C5%9Ft%C3%BCrme)
  - [Değişken Tipleri için Ek Kaynak](#de%C4%9Fi%C5%9Fken-tipleri-i%C3%A7in-ek-kaynak)
  - [Değişken ve Sabitlerde Gizlilik](#de%C4%9Fi%C5%9Fken-ve-sabitlerde-gizlilik)
  - [Değişkenin Tanımlı Olduğunu Kontrol Etme](#de%C4%9Fi%C5%9Fkenin-tan%C4%B1ml%C4%B1-oldu%C4%9Funu-kontrol-etme)
- [Harici Bağlantılar](#harici-ba%C4%9Flant%C4%B1lar)

## Python ile Programlamaya Hazırlanma

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
| `pass`  | Tanımsız (null)                 |
| `is`    | Eşitlik (==)                    |
| `in`    | İçerisindeki elemanlar          |
| `with`  | Açık olduğu sürece anlamı taşır |

> Döngü veya metotların *içleri doldurulana* kadar yer kaplayıcı olarak `pass` kullanılır.

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

### Ana Değişkenler

| Tip     | Açıklama         | Örnek                 |
| ------- | ---------------- | --------------------- |
| bool    | 2'li değer, bit  | `True`                |
| int     | Sayı             | `1`                   |
| float   | Virgüllü sayı    | `1.2`                 |
| complex | Karmaşık sayılar | `2+3j`                |
| str     | String, metin    | `"Hello"` / `'Hello'` |

### Ek Değişkenler

| Tip                                                                   | Oluştuma                           | Erişim         |
| --------------------------------------------------------------------- | ---------------------------------- | -------------- |
| [List](https://www.programiz.com/python-programming/list)             | `liste = [1, 2]`                   | `liste[index]` |
| [Set](https://www.programiz.com/python-programming/set)               | `kume = {1.0, "Hello", (1, 2, 3)}` | `kume.add(1)`  |
| [Dictionary](https://www.programiz.com/python-programming/dictionary) | `site = {"adi":"yemreak"}`         | `site['adi']`  |
| [Tuple](https://www.programiz.com/python-programming/tuple)           | `konum = (1, 2)`                   | `x, y = konum` |

- `[<değişken> for <değişken> in <dizi_veya_liste> if <koşul>` İstenen koşullardaki elemanların listesini verir
  - Örn: `[x for x in a if x != 20]`

### Dictionary

> Alttaki işlemlerin her biri `dict` objesinin alt işlemidir.

| İşlem                        | Açıklama                                        |
| ---------------------------- | ----------------------------------------------- |
| `dict[<key>]` & `get(<key>)` | Anahtar ile veri alma, veri yoksa hata fırlatır |
| `dict[<key>] = <değer>`      | Belirli anahtara değer atama                    |
| `<key> in dict`              | Anahtar `dict`'e var mı kontrolü                |
| `json.dumps(dict)`           | `dict`'i `str`'a çevirme                        |

- [`Dict`'i `str`'a çevirme][Dict'i str'a çevirme]
- [`Dict`'ten hızlı bir yöntem var mı][Dict'ten hızlı var mı]

## Değersiz Değişken Tanımlama

```py
degersiz = None
```

### Sabit Değerler (Constants)

Python'da *constant*'lar yoktur. Sabit değerler büyük harfler ile belirtilir.

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

## Harici Bağlantılar

[Dict'ten hızlı var mı]: https://stackoverflow.com/a/40694623/9770490
[Dict'i str'a çevirme]: https://stackoverflow.com/a/4547331/9770490