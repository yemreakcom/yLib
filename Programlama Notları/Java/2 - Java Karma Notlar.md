# Java Karma Notlar <!-- omit in toc -->

## İçerikler <!-- omit in toc -->

- [Çok Faydalı](#%C3%87ok-Faydal%C4%B1)
- [Değişken Dönüşümleri](#De%C4%9Fi%C5%9Fken-D%C3%B6n%C3%BC%C5%9F%C3%BCmleri)
- [Kesirli Sayıları Formatlama](#Kesirli-Say%C4%B1lar%C4%B1-Formatlama)
- [String İşlemleri](#String-%C4%B0%C5%9Flemleri)
- [Koşul Yapıları](#Ko%C5%9Ful-Yap%C4%B1lar%C4%B1)
  - [Yeni Switch Case](#Yeni-Switch-Case)
- [Dizi İşlemleri](#Dizi-%C4%B0%C5%9Flemleri)
- [Regex](#Regex)
- [WhiteSpaces](#WhiteSpaces)
- [Değişkenler](#De%C4%9Fi%C5%9Fkenler)
- [Döngüler](#D%C3%B6ng%C3%BCler)
- [Interface](#Interface)
- [Kullanıcı Dizinleri](#Kullan%C4%B1c%C4%B1-Dizinleri)
  - [Functional Interface](#Functional-Interface)
- [Tüm Thread'leri Durdurma](#T%C3%BCm-Threadleri-Durdurma)
- [Dosya İşlemleri](#Dosya-%C4%B0%C5%9Flemleri)
  - [Silme İşlemleri](#Silme-%C4%B0%C5%9Flemleri)
  - [Clipboard (Pano) İşlemleri](#Clipboard-Pano-%C4%B0%C5%9Flemleri)
  - [Seçilini Olanı Kopyalama](#Se%C3%A7ilini-Olan%C4%B1-Kopyalama)
- [Sayısı belirtilmemiş parametre kullanımı](#Say%C4%B1s%C4%B1-belirtilmemi%C5%9F-parametre-kullan%C4%B1m%C4%B1)
- [Generic (Çoklu tip desteği)](#Generic-%C3%87oklu-tip-deste%C4%9Fi)
- [Değişkenin Tipi Hakkında Bilgi Alma](#De%C4%9Fi%C5%9Fkenin-Tipi-Hakk%C4%B1nda-Bilgi-Alma)
- [Kod Notları (Code Snippets)](#Kod-Notlar%C4%B1-Code-Snippets)
  - [Generic Olarak Dizileri Birleştirme](#Generic-Olarak-Dizileri-Birle%C5%9Ftirme)
  - [Tarayıcı Üzerinden Açma](#Taray%C4%B1c%C4%B1-%C3%9Czerinden-A%C3%A7ma)
- [Terminal Komutları Çalıştırma](#Terminal-Komutlar%C4%B1-%C3%87al%C4%B1%C5%9Ft%C4%B1rma)
  - [Terminal Komutlarını Çalıştırma ve Çıktısını Görme](#Terminal-Komutlar%C4%B1n%C4%B1-%C3%87al%C4%B1%C5%9Ft%C4%B1rma-ve-%C3%87%C4%B1kt%C4%B1s%C4%B1n%C4%B1-G%C3%B6rme)
- [Harici Bağlantılar](#Harici-Ba%C4%9Flant%C4%B1lar)

## Çok Faydalı

- [AI ile Java Snippets](https://www.codota.com/?utm_source=search-web)

## Değişken Dönüşümleri

```java
double kesir = 0.0;
int sayi = 1;
String metin = "metin";

sayi = (int) kesir;
metin =
```

## Kesirli Sayıları Formatlama

```java
public static String formatDecimal(Double decimal, int digitNum) {
    if (decimal == 0) return "0." + "0".repeat(digitNum - 1);

    int lvl = (int) Math.log10(decimal);
    String format = lvl >= 0 ? "#".repeat(lvl + 1) : "";
    format += lvl - digitNum >= -1 ? "" : "." + "#".repeat(digitNum - lvl - 1);

    return new DecimalFormat(format).format(decimal);
}
```

> [How to round a number to n decimal places in Java]

## String İşlemleri

| İşlem                          | Açıklama                                               |
| ------------------------------ | ------------------------------------------------------ |
| `concat(<str>...)`             | `+` işlemleri yerine yapılır, daha hızlı ve güvenlidir |
| \` `<metin>` \`                | Formatsız (raw) string yazma                           |
| `contains(<char>)`             | Metinde kelime arama                                   |
| `strip()`                      | Boşlukları kaldırma                                    |
| `split(<string | regex>)`      | String ayrıştırma                                      |
| `format(""%.5g%n", 0.912300")` | Formatlı string                                        |
| `repeat(<int>)`                | Metni belli bir sayı kadar tekrarlama                  |

> Split örnekleri için [buraya](https://www.javatpoint.com/java-string-split) bakabilirsin.

## Koşul Yapıları

### Yeni Switch Case

```java
String test = switch (type) {
    case "formatCode" -> data.formatCode;
    case "extension" -> data.extension;
    case "type" -> data.type;
    case "resolution" -> data.resolution;
    case "size" -> data.size;
    default -> "";
}
```

## Dizi İşlemleri

```java
// Dizi tanımlaması
new <arr>[]{"a", "b", "c"}

// Diziyi listeye ekleme
Collections.addAll(<arrlist>, <arr>);
<arrlist>.addAll(<arr>);
<arrlist>.addAll(<index>, <arr>); // Belirli indeksten sonrasına ekleme

// Diziyi parçalama
Arrays.asList(<arr>).subList(<n>, <m>) // n'den m'e kadar (m dahil değil)

// Dizi parçasını ekleme
Collections.addAll(<arrlist>, <arr>);
<arrlist>.addAll(Arrays.asList(<arr>).subList(0, <arr>.length - 2));

// Dönüşümler (generic için çalışmaz)
<arr> = <arrlist>.toArray(<type>::new)
<arrlist> = new ArrayList<>(<arr>)
```

- `<arr>` Array, String[] vs...
- `<arrlist>` ArrayList<String>, ArrayList<Integer> vs...
- `<type>` String, Integer vs.

## Regex

Split işlemlerinde sıklıkla kullanılan ayırıcı özelliklerdir.

| İşlem              | Açıklama                           |
| ------------------ | ---------------------------------- |
| `(<regex><regex>)` | And işlemi                         |
| `[<regex><regex>]` | Or işlemi                          |
| `": \\s+"`         | `": "` göre ayırma                 |
| `\\.`              | `.` ya göre ayırma (`"."` çalışmaz |

| Greedy   | Reluctant | Possessive | Meaning                                 |
| -------- | --------- | ---------- | --------------------------------------- |
| `X?`     | `X??`     | `X?+`      | X, once or not at all                   |
| `X\*`    | `X\*?`    | `X\*+`     | X, zero or more times                   |
| `X+`     | `X+?`     | `X++`      | X, one or more times                    |
| `X{n}`   | `X{n}?`   | `X{n}+`    | X, exactly n times                      |
| `X{n,}`  | `X{n,}?`  | `X{n,}+`   | X, at least n times                     |
| `X{n,m}` | `X{n,m}?` | `X{n,m}+`  | X, at least n but not more than m times |

> Kaynak için [buraya](https://docs.oracle.com/javase/tutorial/essential/regex/quant.html) bakabilirsin.

## WhiteSpaces

| Karakter | Açıklama                              |
| -------- | ------------------------------------- |
| `\t`     | Tab                                   |
| `\b`     | Backspace (remove previous character) |
| `\n`     | New line                              |
| `\r`     | Carriage return                       |
| `\f`     | Form feed                             |
| `\'`     | Single quote character                |
| `\"`     | Double quote character                |
| `\\`     | Backslash character                   |

## Değişkenler

- Final, değiştirilemez (const) anlamına gelir
- Final olursa constructer'da tanımlanması gerekir
- [Hashmap](https://www.geeksforgeeks.org/java-util-hashmap-in-java/)
  - Key ve değer'e göre veri oluşturur
  - `<hashmap>.get("A");`
  - Örn: `"A"` için `1`, `"B"` için `2` değeri verir.

## Döngüler

```java
// For each
for (<type> num : <iterable>) {}
<arr>.foreach(<eleman> -> {<işlemler>});
```

- `<iterable>` İçerisinde çok veri barındıran obje
  - Array, Arraylist vs..

## Interface

Interface'ler metodlardan oluşan classlardır.

## Kullanıcı Dizinleri

Tüm OS'larda çalışır.

```java
System.getProperty("user.home"); // Kullanıcı dizini
System.getProperties() // Tüm sistem bilgileri
System.getenv(); // Sistem değişkenleri
```

### Functional Interface

Tek metodtan oluşan interface'lerdir.

- Lambda expression `() -> {}` ile kullanılabilirler
- Metodlara parametre olarak metod göndermek için çok kullanışlıdır

```java
@FunctionalInterface
public interface ProcessEvent {

    void onOutputChanged(String param);

}

public static void executeCommand(ProcessEvent pe) {
    String param = "Selam";
        pe.onOutputChanged(param); // Gönderilen lambda expression'a param değişkenini atar
}

public static void main(String[] args) {
    executeCommand((param) -> { // Interface içerisinden gelen değişken () arasına yazılır
        System.out.println(param); // Ekrana hello basar
    })
}
```

## Tüm Thread'leri Durdurma

```java
for (Thread t : Thread.getAllStackTraces().keySet()){
    if (t.getState()==Thread.State.RUNNABLE)
    t.interrupt();
}
```

## Dosya İşlemleri

### Silme İşlemleri

```java
File file = new File(<dosyaYolu>); // Dosyayı tanımlama
file.delete(); // Silinirse true döndürür
```

> Tüm işlemler için [buraya](https://www.journaldev.com/830/java-delete-file-directory) bakabilirsin.

### Clipboard (Pano) İşlemleri

```java
Clipboard clipboard = Toolkit.getDefaultToolkit().getSystemClipboard(); // Panoyu alma
clipboard.getAvailableDataFlavors(); // Panodakileri liste olarak alma
```

### Seçilini Olanı Kopyalama

```java
private void pasteSelectionContent() {
  try {
    Clipboard systemSelection = Toolkit.getDefaultToolkit().getSystemSelection();
    if(systemSelection != null) {
      injectStringAsKeyStrokes((String) systemSelection.getData(DataFlavor.stringFlavor));
    }
  }
  catch(Exception ignore) {
  }
}
```

## Sayısı belirtilmemiş parametre kullanımı

Değişken tipinin yanına `...` yazılması ile ifade edilir.

- Çok sayıda tanımsız parametre gelebilir demektir
- For döngüleri ile ele alınır

```java
public void ornekMethod(String ... metinler) {
  for (String metin : metinler) {
    System.out.printf("%s ", metin);
  }
}
```

## Generic (Çoklu tip desteği)

Generic yapısı tipi belirsiz objeler için kullanılır.

- `<T>` ile tanımlanır gösterilir, `T` ile kullanlır
  - `T`, Herhangi bir harf
- Int için `T = int`, string için `T = String` olarak işlem görür
- `<T>` deyimi her alanda kullanılabilir
  - `T[]` dizi, `ArrayList<T>` dizi listesi vs..

```
The most commonly used type parameter names are:

E - Element (used extensively by the Java Collections Framework)
K - Key
N - Number
T - Type
V - Value
S,U,V etc. - 2nd, 3rd, 4th types
```

```java
public static <T> T[] print(T rastgele) {
    System.out.println(rastgele)
    return rasgele;
}

public static <E> void printArray( E[] inputArray ) {
    // Display array elements
    for(E element : inputArray) {
        System.out.printf("%s ", element);
    }
    System.out.println();
}
```

> [Java Generics]

## Değişkenin Tipi Hakkında Bilgi Alma

- `<degisken>.getClass()` İle sınıf bilgilerini alabilirsin
- `<arr | arrlist>.getClass().getComponentType()` İle alt objelerinin sınıf bilgilerini alabilirsin

## Kod Notları (Code Snippets)

### Generic Olarak Dizileri Birleştirme

```java
public static <T> T[] mergeArray(T[]... arrays) {
    int totalLen = 0;
    for (T[] arr: arrays) {
        totalLen += arr.length;
    }

    @SuppressWarnings("unchecked") T[] all = (T[])Array.newInstance(
            arrays.getClass().getComponentType().getComponentType(), totalLen);

    int copied = 0;
    for (T[] arr: arrays) {
        System.arraycopy(arr, 0, all, copied, arr.length);
        copied += arr.length;
    }
    return all;
}
```

> [Simplify this generic method to concatenate Java arrays]

### Tarayıcı Üzerinden Açma

```java
void openInDefaultBrowser(String url) throws URISyntaxException, IOException {
    if (Desktop.isDesktopSupported() && Desktop.getDesktop().isSupported(Desktop.Action.BROWSE)) {
        Desktop.getDesktop().browse(new URI(url));
    }
}
```

> [How to open the default webbrowser using java]

## Terminal Komutları Çalıştırma

```java
Process process = Runtime.getRuntime().exec(command);
// JDK 12
Process pb = new ProcessBuilder("myCommand", "myArg1", "myArg2").start();
Process pb = new ProcessBuilder(<string[]>).start();
```

> - [Process İşlemleri][process işlemleri]
> - [Oracle ProcessBuilder][process işlemleri oracle]

### Terminal Komutlarını Çalıştırma ve Çıktısını Görme

```java
Runtime rt = Runtime.getRuntime();
String[] commands = {"system.exe", "-get t"};
Process proc = rt.exec(commands);

BufferedReader stdInput = new BufferedReader(new
     InputStreamReader(proc.getInputStream()));

BufferedReader stdError = new BufferedReader(new
     InputStreamReader(proc.getErrorStream()));

// Read the output from the command
System.out.println("Here is the standard output of the command:\n");
String s = null;
while ((s = stdInput.readLine()) != null) {
    System.out.println(s);
}

// Read any errors from the attempted command
System.out.println("Here is the standard error of the command (if any):\n");
while ((s = stdError.readLine()) != null) {
    System.out.println(s);
}
```

## Harici Bağlantılar

- [Java Guava ile Hızlı ve Verimli Kodlama](http://javacirecep.blogspot.com/2011/09/isinize-yarayabilecek-hizmet-kitaplklar.html)
- [Jdk12 yeni özellikleri][39 new features (and apis) in jdk 12]
- [Process işlemleri]

[process işlemleri]: https://www.mkyong.com/java/how-to-execute-shell-command-from-java/
[process işlemleri oracle]: https://docs.oracle.com/en/java/javase/12/docs/api/java.base/java/lang/ProcessBuilder.html
[java generics]: https://www.tutorialspoint.com/java/java_generics.htm
[simplify this generic method to concatenate java arrays]: https://stackoverflow.com/a/9481298/9770490
[39 new features (and apis) in jdk 12]: https://www.azul.com/39-new-features-and-apis-in-jdk-12/
[how to open the default webbrowser using java]: https://stackoverflow.com/a/5226244/9770490
[how to round a number to n decimal places in java]: https://stackoverflow.com/q/153724/9770490
