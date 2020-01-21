---
description: 'MySQL, SQL dilini kullanan veri tabanıdır'
---

# 💽 MySQL

## Veri tipleri

| Değişken Tipi | Açıklama | Not |
| :--- | :--- | :--- |
| `BIT` | 0-1 \(True - False\) verilerini tutar. | Değer atanırken tırnaksız atanır |
| `INT` | Tam sayı değeri tutar | Basmak sayısı 1 için 0-9 arası |
| `ENUM` | Özel değişken oluşturma | Değerler tırnaklı olarak atanır |

> Örnekler için [değişkenler]() kısmına bakabilirsin.

## Where Operatörleri

Detaylar için [buraya](https://www.tutorialspoint.com/sql/sql-operators.htm) tıklayabilirsin.

## Tablo İşlemleri

-[Ekleme](http://www.mysqltutorial.org/mysql-add-column/)

### Tablo işlemleri karma Notlar

-[Var olan tabloya varsayılan değerli bir sütun ekleme](https://stackoverflow.com/a/92123)

## Temel Fonksiyonlar

| Fonksiyon | Özelliği |
| :---: | :--- |
| `MAX` | En yüksek değeri bulur |
| `MİN` | En düşük değeri bulur |
| `AVG` | Ortalama değeri bulur |
| `COUNT` | Adet saysını hesaplar |
| `SUM` | Toplam değeri hesaplar |
| `CONCAT` | Verilen metinleri birleştirir |

> Örnekler için [temel fonksiyon örnekleri]() kısmına bakabilirsin.

## Gruplama

`GROUP BY` ile yapılır.

* Tekrarlı verileri göstermez.
* `DISTINCT` anahtar kelimesini kullanmaya gerek kalmaz.

> Gruplama yapılmazsa tek sorgu ekrana basılır.

![](../../.gitbook/assets/image%20%287%29.png)

## Stored Function

Detaylı bilgi için [buraya](http://www.mysqltutorial.org/mysql-stored-function/) tıklayaibilirsin.

```sql
DROP FUNCTION IF EXISTS [FunctionName];
CREATE FUNCTION [FunctionName]([ParamName] [ParamType]) RETURNS [ReturnType]
    DETERMINISTIC
BEGIN
    DECLARE [paramName] [param_type];

    RETURN ( [select_query] );
END;

-- Kullanım Şekli
SELECT
    [FunctionName]([Param])
FROM
    [Table] as [TableNewName]`;
```

* `DROP FUNCTION IF EXIST` Fonksiyon daha önceden var ise kaldırır.
* `CREATE FUNCTION` Fonksiyon oluşturma
* `RETURNS` Fonksiyonun değer döndürmesi
* `BEGIN` Fonksiyon başlangıcı
* `DECLARE` Fonksiyona özgü değişken tanımlama alanı
* `END` Fonksiyon sonu

-**\[FunctionName\]**: _Fonksiyonun ismi, örn: GetProductName_ -**\[ParamName\]**: _Parametre ismi, örn: name_ -**\[ParamType\]**: _Int, Varchar, Float ..._ -**\[ReturnType\]**: _Fonksiyonun döndüreceği sütunun özelliği, Örn: Varchar\(64\), int\(11\), double_ -**Deterministic**: _Aynı girdiler için her zaman aynı değeri üretir._ -**\[select\_query\]**: _Örn: SELECT_  from table;\* -**\*\[ReturnType\]** ile aynı olmak zorundadır.\*

## Debug Bilgileri

### Join

`INNER JOIN` hataları test etmek için `LEFT JOIN` kullanılır. Bu hatalar:

-Boş veri döndürmesi

olabilir.

### Explain

Sorgu ile ilgili detayları gösterir.

```sql
explain SELECT * from table;
```

![](../../.gitbook/assets/image%20%2876%29.png)

## Optimizasyon

Optimizasyon sorgunun hızlı sonuç vermesi için gereklidir. Optimizasyon işlemleri için:

-Indexleme -Key ile birleştirme \(inner join\) -Ek fonksiyonları kaldırma -`explain` anahtar kelimesi ile sorgu detaylarına bakma

gibi işlemlere başvurulur.

> 5s'den kısa sorgular kabul edilebilir hızdadır.

### Ek Kaynaklar

Optimizasyon hakkında detaylı bilgi için [buraya](https://www.sitepoint.com/optimize-mysql-indexes-slow-queries-configuration/) tıklayabilirsiniz.

-[MySQL'de sorguların hızlı çalışması için ne yapılmalıdır?](https://uzmanim.net/soru/mysql-de-sorgularin-hizli-calismasi-icin-ne-yapilabilir/790) -[Indexleme neden yapılır?](https://www.sinanbozkus.com/veritabanlarinda-indexleme-mantigi/#more-78)

## MySQL Yapılandırması

* [DNS sorunu yüzünden yavaşlamayı engelleme](https://stackoverflow.com/a/1292882)

### MySQL yapılandırma dosyası

Yapılandırma dosyası olan `my.ini` dosyasını bulmak için:

* ✲ Ctrl + `R` ile çalıştır uygulamasını açın
* `services.msc` yazıp `ENTER`'a basın
* Servis ekranında MySQL servisini bulup çift tıklayın
* `Genel` sekmesi altında `Path to Executable` kısmında `ini` ile biten yol
* Örnek Yol: _C:\ProgramData\MySQL\MySQL Server 8.0\my.ini_

### MySQL workbench üzerinden yapılandırma

```sql
SET GLOBAL [Ayar]=[Değer];
SET GLOBAL connect_timeout=28800;
SET GLOBAL wait_timeout=28800;
SET GLOBAL interactive_timeout=28800;
```

### Karma yapılandırma notları

* `default-character-set=utf8`

## Karma Notlar

* [Getting Last Record](https://dzone.com/articles/get-last-record-in-each-mysql-group)
* [Select içinde if kullanma](https://stackoverflow.com/a/63480)
* [Koşullu Sayma](https://stackoverflow.com/a/9798978)
* [En yüksek değer sahip satırı alma](https://stackoverflow.com/a/11913444)
* [Sadece en yüksek değere eşit olan satırları alma](https://stackoverflow.com/a/7745635) &lt;- Optimize Edilmiş

## Örnekler

### Temel örnekler

```sql
SELECT [ID], [Sütun] FROM [Tablo] WHERE [ID] = [Sayı];
UPDATE [Tablo] SET [Sütun] = [Değişken Tipine Uygun Değer] WHERE [ID] = [Sayı];
INSERT INTO [Tablo] VALUES ([Sütun1 Değeri], [Sütun2 Değeri]);
```

### Tablo işlemleri

#### Tablo Oluşturma

```sql
CREATE TABLE IF NOT EXISTS [Tablo] (
    [ID Sütunu] [Değişken Tipi] DEFAULT [Varsayılan Değer] PRIMARY KEY,
    [Sütun] [Değişken Tipi]
);
```

#### Tablo değiştirme

```sql
ALTER TABLE [Tablo] ADD COLUMN [Sütun] [Değişken Tipi] DEFAULT [Varsayılan Değeri] AFTER [Önceki Sütun];
ALTER TABLE [Tablo] DROP COLUMN [Sütun];
ALTER TABLE [tablo ismi] ADD COLUMN [sütun ismi] BIT DEFAULT 0; -- veya False
ALTER TABLE [tablo ismi] ADD COLUMN [sütun ismi] INT(1) DEFAULT 1;
ALTER TABLE [tablo ismi] ADD COLUMN [sütun ismi] ENUM('0', '1') DEFAULT '0';
```

> Yönelmek için [veri tipleri]() linkine tıklayabilirsin.

### Temel Fonksiyon Örnekleri

```sql
SELECT MAX(*) FROM Ogrenci;
SELECT MIN(*) FROM Ogrenci;
SELECT AVG(*) FROM Ogrenci;
SELECT COUNT(*) FROM Ogrenci;
SELECT ... WHERE CONCAT("product_id=", "208") = "product_id=208";
```

> Yönelmek için [temel fonksiyonlar]() yazısına bakabilirsin.

### Karma MySQL sorgusu örnekleri

```sql
SELECT COUNT(if(`crr`.`return_reason_id` = 14, `crr`.`return_reason_id`, null)) from ...
```

> Koşul sağlanırsa sayar.

![](../../.gitbook/assets/image%20%2836%29.png)

## Faydalı Kaynaklar

* [MySQL Tutorial](https://www.w3schools.com/sql/default.asp)

