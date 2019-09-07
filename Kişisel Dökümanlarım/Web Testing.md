# Web Testing 

## Web Testing Nedir

Web testing, web projesinin canlıya ya da üretim moduna geçmeden önce projedeki *bug*'ların tespitini amaçlar. Kontrollerden bazıları:

- Güvenlik
- Sitenin işlevselliği
- *Network* trafiği
- Kullanıcın rahat erişebilmesi

## Functionality Testing (İşlevsellik Testi)

Ürünün istenilenleri yerine düzgün getirmesini ve üretim dökümanında verilen işlemlerin yapılabilirliğini test etme eylemidir.

### Link Testing (Bağlantı Testi)

Tüm site bağlantı tiplerinin çalışabilirliği test edilir. Örnek olarak:

- *Outgoing Links*
- *Internal Links*
- *Anchor Links*
- *MailTo Links*

### Forms Testing (Form Testi)

Form elemanlarının düzgün çalışabilirliği test edilir, bu testlerden bazıları:

- Veri kontrol *script*'lerinin çalışabilirliği (şifre istenildiği gibi girilmezse uyarı verme gibi)
- Varsayılan değerlerin uygun doldurulması
- Girdilerin veritabanın veya ilgili bağlantılara doğru aktarılması
- Formların düzgün konumlandırılmış ve okunabilir halde olması

### Cookie Testing (Çerez Testi)

*Cookie*'lerin istenildiği gibi çalışıp çalışmadığı test edilir, istenilen durumlar:

- *Cookie*'lerin süresi dolduğunda veya *cache*'in temizlenmesi durumunda kaldırılması
- *Cookie*'ler kaldırıldığında, yeni girişte tekrardan oluşturulabilmesi ve bilgilerin istenmesi

> *Cookie* siteye ilk giriş yaptığımızda yerel hafızada depolanan ve birkaç günlük süre içerisinde bilgilerimizi tekrar girmememizi sağlayan kullanıcı bilgilerine verilen isimdir.

<div class="page"/>

### HTML and CSS Testing

HTML ve CSS dosyalarındaki sorunlardan kaynaklı sitede yavaş yüklenme söz konusu olabilmekte, bu testte bu kusurlar belirlenmeye çalışılır.

- Herhangi bir *Syntax* hatası olup olmadığı kontrolü
- Okunabilir olan *Renk Şemalarının* kontrol edilmesi
- HTML ve CSS *W3C, ECMA, OASIS* gibi genel standardlara uygun olup olmadığı kontrolü

> Kullanılabilir araçlar: `QTP`, `Selenium`

### Business Workflow Testing (İş Akışı Testi)

Web sitesinin belilenen iş süreçlerini tamamlayabilmesi test edilir. Bu testin yöntemleri:

- Kullanıcının yapacağı işlemleri baştan aşağı kontrol edilmesi
- Kullanıcının yanlışlıkla veya yapmaması gereken işlemlerin kontrol edilmesi gerekli hata veya uyarı mesajlarının verilmesi

<div class="page"/>

## Usability Testing (Kullanılabilirlik Testi)

Kullanılabilirlik testi hedef kitleye yakın ufak *tester* grubu tarafından yürütülen hayati önem taşıyan testlerdendir.

- Site menülerin, butonların ve yönlendirmelerinin tüm site içerisinde kolaylıkla görülebilir olması
- İçeriklerin yazım hataları içermemesi ve anlaşılabilir olması, sitede resim varsa her birinin `alt` metni içermesi
  - `alt`, HTML resimlerinin bir etiketi
  
> Kullanılabilir araçlar: `Chalkmark`, `Clicktale`

## Interface Testing (Arayüz Testi)

Arayüz testi 3 farklı aşamadan oluşur bu aşamaların her birinin ve sistem yanıtını test eder.

- *Application* (Uygulama)
  - *Request*'lerin *database*'e doğru ulaşması ve *client* tarafında düzgün görüntülenmesi
  - Uygulamadaki hataların sadece yetkililere (kullanıcılara değil) gözükmesi
