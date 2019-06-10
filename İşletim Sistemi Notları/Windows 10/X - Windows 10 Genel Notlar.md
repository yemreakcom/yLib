# Windows 10 Genel Notlar <!-- omit in toc -->

## İçerikler <!-- omit in toc -->

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
