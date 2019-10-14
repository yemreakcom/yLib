# 🖤 Windows 10 Komut İstem (CMD) Notları

## Command Promp (CMD)

Terminalde dosya isimlerinin **sonu veya başı sayı içerirse** çeşitli sorunlara neden olmakta.

### Tab ile Kod Tamamlama

Buradan [clink] ile daha verimli kod tamamlayı cmd için aktif edebilirsin.

### Cmder Komut İstemi Alternatifi

[Cmder](https://cmder.net/) windows cmd alternatifi olan bir yazılımdır.

- Linux komutlarını destekler
- Tab ile tamamlama imkanı sunar

#### CmDer Yapılandırma Ayarları

- <kbd>❖ Win</kbd> + <kbd>⎇ Alt</kbd> + `P` ile ayarları açın
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
| `%SystemRoot%`  | System dizini (Örn: `C:\Windows`)          |

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

## 🔗 Harici Bağlantılar

- [👜 Windows Mağazasından İndirilen Uygulamaları Komut ile Çalıştırma](./Windows%2010%20Di%C4%9Fer%20Notlar/Windows%20Ma%C4%9Fazas%C4%B1ndan%20%C4%B0ndirilen%20Uygulamalar%C4%B1%20Komut%20ile%20%C3%87al%C4%B1%C5%9Ft%C4%B1rma.md)
- [💙 PowerShell Kullanımı](Windows10%20Kaynaklar%C4%B1\Windows%20PowerShell%20Tutorial%20for%20Beginners.pdf)

[clink]: http://mridgers.github.io/clink/
