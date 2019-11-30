---
description: String işlemleri her dil için olduğu gibi java'da da çok önemli bir kavramdır
---

# 🔡 String İşlemleri

## String İşlemleri

| İşlem | Açıklama |  |
| :--- | :--- | :--- |
| `concat(<str>...)` | `+` işlemleri yerine yapılır, daha hızlı ve güvenlidir |  |
| \` `<metin>` \` | Formatsız \(raw\) string yazma |  |
| `contains(<char>)` | Metinde kelime arama |  |
| `strip()` | Boşlukları kaldırma |  |
| \`split\(&lt;string | regex&gt;\)\` | String ayrıştırma |
| `format(""%.5g%n", 0.912300")` | Formatlı string |  |
| `repeat(<int>)` | Metni belli bir sayı kadar tekrarlama |  |

> Split örnekleri için [buraya](https://www.javatpoint.com/java-string-split) bakabilirsin.

## WhiteSpaces

| Karakter | Açıklama |
| :--- | :--- |
| `\t` | Tab |
| `\b` | Backspace \(remove previous character\) |
| `\n` | New line |
| `\r` | Carriage return |
| `\f` | Form feed |
| `\'` | Single quote character |
| `\"` | Double quote character |
| `\\` | Backslash character |

## Regex

Fazla miktardaki metinleri veya büyük boyutlu string metinlerini ayrıştam için kullanılan dil formatı 🕵️‍

> Siteden **Regex** araması yaparak, ilgili alana bakmanı tavsiye ederim.

## Verimli String İşlemleri

| En hızlısı | Açıklama |
| :--- | :--- |
| `"baeldung"` &gt; `new String("baeldung")` | Oluşturma |
| `concat(<str[]>)` &gt; `+=` | birleştirme |
| `StringBuilder.append` &gt; `StringBuffer.append` | Döngüsel toplama |
| `StringUtils.replace` &gt; `"".replace` | Değiştirme |
| `<str>.indexOf` &gt; `<str>.split` | Ayrıştırma |
| `Integer.toString(<int>)` &gt; `"" + <int>` | String'e çevirme |
| `equals(<str>)` | Eşitlik kontrolü |
| `isEmpty()` &gt; `lenght > 0` | Boş olma kontrolü |

> [String performance](https://www.baeldung.com/java-string-performance)

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

