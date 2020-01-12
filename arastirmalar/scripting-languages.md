---
description: Scripting diller hakkında aldığım notlar
---

# 👨‍💻 Scripting Languages

## Terimler

| Terim | Açıklama |
| :--- | :--- |
| Executable | Daha önceden oluşturulmuş ve işletim sistemin direkt olarak çalıştırabilir uygulamalar |
| Byte Code | Daha sonradan yorumlanmak için hazırlanmış kodlardır, direkt olarak işletim sistemi çalıştıramaz |
| Compiler | Derleyici. Kodlardan **executable** veya **byte code** oluşturur |
| Interpreter | Yorumlayıcı. Kodları direkt olarak çalıştırır . Her seferinden yorumlanması gerekir |

## Dillerinin Çalışma Yapısı

* Java, Python gibi diller **byte code** yapısını kullanır
* C, C\# gibi diller **executable** \(`.exe`\) yapısını kullanır

![Dillerin &#xE7;al&#x131;&#x15F;ma yap&#x131;s&#x131;](../.gitbook/assets/image%20%2885%29.png)

## Scripting Özellikleri

| Terim | Açıklama |
| :--- | :--- |
| Extending | Diğer programların kütüphanelerini de kullanma ve çalıştırma \(?\) |
| Dynamic Typing | Değişken tiplerini belirtmeye gerek yoktur. \(int, str vs gibi\) |
| Data Structures | Kendilerine özgü veri yapıları vardır \(örn `dictionary`, `hash tables`, `list` |

### Dynamic Typing

* Değişken tiplerine **otomatik** karar verilir
  * İsteğe bağlı tiplerin belirtilmesini de kabul eder
* Scripting işlemlerinde sorun oluşturmasa da programlama dilleirnde **sorunlara** sebeb olduğundan tercih edilmez
  * Değişkenlerin **önceden tanımlanması gerekmediğinden** yazım hataları durumunda program yanlış çalışır ama hata vermez
* Bazı scripting dillerinde tüm verileri `string` olarak tutulur, kullandıkları zaman uygun tiplere çevrilerek kullanırlır. Bu işlem verilerin **optimize** tutulmasını sağlar

### Scripting Dillerinde Hafıza Yönetimi Sorunları

* Değişkenlerin kontrolü scripting dillerinde **zordur**
* Belli bir süre sonrasında kullanılmayan veriler hafızada şişkinliğe sebep olur
* **Garbage Collector** gibi kullanılmayacak değişkenleri temizleyen yapılara ihtiyaç duyulur

### Dynamic Code Creation \(Dinamik Kod Oluşturma\)

* Kod içerisinde kod oluşturulup derlenebilmesini mümkün kılar
  * Bazı programlama dillerinde bu mümkün değil veya zordur \(örn C\)

```python
a = 10
x = "print a"
exec(x)
```

## 🔗 Kaynaklar

* [Scripting \(Betik\) dilleri nedir? \(Soru Cevap 14 Kasım 2015\)](https://www.youtube.com/watch?v=z7uJNyhLzOQ)

