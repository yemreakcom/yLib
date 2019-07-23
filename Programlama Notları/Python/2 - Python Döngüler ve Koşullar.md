# Python Döngüler ve Koşullar <!-- omit in toc -->

## İçerikler <!-- omit in toc -->

- [If / Else Koşul (Constraints) Yapısı](#if--else-ko%c5%9ful-constraints-yap%c4%b1s%c4%b1)
  - [Üçlü (Ternary) If / Else Yapısı](#%c3%9c%c3%a7l%c3%bc-ternary-if--else-yap%c4%b1s%c4%b1)
- [Döngüler (Loop)](#d%c3%b6ng%c3%bcler-loop)
  - [For Döngüsü](#for-d%c3%b6ng%c3%bcs%c3%bc)
    - [Değişken içinde For Döngüsü](#de%c4%9fi%c5%9fken-i%c3%a7inde-for-d%c3%b6ng%c3%bcs%c3%bc)
    - [İki Liste Üzerinde Paralel For Döngüsü](#%c4%b0ki-liste-%c3%9czerinde-paralel-for-d%c3%b6ng%c3%bcs%c3%bc)
  - [Range Fonksiyonu](#range-fonksiyonu)
  - [While Döngüsü](#while-d%c3%b6ng%c3%bcs%c3%bc)
- [Break / Continue](#break--continue)
- [Operatörler](#operat%c3%b6rler)
  - [Aritmatik Operatörler](#aritmatik-operat%c3%b6rler)
    - [Ek Aritmatik Operatörler](#ek-aritmatik-operat%c3%b6rler)
  - [Karşılaştırma Operatörleri](#kar%c5%9f%c4%b1la%c5%9ft%c4%b1rma-operat%c3%b6rleri)
  - [Mantıksal Operatörler](#mant%c4%b1ksal-operat%c3%b6rler)
  - [Bit Düzeyinde Operatörler](#bit-d%c3%bczeyinde-operat%c3%b6rler)
  - [Kimlik Belirleme Operatörleri](#kimlik-belirleme-operat%c3%b6rleri)
    - [Kimlik Belirleme Operatörleri Örneği](#kimlik-belirleme-operat%c3%b6rleri-%c3%96rne%c4%9fi)
  - [Üyelik Operatörleri](#%c3%9cyelik-operat%c3%b6rleri)
    - [Üyelik Operatörleri Örneği](#%c3%9cyelik-operat%c3%b6rleri-%c3%96rne%c4%9fi)

## If / Else Koşul (Constraints) Yapısı

If içerisine yazılan koşul otomatik olarak `bool` değişkenine dönüştürülür, değer `True` ise içindeki kodlar çalıştırılır.

- `None`, `""`, `0` gibi değerler `False` değerine denktir
- `:` ile if / else satırı sonlandırılır
- `Tab` kadar boşluk atılırsa if scope\*'u içerisinde olur

```python
num = float(input("Sayı giriniz: "))
if num >= 0:
    if num == 0:
        print("Sıfır")
    elif num == 1:
        print("Bir")
    else:
        print("Pozitif sayı")
else:
    print("Negatif sayı")
```

### Üçlü (Ternary) If / Else Yapısı

```python
fruit = 'Apple'
isApple = True if fruit == 'Apple' else False
```

## Döngüler (Loop)

### For Döngüsü

```python
sayilar = [6, 5, 3, 8, 4, 2, 5, 4, 11]
toplam = 0 # Toplam değeri tutacak değişken

for sayi in sayilar: # Liste üzerinde döngü ile ilerleme
  toplam = toplam + sayi

print("Toplam değer:", sum) # Toplam Değer: 48
```

#### Değişken içinde For Döngüsü

```python
values = [item.value for item in Fruit]  # [4, 5, 6]
values = set(item.value for item in Fruit)  # {4, 5, 6}
```

#### İki Liste Üzerinde Paralel For Döngüsü

```python
for num, cheese, color in zip([1,2,3], ['manchego', 'stilton', 'brie'],
                              ['red', 'blue', 'green']):
    print('{} {} {}'.format(num, color, cheese))
```

```sh
1 red manchego
2 blue stilton
3 green brie
```

### Range Fonksiyonu

- Python 2'deki `xrange` metoduna eş değerdir.
- `generator` tipinde veri döndürür
- Sadece döngüler ile verilerine erişilebilir

```python
# for i in <range>:
for i in range(0,3):
    print(i)
```

| Kullanım             | Çıktı                            |
| -------------------- | -------------------------------- |
| `range(10)`          | `[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]` |
| `range(2, 8)`        | `[2, 3, 4, 5, 6, 7]`             |
| `range(2, 20, 3)`    | `[2, 5, 8, 11, 14, 17]`          |
| `reversed(range(3))` | `2 1 0`                          |

### While Döngüsü

```python
sayac = 0

while sayac < 3:
    print("Döngü içinde")
    sayac = sayac + 1
else:
    print("Döngü dışında")
```

```out
Döngü içinde
Döngü içinde
Döngü içinde
Döngü dışında
```

## Break / Continue

```python
for deger in "string":
    if deger == "i":
        break # Döngüyü sonlandırır
    if deger == "t"
        continue # Döngüdeki adımı sonlandırır
    print(deger)

print("Son")
```

```out
s
r
Son
```

## Operatörler

| Operatör                             | Açıklama |
| ------------------------------------ | -------- |
| `\` | Satır atlatmayı geçersiz kılma |

### Aritmatik Operatörler

| Operatör         | Açıklama                                |
| ---------------- | --------------------------------------- |
| `+, -, /, *`     | 4 işlem                                 |
| `=`              | Atama işlemi                            |
| `a, b = c, d`    | Tek satırda çoklu atama                 |
| `+=, -=, /=, *=` | Kendisiyle işleme sokup kendisine atama |
| `<operatör>=`    | Kendisiyle işleme sokup kendisine atama |
| `( )`            | Parantej ile öncelik belirleme          |

> `<operatör>` herhangi bir operatörü temsil eder.

#### Ek Aritmatik Operatörler

| Operatör | Açıklama             | Örnek     | Çıktı |
| -------- | -------------------- | --------- | ----- |
| `%`      | Mod alma işlemi      | `6 % 2`   | `0`   |
| `**`     | Kuvvet alma          | `6 ** 2`  | `36`  |
| `//`     | Kalansız bölümü alma | `13 // 2` | `6`   |

### Karşılaştırma Operatörleri

| Operatör | Açıklama   | Örnek    | Çıktı   |
| -------- | ---------- | -------- | ------- |
| `>`      | Büyük      | `3 > 2`  | `True`  |
| `<`      | Küçük      | `3 < 2`  | `False` |
| `==`     | Eşit       | `3 == 3` | `True`  |
| `!=`     | Eşit değil | `2 != 2` | `False` |
| `>=`     | Büyük eşit | `2 >= 5` | `False` |
| `<=`     | Küçük eşit | `2 <= 2` | `True`  |

### Mantıksal Operatörler

| Operatör | Açıklama    | Örnek            | Çıktı   |
| -------- | ----------- | ---------------- | ------- |
| `and`    | Ve işlemi   | `True and False` | `False` |
| `or`     | Veya işlemi | `False or True`  | `True`  |
| `not`    | Değili      | `not False`      | `True`  |

### Bit Düzeyinde Operatörler

| Operatör | Açıklama      | Örnek                     |
| -------- | ------------- | ------------------------- |
| `&`      | Ve            | `x & y = 0 (0000 0000)`   |
| `|`      | Veya          | `x | y = 14 (0000 1110)`  |
| `~`      | Değili        | `~ x = -11 (1111 0101)`   |
| `^`      | XOR           | `x ^ y = 14 (0000 1110)`  |
| `>>`     | Sağa kaydırma | `x >> 2 = 2 (0000 0010)`  |
| `<<`     | Sola kaydırma | `x << 2 = 40 (0010 1000)` |

### Kimlik Belirleme Operatörleri

| Operatör | Açıklama                  | Örnek                     | Çıktı   |
| -------- | ------------------------- | ------------------------- | ------- |
| `is`     | Aynı objeye işaret etme   | `[1, 2, 3] and [1, 2, 3]` | `False` |
| `is not` | Farklı objeye işaret etme | `1 is not 1`              | `False` |

> Ek değişkenlerde objelerin adresleri farklı olduğunda ilk çıktı `False` olur.

#### Kimlik Belirleme Operatörleri Örneği

```python
x1 = 5
y1 = 5
x2 = 'Hello'
y2 = 'Hello'
x3 = [1,2,3]
y3 = [1,2,3]

# Output: False
print(x1 is not y1)

# Output: True
print(x2 is y2)

# Output: False
print(x3 is y3)
```

### Üyelik Operatörleri

| Operatör | Açıklama    | Örnek        | Çıktı   |
| -------- | ----------- | ------------ | ------- |
| `in`     | Anahtar var | `5 in x`     | `False` |
| `not in` | Anahtar yok | `1 not in x` | `False` |

> `x = [1, 2, 3, 4]`

#### Üyelik Operatörleri Örneği

```python
x = 'Hello world'
y = {1:'a',2:'b'}

print('H' in x) # True
print('hello' not in x) # True (h'si büyük değil)
print(1 in y) # True
print('a' in y) # False ('a' bir değerdir anahtar değildir)
```
