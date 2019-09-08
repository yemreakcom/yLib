# Java String İşlemleri 

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

## Verimli String İşlemleri

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
