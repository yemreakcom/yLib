# Python'da String İşlemleri <!-- omit in toc -->

## İçerikler <!-- omit in toc -->

- [Temel String İşlemleri](#temel-string-i%CC%87%C5%9Flemleri)
  - [String Üzerinde Karakter Değiştirme](#string-%C3%BCzerinde-karakter-de%C4%9Fi%C5%9Ftirme)
  - [Karakterleri Ters Çevirme](#karakterleri-ters-%C3%A7evirme)
  - [Cümlenin Kelimelerini Ters Çevirme](#c%C3%BCmlenin-kelimelerini-ters-%C3%A7evirme)
- [String Fonksiyonları](#string-fonksiyonlar%C4%B1)
- [String İçerisinde Metin Arama](#string-i%CC%87%C3%A7erisinde-metin-arama)
- [String Üzerinde Sayma İşlemleri](#string-%C3%BCzerinde-sayma-i%CC%87%C5%9Flemleri)
  - [Metin karakterlerini sayma](#metin-karakterlerini-sayma)
  - [Dosya satırlarını a'dan başlayarak sayma](#dosya-sat%C4%B1rlar%C4%B1n%C4%B1-adan-ba%C5%9Flayarak-sayma)
- [Harici Fonksiyonlarla String İşlemleri](#harici-fonksiyonlarla-string-i%CC%87%C5%9Flemleri)

## Temel String İşlemleri

String'ler karakter listesi olarak geçtiğinden `list` özelliklerini taşır.

| İşlem           | Açıklama                                                                |
| --------------- | ----------------------------------------------------------------------- |
| `+`, `=-` ...   | Aritmatik operatörleri destekler                                        |
| `len(string)`   | Karakter sayısı                                                         |
| `string[i]`     | `i`. karakter                                                           |
| `string[-i]`    | `len-i`. karakter (Sondan `i` kadar önceki)                             |
| `string[i:]`    | `i`. eleman ve sonrasındakiler                                          |
| `string[:i]`    | `i`. elemana kadar (`i` dahil değil) olanlar                            |
| `string[i:j]`   | `i`. eleman ve `j`. elemana kadar (`j` dahil değil) olanlar             |
| `string[-j:-i]` | `len-j`. eleman ve `len-i`. elemana kadar (`len-i` dahil değil) olanlar |

### String Üzerinde Karakter Değiştirme

Stringler `string[i] = char` yapısını desteklemez, alttaki yöntem gibi işlemler kullanılır

**Slice özelliği ile:**

```py
def change_char(string, i, char):
    return string[:i]+char+string[i+1:]
```

**List yapısı ile:**

```py
def change_char(string, i, char):
    string = list[string]
    string[i] = char
    return string.join("")
```

### Karakterleri Ters Çevirme

```py
reverse = ""
for i in range(1, len(sentence) + 1):
    reverse += sentence[-i]
```

### Cümlenin Kelimelerini Ters Çevirme

```py
words = sentence.split(' ')
for i in range(1, len(words) + 1):
    sentence += words[-i] + " "
sentence = sentence[:-1]
```

## String Fonksiyonları

Çok önemli ve ileride kullanılacak bir konudur. 🌟

- `r` ök eki ile yazılan string daha hızlı işlenir
- `replace` metodu en hızlı string değiştirme metodudur.
  - `replace(...).replace(...)` ile çoklu değişim yapılması daha hızlıdır

<!-- TODO linkleri ekle -->

| Metot                   | Açıklama                 | Örnek                                  | Çıktı                  |
| ----------------------- | ------------------------ | -------------------------------------- | ---------------------- |
| `len`                   | Uzunluk                  | `len("yemreak")`                       | `7`                    |
| `format`                | Formatlama               | `"X: {}, Y: {}".format(1, 2)`          | `'X: 1, Y: 2'`         |
| `%`                     | Operatör ile formatlama  | `'new(%s %d)' % ('help', 5)`           | `'new(help 5)'`        |
| `f`                     | Format string ön eki     | `f'X: {a}'`                            | `'X: 2'`               |
| `r`                     | Raw String ön eki        | `r"C:\Users"`                          | `C:\\Users`            |
| `"""`                   | Çok satırlı string       |
| `split`                 | Parçalama                | `"ye mre ak".split(" ")`               | `['ye', 'mre', 'ak']`  |
| `[<başlangıç>:<bitiş>]` | Kesme                    | `"yemreak".[2:5]`, `"yemreak".[-3:-1]` | `"mre"`, `"ea"`        |
| `join`                  | Birleştirme              | `','.join(['do', 're', 'mi'])`         | `'do,re,mi'`           |
| `split & join`          | Yeniden formatlama       | `arr.split("\t").join("|")`            | `'İsim|Soyisim|Numara` |
| `find`                  | Karakter indeksini bulma | `"yemreak".find('e')`                  | `1` (yoksa `-1`)       |
| `replace`               | Metin değiştirme         | `"yemreak".replace("ak", "")`          | `'yemre'`              |
| `strip`                 | Metin düzeltme           | `' abc '.strip()`                      | `'abc'`                |
| `ltrip`                 | Metnin solunu düzeltme   | `' abc '.ltrip()`                      | `'abc '`               |
| `rtrip`                 | Metnin sağını düzeltme   | `' abc '.rtrip()`                      | `' abc'`               |
| `sort`                  | Metni sıralama           | `['n', 'a', 'i']`                      | `['a', 'i', 'n']`      |

> Ek kaynaklar:
>
> - Daha fazla bilgi için [buraya](https://www.programiz.com/python-programming/methods/string) ve [buraya](https://stackoverflow.com/questions/10660435/pythonic-way-to-create-a-long-multi-line-string) bakabilirsin
> - Slice hakkında ek bilgi için [buraya][Slice - Stackoverflow] bakabilirsin
> - String değiştirme hızları kıyaslaması için [buraya][String değiştirme hızları] bakabilirsin

## String İçerisinde Metin Arama

Alttaki yöntem ile tek bir karakteri string içerisinde bulabilirsiniz.

```py
string = "yemreak"
tek_metin = "yemre"
metinler = ['emre', 'ak']

# Tek metin işlemi
if tek_metin in string:
  print("Metin bulundu")

# Çok fazla metin işlemleri
if all(metin in string for metin in metinler):
  print("Hepsi bulundu")

if any(metin in string for metin in metinler):
  print("Herhangi biri bulundu)
```

> Kaynak için [buraya][String içerisinde çoklu metin arama] bakabilirsin.

## String Üzerinde Sayma İşlemleri

### Metin karakterlerini sayma

```py
string = "Yemreak"
for i, char in enumerate(string):
  print(i, char)

# 0 Y
# 1 e
# 2 m
# ...
```

### Dosya satırlarını a'dan başlayarak sayma

```py
with open(FILE, "r") as file:
  for i, line in enumerate(file, a):
    print(f"{i}. {line}")

# a. satır
# (a+1). satır
# ...
```

## Harici Fonksiyonlarla String İşlemleri

| Paket | Fonksiyon                                | Açıklama                              |
| ----- | ---------------------------------------- | ------------------------------------- |
| `re`  | `split(<ayırıcı_karakterler>, <string>)` | Birden fazla karaktere göre parçalama |

- `<ayırıcı_karakterler>` Metni hangi karakterlere göre böleceğimizi ifade eder
  - Birden fazla olacaksa `|` ile birbirinden ayrılır
  - Ayırma sırasında `boşluk karakteri`nin kullanılması sorun oluşturur
  - *Örn:* `'\n|\t|\*'`
- `<string>` Ayrıştırılacak metin
  - *Örn:* `'yemreak.com'`

[String değiştirme hızları]: https://stackoverflow.com/a/27086669/9770490
[String içerisinde çoklu metin arama]: https://stackoverflow.com/a/3389611/9770490
