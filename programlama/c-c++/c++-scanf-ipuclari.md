---
description: C'deki kullanıcıdan veri alma metodu olan scanf hakkında bilgiler
---

# 💡 C++ Scanf İpuçları

## Scanf Veri Alma Sorunu

Bir çok kodlamada `scanf("%c",&x);` şeklinde veri talebinde bulunuyoruz. Bu verileri kullanıcıdan talep ederken eğer kullanıcı satır atlatıcı tuşa bastığında ENTER ard arda olan scanf fonksiyonlarında girdi almada problemler oluşuyor.

![](../../.gitbook/assets/image%20%2813%29.png)

Örneğin yukarıdaki koddaki gibi bir scanf kullanımında, kullanıcı sırasıyla `'a'`, `'b'`, `'c'` verilerini girmiş olsun. `x`, `y` ,`z` 'yi ayrı ayrı ekrana bastığımızda çıktı şu şekilde olacaktır:

![](../../.gitbook/assets/image%20%2877%29.png)

### Neden Veri Almada Sorun Var

Programa `'a'` yazıp ENTER'a bastığımız zaman:

* ENTER'ı da veri olarak yani `'\n'` olarak algılıyor.
* Elimizde `'a'` ve `'\n'` karakterleri oluyor
* İlk `char` değişkenine `'a'` harfi, ikinci `char` değişkenine `'\n'` harfi atanıyor
* İki karakter girdiğimizi zannederken program üç karakter aldığı için ekrana yazdırma işlemlerine geçiyor
* Fark edildiği üzere `İkinci eleman:` dan sonra bir satır atlatılmış. İşte bu `'\n'` olarak ifade ettiğimiz ENTER'a basınca `y` değişkenine atanan karakter.

### Nasıl Engellenir

Çözüm oldukça basit. `scanf`'lerin içine `"%c"` yerine `" %c"` yazmak. Bu sayede fonksiyon SPACE, ENTER gibi özel karakterleri girdi olarak algılamıyor.

![](../../.gitbook/assets/image%20%288%29.png)

### Ya Bu %20s'in Olayı Nedir

Yazdırılacak olan **string** değeri için **20 karakterlik** bir alan ayırıp, ayrılan alanın **sağına dayalı** yazdırmak için kullanılmaktadır.

> Görsel anlamda yazıları birbirine hizalamak için tercih edilmekte.

### Peki ya -%20s

Önceki kullanım ile aynı şekilde 20 karakterlik bir alan ayırmakta lakin bu sefer çıktı, ayrılan alanın **soluna dayalı** şekilde yazılmakta.

![](../../.gitbook/assets/image%20%28100%29.png)

