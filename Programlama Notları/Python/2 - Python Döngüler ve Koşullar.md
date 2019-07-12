# Python Döngüler ve Koşullar <!-- omit in toc -->

## İçerikler <!-- omit in toc -->

- [If / Else Koşul (Constraints) Yapısı](#If--Else-Ko%C5%9Ful-Constraints-Yap%C4%B1s%C4%B1)
  - [Üçlü (Ternary) If / Else Yapısı](#%C3%9C%C3%A7l%C3%BC-Ternary-If--Else-Yap%C4%B1s%C4%B1)
- [Döngüler (Loop)](#D%C3%B6ng%C3%BCler-Loop)
  - [For Döngüsü](#For-D%C3%B6ng%C3%BCs%C3%BC)
    - [Değişken içinde For Döngüsü](#De%C4%9Fi%C5%9Fken-i%C3%A7inde-For-D%C3%B6ng%C3%BCs%C3%BC)
    - [İki Liste Üzerinde Paralel For Döngüsü](#%C4%B0ki-Liste-%C3%9Czerinde-Paralel-For-D%C3%B6ng%C3%BCs%C3%BC)
  - [Range Fonksiyonu](#Range-Fonksiyonu)
  - [While Döngüsü](#While-D%C3%B6ng%C3%BCs%C3%BC)
- [Break / Continue](#Break--Continue)
- [Operatörler](#Operat%C3%B6rler)
  - [Aritmatik Operatörler](#Aritmatik-Operat%C3%B6rler)
    - [Ek Aritmatik Operatörler](#Ek-Aritmatik-Operat%C3%B6rler)
  - [Karşılaştırma Operatörleri](#Kar%C5%9F%C4%B1la%C5%9Ft%C4%B1rma-Operat%C3%B6rleri)
  - [Mantıksal Operatörler](#Mant%C4%B1ksal-Operat%C3%B6rler)
  - [Bit Düzeyinde Operatörler](#Bit-D%C3%BCzeyinde-Operat%C3%B6rler)
  - [Kimlik Belirleme Operatörleri](#Kimlik-Belirleme-Operat%C3%B6rleri)
    - [Kimlik Belirleme Operatörleri Örneği](#Kimlik-Belirleme-Operat%C3%B6rleri-%C3%96rne%C4%9Fi)
  - [Üyelik Operatörleri](#%C3%9Cyelik-Operat%C3%B6rleri)
    - [Üyelik Operatörleri Örneği](#%C3%9Cyelik-Operat%C3%B6rleri-%C3%96rne%C4%9Fi)
- [Sayılar, Sayılar Arası Dönüşüm ve Matematik](#Say%C4%B1lar-Say%C4%B1lar-Aras%C4%B1-D%C3%B6n%C3%BC%C5%9F%C3%BCm-ve-Matematik)
  - [Tabanlı Sayılar](#Tabanl%C4%B1-Say%C4%B1lar)
  - [Ondalıklı Sayılar (Decimals / Floats)](#Ondal%C4%B1kl%C4%B1-Say%C4%B1lar-Decimals--Floats)
    - [Decimal Float Kullanımları ve Farkı](#Decimal-Float-Kullan%C4%B1mlar%C4%B1-ve-Fark%C4%B1)
    - [Kesirli Sayılar (Fractions)](#Kesirli-Say%C4%B1lar-Fractions)
    - [Kesirli Sayılarla İşlemler](#Kesirli-Say%C4%B1larla-%C4%B0%C5%9Flemler)
  - [Matematik İşlemleri](#Matematik-%C4%B0%C5%9Flemleri)
    - [Matematikte Rastgelelik](#Matematikte-Rastgelelik)

## If / Else Koşul (Constraints) Yapısı

If içerisine yazılan koşul otomatik olarak `bool` değişkenine dönüştürülür, değer `True` ise içindeki kodlar çalıştırılır.

- `None`, `""`, `0` gibi değerler `False` değerine denktir
- `:` ile if / else satırı sonlandırılır
- `Tab` kadar boşluk atılırsa if scope\*'u içerisinde olur

```py
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

```py
fruit = 'Apple'
isApple = True if fruit == 'Apple' else False
```

## Döngüler (Loop)

### For Döngüsü

```py
sayilar = [6, 5, 3, 8, 4, 2, 5, 4, 11]
toplam = 0 # Toplam değeri tutacak değişken

for sayi in sayilar: # Liste üzerinde döngü ile ilerleme
  toplam = toplam + sayi

print("Toplam değer:", sum) # Toplam Değer: 48
```

#### Değişken içinde For Döngüsü

```py
values = [item.value for item in Fruit]  # [4, 5, 6]
values = set(item.value for item in Fruit)  # {4, 5, 6}
```

#### İki Liste Üzerinde Paralel For Döngüsü

```py
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

**Temel Kullanım:**

```py
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

```py
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

```py
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

```py
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

```py
x = 'Hello world'
y = {1:'a',2:'b'}

print('H' in x) # True
print('hello' not in x) # True (h'si büyük değil)
print(1 in y) # True
print('a' in y) # False ('a' bir değerdir anahtar değildir)
```

## Sayılar, Sayılar Arası Dönüşüm ve Matematik

### Tabanlı Sayılar

| Taban  | Ön ek           | Örnek                | Çıktı         |
| ------ | --------------- | -------------------- | ------------- |
| 2'lik  | `0b` ya da `0B` | `print(0b1101011)`   | 107           |
| 8'lik  | `0o` ya da `0O` | `print(0xFB + 0b10)` | 253 (251 + 2) |
| 16'lık | `0x` ya da `0X` | `print(0o15)`        | 13            |

### Ondalıklı Sayılar (Decimals / Floats)

```py
>>> (1.1 + 2.2) == 3.3
False
>>> 1.1 + 2.2
3.3000000000000003
```

```py
import decimal

print(0.1) # 0.1
print(decimal.Decimal(0.1)) # Decimal('0.1000000000000000055511151231257827021181583404541015625')
```

```py
from decimal import Decimal as D

print(D('1.1') + D('2.2')) #  Decimal('3.3')
print(D('1.2') * D('2.50')) # Decimal('3.000')
```

#### Decimal Float Kullanımları ve Farkı

- Decimal daha fazla bellek kaplar
- Finansal işlemlerde decimal tercih edilir

#### Kesirli Sayılar (Fractions)

```py
import fractions

print(fractions.Fraction(1.5)) # 3/2
print(fractions.Fraction(5)) # 5
print(fractions.Fraction(1,3)) # 1/3
```

```py
import fractions

# Floatlar virgülden sonra da sayı barındırdığından dolayı farklı sonuç verir
print(fractions.Fraction(1.1)) # 2476979795053773/2251799813685248
print(fractions.Fraction('1.1')) # 11/10
```

#### Kesirli Sayılarla İşlemler

```py
from fractions import Fraction as F

print(F(1,3) + F(1,3)) # 2/3
print(1 / F(5,6)) # 6/5
print(F(-3,10) > 0) # False
print(F(-3,10) < 0) # True
```

### Matematik İşlemleri

```py
import math

print(math.pi) # 3.141592653589793
print(math.cos(math.pi)) # -1.0
print(math.exp(10)) # 22026.465794806718
print(math.log10(1000)) # .0
print(math.sinh(1)) # 1.1752011936438014
print(math.factorial(6)) # 720
```

#### Matematikte Rastgelelik

```py
import random

x = ['a', 'b', 'c', 'd', 'e']

print(random.randrange(10,20)) # Rastgele 10, 20 arasında sayı yazdırma
print(random.choice(x)) # Rastgele seçim yapma
random.shuffle(x) # Karıştrma
print(x) # Karışım sonucunu yazma
print(random.random()) # Rastgele eleman yazma
```
