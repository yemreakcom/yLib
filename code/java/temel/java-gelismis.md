---
description: İlgilenenlere biraz daha ileri seviye notlar
---

# 🤯 İleri Seviye

## Modül Programlama

Modüller tek bir iş için yapılandırılmış projelerdir.

* Büyük projeler birdenn fazla modülden oluşur
* Her modül diğerlerinden bağımsız olarak işler
* Java 9 ve sonrasında gelen bir sistemdir

> Java modül yapısı olan `module-info.java` dosyasını kullandığımızda `src` dizini **sources** özelliğine sahip olmazsa `java.datatransfer` ile `java.desktop` modülleri içerisindeki `java.awt`'ler çakışmakta ve hata vermekte 😢 \([module yapısı](http://tutorials.jenkov.com/java/modules.html)\)

### `module-info.java` Yapısı

```java
module ModulIsmı {
    // Projeye dahil edilenler
    requires javafx.fxml;
    requires javafx.controls;
    requires java.datatransfer;
    requires java.desktop;
    requires com.jfoenix;
    requires com.gluonhq.charm.glisten;

    // API isteklerini yardımcı araç ile açma @FMXL vs gibi
    opens com.yedhrab.controllers to javafx.fxml;

    // Dışa aktarılacak erişebilir class'lar (genelde Main)
    exports com.yedhrab.ytoolsfx.application.MainApp;
}
```

## Tüm Thread'leri Durdurma

```java
for (Thread t : Thread.getAllStackTraces().keySet()){
    if (t.getState()==Thread.State.RUNNABLE)
    t.interrupt();
}
```

## Generic \(Çoklu tip desteği\)

Generic yapısı tipi belirsiz objeler için kullanılır.

* `<T>` ile tanımlanır gösterilir, `T` ile kullanlır
  * `T`, Herhangi bir harf
* Int için `T = int`, string için `T = String` olarak işlem görür
* `<T>` deyimi her alanda kullanılabilir
  * `T[]` dizi, `ArrayList<T>` dizi listesi vs..

```text
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

> [Java Generics](https://www.tutorialspoint.com/java/java_generics.htm)

## Kod Notları \(Code Snippets\)

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

> [Simplify this generic method to concatenate Java arrays](https://stackoverflow.com/a/9481298/9770490)

### Tarayıcı Üzerinden Açma

```java
void openInDefaultBrowser(String url) throws URISyntaxException, IOException {
    if (Desktop.isDesktopSupported() && Desktop.getDesktop().isSupported(Desktop.Action.BROWSE)) {
        Desktop.getDesktop().browse(new URI(url));
    }
}
```

> [How to open the default webbrowser using java](https://stackoverflow.com/a/5226244/9770490)

## Terminal Komutları Çalıştırma

```java
Process process = Runtime.getRuntime().exec(command);
// JDK 12
Process pb = new ProcessBuilder("myCommand", "myArg1", "myArg2").start();
Process pb = new ProcessBuilder(<string[]>).start();
```

> * [Process İşlemleri](https://www.mkyong.com/java/how-to-execute-shell-command-from-java/)
> * [Oracle ProcessBuilder](https://docs.oracle.com/en/java/javase/12/docs/api/java.base/java/lang/ProcessBuilder.html)

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

## Hata Notları

### Error:\(1, 1\) java: modules are not supported in -source 8 \(use -source 9 or higher to enable modules\)

* `Settings`
* `Build, Execution, Development`
* `Compiler`
* `Java Compiler`
* `Project Byte Code Version` ****ve `Target Byte Code Version` alanlarını `12` yapın

## Harici Bağlantılar

* [Java Guava ile Hızlı ve Verimli Kodlama](http://javacirecep.blogspot.com/2011/09/isinize-yarayabilecek-hizmet-kitaplklar.html)
* [Jdk12 yeni özellikleri](https://www.azul.com/39-new-features-and-apis-in-jdk-12/)
* [Process işlemleri](https://www.mkyong.com/java/how-to-execute-shell-command-from-java/)

