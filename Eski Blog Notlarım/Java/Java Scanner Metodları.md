# Java Scanner Metodları

`Scanner` methodu kullanıcıdan girdi almak amaçlı kullanılan bir metottur.

- Herhangi bir obje türünde girdi alınabilmekte
- Obje türünü belirlemek için sınıfın içindeki alt metotları kullanıyoruz

## Scanner Metodları Özeti

| Metod                    | Döndürdükleri |
| ------------------------ | ------------- |
| `next()`                 | String        |
| `nextLine()`             | String        |
| `nextByte()`             | byte          |
| `nextShort()`            | short         |
| `nextInt()`              | int           |
| `nextLong()`             | long          |
| `nextFloat()`            | float         |
| `nextDouble()`           | double        |
| `hasNext()`              | boolean       |
| `useDelimeter(<ayıraç>)` | void          |
| `delimeter()`            | String        |
| `close()`                | void          |

### `next` Metodu

Klavyeden alınan girdileri, ilk **whitespace** girdisine kadar almakta ve bu girdiyi **string** türünde döndürmekte.

![next](../res/scanner_next.png)

### `nextLine` Metodu

Klavyeden alınan girdileri, ilk <kbd>ENTER</kbd> (`"\n"`) girdisine kadar almakta ve bu girdiyi **string** türünde döndürmekte.

![nextline](../res/scanner_nextline;.png)

### `nextByte` `nextShort` `nextInt` `nextLong` `nextFloat` `nextDouble` Metodları

Klavyeden alınan girdileri `byte` / `short`/ `int` / `long` / `float` / `double` türünden alır.

> Farklı bir aralıkta sayı değeri girilirse, hata (`exception`) verir.

![nextvar](../res/scanner_nextvar.jpg)

### `hasNext` Metodu

Scanner tipinde tanımlamış olduğumuz değişkenin bir satır sonrasında veri olup olmadığını kontrol eder.

> Şekillendirilebilir. `hasNextInt()` bir sonraki satırda `int` olup olmadığını kontrol eder ve sonuca göre `true` / `false` döndürür.

![hasnext](../res/scanner_hasnext.png)

### `useDelimeter` Metodu

`next` metodun veri alma sınırını paremetre olarak aldığı değere göre belirler.

- Parametre olarak **string** tipinde değişken alır.
- Normalde `next` metodu whitespace karakterine geldiğinde veri almayı kesmektedir.
- Bu metotdan sonra `next` metodu **parametreye** denk geldiğinde veri almayı kesmiş olacak.

![usedelim](../res/scanner_usedelim.png)

### `delimeter` Metodu

Scanner tipinde tanımlanmış olan değişkenin sınırlayıcısını döndürür. 

- Yani `useDelimiter("mi")` yapıtğımız bir objenin `delimiter` metodu `"mi"` *string*'ini döndürecektir.
- Varsayılan sınırlayıcı değiştirilmediyse `next` metodu `"\p{javaWhitespace}+"` *string*'ini döndürür.

> `"\p{javaWhitespace}+"` deyimi Java whitespace olarak aşağıda tanımlanmıştır.

![delim](../res/scanner_delim.png)

### `close` Metodu

Herhangi bir değer döndürmeyen bu fonskiyon, `Scanner` objesini kapatır.

## Java Whitespaces

Javada tanımlı olan **whitespace**'ler:

- `"\n"` - Satır atlatma <kbd>ENTER</kbd>
- `"\t"` - Bir <kbd>TAB</kbd> kadar boşluk atlatma
- `"\r"` - Bir <kbd>TAB</kbd> kadar satır atlatma
- `" "`- Boşluk atma <kbd>SPACE</kbd>