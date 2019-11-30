---
description: Kotlin'de diziler
---

# 🚅 Diziler

## 🔰 Diziler \(Arrays\)

`val dizi = arrayOfNulls<String>(10)`

* String : Değişken tipi
* 10 : Dizi boyutu
* dizi\[0\] = "Dizi 0"
* dizi\[1\] = "dizi 1" şeklinde tanımlanır.

> Not: val olan dizi değişkenimiz oluyor, dizi\[0\] val olmuyor, var oluyor. Atama yapılabiliyor.

`val sayıDizisi = intArrayOf(1, 2, 3, 4)`

* 1, 2, 3, 4 sırasıyla 0, 1 ,2 ,3. indexlerin değerleri
* sayıDizisi.set\(2, 9\)
  * 2 : index
  * 9 : index'e yerleşecek değer.

> \(dizideki 3 değeri 9 olacak, yeni dizi : 1, 2, 9, 4\)

## ✨ Boyutu Değiştirilebilen Diziler

`val liste = ArrayList<String>()`

* String : değişken tipi
* liste.add\("liste1"\)
* liste.add\("liste 2"\)
* liste.add\("liste 2"\)
* liste.add\(1, "Hello"\)
  * 1 : index
  * "Hello" değişkene atanan değer
  * liste'nin değerleri \["liste1", "Hello", "liste2", "liste2"\]

## 🎡 Her Elemanı Farklı Olan Diziler

`val küme = HashSet<Int>()`

* Int : Değişken tipi
* küme.add\(2\)
* küme.add\(2\) // 2 tane aynı değer olamaz bu kaydedilmez. \(Set özelliği\)
* küme.add\(0, 3\)
  * 0 : index
  * 3 : değer
  * küme'nin değerleri \[3, 2\]

`val harita= HashMap<String, Double>`

* String : Key \(Konum bilgisi , anahtarı\)
* Double : Değer
* harita.add\("ilkdeger", 1.0\)
* harita.add\("ikincideger", 2.6\)
* harita.get\("ilkdeğer"\) // Verileri almak için yapılır.
  * ilkdeğer : anahtar değeri
* harita dizisinde
  * ilkdeğer indexinde 1.0
  * ikincideğer indexinde 2.6 var.

