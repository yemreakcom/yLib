# Genel Bilgiler <!-- omit in toc -->

> Faydalı Kaynaklara göz atmayı unutma

## Diller Arasındaki Bağlantı

![lang_network](../res/lang_network.jpg)

## Adlandırma Yapısı

Fare ile çift tıklandığında metinler içerdikleri karakterlere göre seçilir.

- `-` `(tire)` ile parçalı oluşturursunuz
- `_ (alt tire)` ile uzun metinler oluştururusunuz

### Adlandırma Örnekleri

```sh
model_ismi # Modelin ismi seçilir. Başka özelliği yoktur
veriler-resim # Verilerin resim özelliği alınır. Başka özelliği de vardır
```

## Terimler

### Ana Terimler

| Terim     | Açıklama                                                                |
| --------- | ----------------------------------------------------------------------- |
| library   | Özel bir iş için toplanmış metodlar fonksiyonlar (ev için alet çantası) |
| framework | Kapsamlı işler için toplanmış metodlar (önceden yapılmış ev)            |
| API       | Uygulama ile karşılıkla haberleşme (istek gönderip, karşılık alma)      |
| Singleton | Tek seferlik tanımlanabilen uygulama türü                               |

### Tüm Terimler

Yazılımda kullanılan terimler

| Kavram       | Türkçe Karşılığı | Ek Açıklama                                                                                       |
| ------------ | ---------------- | ------------------------------------------------------------------------------------------------- |
| Feed         | Akış             | Instagramdaki resim alanı, veya sitelerdeki ana verilerin alanı                                   |
| Feature      | Özellik          |                                                                                                   |
| Bug          | Hata - Sıkıntı   | Yazılımın açılmaması gibi çeşitli sorunlar                                                        |
| Dev          | Geliştirici      |                                                                                                   |
| Script       | Dile özgü kod    | Belli bir de yazılan proje kadar iyi olmayan kod topluluğu                                        |
| Code Snipped | Kod Parçası      | 1-2 satırlık kodlardan oluşan kod parçası                                                         |
| Register     | Yazmaç           |                                                                                                   |
| Cache        | Önbellek         | Verileri hafızada tutup hızlı açmak için önbellek kullanılır                                      |
| Cookie       | Çerez            | Bir siteye tekrardan girdiğimizde giriş bilgilerimiz gibi bilgileri koruması, çerezlerle sağlanır |
| Run          | Çalıştırma       | Yazılan kodu derleyici üzerinde çalıştırma                                                        |
| Debug        | Hata Ayıklama    | Kodu derleyici üzerinde adım adım gerekli yerlerde duracak şekilde çıktılarla çalıştırma          |
| Banner       | Afiş             |                                                                                                   |
| Slider       | Kayan Afiş       |
| Namespace    | İsim alanı       | Aynı amaca hizmet eden özellikleri, sınıfları ve fonksiyonları aynı çatı altında toplama          |
| Wild Card    |                  | `..` `.` `*` gibi terimleri içeren metne verilen isim                                             |

### Değişken Terimleri

| Kavram | Türkçe Karşılığı | Ek Açıklama                                             |
| ------ | ---------------- | ------------------------------------------------------- |
| Flag   | Bayrak           | Varlık (evet, hayır) değeri tutan değişkenler - Booelan |

### Raporlama (Logging) Seviyeleri

Aşağıya doğru inildikçe, ekrana basılan çıktı azalır.

- DEBUG
- INFO
- WARNING
- ERROR
- CRITICAL

## Platformlar

| Platform                                                                     | Açıklama                |
| ---------------------------------------------------------------------------- | ----------------------- |
| [Github](https://github.com/), [Gitlab](https://gitlab.com/)                 | Kaynak kod paylaşımı    |
| [Read The Docs](https://readthedocs.org/)                                    | Döküman paylaşımı       |
| [StackOverflow](https://stackoverflow.com/), [Quora](https://www.quora.com/) | Soru cevap platformları |

### Google Summer of Code

Resmi sitesi için [buraya](https://summerofcode.withgoogle.com/) bakabilirsin.

- Bir mentörünüz ve bir projeniz oluyor
  - Proje fikriniz yoksa fikir de önermekteler
- Para desteği de sağlanıyor
- Yaz boyunca onunla uğraşıyorsunuz

> Uzaktan işleyen bir sistemdir.

## Yazı Fontları

| Font        | Özelliği                                                                             | Bağlantılar                                                                                                                 |
| ----------- | ------------------------------------------------------------------------------------ | --------------------------------------------------------------------------------------------------------------------------- |
| Fira Code   | Programlama dilleri için geliştirilmiş != gibi karakterleri değildir olarak gösterir | [🌐](https://github.com/tonsky/FiraCode) [⬇](https://github.com/tonsky/FiraCode/releases/download/1.206/FiraCode_1.206.zip) |
| Roboto Mono | Android varsayılan fontunun kodlama için yapılmış hali                               | [🌐](https://fonts.google.com/specimen/Roboto+Mono)                                                                         |

> Fira Code için `Enable font ligaratures` ayarını aktif etmeniz gerekmekte. Aksi halde `!=`, `>=` gibi karakteri birleştiremez.

## Faydalı Kaynaklar

- [How to Select Your First Programming Language](https://www.youtube.com/watch?v=2EaopRDxNrw)
- [Türkçe Yazılım Geliştirme Kaynakları][türkçe kaynaklar]
- [Görsel Programlama Dilleri](https://maker.pro/custom/tutorial/which-programming-language-should-i-choose-graphics-and-guis)
- [Kodlama organizasyonu ve yapısı](https://medium.com/@msandin/strategies-for-organizing-code-2c9d690b6f33)

[türkçe kaynaklar]: https://turkcekaynaklar.com/
