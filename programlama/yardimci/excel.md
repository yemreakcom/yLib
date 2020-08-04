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



## N. Hücrelerin Toplamını Hesaplama

* İlk olarak `=ROW(A3)` ile satır bilgisini alırız
* `ROW` işlemi ile A'nın satır numarası olan 3 değerini alırız
* Ardından aradığımız satır olup olmadığını anlamak için `=MOD(ROW(A3); 3)` yaparız
* Yukarıdaki örnekte `3`. katları olan satırlar için True değeri gelecektir
* 3.katı olan satırları toplamak için `3`'ün katı olmayanları `0` ile çarpacağız
* `A1:A9 * (MOD(ROW(A1:A9); 3)=0)` ile `3`. katı olmayan her satır değeri `0` olacaktır
* Son olarak `SUM` ile yukarıdaki sonuçları toplarız
* `=SUM(A1:A9 * (MOD(ROW(A1:A9); 3)=0))`

## Harici Bağlantılar

* [Excel çalışma sitesi](https://exceljet.net/)
* [Döviz kurlarını Excel'e aktarma](https://vidoport.com/excel-finansal-ve-ticari-islemler/2019-doviz-kurlarini-excel-e-aktarma-nasil-yapilir)

