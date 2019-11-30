---
description: Scanner metodu kullanıcıdan girdi almak amaçlı kullanılan bir metottur.
---

# 💠 Scanner Metotları

## Scanner Metotları Özeti

* Herhangi bir obje türünde girdi alınabilmekte
* Obje türünü belirlemek için sınıfın içindeki alt metotları kullanıyoruz

| Metot | Döndürdükleri |
| :--- | :--- |
| `next()` | String |
| `nextLine()` | String |
| `nextByte()` | byte |
| `nextShort()` | short |
| `nextInt()` | int |
| `nextLong()` | long |
| `nextFloat()` | float |
| `nextDouble()` | double |
| `hasNext()` | boolean |
| `useDelimeter(<ayıraç>)` | void |
| `delimeter()` | String |
| `close()` | void |

### `next` Metodu

Klavyeden alınan girdileri, ilk [**whitespace**](https://wiki.yemreak.com/programlama-notlari/java/diger-java-notlari/java-scanner-metodlari#java-whitespaces) ****girdisine kadar almakta ve bu girdiyi **string** türünde döndürmekte.

![next](../../../.gitbook/assets/image%20%2831%29.png)

### `nextLine` Metodu

Klavyeden alınan girdileri, ilk ENTER \(`"\n"`\) girdisine kadar almakta ve bu girdiyi **string** türünde döndürmekte.

![nextline](../../../.gitbook/assets/image%20%2862%29.png)



### `nextByte` `nextShort` `nextInt` `nextLong` `nextFloat` `nextDouble` Metodları

Klavyeden alınan girdileri `byte` / `short`/ `int` / `long` / `float` / `double` türünden alır.

> Farklı bir aralıkta sayı değeri girilirse, hata \(`exception`\) verir.

![nextvar](../../../.gitbook/assets/image%20%2843%29.png)



### `hasNext` Metodu

Scanner tipinde tanımlamış olduğumuz değişkenin bir satır sonrasında veri olup olmadığını kontrol eder.

> Şekillendirilebilir. `hasNextInt()` bir sonraki satırda `int` olup olmadığını kontrol eder ve sonuca göre `true` / `false` döndürür.

![hasnext](../../../.gitbook/assets/image%20%2885%29.png)



### `useDelimeter` Metodu

`next` metodun veri alma sınırını paremetre olarak aldığı değere göre belirler.

* Parametre olarak **string** tipinde değişken alır.
* Normalde `next` metodu whitespace karakterine geldiğinde veri almayı kesmektedir.
* Bu metotdan sonra `next` metodu **parametreye** denk geldiğinde veri almayı kesmiş olacak.

![usedelimeter](../../../.gitbook/assets/image%20%2891%29.png)



### `delimeter` Metodu

Scanner tipinde tanımlanmış olan değişkenin sınırlayıcısını döndürür.

* Yani `useDelimiter("mi")` yapıtğımız bir objenin `delimiter` metodu `"mi"` _string_'ini döndürecektir.
* Varsayılan sınırlayıcı değiştirilmediyse `next` metodu `"\p{javaWhitespace}+"` _string_'ini döndürür.

> `"\p{javaWhitespace}+"` deyimi Java whitespace olarak aşağıda tanımlanmıştır.

![delimeter](../../../.gitbook/assets/image%20%2897%29.png)

### `close` Metodu

Herhangi bir değer döndürmeyen bu fonskiyon, `Scanner` objesini kapatır.

## Java Whitespaces

Javada tanımlı olan **whitespace**'ler:

* `"\n"` - Satır atlatma ENTER
* `"\t"` - Bir TAB kadar boşluk atlatma
* `"\r"` - Bir TAB kadar satır atlatma
* `" "`- Boşluk atma SPACE

