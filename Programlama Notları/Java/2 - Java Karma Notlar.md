# Java Karma Notlar <!-- omit in toc -->

## İçerikler <!-- omit in toc -->

- [String İşlemleri](#String-%C4%B0%C5%9Flemleri)
- [Koşul Yapıları](#Ko%C5%9Ful-Yap%C4%B1lar%C4%B1)
  - [Yeni Switch Case](#Yeni-Switch-Case)
- [Dizi İşlemleri](#Dizi-%C4%B0%C5%9Flemleri)
- [Regex](#Regex)
- [WhiteSpaces](#WhiteSpaces)
- [Değişkenler](#De%C4%9Fi%C5%9Fkenler)
- [Terminal Komutları Çalıştırma](#Terminal-Komutlar%C4%B1-%C3%87al%C4%B1%C5%9Ft%C4%B1rma)
- [Terminal Komutlarını Çalıştırma ve Çıktısını Görme](#Terminal-Komutlar%C4%B1n%C4%B1-%C3%87al%C4%B1%C5%9Ft%C4%B1rma-ve-%C3%87%C4%B1kt%C4%B1s%C4%B1n%C4%B1-G%C3%B6rme)
- [Harici Bağlantılar](#Harici-Ba%C4%9Flant%C4%B1lar)

## String İşlemleri

| İşlem                     | Açıklama                     |
| ------------------------- | ---------------------------- |
| \` `<metin>` \`           | Formatsız (raw) string yazma |
| `contains(<char>)`        | Metinde kelime arama         |
| `strip()`                 | Boşlukları kaldırma          |
| `split(<string | regex>)` | String ayrıştırma            |

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
// Diziyi listeye ekleme
Collections.addAll(<arrlist>, <arr>);
<arrlist>.addAll(<arr>);
<arrlist>.addAll(<index>, <arr>); // Belirli indeksten sonrasına ekleme

// Diziyi parçalama
Arrays.asList(<arr>).subList(<n>, <m>) // n'den m'e kadar (m dahil değil)

// Dizi parçasını ekleme
Collections.addAll(<arrlist>, <arr>);
<arrlist>.addAll(Arrays.asList(<arr>).subList(0, <arr>.length - 2));

// Dönüşümler
<arr> = <arrlist>.toArray(new <type>[0])
<arrlist> = new ArrayList<>(<arr>)
```

- `<arr>` Array, String[] vs...
- `<arrlist>` ArrayList<String>, ArrayList<Integer> vs...
- `<type>` String, Integer vs.

## Regex

Split işlemlerinde sıklıkla kullanılan ayırıcı özelliklerdir.

| İşlem              | Açıklama   |
| ------------------ | ---------- |
| `(<regex><regex>)` | And işlemi |
| `[<regex><regex>]` | Or işlemi  |

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

## Terminal Komutları Çalıştırma

```java
Process process = Runtime.getRuntime().exec(command);
```

## Terminal Komutlarını Çalıştırma ve Çıktısını Görme

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

- <https://www.azul.com/39-new-features-and-apis-in-jdk-12/>
