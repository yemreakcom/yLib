# Windows 10 Komut İstem (CMD) Notları <!-- omit in toc -->

## İçerikler <!-- omit in toc -->

- [Command Promp (CMD)](#command-promp-cmd)
  - [Tab ile Kod Tamamlama](#tab-ile-kod-tamamlama)
  - [Cmder Komut İstemi Alternatifi](#cmder-komut-%c4%b0stemi-alternatifi)
    - [CmDer Yapılandırma Ayarları](#cmder-yap%c4%b1land%c4%b1rma-ayarlar%c4%b1)
  - [CMD Komutları](#cmd-komutlar%c4%b1)
    - [CMD Ek Komutlar](#cmd-ek-komutlar)
  - [CMD Değişkenleri](#cmd-de%c4%9fi%c5%9fkenleri)
    - [Temel Kullanım](#temel-kullan%c4%b1m)
    - [Sık Kullanılanlar](#s%c4%b1k-kullan%c4%b1lanlar)
  - [CMD Operatörleri](#cmd-operat%c3%b6rleri)
  - [CMD Kod Parçaları](#cmd-kod-par%c3%a7alar%c4%b1)
    - [CMD Döngü Kullanımı](#cmd-d%c3%b6ng%c3%bc-kullan%c4%b1m%c4%b1)
    - [CMD Dosyaları Ardışık olarak adlandırma](#cmd-dosyalar%c4%b1-ard%c4%b1%c5%9f%c4%b1k-olarak-adland%c4%b1rma)
  - [CMD'yi Arkaplanda Çalıştırma](#cmdyi-arkaplanda-%c3%87al%c4%b1%c5%9ft%c4%b1rma)
- [Windows için Paket Yöneticisi](#windows-i%c3%a7in-paket-y%c3%b6neticisi)
  - [Hızlı Komut Bilgisi](#h%c4%b1zl%c4%b1-komut-bilgisi)
  - [Sık Kullanılan Paketler](#s%c4%b1k-kullan%c4%b1lan-paketler)
- [PowerShell Kullanımı](#powershell-kullan%c4%b1m%c4%b1)

## Command Promp (CMD)

Terminalde dosya isimlerinin **sonu veya başı sayı içerirse** çeşitli sorunlara neden olmakta.

### Tab ile Kod Tamamlama

Buradan [clink] ile daha verimli kod tamamlayı cmd için aktif edebilirsin.

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

| Komut                                    | Açıklama                                  |
| ---------------------------------------- | ----------------------------------------- |
| `cls`                                    | Konsolu temizleme                         |
| `cd <yol>`                               | Dizin değiştirme                          |
| `mkdir <dizin_adı>`                      | Klasör oluşturma                          |
| `start <dosya | dizin>`                  | Dosya veya dizin açma                     |
| `start "" <dosya | dizin | komut>`       | CMD ekranı olmadan açma                   |
| `ren <eski_isim> <yeni_isim>`            | Dosyayı yeniden adlandırma                |
| `move <dosya> <konum>`                   | Dosyayı belirli konuma taşıma             |
| `del <bayrak> <file>`                    | Dosya silme                               |
| `rd <switch> <folder>`                   | Dizin silme                               |
| `set <ortam_değişkeni>`                  | Ortam değişkeni tanımlama                 |
| `<komut> > <dosya_ismi>.<uzantı>`        | Komutun çıktılarını dosyaya yazma         |
| `echo >> <dosya>`                        | Dosyaya yazma                             |
| `%<değişken>:<çıkartılacak_karakterler>` | Değişkender karakter çıkartma             |
| `start "" "cmd /k <komut> <parametre>"`  | Cmd'yi parametleri olarak sessiz başlatma |

- `<bayrak>` **/?** yazdığınızda çıkan /'li karakterler.
- `<değişken>` HOMEDRIVE, HOMVEPATH veya kullanıcı ortam değişkenleri
- `<çıkartılacak_karakterler>` Herhangi bir metin, harf veya sayı

> Komut kullanımlarını öğrenmek için cmd üzerinden `<komut> /?` yazabilirsin.

#### CMD Ek Komutlar

- `powershell.exe Expand-Archive "<zip_dosyası>" "<çıkarılacağı_yer>"` Sıkıştırılmış dosyayı çıkarma
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

### CMD'yi Arkaplanda Çalıştırma

Alttaki visual basic script'i ile bu işlemi gerçekleştirebiliriz.

- Kodları `dosyaIsmi.vbs` adlı dosya oluşturup içine yazın
- `path\to\bat` alanına `.bat` uzantılı scriptinizin yolunu yazın
- Artık `dosyaIsmi.vbs` adlı dosyanızı çalıştırdığınızda arka planda `bat` scriptiniz çalışaktır

> Görev yöneticisinden sonlandırabilrisiniz

```vbs
Set WshShell = CreateObject("WScript.Shell")
WshShell.Run chr(34) & "path\to\bat" & Chr(34), 0
Set WshShell = Nothing
```

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

[clink]: http://mridgers.github.io/clink/
