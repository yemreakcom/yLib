# 🔰 Nodejs Giriş

## ❔ Nodejs Nedir

Node.js js \(javascript\) tabanlı bir platformdur.

* Kullandığı motor: v8 java-engine'dir. Ki bu motor, chrome için  Google tarafından geliştirilmiştir. Chrome, chromium, opera gibi tarayıcılarda kullanılmaktadır.
* Temel olarak 2 yapıda çalışır:
  * Script işleme
  * A REPL \(Read Eval Print Loop\)

## Event Loop

* Normal çalışma mantığında; Kodlar todo list'e atılır. Ve yapılacak işlemler bitince motor durur.
* Node.js; Kodlar todo list'e atılır ve her kod yeni bir işlem daha oluşturur, böylece sonsuz döngüye girer ve motor durmaz. \(serverlar böyle tasarlanır.\)

## Asenkron Yapısı

Normal işlemler sıra ile yapılır:

* Siteden database'ye mesaj gönderilir.
* Database mesajı alır ve hazırlar, cevap verme sürecine geçer.
* Bu süreçte server beklemede kalır, devam etmez !  \(Blocking\)

Nodejs'in asenkron yapısıyla:

* Database'den cevap gelene kadar, server diğer işlemlerine devam eder.
* Cevap geldiğinde database verisini işlemeye başlar \(Non-Blocking / asynchronize \)

## Node Module System

* Bir dosyayı derleyerek bütün dosyaların çalışması sağlanır.
  * `var lib = require('.lib/');`
    * Dosyanın modülü, değişkene atanır.
    * ".lib/" değişkendir.
  * module.exports = veri;
    * Modulümüzün "require" ile çağrıldığında, göndereceği veriyi  \("veri"\) atıyoruz.
* Bu şekilde tüm istenen dosyalar birbirine bağlı oluyor ve tek bir dosyadan derleniyor.

### Modül Sistemine Örnek

```javascript
// Dosya1;
// dosya2'i (module.export'unu) bir fonksiyona atadık.
var aktarılanFonksiyon = require('dosya2');

// Aktarılan dosyanın içindeki test metodunu kullanıyoruz.
aktarılanFonksiyon.test();
```

```javascript
// Dosya 2;
// Kütüphane objesi oluşturduk.
var kütüphane = {};

// Test fonksiyonunu oluşturduk.
kütüphane.test = function() {
    console.log('selam')
}

Dışarı aktarılacak olan objemizi ayarladık.
module.export = kütüphane;
```

> Artık "node dosya1.js" diyerek iki dosyayı da derleyebiliyoruz.

## Sonuç olarak

* Okumak istediğimiz dosyayı okuyur \(Yukarıdaki örnekte "dosya1.js"\)
* Bu dosyaya bağlı olan tüm diğer dosyaları da okur.
* Bu dosyalardaki senkronize görevleri işlemeye başlar.
* "todo list" teki kodları  ,yapılacak herhangi bir iş kalmayana kadar, "event loop" ile tekrarlı olarak işlemeye başlar.

