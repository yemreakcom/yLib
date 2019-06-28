# Java Verimli Kodlama <!-- omit in toc -->

## İçerikler <!-- omit in toc -->

- [String İşlemleri](#String-%C4%B0%C5%9Flemleri)
  - [String Ayrıştırma](#String-Ayr%C4%B1%C5%9Ft%C4%B1rma)

## String İşlemleri

| En hızlısı                                     | Açıklama          |
| ---------------------------------------------- | ----------------- |
| `"baeldung"` > `new String("baeldung")`        | Oluşturma         |
| `concat(<str[]>)` > `+=`                       | birleştirme       |
| `StringBuilder.append` > `StringBuffer.append` | Döngüsel toplama  |
| `StringUtils.replace` > `"".replace`           | Değiştirme        |
| `<str>.indexOf` > `<str>.split`                | Ayrıştırma        |
| `Integer.toString(<int>)` > `"" + <int>`       | String'e çevirme  |
| `equals(<str>)`                                | Eşitlik kontrolü  |
| `isEmpty()` > `lenght > 0`                     | Boş olma kontrolü |

> [String performance]

### String Ayrıştırma

```java
public static ArrayList<String> stringSplit(String string, String delimiter) {
    ArrayList<String> split = new ArrayList<>();
    int pos = 0, end;

    while ((end = string.indexOf(delimiter, pos)) >= 0) {
        split.add(string.substring(pos, end));
        pos = end + 1;
    }

    return split;
}
```

[string performance]: https://www.baeldung.com/java-string-performance
