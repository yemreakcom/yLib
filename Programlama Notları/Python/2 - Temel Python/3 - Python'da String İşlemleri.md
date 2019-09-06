# Python'da String İşlemleri <!-- omit in toc -->

_String_'lere kabaca **metin** diyebiliriz 🤔

## Temel String İşlemleri

String'ler karakter listesi olarak geçtiğinden `list` özelliklerini taşır.

| İşlem                    | Açıklama                                                                |
| ------------------------ | ----------------------------------------------------------------------- |
| `+`, `=-` ...            | Aritmatik operatörleri destekler                                        |
| `len(string)`            | Karakter sayısı                                                         |
| `string[i]`              | `i`. karakter                                                           |
| `string[-i]`             | `len-i`. karakter (Sondan `i` kadar önceki)                             |
| `string[i:]`             | `i`. eleman ve sonrasındakiler                                          |
| `string[:i]`             | `i`. elemana kadar (`i` dahil değil) olanlar                            |
| `string[i:j]`            | `i`. eleman ve `j`. elemana kadar (`j` dahil değil) olanlar             |
| `string[-j:-i]`          | `len-j`. eleman ve `len-i`. elemana kadar (`len-i` dahil değil) olanlar |
| `'{:>i}'.format('test')` | `i` karakter ayırır metni sağa yaslar                                   |
| `'{:i}'.format('test')`  | `i` karakter ayırır metni sola sağlar                                   |

> Detaylar için [string formatlama] sayfasına bakabilirsin.

## String Fonksiyonları

Çok önemli ve ileride kullanılacak bir konudur. 🌟

- `r` ök eki ile yazılan string daha hızlı işlenir
- `replace` metodu en hızlı string değiştirme metodudur.
  - `replace(...).replace(...)` ile çoklu değişim yapılması daha hızlıdır

<!-- TODO linkleri ekle -->

| Metot                   | Açıklama                 | Örnek                                  | Çıktı                 |
| ----------------------- | ------------------------ | -------------------------------------- | --------------------- |
| `len`                   | Uzunluk                  | `len("yemreak")`                       | `7`                   |
| `format`                | Formatlama               | `"X: {}, Y: {}".format(1, 2)`          | `'X: 1, Y: 2'`        |
| `lower`, `upper`        | Küçük / büyük harf       | `"As".lower()`, `"As".upper()`         | `"as"`, `AS`          |
| `%`                     | Operatör ile formatlama  | `'new(%s %d)' % ('help', 5)`           | `'new(help 5)'`       |
| `f`                     | Format string ön eki     | `f'X: {a}'`                            | `'X: 2'`              |
| `r`                     | Raw String ön eki        | `r"C:\Users"`                          | `C:\\Users`           |
| `u`                     | Unicode string ön eki    |                                        |                       |
| `"""`                   | Çok satırlı string       |                                        |                       |
| `split`                 | Parçalama                | `"ye mre ak".split(" ")`               | `['ye', 'mre', 'ak']` |
| `[<başlangıç>:<bitiş>]` | Kesme                    | `"yemreak".[2:5]`, `"yemreak".[-3:-1]` | `"mre"`, `"ea"`       |
| `join`                  | Birleştirme              | `','.join(['do', 're', 'mi'])`         | `'do,re,mi'`          |
| `split`                 | Yeniden formatlama       | `"Selam ben".split(" ")`               | `["Selam", "Ben"]`    |
| `find`                  | Karakter indeksini bulma | `"yemreak".find('e')`                  | `1` (yoksa `-1`)      |
| `replace`               | Metin değiştirme         | `"yemreak".replace("ak", "")`          | `'yemre'`             |
| `strip`                 | Metin düzeltme           | `' abc '.strip()`                      | `'abc'`               |
| `ltrip`                 | Metnin solunu düzeltme   | `' abc '.ltrip()`                      | `'abc '`              |
| `rtrip`                 | Metnin sağını düzeltme   | `' abc '.rtrip()`                      | `' abc'`              |
| `sort`                  | Metni sıralama           | `['n', 'a', 'i']`                      | `['a', 'i', 'n']`     |

> Ek kaynaklar:
>
> - Daha fazla bilgi için [buraya](https://www.programiz.com/python-programming/methods/string) ve [buraya](https://stackoverflow.com/questions/10660435/pythonic-way-to-create-a-long-multi-line-string) bakabilirsin
> - Slice hakkında ek bilgi için [buraya][slice - stackoverflow] bakabilirsin
> - String değiştirme hızları kıyaslaması için [buraya][string değiştirme hızları] bakabilirsin

### String Üzerinde Karakter Değiştirme

Stringler `string[i] = char` yapısını desteklemez, alttaki yöntem gibi işlemler kullanılır

**Slice özelliği ile:**

```python
def change_char(string, i, char):
    if i != -1:
        return string[:i]+char+string[i+1:]
    else:
        return string[:i]+char
```

### String'in Karakterleri Ters Çevirme

```python
def reverse_char(sentence):
    rev = ""
    for i in range(1, len(sentence) + 1):
        rev += sentence[-i]

    return rev
```

### String'in Kelimelerini Ters Çevirme

```python
def reverse_word(sentence):
    words = sentence.split(' ')
    for i in range(1, len(words) + 1):
        sentence += words[-i] + " "

    return sentence[:-1] # Sondaki, fazladan ' ' karakteri kaldırılıyor
```

## String İçerisinde Metin Arama

Alttaki yöntem ile tek bir karakteri string içerisinde bulabilirsiniz.

```python
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

> Kaynak için [buraya][string içerisinde çoklu metin arama] bakabilirsin.

## String Üzerinde Sayma İşlemleri

### Metin karakterlerini sayma

```python
string = "Yemreak"
for i, char in enumerate(string):
  print(i, char)

# 0 Y
# 1 e
# 2 m
# ...
```

### Dosya satırlarını a'dan başlayarak sayma

```python
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
  - _Örn:_ `'\n|\t|\*'`
- `<string>` Ayrıştırılacak metin
  - _Örn:_ `'yemreak.com'`

[string değiştirme hızları]: https://stackoverflow.com/a/27086669/9770490
[string içerisinde çoklu metin arama]: https://stackoverflow.com/a/3389611/9770490
[string formatlama]: https://pyformat.info/
