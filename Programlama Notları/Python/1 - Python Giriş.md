# Python Giriş <!-- omit in toc -->

<!-- TODO: Immutabble mutable kavramını açıkla -->

- Ek başlangıç yazısı için [buraya][Python türkçe başlangıç] bakabilirsin
- Kod yeteneklerini test etmek için [buraya][Python hackerrank] bakabilirsin

## İçerikler <!-- omit in toc -->

- [Python ile Programlamaya Hazırlanma](#python-ile-programlamaya-haz%C4%B1rlanma)
  - [Yazım Kuralları](#yaz%C4%B1m-kurallar%C4%B1)
  - [Çok Satırlı Kod Yazma](#%C3%A7ok-sat%C4%B1rl%C4%B1-kod-yazma)
  - [Dökümantasyon PyDoc](#d%C3%B6k%C3%BCmantasyon-pydoc)
- [Anahtar Kelimeler (Keywords)](#anahtar-kelimeler-keywords)
  - [Fonksyion Oluşturma Anahtar Kelimeleri](#fonksyion-olu%C5%9Fturma-anahtar-kelimeleri)
    - [Fonksiyon Anahtar Kelimeleri](#fonksiyon-anahtar-kelimeleri)
- [Değişkenler](#de%C4%9Fi%C5%9Fkenler)
  - [Değişkenlere Hızlı Bakış](#de%C4%9Fi%C5%9Fkenlere-h%C4%B1zl%C4%B1-bak%C4%B1%C5%9F)
  - [List](#list)
  - [Set](#set)
  - [Dictionary](#dictionary)
  - [Değersiz Değişken Tanımlama](#de%C4%9Fersiz-de%C4%9Fi%C5%9Fken-tan%C4%B1mlama)
  - [Sabit Değerler (Constants)](#sabit-de%C4%9Ferler-constants)
  - [Değişkenler Arası Dönüşüm (Casting)](#de%C4%9Fi%C5%9Fkenler-aras%C4%B1-d%C3%B6n%C3%BC%C5%9F%C3%BCm-casting)
    - [Eval Fonksiyonu ile Dönüştürme](#eval-fonksiyonu-ile-d%C3%B6n%C3%BC%C5%9Ft%C3%BCrme)
    - [İleri Seviye Değişken Dönüştürme](#i%CC%87leri-seviye-de%C4%9Fi%C5%9Fken-d%C3%B6n%C3%BC%C5%9Ft%C3%BCrme)
  - [Değişken Tipleri için Ek Kaynak](#de%C4%9Fi%C5%9Fken-tipleri-i%C3%A7in-ek-kaynak)
  - [Değişken ve Sabitlerde Gizlilik](#de%C4%9Fi%C5%9Fken-ve-sabitlerde-gizlilik)
  - [Değişkenin Tanımlı Olduğunu Kontrol Etme](#de%C4%9Fi%C5%9Fkenin-tan%C4%B1ml%C4%B1-oldu%C4%9Funu-kontrol-etme)
- [Programı Sonlandırma](#program%C4%B1-sonland%C4%B1rma)

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

> Değişkenin daha önceden tanımlandığını kontorl etme için [buraya][Değişkenin daha önceden tanımlandığını kontrol etme] bakabilirsin.

### List

Birden fazla veriyi saklamak için kullanılan değişkendir. (array)

- Birbirinden farklı değişkenleri tutabilir
- Aynı değişken birden fazla tekrar edebilir
- Hızlıca göz atmak için [buraya][List] buraya bakabilirsin

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

- Set'in kendine özgü bir yerleştirme yapısı (*hash*) vardır.
  - Bu yapı sayesinde veriler, en hızlı olacak şekilde, **karmaşık** olarak dizilir
  - List'ten daha **hızlıdır**
  - Kaynak için [buraya][Set mi yoksa list mi daha hızlı] bakabilirsin
- Birbirinden farklı değişkenleri tutabilir
- Aynı değişken birden fazla **yazılamaz** (küme özelliği)
- Tüm değerlerin *inmutable* (değiştirilemez) olması gerekmektedir
  - `myset = {[1, 2, 3]}` komutunda `[1, 2, 3]` list öğesi *mutable* olduğundan değiştirilebilir (ekleme çıkarma olabilir)
- *Indexing* (indekslenme) ve *slicing, subscription* (kesme, parçalama) işlemlerini desteklemez
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
> - [Hızlıca set açıklaması][Set]
> - [Detaylı set açıklaması][Set Detaylı]

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

### Değersiz Değişken Tanımlama

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

## Programı Sonlandırma

Alttaki metodlarla programı sonlandırabilirsin.

- `exit(<mesaj>)`
- `quit(<mesaj>)`
- `sys.exit(<mesaj>)`

<!-- ## Harici Bağlantılar -->

[List]: https://www.programiz.com/python-programming/list
[Set]: https://www.programiz.com/python-programming/set
[Set Detaylı]: https://www.datacamp.com/community/tutorials/sets-in-python
[Tuple]: https://www.programiz.com/python-programming/tuple
[Dictionary]: https://www.programiz.com/python-programming/dictionary
[Dict'ten hızlı var mı]: https://stackoverflow.com/a/40694623/9770490
[Dict'i str'a çevirme]: https://stackoverflow.com/a/4547331/9770490
[Set mi yoksa list mi daha hızlı]: https://stackoverflow.com/a/7717046/9770490
[Değişkenin daha önceden tanımlandığını kontrol etme]: https://stackoverflow.com/questions/843277/how-do-i-check-if-a-variable-exists

[Python türkçe başlangıç]: https://github.com/fuatbeser/python-notlarim/blob/master/python_turkce_baslangic.ipynb
[Python hackerrank]: https://www.hackerrank.com/domains/python
