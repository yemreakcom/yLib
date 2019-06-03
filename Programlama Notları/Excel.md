# Excel <!-- omit in toc -->

## İçerikler <!-- omit in toc -->

- [Temel Değişkenler](#temel-de%C4%9Fi%C5%9Fkenler)
- [Excel Fonksiyonları](#excel-fonksiyonlar%C4%B1)
  - [IF, Koşul Yapısı](#if-ko%C5%9Ful-yap%C4%B1s%C4%B1)
  - [CONCAT, String Birleştirme](#concat-string-birle%C5%9Ftirme)
- [String İşlemleri](#string-i%CC%87%C5%9Flemleri)
  - [String Parçalama (MID)](#string-par%C3%A7alama-mid)
- [Harici Bağlantılar](#harici-ba%C4%9Flant%C4%B1lar)

## Temel Değişkenler

| Değişken | Açıklama  |
| -------- | --------- |
| String   | `"Selam"` |
| int      | `1`       |
| hücre    | `A3`      |

## Excel Fonksiyonları

Fonksiyonların kullanımı `=` ön eki ile başlar

| Fonksiyon    | Açıklama                          |
| ------------ | --------------------------------- |
| `IF`         | Koşul yapısı                      |
| `+`, `*` ... | Aritmetik işlemleri destekler     |
| `<>`         | Eşit değildir (`!=` desteklenmez) |
| `CONCAT`     | Stringleri birleştirme            |

### IF, Koşul Yapısı

```excel
=IF(kosul, dogruysa, yanlissa)
```

- `=IF(1, 1, 0)` 1 döndürür
- `=IF("A" <> "B", 1, 0)` 1 döndürür

### CONCAT, String Birleştirme

```excel
=CONCAT(<hucre | string | sayı>, <hucre | string | sayı>, ...)
```

- `=CONCAT("1",1,P17)` 11 ve P17'deki metni yazar (P17 = 68 ise 1168)
- `=CONCAT("~", "YEm", "re", "Ak")` ~ YEmreAk

## String İşlemleri

### String Parçalama (MID)

```excel
=MID(<string | hucre>, <index>, <uzunluk>)
```

- `=MID(L7,1,2)` L7'hücresinden 1. karakterden itibaren 2 karakter alır
- `=MID("YEmreAK",1,2)` YE

> Index 1'den başlar 😢

## Harici Bağlantılar

- [Excel çalışma sitesi]

[Excel çalışma sitesi]: https://exceljet.net/
