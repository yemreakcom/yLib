# C++ Scanf İpuçları

## Scanf Veri Alma Sorunu

Bir çok kodlamada `scanf("%c",&x);` şeklinde veri talebinde bulunuyoruz. Bu verileri kullanıcıdan talep ederken eğer kullanıcı satır atlatıcı tuşa bastığında <kbd>ENTER</kbd> ard arda olan scanf fonksiyonlarında girdi almada problemler oluşuyor.

![scanf][Scanf Example]

Örneğin yukarıdaki koddaki gibi bir scanf kullanımında, kullanıcı sırasıyla
`'a'`, `'b'`, `'c'` verilerini girmiş olsun. `x`, `y` ,`z` 'yi ayrı ayrı ekrana bastığımızda çıktı şu şekilde olacaktır:

![scanf_out][Scanf Out]

### Neden Veri Almada Sorun Var

Programa `'a'` yazıp <kbd>ENTER</kbd>'a bastığımız zaman:

- <kbd>ENTER</kbd>'ı da veri olarak yani `'\n'` olarak algılıyor.
- Elimizde `'a'` ve `'\n'` karakterleri oluyor
- İlk `char` değişkenine `'a'` harfi, ikinci `char` değişkenine `'\n'` harfi atanıyor
- İki karakter girdiğimizi zannederken program üç karakter aldığı için ekrana yazdırma işlemlerine geçiyor
- Fark edildiği üzere `İkinci eleman:` dan sonra bir satır atlatılmış. İşte bu `'\n'` olarak ifade ettiğimiz <kbd>ENTER</kbd>'a basınca `y` değişkenine atanan karakter.

### Nasıl Engellenir

Çözüm oldukça basit. `scanf`'lerin içine `"%c"` yerine `" %c"` yazmak. Bu sayede fonksiyon <kbd>SPACE</kbd>, <kbd>ENTER</kbd> gibi özel karakterleri girdi olarak algılamıyor.

![scanf_fix][Scanf Fix]

### Ya Bu %20s'in Olayı Nedir

Yazdırılacak olan **string** değeri için **20 karakterlik** bir alan ayırıp, ayrılan alanın **sağına dayalı** yazdırmak için kullanılmaktadır.

> Görsel anlamda yazıları birbirine hizalamak için tercih edilmekte.

### Peki ya -%20s

Önceki kullanım ile aynı şekilde 20 karakterlik bir alan ayırmakta lakin bu sefer çıktı, ayrılan alanın **soluna dayalı** şekilde yazılmakta.

![scanf_negative_s][Scanf Negative]

[Scanf Example]: ../../res/blogger_scanf.png
[Scanf Out]: ../../res/blogger_scanf_out.png
[Scanf Fix]: ../../res/blogger_scanf_fix.png
[Scanf Negative]: ../../res/scanf_negative_s.png
