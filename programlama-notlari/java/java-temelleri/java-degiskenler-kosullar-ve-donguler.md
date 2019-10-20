# 💫 Java Değişkenler Koşullar ve Döngüler

## Değişkenler

* Final, değiştirilemez \(const\) anlamına gelir
* Final olursa constructer'da tanımlanması gerekir
* [Hashmap](https://www.geeksforgeeks.org/java-util-hashmap-in-java/)
  * Key ve değer'e göre veri oluşturur
  * `<hashmap>.get("A");`
  * Örn: `"A"` için `1`, `"B"` için `2` değeri verir.

### Değişken Dönüşümleri

```java
double kesir = 0.0;
int sayi = 1;
String metin = "metin";

sayi = (int) kesir;
metin =
```

### Kesirli Sayıları Formatlama

```java
public static String formatDecimal(Double decimal, int digitNum) {
    if (decimal == 0) return "0." + "0".repeat(digitNum - 1);

    int lvl = (int) Math.log10(decimal);
    String format = lvl >= 0 ? "#".repeat(lvl + 1) : "";
    format += lvl - digitNum >= -1 ? "" : "." + "#".repeat(digitNum - lvl - 1);

    return new DecimalFormat(format).format(decimal);
}
```

> [How to round a number to n decimal places in Java](https://stackoverflow.com/a/153785/9770490)

### Değişkenin Tipi Hakkında Bilgi Alma

* `<degisken>.getClass()` İle sınıf bilgilerini alabilirsin
* `<arr | arrlist>.getClass().getComponentType()` İle alt objelerinin sınıf bilgilerini alabilirsin

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

* `<arr>` Array, String\[\] vs...
* `<arrlist>` ArrayList, ArrayList vs...
* `<type>` String, Integer vs.

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

## Döngüler

```java
// For each
for (<type> num : <iterable>) {}
<arr>.foreach(<eleman> -> {<işlemler>});
```

* `<iterable>` İçerisinde çok veri barındıran obje
  * Array, Arraylist vs..

