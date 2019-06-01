# Python Fonksiyonlar <!-- omit in toc -->

## İçerikler <!-- omit in toc -->

- [Dahili Fonksiyon Kullanımları](#dahili-fonksiyon-kullan%C4%B1mlar%C4%B1)
  - [Genel Fonksiyonlar](#genel-fonksiyonlar)
    - [Enumerata (Numaralandırma, Sayma) İşlemi](#enumerata-numaraland%C4%B1rma-sayma-i%CC%87%C5%9Flemi)
- [Harici Fonksiyon Kullanımları](#harici-fonksiyon-kullan%C4%B1mlar%C4%B1)
- [Fonksiyon Oluşturma](#fonksiyon-olu%C5%9Fturma)
  - [Fonksiyon İskeleti](#fonksiyon-i%CC%87skeleti)
  - [Fonksiyon Örneği](#fonksiyon-%C3%B6rne%C4%9Fi)
  - [Fonksyion Dökümantasyonu](#fonksyion-d%C3%B6k%C3%BCmantasyonu)
  - [Fonksyion Varsayılan Parametreler](#fonksyion-varsay%C4%B1lan-parametreler)
  - [Fonksiyonlarda Keyfi Parametreler](#fonksiyonlarda-keyfi-parametreler)
- [Özyineleyen Fonksiyonlar](#%C3%B6zyineleyen-fonksiyonlar)
  - [Özyineleyen Fonksiyonların Avantajları](#%C3%B6zyineleyen-fonksiyonlar%C4%B1n-avantajlar%C4%B1)
  - [Özyineleyen Fonksiyonların Zararları](#%C3%B6zyineleyen-fonksiyonlar%C4%B1n-zararlar%C4%B1)
- [Lambda Fonksiyonlar](#lambda-fonksiyonlar)
  - [Filter ile Lambda Kullanımı](#filter-ile-lambda-kullan%C4%B1m%C4%B1)
  - [Map ile Lambda Kullanımı](#map-ile-lambda-kullan%C4%B1m%C4%B1)
- [İç İçe Fonksiyonlar](#i%CC%87%C3%A7-i%CC%87%C3%A7e-fonksiyonlar)
- [Global, Local ve Nonlocal Kavramları](#global-local-ve-nonlocal-kavramlar%C4%B1)
  - [Global, Local ve Nonlocal Kavramlarına Örnek (Scopes and Namespaces)](#global-local-ve-nonlocal-kavramlar%C4%B1na-%C3%B6rnek-scopes-and-namespaces)
  - [Global Kullanımına Örnek](#global-kullan%C4%B1m%C4%B1na-%C3%B6rnek)
  - [Global Kullanımına Ek Örnek](#global-kullan%C4%B1m%C4%B1na-ek-%C3%B6rnek)
- [Fonksiyonlarda Hız](#fonksiyonlarda-h%C4%B1z)
  - [Fonksiyon Hızı Ölçme Scripti](#fonksiyon-h%C4%B1z%C4%B1-%C3%B6l%C3%A7me-scripti)

## Dahili Fonksiyon Kullanımları

### Genel Fonksiyonlar

| Fonksiyon                 | Açıklama                  | Örnek                           | Çıktı              |
| ------------------------- | ------------------------- | ------------------------------- | ------------------ |
| `print(<string>)`         | Ekrana yazma              | `print("X: {1}, Y: {2}")`       | `X: {1}, Y: {2}`   |
| `eval(<string>)`          | Verilen stringi hesaplama | `eval("x + 5")`                 | `6`                |
| `type(<obje>)`            | Objenin türünü bulma      | `type(x)`                       | `<class 'number'>` |
| `enumerate(<obje>, <si>)` | Numaralandırma            | `i, line in enumerate(file, 0)` |

#### Enumerata (Numaralandırma, Sayma) İşlemi

Metin karakterlerini sayma

```py
string = "Yemreak"
for i, char in enumerate(string):
  print(i, char)

# 0 Y
# 1 e
# 2 m
# ...
```

Dosya satırlarını a'dan başlayarak sayma

```py
with open(FILE, "r") as file:
  for i, line in enumerate(file, a):
    print(f"{i}. {line}")

# a. satır
# (a+1). satır
# ...
```

## Harici Fonksiyon Kullanımları

- Fonksiyonları kullanmadan önce `import <paket>` ile paketi dahil etmeniz lazım
- Fonksiyonların kullanımı `<paket>.<fonksiyon>` şeklindedir

## Fonksiyon Oluşturma

Kodların derlenme yapısı yukarıdan aşağı olduğu için fonksiyonlar **yukarıda (önceden) tanımlanmadan** kullanılamaz.

### Fonksiyon İskeleti

```py
def function_name(parameters):
  """docstring"""
  statement(s)
```

### Fonksiyon Örneği

```py
def greet(name):
  """This function greets to
  the person passed in as
  parameter"""
  print("Hello, " + name + ". Good morning!")
```

### Fonksyion Dökümantasyonu

```cmd
>>> print(greet.__doc__)
This function greets to
  the person passed into the
  name paramete
```

### Fonksyion Varsayılan Parametreler

```py
def greet(name, msg = "Good morning!"):
   """
   This function greets to
   the person with the
   provided message.

   If message is not provided,
   it defaults to "Good
   morning!"
   """

   print("Hello",name + ', ' + msg)

greet("Kate") # Varsayılan parametreyi kullanma
greet("Bruce","How do you do?") # Sıralı parametre verme
greet("Bruce", msg="Naber") # İşaretleyerek paremetre verme
```

### Fonksiyonlarda Keyfi Parametreler

```py
def greet(*names):
   """This function greets all
   the person in the names tuple."""

   # names is a tuple with arguments
   for name in names:
       print("Hello",name)

greet("Monica","Luke","Steve","John")
```

> `*` ön eki ile ile kaç tane isim gelirse o kadar kullanıyoruz.

## Özyineleyen Fonksiyonlar

```py
def calc_factorial(x):
    """This is a recursive function
    to find the factorial of an integer"""

    if x == 1:
        return 1
    else:
        return (x * calc_factorial(x-1))

num = 4
print("The factorial of", num, "is", calc_factorial(num))
```

```out
calc_factorial(4)              # 1st call with 4
4 * calc_factorial(3)          # 2nd call with 3
4 * 3 * calc_factorial(2)      # 3rd call with 2
4 * 3 * 2 * calc_factorial(1)  # 4th call with 1
4 * 3 * 2 * 1                  # return from 4th call as number=1
4 * 3 * 2                      # return from 3rd call
4 * 6                          # return from 2nd call
24                             # return from 1st call
```

### Özyineleyen Fonksiyonların Avantajları

- Özyineleyen fonksiyonlar kodun daha temiz ve zarif gözükmesini sağlar
- Karmaşık bir görev alt görevlere ayrılarak rahat çözülebilir
- İç içe döngülere göre daha iyidir

### Özyineleyen Fonksiyonların Zararları

- Bazı durumlarda anlaşılabilmesi zordur
- Uzun tekrarlarda çok fazla vakit ve zaman harcarlar
- Hata ayıklama oldukça zordur

## Lambda Fonksiyonlar

```py
double = lambda x: x * 2 # lambda fonksiyon


def double(x): # Fonksiyon
   return x * 2
```

### Filter ile Lambda Kullanımı

Sadece koşulu sağlayan değerleri döndürür.

```py
listem = [1, 5, 4, 6, 8, 11, 3, 12]

cift_listem = list(filter(lambda x: (x%2 == 0) , listem))
print(cift_listem) # [4, 6, 8, 12]
```

### Map ile Lambda Kullanımı

Her eleman için işlem yapar.

```py
listem = [1, 5, 4, 6, 8, 11, 3, 12]

katlanmis_listem = list(map(lambda x: x * 2 , listem))
print(katlanmis_listem) # Output: [2, 10, 8, 12, 16, 22, 6, 24]
```

## İç İçe Fonksiyonlar

Python ile fonksiyon içinde fonksiyon tanımalamak mümkündür.

- İç içe fonksiyonlarda parametreler ortak kullanılır

> Hatırlatma: Kodların derlenme yapısı yukarıdan aşağı olduğu için fonksiyonlar **yukarıda (önceden) tanımlanmadan** kullanılamaz.

```py
def func1(param):

    # func2() bu alanda kullanılamaz

    def func2():
        # Parametreler ortak kullanıldığından ek olarak almasına gerek yoktur
        print("2.", param)

    print(param)
    func2() # Bu alanda ekrana '2.Selam' basar

func1("Selam")
```

## Global, Local ve Nonlocal Kavramları

| Kavram     | Açıklama                                                                                    | Erişim         |
| ---------- | ------------------------------------------------------------------------------------------- | -------------- |
| `global`   | Tüm modülde geçerli değişkenler                                                             | Okuma          |
| `local`    | Fonksiyonların içerisindeki yerel değişkenler                                               | Okuma ve Yazma |
| `nonlocal` | Modül ile fonksiyon arasında kalan, genellikle iç içe fonksiyonlarda kullanılan değişkenler | Okuma          |

### Global, Local ve Nonlocal Kavramlarına Örnek (Scopes and Namespaces)

```py
x = 5 # Global değişken

def func1(param):

    x = 4 # Nonlocal değişken
  
    def func11():
      x = 1 # Local değişken

      # print(param)
      # Otomatik olarak üst fonksiyonun parametresini ele alır

      # print(param)
      # param = 5
      # Yukarıdaki işlemde param'a atama yapıldığından `local param` olarak tanımlanır.
      # Print içindeki param tanımlanmadan kullanılmaktadır, bu sebeple `print(param)` komutu çalışmaz hata verir.
      # param tanımlanmadan kullanıldı (`nonlocal param` olarak yazılması lazım)

    print(x)
    # Python otomatik olarak `global x` deyimini kullanır
    #  x'i global değişkenlerde arar ve ekrana '5' basar

    # print(x)
    # x = 3
    # Yukarıdaki işlemde x'e atama yapıldığından `local x` olarak tanımlanır.
    # Print içindeki x tanımlanmadan kullanılmaktadır, bu sebeple `print(x)` komutu çalışmaz hata verir.
    # x tanımlanmadan kullanıldı (`global x` olarak yazılması lazım)
    global x
    print(x)
    x = 3
    print(x)

```

### Global Kullanımına Örnek

```py
x = 5
  
  def xDegistir():
    x = 3 # Yerel x değişkenine 3 değeri atanır, evrensel x değişmez.

  
  def globalXDegistir():
    global x
    x = 4 # Evrensel x değişir
```

### Global Kullanımına Ek Örnek

```py
def scope_test():
    def do_local():
        spam = "local spam"

    def do_nonlocal():
        nonlocal spam
        spam = "nonlocal spam"

    def do_global():
        global spam
        spam = "global spam"

    spam = "test spam"
    do_local()
    print("After local assignment:", spam)
    do_nonlocal()
    print("After nonlocal assignment:", spam)
    do_global()
    print("After global assignment:", spam)

scope_test()
print("In global scope:", spam)
```

```txt
After local assignment: test spam
After nonlocal assignment: nonlocal spam
After global assignment: nonlocal spam
In global scope: global spa
```

## Fonksiyonlarda Hız

Fonksiyonlarda işlem yapılma hızı, manuel (kod satırı olarak) işlem yapılmasından daha hızlıdır.

- ~%80 daha hızlı çalıştığını script üzerinden görebilirsiniz
- Bu değer bilgisayar **donanımınıza göre değişiklik** gösterecektir

> **Ek kaynaklar:**
>
> - [Fonksiyonların CPU ve Memory kullanımını ölçme]
> - [Fonksiyonun CPU kullanımını bulma - StackOverflow]

### Fonksiyon Hızı Ölçme Scripti

> Google colabratory üzerinden çalıştırmak için [buraya][Fonksiyon testini colab üzerinde çalıştırma] tıklayabilirsin.

```py
from time import time

# Obje uzunluğu
RANGE = 1000

# Toplam test sayısı
TEST_RANGE = 10000

# Fonksiyonun yavaş kaldığı testlerin sayısı
func_slow_count = 0

# Objeyi oluşturma
data1 = [i for i in range(RANGE)]
data2 = [i for i in range(RANGE)]
data3 = [i for i in range(RANGE)]

avg_func_speed = 0
for test in range(TEST_RANGE):
    first_time = time()

    # Normal işleme
    data = []
    for test2 in range(len(data1)):
        data.append(data1[test2])
    for test2 in range(len(data2)):
        data.append(data2[test2])
    for test2 in range(len(data3)):
        data.append(data3[test2])

    normal_time = time() - first_time

    # Fonksiyon ile işleme
    def fdata(data1, data2, data3):
        data = []
        for test2 in range(len(data1)):
            data.append(data1[test2])
        for test2 in range(len(data2)):
            data.append(data2[test2])
        for test2 in range(len(data3)):
            data.append(data3[test2])
        return data

    data = [i for i in range(RANGE)]

    first_time = time()

    # Fonksiyon ile veri atama
    fdata = fdata(data1, data2, data3)

    func_time = time() - first_time

    if normal_time - func_time < 0:
        func_slow_count += 1

    avg_func_speed = (
        avg_func_speed * test + (normal_time / func_time - 1) * 100
    ) / (test + 1)

print("Fonksiyon işlemi normalden %" + "%.2f daha hızlı, testlerde " % avg_func_speed + "%" + "%.2f ihtimalle yavaş kalmıştır." %
      (func_slow_count * 100 / TEST_RANGE))

```

```py
# Colab çıktıları
Fonksiyon işlemi normalden %47.32 daha hızlı, testlerde %0.09 ihtimalle yavaş kalmıştır.
Fonksiyon işlemi normalden %46.86 daha hızlı, testlerde %0.21 ihtimalle yavaş kalmıştır.
Fonksiyon işlemi normalden %52.29 daha hızlı, testlerde %0.31 ihtimalle yavaş kalmıştır.
Fonksiyon işlemi normalden %48.02 daha hızlı, testlerde %0.41 ihtimalle yavaş kalmıştır.
Fonksiyon işlemi normalden %46.89 daha hızlı, testlerde %0.53 ihtimalle yavaş kalmıştır.
Fonksiyon işlemi normalden %46.73 daha hızlı, testlerde %0.68 ihtimalle yavaş kalmıştır.
Fonksiyon işlemi normalden %47.21 daha hızlı, testlerde %0.86 ihtimalle yavaş kalmıştır.
Fonksiyon işlemi normalden %47.02 daha hızlı, testlerde %1.09 ihtimalle yavaş kalmıştır.
Fonksiyon işlemi normalden %47.60 daha hızlı, testlerde %1.27 ihtimalle yavaş kalmıştır.
Fonksiyon işlemi normalden %52.76 daha hızlı, testlerde %1.41 ihtimalle yavaş kalmıştır.
Fonksiyon işlemi normalden %48.76 daha hızlı, testlerde %1.74 ihtimalle yavaş kalmıştır.
Fonksiyon işlemi normalden %46.28 daha hızlı, testlerde %1.90 ihtimalle yavaş kalmıştır.
Fonksiyon işlemi normalden %46.94 daha hızlı, testlerde %2.11 ihtimalle yavaş kalmıştır.
Fonksiyon işlemi normalden %46.21 daha hızlı, testlerde %2.25 ihtimalle yavaş kalmıştır.
Fonksiyon işlemi normalden %46.50 daha hızlı, testlerde %2.39 ihtimalle yavaş kalmıştır.
Fonksiyon işlemi normalden %52.01 daha hızlı, testlerde %2.49 ihtimalle yavaş kalmıştır.
```

[Slice - Stackoverflow]: https://stackoverflow.com/a/509295/9770490
[Fonksiyonların CPU ve Memory kullanımını ölçme]: http://www.marinamele.com/7-tips-to-time-python-scripts-and-control-memory-and-cpu-usage
[Fonksiyonun CPU kullanımını bulma - StackOverflow]: https://stackoverflow.com/a/8957968/9770490
[Fonksiyon testini colab üzerinde çalıştırma]: https://colab.research.google.com/drive/1zD_AFxZSqhcY8MVp2nsCl_9ftDIytVGS
