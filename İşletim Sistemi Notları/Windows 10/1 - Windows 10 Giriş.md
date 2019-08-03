# Windows 10 Giriş <!-- omit in toc -->

## İçerikler <!-- omit in toc -->

- [İndirme](#%C4%B0ndirme)
- [Faydalı Programlar](#Faydal%C4%B1-Programlar)
- [Temel Dizinler](#Temel-Dizinler)
- [Uygulama Verileri](#Uygulama-Verileri)
- [Otomatik Olarak Oturum Açma](#Otomatik-Olarak-Oturum-A%C3%A7ma)
- [Kısayollar](#K%C4%B1sayollar)
  - [Kısayol Oluşturma](#K%C4%B1sayol-Olu%C5%9Fturma)
  - [Faydalı Kısayollar](#Faydal%C4%B1-K%C4%B1sayollar)
  - [Uygulama İşlemleri](#Uygulama-%C4%B0%C5%9Flemleri)
  - [Gezinti](#Gezinti)
  - [Girdi İşlemleri](#Girdi-%C4%B0%C5%9Flemleri)
  - [Menü Kısayolları](#Men%C3%BC-K%C4%B1sayollar%C4%B1)

## İndirme

_Windows 10 October 2019 EN_ orjinal dosyasını [buradan](https://drive.google.com/open?id=1uzLjabuUUVYaOuRM2f5fX4HtHrb9XMgI) indirebilirsin.
Wİndows 10 son sürümünü indirmek için [buraya](https://www.microsoft.com/tr-tr/software-download/windows10) tıklayabilirsin.

**Media creating tools kullanmadan indirme:**

Siteye girdiğinizde sırasıyla alttaki ayarları açamınız | seçmeniz gerekmekte:

- Geliştirici Ayarları
- _Network conditions_
- _User Agent_ başlığı altında
  - _Select automatically_ seçimini kaldırın
  - _Safari – iPad iOS 9_
- Sayfayı yenileyin

> Detaylı bilgi için [buraya](https://pureinfotech.com/download-windows-10-iso-without-media-creation-tool/) tıklayabilirsin.

## Faydalı Programlar

- Windows ile gelen video düzenleyicisinin kullanımı hakkında [buraya](https://www.howtogeek.com/355524/how-to-use-windows-10s-hidden-video-editor/) bakabilirsin
  - Birleştirme
  - Kırpma
  - Ses ekleme
  - Yavaşlatma
  - Efekt ekleme

| Program                                                                                                                                             | Açıklama                                        |
| --------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------- |
| [Sharex]                                                                                                                                            | Ekran görüntüsü ve video kaydı                  |
| [QuickLook](https://www.microsoft.com/tr-tr/p/quicklook/9nv4bs3l1h4s?activetab=pivot:overviewtab)                                                   | Dosyaları ön izleme (<kbd>SPACE</kbd> tuşu ile) |
| [Microsoft To-Do](https://www.microsoft.com/tr-tr/p/microsoft-to-do-list-task-reminder/9nblggh5r558?cid=msft_web_chart&activetab=pivot:overviewtab) | Yapılacaklar yönetimi                           |
| [Notepads - Beta](https://www.microsoft.com/tr-tr/p/notepads-beta/9nhl4nsc67wm?activetab=pivot:overviewtab)                                         | Hafif ve şık notepad alternatifi                |
| [PDF Conversion Suite]                                                                                                                              | PDF'e dönüştürme işlemleri                      |
| [Pichon - Free Icons]                                                                                                                               | Ücresiz icon kütüphanesi                        |
| [Paint.NET]                                                                                                                                         | Paint'in gelişmiş hali, transparant destekli    |
| [Whatsapp Desktop]                                                                                                                                  | Whatsapp masajlaşma uygulaması                  |
| [Numix Cursors](https://www.deviantart.com/alexgal23/art/Numix-Cursors-631491782)                                                                   | Hafif ve ufak mouse teması                      |
| [Capitaine Cursors r2]                                                                                                                              | Mouse için karanlık tema                        |
| Light Key                                                                                                                                           | Metin tamamlama (Ctrl + TIklama ile) 🤔         |

## Temel Dizinler

Alttaki komutları <kbd>WINDOWS</kbd> + <kbd>R</kbd> ile açılan **run** pencerisine yazmanız gerekmekte.

- `shell:startup` Başlangıçta çalışan uygulamalar
- `shell:AppsFolder` Tüm uygulamalar

## Uygulama Verileri

- `C:\Users\%username%\AppData\Roaming` yani `%appdata%` dizininde yer alır.
  - Arama yerine `%appdata%` yazarak erişebilirsin
- `C:\Users\%username%\AppData\Local`
- `C:\ProgramData`

## Otomatik Olarak Oturum Açma

- İlk olarak <kbd>WINDOWS</kbd> + <kbd>R</kbd> ile `Run` alanını açın
- Çıkan ekrana `netplwiz` yazın ve <kbd>ENTER</kbd>'a basın
- Kutucuğun işaretini kaldırın ve gerekli alana şifrenizi girip `APPLY` butonuna basın

## Kısayollar

Windowsun bize sunduğu nu kısayollar tüm ekranlara baskındır, her yerde çalışır.

> Kısayollarını kendin düzenlemek istersen [AutoHotkey](https://www.autohotkey.com) adlı uygulamayı kullanabilirsin.

### Kısayol Oluşturma

- İlk olarak <kbd>WINDOWS</kbd> + <kbd>R</kbd> ile `Run` alanını açın
- İçerisine `shell:AppsFolder` yazıp <kbd>ENTER</kbd>'a basın
- Çıkan dizinde kısayolunu oluşturmak istediğiniz uygulamaya tıklayın `Create Shortcut` deyin
- Oluşturulamadı ekranı gelecek ve `Yes` deyin
- Masaüstüne gelip oluşan kısayola sağ tıklayın
- `Shortcut` alnına tıklayıp klavyenizden bir tuşa basın
- <kbd>CTRL</kbd> + <kbd>ALT</kbd> kombinasyonları ile kısayol oluşturabilirsiniz

### Faydalı Kısayollar

| Kısayolalr                                                   | Açıklama                                   |
| ------------------------------------------------------------ | ------------------------------------------ |
| <kbd>WINDOWS</kbd> + <kbd>G</kbd>                            | **Game bar** ile video veya ses kayda alma |
| <kbd>WINDOWS</kbd> + <kbd>Ş</kbd>                            | Emoji klavyesi                             |
| <kbd>CTRL</kbd> + <kbd>WINDOWS</kbd> + <kbd>-> veya <-</kbd> | Desktop değiştirme                         |

### Uygulama İşlemleri

| Kısayol                                     | Açıklama                                                                                           |
| ------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| `CTRL` + `W`                                | Pencereyi kapatır                                                                                  |
| `ALT` + `F4`                                | Uygulamayı ve pencerelerini kapatır                                                                |
| `CTRL` + `SHIFT` + `ENTER`                  | Uygulamayı Yönetici olarak açma (`ENTER` yerine fare ile de tıklanabilir)                          |
| `WİNDOWS TUŞU (SUPER)` + `E`                | File explorer'ı açar (Dosya Gezgini)                                                               |
| `WİNDOWS TUŞU (SUPER)` + `R`                | Komutla uygulama çalıştırma penceresi                                                              |
| `WİNDOWS TUŞU (SUPER)` + `<SAYI>`           | Taskbardaki (görev çubuğu / alttaki bar) sıralamaya göre uygulamları gösterir, çalıştırır / gizler |
| `WİNDOWS TUŞU (SUPER)` + `SHIFT` + `<SAYI>` | Üsttekine ek olarak, yeni bir tane açar                                                            |
| `WİNDOWS TUŞU (SUPER)` + `G`                | Kayıt işlemleri, ekran görüntüsü vs.                                                               |
| `WİNDOWS TUŞU (SUPER)` + `X`                | Windows araçları bölümü                                                                            |
| `WİNDOWS TUŞU (SUPER)` + `YUKARI YONU`      | Uygulamayı tam ekran yapma                                                                         |
| `WİNDOWS TUŞU (SUPER)` + `AŞAĞI YONU`       | Uygulamayı küçük ekran yapma                                                                       |

### Gezinti

- `ALT` + `TAB` Uygulamalar arası gezinti
- `CTRL` + `WİNDOWS TUŞU (SUPER)` + `<YON TUŞLARI>` Masaüstleri arası gezinti
- `WİNDOWS TUŞU (SUPER)` + `D` Masaüstünü gösterme / geri alam
- `WİNDOWS TUŞU (SUPER)` + `M` Tüm uygulamaları gizleme (masaüstünü gösterme gibi)
- `WİNDOWS TUŞU (SUPER)` + `,` Anlık masaüstüne bakma
- `WİNDOWS TUŞU (SUPER)` + `L` Oturumu kitleme

### Girdi İşlemleri

- `WİNDOWS TUŞU (SUPER)` + `V` Son kopyalananları gösterir (Clipboard / Pano)
- `WİNDOWS TUŞU (SUPER)` + `Ş` veya `.` Emoji ekleme 👌
- `WİNDOWS TUŞU (SUPER)` + `SHIFT` + `S` Bell bir alanın ekran görüntüsü alma

### Menü Kısayolları

- `WİNDOWS TUŞU (SUPER)` + `I` Ayarlar menüsü
- `WİNDOWS TUŞU (SUPER)` + `U` Görünüm ayarları
- `WİNDOWS TUŞU (SUPER)` + `P` Ekran yansıtma ayarları
- `WİNDOWS TUŞU (SUPER)` + `K` Ağdaki cihaza bağlanma
- `WİNDOWS TUŞU (SUPER)` + `A` Aksiyon Merkezi (Action Center) menüsü
- `WİNDOWS TUŞU (SUPER)` + `Q` veya `S` Arama penceresini açma
- `WİNDOWS TUŞU (SUPER)` + `W` Windows INK çalışma alanını açma

<!-- Bağlantılar -->

[sharex]: https://www.microsoft.com/en-us/p/sharex/9nblggh4z1sp?rtc=1&activetab=pivot:overviewtab
[pichon - free icons]: https://www.microsoft.com/en-us/p/icons8-pichon/9nk8t1kshffr?rtc=1&activetab=pivot:overviewtab
[pdf conversion suite]: https://www.microsoft.com/en-us/p/pdf-conversion-suite/9nblggh0c572?cid=msft_web_chart&activetab=pivot:overviewtab
[paint.net]: https://www.dotpdn.com/downloads/pdn.html
[whatsapp desktop]: https://www.microsoft.com/en-us/p/whatsapp-desktop/9nksqgp7f2nh?activetab=pivot:overviewtab
[capitaine cursors r2]: https://drive.google.com/uc?id=1lnR48aQI9nq4NJlEHyHLO7RoKx46Wl3X
