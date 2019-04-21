# Protocol Buffer (Protobuf) <!-- omit in toc -->

## İçerik <!-- omit in toc -->

> `HOME` tuşu ile yukarı yönlenebilrsiniz.

- [Nedir](#nedir)
- [JSON Hangi Durumlarda Kullanılmalı](#json-hangi-durumlarda-kullan%C4%B1lmal%C4%B1)
- [XML yerine neden protobuf kullanılmalı](#xml-yerine-neden-protobuf-kullan%C4%B1lmal%C4%B1)
- [Terimler](#terimler)
- [Kaynaklar](#kaynaklar)

## Nedir

- Sınıf[*](#Terimler) yapısı ile verileri tutmamızı sağlar
- Hızlıdır ve az kod yazdırır
- Google geliştiricileri tarafından desteklendiğinden süreklilir ve yenilik vaad eder

## JSON Hangi Durumlarda Kullanılmalı

- Verilerin insan tarafından okunabilir olması gerekirse
- Servisin verileri web tarayıcısı tarafından doğrudan işleniyorsa
- Sunucu kısmı javascript ile yazıldıysa
- Verileri sınıf[*](#Terimler) yapısına bağlamak için hazır değilseniz
- Bant genişliğiniz başka araç eklemeye izin vermiyorsa
- Farkı türde bir servis kullanmanın yükü çok fazla ise

## XML yerine neden protobuf kullanılmalı

- Kolaydır
- 3 ila 10 kat daha az kod yazarız
- 20 ile 100 kat daha hızlı işlenir
- Daha belirgiindir
- Verileri ulaşmak için veri sınıfları oluşturur, bu sayede programlamada erişilebilir

## Terimler

- Sınıf: *Class*

## Kaynaklar

- [5 Reasons to Use Protocol Buffers Instead of JSON For Your Next Service](https://codeclimate.com/blog/choose-protocol-buffers/)
- [Google Developer Guide](https://developers.google.com/protocol-buffers/docs/overview)
- [Google Protocol Buffers](https://developers.google.com/protocol-buffers/)