---
description: MS Office üzerindeki excelde formül yazmayı anlatır
---

# 📈 Excel

## Temel Değişkenler

| Değişken | Açıklama |
| :--- | :--- |
| String | `"Selam"` |
| int | `1` |
| hücre | `A3` |

## Excel Fonksiyonları

Fonksiyonların kullanımı `=` ön eki ile başlar

| Fonksiyon | Açıklama |
| :--- | :--- |
| `IF` | Koşul yapısı |
| `+`, `*` ... | Aritmetik işlemleri destekler |
| `<>` | Eşit değildir \(`!=` desteklenmez\) |
| `CONCAT` | Stringleri birleştirme |

### IF, Koşul Yapısı

```text
=IF(kosul, dogruysa, yanlissa)
```

* `=IF(1, 1, 0)` 1 döndürür
* `=IF("A" <> "B", 1, 0)` 1 döndürür

### CONCAT, String Birleştirme

```text
=CONCAT(<hucre | string | sayı>, <hucre | string | sayı>, ...)
```

* `=CONCAT("1",1,P17)` 11 ve P17'deki metni yazar \(P17 = 68 ise 1168\)
* `=CONCAT("~", "YEm", "re", "Ak")` ~ YEmreAk

## String İşlemleri

### String Parçalama \(MID\)

```text
=MID(<string | hucre>, <index>, <uzunluk>)
```

* `=MID(L7,1,2)` L7'hücresinden 1. karakterden itibaren 2 karakter alır
* `=MID("YEmreAK",1,2)` YE

> Index 1'den başlar 😢

## Harici Bağlantılar

* [Excel çalışma sitesi](https://exceljet.net/)

