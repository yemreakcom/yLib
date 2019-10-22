---
description: Java ile ilk programı oluşturma
---

# 👩‍💻 Java Programlama

## İlk Programı Oluşturma <a id="ilk-programi-olusturma"></a>

Programlamaya başlamanın olmazsa olmazlarından biri de _consola_ `"Merhaba Dünya"` \(`"Hello World"`\) yazdırmaktır, o halde biz de bu geleneği bozmadan başlayalım 😊

![&#x130;lk program&#x131; olu&#x15F;turma](../../../.gitbook/assets/image%20%2855%29.png)

> Bu yazımda **NetBeans** tabanlı ilerleyeceğim, eğer _NetBeans_ kullanmak istiyorsan [buraya](https://github.com/yedhrab/YWiki/tree/169abadfd1b8862c004399268f6ca1f9f9359d61/1%20-%20Programlama%20Notlar%C4%B1/2%20-%20Java/1%20-%20Java%27ya%20Giri%C5%9F/NetBeans%20Kurulumu.md) tıklayarak _NetBeans_ kurulum talimatlarına ve proje açılımına bakabilirsin.

## Birkaç Faydalı Terim <a id="birkac-faydali-terim"></a>

Kesinlikle Bilmeliyiz ki, Java'da kodlar **main** metodu üzerinden okunmaya başlar, bu sebeple kodlamayı **main** metodunun içine yapmamız gerekmektedir.

| Terim | Açıklama |
| :--- | :--- |
| Class | Soyut bir veri kümesidir, kodlamaların her biri bunlar içinde olmak zorundadır. Metodlardan oluşur |
| Method | Diğer programlama dillerinde Fonksiyon olarak da anılır, birden fazla kez kullanılabilen, kod bloklarıdır. Matematik dersindeki fonksiyonlar gibi... |

> İlerleyen zamanlarda methodlar hakkında geniş bir bilgi vereceğim, şimdilik ismen yabancı olmamanız için adlarına kısaca değindim ama ben merak ettim şimdi bakacağım diyorsan [buraya](http://umiitkose.com/2015/08/metodlar/) tıklayabilirsin 😁

### Class ve Method Resmi <a id="class-ve-method-resmi"></a>

> Soldan sağa ilerler.

​![class](https://firebasestorage.googleapis.com/v0/b/gitbook-28427.appspot.com/o/assets%2F-LnsQQcX0CRx75Vk7yi2%2F-Lr_T4cte-AnjWwF1ImB%2F-Lr_TClKw8F1n_-mJFOa%2Fjava_class.jpg?generation=1571512981808849&alt=media) ![method](https://firebasestorage.googleapis.com/v0/b/gitbook-28427.appspot.com/o/assets%2F-LnsQQcX0CRx75Vk7yi2%2F-Lr_T4cte-AnjWwF1ImB%2F-Lr_TClMH8rMhA7sWPYP%2Fjava_method.jpg?generation=1571512976241074&alt=media)​‌

## Ekrana Yazı Basma <a id="ekrana-yazi-basma"></a>

`System.out.println("isteğimiz yazı");` yazarak istediğimiz yazıyı ekranda bastıra biliriz.‌

* Ekrandaki yeşil **play** butona ya da F6 'ya basarak derleyin
* Çıktı _java console_unda \(alttaki ekran\) oluşacaktır

![](https://blobscdn.gitbook.com/v0/b/gitbook-28427.appspot.com/o/assets%2F-LnsQQcX0CRx75Vk7yi2%2F-Lr_T4cte-AnjWwF1ImB%2F-Lr_TClOZN6lZBR0puZf%2Fjava_console_out.png?generation=1571512982879054&alt=media)

> `sout` yazıp CTRL + SPACE yaparsan ENTER'a absarak derleyici sana tam halini gösterecektir. \(İmleç olması gereken yerde olacaktır\)

![](https://blobscdn.gitbook.com/v0/b/gitbook-28427.appspot.com/o/assets%2F-LnsQQcX0CRx75Vk7yi2%2F-Lr_T4cte-AnjWwF1ImB%2F-Lr_TClQDIb_7vahgxnn%2Fjava_sout.png?generation=1571512983518491&alt=media)

## Ekrana Çoklu Yazı Basma <a id="ekrana-coklu-yazi-basma"></a>

* `System.out.println("");` Tırnak işareti içindeki veriyi ekrana yazdırıp, **yeni bir satır** atlatır.
* `System.out.print("");` Tırnak işareti içindeki veriyi ekrana yazdırıp, **satır atlatmaz**

‌

​![Sout1](https://firebasestorage.googleapis.com/v0/b/gitbook-28427.appspot.com/o/assets%2F-LnsQQcX0CRx75Vk7yi2%2F-Lr_T4cte-AnjWwF1ImB%2F-Lr_TClSw0PWJPWvhWX3%2Fjava_sout_ex.png?generation=1571512982398448&alt=media) ![Sout2](https://firebasestorage.googleapis.com/v0/b/gitbook-28427.appspot.com/o/assets%2F-LnsQQcX0CRx75Vk7yi2%2F-Lr_T4cte-AnjWwF1ImB%2F-Lr_TClUrcDy9mgCZfTu%2Fjava_sout_ex2.png?generation=1571512977719240&alt=media)

