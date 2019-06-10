# Windows 10 Komut İstemi Notları <!-- omit in toc -->

## İçerikler <!-- omit in toc -->

- [Command Promp (CMD)](#command-promp-cmd)
  - [Tab ile Kod Tamamlama](#tab-ile-kod-tamamlama)
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

[clink]: http://mridgers.github.io/clink/
