# Windows 10 Notları <!-- omit in toc -->

Sık kullanılan işletim sistemi notlarım.

## İçerikler <!-- omit in toc -->

> `HOME` tuşu ile yukarı yönlenebilrsiniz.

- [İndirme](#i%CC%87ndirme)
  - [Media creating tools kullanmadan indirme](#media-creating-tools-kullanmadan-indirme)
- [Kısayollar](#k%C4%B1sayollar)
  - [Uygulama İşlemleri](#uygulama-i%CC%87%C5%9Flemleri)
  - [Gezimti](#gezimti)
  - [Girdi İşlemleri](#girdi-i%CC%87%C5%9Flemleri)
  - [Menü Kısayolları](#men%C3%BC-k%C4%B1sayollar%C4%B1)
- [Command Promp (CMD)](#command-promp-cmd)
  - [Cmder Komut İstemi Alternatifi](#cmder-komut-i%CC%87stemi-alternatifi)
    - [CmDer Yapılandırma Ayarları](#cmder-yap%C4%B1land%C4%B1rma-ayarlar%C4%B1)
  - [CMD Komutları](#cmd-komutlar%C4%B1)
    - [CMD Ek Komutlar](#cmd-ek-komutlar)
  - [CMD Değişkenleri](#cmd-de%C4%9Fi%C5%9Fkenleri)
    - [Temel Kullanım](#temel-kullan%C4%B1m)
    - [Sık Kullanılanlar](#s%C4%B1k-kullan%C4%B1lanlar)
  - [CMD Operatörleri](#cmd-operat%C3%B6rleri)
  - [CMD Kod Parçaları](#cmd-kod-par%C3%A7alar%C4%B1)
    - [CMD Döngü Kullanımı](#cmd-d%C3%B6ng%C3%BC-kullan%C4%B1m%C4%B1)
    - [CMD Dosyaları Ardışık olarak adlandırma](#cmd-dosyalar%C4%B1-ard%C4%B1%C5%9F%C4%B1k-olarak-adland%C4%B1rma)
- [Windows için Paket Yöneticisi](#windows-i%C3%A7in-paket-y%C3%B6neticisi)
  - [Hızlı Komut Bilgisi](#h%C4%B1zl%C4%B1-komut-bilgisi)
  - [Sık Kullanılan Paketler](#s%C4%B1k-kullan%C4%B1lan-paketler)
- [PowerShell Kullanımı](#powershell-kullan%C4%B1m%C4%B1)
- [Özelleştirmelerim](#%C3%B6zelle%C5%9Ftirmelerim)
  - [CMD Düzeni](#cmd-d%C3%BCzeni)
  - [Tema Düzeni](#tema-d%C3%BCzeni)
  - [Taskbar Düzeni](#taskbar-d%C3%BCzeni)
  - [Ek Ayalarım](#ek-ayalar%C4%B1m)
- [Windows Özellikleri](#windows-%C3%B6zellikleri)
  - [Varsayılan Windows Özellikleri](#varsay%C4%B1lan-windows-%C3%B6zellikleri)
  - [Alt İşletim Sistemleri](#alt-i%CC%87%C5%9Fletim-sistemleri)
- [Uygulama Ayarları](#uygulama-ayarlar%C4%B1)
  - [Video Ayarları](#video-ayarlar%C4%B1)
- [Terimler](#terimler)
- [Windows 10 Ön Belleğini Temizleme](#windows-10-%C3%B6n-belle%C4%9Fini-temizleme)
  - [CMD Üzerinden Önbelleği Elle Temizleme](#cmd-%C3%BCzerinden-%C3%B6nbelle%C4%9Fi-elle-temizleme)
- [Windows10 Insider Programı](#windows10-insider-program%C4%B1)
  - [Insider Kısayolları](#insider-k%C4%B1sayollar%C4%B1)
  - [Arka Plandaki Evolution Copy Logosunu Kaldırma](#arka-plandaki-evolution-copy-logosunu-kald%C4%B1rma)
- [Harici Linkler](#harici-linkler)

## İndirme

*Windows 10 October 2019 EN* orjinal dosyasını [buradan](https://drive.google.com/open?id=1uzLjabuUUVYaOuRM2f5fX4HtHrb9XMgI) indirebilirsin.
Wİndows 10 son sürümünü indirmek için [buraya](https://www.microsoft.com/tr-tr/software-download/windows10) tıklayabilirsin.

### Media creating tools kullanmadan indirme

Siteye girdiğinizde sırasıyla alttaki ayarları açamınız | seçmeniz gerekmekte:

- Geliştirici Ayarları
- *Network conditions*
- *User Agent* başlığı altında
  - *Select automatically* seçimini kaldırın
  - *Safari – iPad iOS 9*
- Sayfayı yenileyin

> Detaaylı bilgi için [buraya](https://pureinfotech.com/download-windows-10-iso-without-media-creation-tool/) tıklayabilirsin.

## Kısayollar

Windowsun bize sunduğu nu kısayollar tüm ekranlara baskındır, her yerde çalışır.

> Kısayollarını kendin düzenlemek istersen [AutoHotkey](https://www.autohotkey.com) adlı uygulamayı kullanabilirsin.

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

### Gezimti

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

## Command Promp (CMD)

Terminalde dosya isimlerinin **sonu veya başı sayı içerirse** çeşitli sorunlara neden olmakta.

### Cmder Komut İstemi Alternatifi

[Cmder](https://cmder.net/) windows cmd alternatifi olan bir yazılımdır.

- Linux komutlarını destekler
- Tab ile tamamlama imkanı sunar

#### CmDer Yapılandırma Ayarları

- `WİNDOWS TUŞU (SUPER)` + `ALT` + `P` ile ayarları açın
- `General`kısmından `{cmd::Cmder as Admin}`'i seçin
- Color scheme: `Tomorrow Night`
- `Font` kısmından `Size` 14 `Font Charset` Turkish
- `Size % Pos` kısmında w: 93 h:27

### CMD Komutları

Tabloda `< >` arasına yazılanlar sizin tarafınızdan girilecek değerlerdir.

| Komut                                    | Açıklama                          |
| ---------------------------------------- | --------------------------------- |
| `cls`                                    | Konsolu temizleme                 |
| `cd <yol>`                               | Dizin değiştirme                  |
| `mkdir <dizin_adı>`                      | Klasör oluşturma                  |
| `start <dosya | dizin>`                  | Dosya veya dizin açma             |
| `start "" <dosya | dizin>`               | Dosya veya dizini başlıksız açma  |
| `ren <eski_isim> <yeni_isim>`            | Dosyayı yeniden adlandırma        |
| `move <dosya> <konum>`                   | Dosyayı belirli konuma taşıma     |
| `del <bayrak> <file>`                    | Dosya silme                       |
| `rd <switch> <folder>`                   | Dizin silme                       |
| `set <ortam_değişkeni>`                  | Ortam değişkeni tanımlama         |
| `<komut> > <dosya_ismi>.<uzantı>`        | Komutun çıktılarını dosyaya yazma |
| `echo >> <dosya>`                        | Dosyaya yazma                     |
| `%<değişken>:<çıkartılacak_karakterler>` | Değişkender karakter çıkartma     |

- `<bayrak>` **/?** yazdığınızda çıkan /'li karakterler.
- `<değişken>` HOMEDRIVE, HOMVEPATH veya kullanıcı ortam değişkenleri
- `<çıkartılacak_karakterler>` Herhangi bir metin, harf veya sayı

> Komut kullanımlarını öğrenmek için cmd üzerinden `<komut> /?` yazabilirsin.

#### CMD Ek Komutlar

- `powershell.exe Expand-Archive "<zip_dosyası>" "<çıkarılacağı_yer>"`  Sıkıştırılmış dosyayı çıkarma
- `for /f %i in ('dir /a:d /s /b A*') do echo rd /s /q %i` döngü ile dosya silme
- `if not %IDS:1=%==%IDS% /I GOTO LIGHSHOT` komutu koşullu olarak`: LIGHTSHOT` alanına gider

### CMD Değişkenleri

Ayrıntılı bilgi için [buraya](https://ss64.com/nt/syntax-variables.html) tıklayabilirsin.

#### Temel Kullanım

```cmd
<command> %<env_var>%
```

> Enviroment Variables yönetimi için `Bilgisayarım` - `Sağ Tık` - `Özellikleri` - `Gelişmiş Sistem Seçenenekleri` - `Ortam Değişkenleri`

#### Sık Kullanılanlar

| Şablon          | Açıklama                                   |
| --------------- | ------------------------------------------ |
| `.`             | Bulunan dizin (working directory)          |
| `..`            | Bir üst dizin (parent directory)           |
| `*`             | Tüm dosyalar                               |
| `**`            | Tüm dosya ve dizinler                      |
| `*.js`          | Uzantısı js olan tüm dosyalar              |
| `*lib/**/*.js`  | Lib içindeki uzantısı js olan tüm dosyalar |
| `%username%`    | Kullanıcı adı                              |
| `%appdata%`     | Uygulama verileri dizini                   |
| `%HOMEDRIVE%`   | Kullanıcı diski                            |
| `%homepath%`    | Kullanıcı Yolu                             |
| `%userprofile%` | Kullanıcı diskiyle yolu                    |

### CMD Operatörleri

| Şablon                 | Açıklama                                                   |
| ---------------------- | ---------------------------------------------------------- |
| `<komut1> & <komut2>`  | Komut1 ve komut2 işlemini çalıştırır                       |
| `<komut1> && <komut2>` | Komut1 işlemini yaptıktan sonra komut2 işlemini çalıştırır |
| `|`                    | Pipe                                                       |

### CMD Kod Parçaları

#### CMD Döngü Kullanımı

```cmd
for /f %i in ('dir /b object_detection\protos\*.proto') do protoc object_detection\protos\%i --python_out=.
```

#### CMD Dosyaları Ardışık olarak adlandırma

```cmd
@echo off
setlocal EnableDelayedExpansion
set i=0
for %%a in (<dosya_belirteci>) do (
    set /a i+=1
    ren "%%a" "!i!.new"
)
ren *.new *.<yeni_dosya_uzantısı>
```

- `<dosya_belirteci>` Adlandırılacak dosyaların isim yapısı:
  - `*` Her dosyası adlandırır
  - `download*` 'download' ile başlayan her dosyayı adlandırır
  - `*.png` 'png' ile biten her dosyayı
- `<yeni_dosya_uzantısı>` Çıktıların uzantısı
  - `jpg`, `png`, `txt` vs ...

## Windows için Paket Yöneticisi

Windows için popüler olan **Chocolatey** paket yöneticisi, powershell üzerinden `choco install <paket>` komutuyla yükleme yapmanızı sağlar.

- Resmi sitesine [buraya](https://chocolatey.org/) tıklayarak erişebilirsin.
- Başlangıç videosu için [buraya](https://www.youtube.com/watch?v=hfgZYpo5moA) bakabilirsin
- Yükleyebileceğin paketler için [buraya](https://chocolatey.org/packages) bakabilirsin

### Hızlı Komut Bilgisi

| Komut                                                | Açıklama                              |
| ---------------------------------------------------- | ------------------------------------- |
| `choco list -lo`                                     | Yüklü yerel uygulamaları gösterir     |
| `choco install -y <paket>`                           | Paketi sessiz yükleme                 |
| `choco uninstall <paket>`                            | Paket kaldırma                        |
| `choco install -y <paket> --params "<parametreler>"` | Paketi belirli ayarlarla sessiz kurma |

### Sık Kullanılan Paketler

```sh
choco install -y googlechrome winrar # Genel kullanım için
choco install -y vscode git minicoda3 # Programlama için
```

## PowerShell Kullanımı

İlgili dökümana [buraya](Windows10%20Kaynaklar%C4%B1\Windows%20PowerShell%20Tutorial%20for%20Beginners.pdf) tıklayarak erişebilirsin.

## Özelleştirmelerim

Kendime özgü görsellik ayarlarım

> Kendime not amaçlı eklenmiştir 🙄

### CMD Düzeni

Düzenin görüntüsü için [buraya](../images/cmd.png) bakabilirsin.

- `**Font:**` *14 - Consolas*
- **Layout:** *Windows Size - w: 120 h: 30*
- **Color**
  - **Screen Text:** *R: 242 G: 242 B: 242*
  - **Screen Background** *R: 50 G: 47 B: 65*
  - **Opacity** *%89*

### Tema Düzeni

- [Arka plan resmi](../images/bg.jpg)
- [Fare Teması](https://drive.google.com/open?id=1Xs1YcQhwH4bo9SwHFQ06yMihJY8QQn15)
- [Tema Rengi](../images/theme_color.png)
  - Transparan etkisi `açık`
  - Yüzeylerde renk gösterme `aktif`
  - Uygulama modu `karanlık`

### Taskbar Düzeni

![taskbar](../images/taskbar.jpg)

### Ek Ayalarım

| Ayar                                                                                           | Açıklama                                        |
| ---------------------------------------------------------------------------------------------- | ----------------------------------------------- |
| Open With Code                                                                                 | Dosyayı vscode ile açma                         |
| Open With Code                                                                                 | Dizini vscode ile açma                          |
| [Open command prompt here](https://drive.google.com/open?id=1EEIlewepCu8xCZsiWdFa_OeBq9VfYnE_) | CMD'yi dizinde açma                             |
| `%b%`                                                                                          | Bilgiler projesini vscode'da açan özel değişken |

## Windows Özellikleri

> Aramaya alanına `Turn Windows Feature On or Off` veya `Windows Özelliklerini Aç veya Kapat` yazarak erişebilirsin.

### Varsayılan Windows Özellikleri

- `.NET Framework 4.7 Advanced Services`
  - `WCF Services`
    - `TCP Port Sharing`
- `Internet Explorer 11`
- `Media Features`
- `Microsoft Print to PDF`
- `Microsoft XPS Document Writer`
- `Print and Document Services`
  - `Internet Printing Client`
  - `Windows Fax and Scan`
- `Remote Differential Compression API Support`
- `SMB Direct`
- `Windows PowerShell 2.0`
- `Work Folders Client`

### Alt İşletim Sistemleri

Alt sistem kurulum dökümantasyonlarına üzerlerine tıklayarak erişlebilirsin.

- [Ubuntu bash](https://docs.microsoft.com/en-us/windows/wsl/install-win10)

## Uygulama Ayarları

### Video Ayarları

| Ayar    | Ulaşım                                                | Açıklama                                           | Kaynak                                                                                                           |
| ------- | ----------------------------------------------------- | -------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- |
| Altyazı | Options - Ease of Access -  Hearing / Closed captions | Yerel uygulamalardaki altyazı metnini özelleştirme | [Microsoft](https://support.microsoft.com/en-us/help/3078107/closed-captions-in-movies-tv-content-on-windows-10) |

## Terimler

- Wild Card: `..`, `.`, `*` gibi terimleri içeren kelimeye verilen isim
  - `help*`, `..\*` vs ...

## Windows 10 Ön Belleğini Temizleme

[Buraya](https://drive.google.com/open?id=1E-EDDSFxAvPM9QZAzciQ2fCaakgRwl6k) tıklayarak derlenebilir scriptimi indirip, **yönetici olarak** çalıştırman gerekmekte.

### CMD Üzerinden Önbelleği Elle Temizleme

Alttaki komut topluluğunu **yönetici olarak açtığınız cmd** üzerine yapıştırın.

```cmd
@echo off

echo "Windows Update Temizleniyor"
rd /s /q C:\Windows\SoftwareDistribution\Download
mkdir C:\Windows\SoftwareDistribution\Download

echo "Magaza Bilgileri Temizleniyor"
WSReset.exe

echo "Disk Temizleme"
cleanmgr.exe

echo "Windows Ikon ve Resim Bilgileri Siliniyor"
del /f /s /q %USERPROFILE%\AppData\Local\Microsoft\Windows\Explorer\*cache*

echo "Sistem Kurtarma Bilgilerini Temizleme"
echo "Cikan Ekranda 'Yapilandir' butonuna bastiktan sonra 'Temizle' butonuna basin"
SystemPropertiesProtection.exe

```

## Windows10 Insider Programı

Tanıtım videosu 📺 için [buraya](https://www.youtube.com/watch?v=wH_lKkzHHR0) bakabilirsin.

- Windows'a gelecek olan güncellemeleri erkenden deneyen kullanıcı programıdır
- `Ayarlar` > `Güncelleme ve Güvenlik` > `Windows Insider Program` ile beta kullanıcısı olabilirsiniz

### Insider Kısayolları

- `WİNDOWS TUŞU (SUPER)` + `SHIFT` + `V` Ekranda belli bir alanı panoya kaydetme
  - Lightshot gibi

### Arka Plandaki Evolution Copy Logosunu Kaldırma

Logoyu kaldırmak için harici uygulamayı [buraya](https://drive.google.com/open?id=1LkKdUCG1XKO3mrXwNV-OK50Y8vGvLRpt) tıklayrak indirmeniz ve çalıştırmanız gerekmekte.

> Basit bit kurulumdan sonra **PC yeninden başlatılır** ve logo kalkar.

## Harici Linkler

- [How to rename image files in a folder all to .jpg format](https://answers.microsoft.com/en-us/windows/forum/windows_10-files/how-to-rename-image-files-in-a-folder-all-to-jpg/2a7e2873-e04b-472b-b239-afad2f2020fc)
- [Move Komutu](https://www.windows-commandline.com/move-files-directories/)
- [How to copy a list of file names to text file?](https://superuser.com/questions/395836/how-to-copy-a-list-of-file-names-to-text-file)
- [Windows 10 Cache Temizleme](https://www.itechtics.com/clear-types-windows-10-cache/)