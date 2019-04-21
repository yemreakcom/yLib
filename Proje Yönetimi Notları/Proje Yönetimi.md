# Proje Yönetimi <!-- omit in toc -->

Projelerde yapılacak iş ve rotasyon önceden belirlenir, gidişat kurgulanır.

## İçerikler <!-- omit in toc -->

> `HOME` tuşu ile yukarı yönlenebilrsiniz.

- [Kaynak Kod odaklı Proje Yönetimi](#kaynak-kod-odakl%C4%B1-proje-y%C3%B6netimi)
  - [Proje Oluşturma & Güncelleme Yapısı](#proje-olu%C5%9Fturma--g%C3%BCncelleme-yap%C4%B1s%C4%B1)
    - [Ufak Projeler için Branch (Tam hazır değil)](#ufak-projeler-i%C3%A7in-branch-tam-haz%C4%B1r-de%C4%9Fil)
    - [Büyük Projeler için Branch Prefix (Ön ek)](#b%C3%BCy%C3%BCk-projeler-i%C3%A7in-branch-prefix-%C3%B6n-ek)
    - [Branch Naming Convention (Yazım kuralı)](#branch-naming-convention-yaz%C4%B1m-kural%C4%B1)
      - [Örnek Kullanım](#%C3%B6rnek-kullan%C4%B1m)
  - [Model View Controller Yapısı](#model-view-controller-yap%C4%B1s%C4%B1)
    - [Yapı düzenleme sırası](#yap%C4%B1-d%C3%BCzenleme-s%C4%B1ras%C4%B1)
  - [Değişken İsimlendirmeleri](#de%C4%9Fi%C5%9Fken-i%CC%87simlendirmeleri)
- [Faydalı Yazılımlar](#faydal%C4%B1-yaz%C4%B1l%C4%B1mlar)
  - [Yönetim Uygulamaları & Siteleri](#y%C3%B6netim-uygulamalar%C4%B1--siteleri)
  - [Web programlama](#web-programlama)

## Kaynak Kod odaklı Proje Yönetimi

Çok kişi ile yapılan projelerde her konuyu birbirimize anlatmak vakit kaybıdır, bu sebeple herkesin sadece kendi işi ile uğraşacağı yapı kurulmalıdır.

- Her fonksyionun nereye yazılacağı belirtilmeli ve projenin taslak yapısı kurulmalıdır.
  - İstenen fonksiyonların taslakları kod içerisine yerleştirilir
  - Kişi istenen tipte veriler veya gönderdiği veriler gönderir
  - Göndereceği veriler için açıklayıcı bir dökümantasyon eklemelidir
  - Yapacağı işlemlerin detaylarını çok fazla anlatmadan istenen veri hakkında bilgi verilmelidir. (Vakit kaynını engeller)
- Projenin en üst kısmında değiştirlebilir veriler saklanmalı ve switch yapısı kurulmalıdır.

### Proje Oluşturma & Güncelleme Yapısı

Proje yönetimi için git kullanılması çok faydalıdır.

- Her yeni ekleme için onu tanımlayan bir **branch** oluşturulur.
  - Branch oluşturma işlemi `checkout` komutuyla yapılır
  - Oluşturulan her branch `master` branch'inden `pull from` komutu ile güncellenir.
    - Güncellenmez ise `merge conflict` hataları meydana gelir ve çok vakit harcar 😢
  - Tüm işlemler yapıldıktan sonra branch'i uzak sunucuda saklamak adına `pull` komutu kullanılır
- **Merge Request** ile *master branch* kısmına eklenme talebi oluşturulur.
- Yönetici, talebi kontrol edip, onaylayarak projeye katar.

> Küresel çalışma adına ingilizce dili tercih edilmektedir.

#### Ufak Projeler için Branch (Tam hazır değil)

Bir proje üzerinde herkes kendi adıyla bir branch açabilir.

#### Büyük Projeler için Branch Prefix (Ön ek)

Büyük projelerdeki temel yapı `konu` / `detay veya dosya` şeklinde branch oluşturmaya dayanır.

- `feature/<detail>` Yenilikler
- `bugfix/<detail>` Hata çözümleri
- `sf/<detail>` Tasarım değişikleri (Store front-end)

> Ardından **merge request** ile geliştirici (dev) ortamına birleştirme isteği oluşturulur.

#### Branch Naming Convention (Yazım kuralı)

- Camel Case
- `<prefix>/thisIsExampleDetail`

##### Örnek Kullanım

- sf/newBannerRow
- feature/excelPhp

### Model View Controller Yapısı

Ek kaynak için [buraya](https://blog.koddit.com/yazilim/mvc-nedir-gercek-orneklerle-mvc-nedir-anlayalim/) tıklayabilirsin.

> Temel amaç *model* ile *view* katmanını ayırmaktır. Bu sayede tasarımı değiştireceğimiz zaman yapısal kodlarla uğraşmak zorunda kalmayız. (*model: back-end view: front-end denebilir*)

| Yapı Ögesi | Özet                          | Örnek                                                     |
| :--------: | :---------------------------- | :-------------------------------------------------------- |
|   Model    | Veriler ile ilgili işlemler   | Veritabanına veri kaydedilmesi ve veritabanından alınması |
|    View    | Kullanıcıya görünen kısım     | Anasayfa gibi web sayfaları                               |
| Controller | Model ile View arası bağlantı | Verinin web sayfasına aktarılması                         |

#### Yapı düzenleme sırası

- **Model** kısmı düzenlenir.
- **Controller** üzerinde bağlantılar oluşturulur.
- **View** ile kullanıcıya sunulur.

### Değişken İsimlendirmeleri

| İsim          | Açıklama                                                   |
| ------------- | ---------------------------------------------------------- |
| `NAME`_PREFİX | Veri tabanı ön eki. *Örn: DB_PREFIX, BRANCH_PREFIX*        |
| Flag          | Checkbox gibi boolean değerleri tutan değişkenlerin adıdır |

## Faydalı Yazılımlar

Eklentileri ile meşhur olan `VsCode` yazılımı tavsiye edilir.

### Yönetim Uygulamaları & Siteleri

| Uygulama İsmi                                                | Açıklama                                                     |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| [Github](https://github.com/) & [Gitlab](https://gitlab.com) | Kaynak kod yöneticisi                                        |
| [Asana](https://asana.com/)                                  | Proje yönetimi & Yapılacaklar Aşaması & İş aktarımı / eşleme |
| [Slack](https://slack.com/)                                  | Takım yönetimi                                               |

### Web programlama

| Uygulama İsmi                                                            | Açıklama                                                         |
| ------------------------------------------------------------------------ | ---------------------------------------------------------------- |
| [Git](https://git-scm.com/downloads)                                     | Kaynak kod yönetimi                                              |
| [PhpStorm](https://www.jetbrains.com/phpstorm/download/#section=windows) | Çok fonksiyonel PHP IDE                                          |
| [Xammpp](https://www.apachefriends.org/tr/download.html)                 | Php için sunucu, veri tabanı vs. işlemleri sunan platform        |
| [Nodejs](https://nodejs.org/en/download/)                                | Javascript kodlarını makine koduna çevir. Js'i sunucuda kullanma |
| [MySQL](https://www.mysql.com/downloads/)                                | Veri tabanı yönetimi                                             |
| [Composer](https://getcomposer.org/download/)                            | Php paket yönetimi (NPM)                                         | Nodejs) gibi |