- *Web server* (Web sunucusu)
  - *Web server*'ın tüm istekleri red olmaksızın kontrol edebiliyor olması
- *Database server* (Veritabanı sunucusu)
  - Veritabanına gönderilen sorguların istenilen sonuçlar üretmesi

> Kullanılabilir araçlar: `AlertFox`, `Ranorex`

## Database Testing (Veritabanı Testi)

Web uygulaması için çok kritik yere sahip olan veritabanının testini ele alır. İstenilen kontroller:

- Sorgular gerçekleştirilirken olası hataların kontrolü
- Ekleme, silme ve güncelleme işlerinde veri bütünlüğün korunması kontrolü
- Sorguların yanıt sürelerinin kontrolü ve gerekirse ince ayarların yapılması
- Veritabanından gelen verilerin uygulamada düzgün olarak gösterebilmesi

> Kullanılabilir araçlar: `QTP`, `Selenium`

## Compatibility Testing (Uyumluluk Testi)

Farklı cihazlarda uygulamanın sağlıklı çalışıp çalışmadığının test edilmesi amaçlanır.

- *Tarayıcı Uyumluluk Testi*
  - Farklı tarayıcılarda uygulamanın sağlıklı çalışıp çalışmadığı kontrol edilir. Örnek verilicek olunursa Javascript ve Ajax çağrılarının düzgün çalışıp çalışmaması.
- *Mobil Tarayıcı Uyumluluk Tesi*
  - Mobil tarayıcılarında istenen testler yapılır.

> Kullanılabilir araçlar: `NetMechanic`

<div class="page"/>

## Uygulamalı Security Testing(Güvenlik Testi)

Güvenlik Testi hassas veri taşıyan uygulamalarda ayrılmaz bir bütün arz eder. E-Ticaret sitelerinde kredi kartı işlemleri örnek verilebilir.

- Yetkisiz giriş olup olmadığı
- Hassas dosyaların yetkisiz indirilmemesi
- Session kontrolü
- SSL sertifikası sahip sitelerin şifrelenmiş(encrypted) SSL sayfasına yönlenmesi
test edilir

> Kullanılabilir araçlar: `Babel Enterprise`, `CROSS`

## Uygulamalı Performance Testing(Performans Testi)

Uygulamaya olan bütün yüklenmelerde çalışabilme durumu test edilir.

- Farklı bağlantı hızlarında hizmet süresi hesaplaması

> Kullanılabilir araçlar: `Loadrunner`, `JMeter`

## Uygulamalı Cookie Testing

> Kaynak için [buraya](https://www.guru99.com/cookie-testing-tutorial-with-sample-test-cases.html) bakabilirsin.

## Uygulamalı Responsive Testing

- Google responsive testing [sitesine](https://search.google.com/test/mobile-friendly) girilecek
- `oguzhanoztas.com` sitesi test edilecek
- Ya da html'i indir hazır bak

## Uygulamalı SQL Injected

String atamaları *encode* işlemine uğramadan yapılıyorsa hata verilmesini sağlar.

- `select * from table where password = " "` kısmında *password* alanına `"` karakteri konulursa *string*'i kapatacağından hata verecektir.
- [Test1](https://tech.io/playgrounds/154/sql-injection-demo/sql-injection-2), [Test2](https://sqlzoo.net/hack/)

<div class="page"/>

## Uygulamalı Diğer Testler

- [Link1](https://github.com/JustinBonaccorso/parking-calculator-tests), [Link2](https://github.com/lowfr3q/MindbodyParking)
- [Sunucu bağlantı kontrolü][Uptime Testing]

## Kaynaklar

- [Web Application Testing: 8 Step Guide to Website Testing](https://www.guru99.com/web-application-testing.html)
- [Responsive Testing](http://learningcms.com/responsive-website-testing/)

[Uptime Testing]: https://www.uptrends.com/tools/uptime
