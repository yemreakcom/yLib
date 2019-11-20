---
description: Protobuf deyimi ve neden kullanılması gerektiği
---

# 💽 Protocol Buffer \(Protobuf\)

## Nedir

* Sınıf[\*]() yapısı ile verileri tutmamızı sağlar
* Hızlıdır ve az kod yazdırır
* Google geliştiricileri tarafından desteklendiğinden süreklilir ve yenilik vaad eder

## JSON Hangi Durumlarda Kullanılmalı

* Verilerin insan tarafından okunabilir olması gerekirse
* Servisin verileri web tarayıcısı tarafından doğrudan işleniyorsa
* Sunucu kısmı javascript ile yazıldıysa
* Verileri sınıf[\*]() yapısına bağlamak için hazır değilseniz
* Bant genişliğiniz başka araç eklemeye izin vermiyorsa
* Farkı türde bir servis kullanmanın yükü çok fazla ise

## XML yerine neden protobuf kullanılmalı

* Kolaydır
* 3 ila 10 kat daha az kod yazarız
* 20 ile 100 kat daha hızlı işlenir
* Daha belirgiindir
* Verileri ulaşmak için veri sınıfları oluşturur, bu sayede programlamada erişilebilir

## Terimler

* Sınıf: _Class_

## Kaynaklar

* [5 Reasons to Use Protocol Buffers Instead of JSON For Your Next Service](https://codeclimate.com/blog/choose-protocol-buffers/)
* [Google Developer Guide](https://developers.google.com/protocol-buffers/docs/overview)
* [Google Protocol Buffers](https://developers.google.com/protocol-buffers/)

