# Linux <!-- omit in toc -->

Birkaç distro örneği:

| Distro                            | İyi Yanı                                 | Kötü Yanı                           |
| --------------------------------- | ---------------------------------------- | ----------------------------------- |
| [ubuntu](https://www.ubuntu.com/) | Çok fazla kaynak ve bilgi desteği vardır | Arayüz tasarımı hususunda geridedir |
| [deepin](https://www.deepin.org/) | Çok şık bir arayüz tasarımına sahiptir   | Donanım ve bilgi desteği zayıftır   |

> Tüm distrolara [buradaki](https://distrowatch.com/) siteden bakabilirsin.

## İçerikler <!-- omit in toc -->

> `Home` tuşu ile yukarı yönelebilirsin.

- [Linux Kullanım Notları](#linux-kullan%C4%B1m-notlar%C4%B1)
- [Linux Terminali Notları](#linux-terminali-notlar%C4%B1)
  - [Terminal Numaları](#terminal-numalar%C4%B1)
  - [Temel Terminal Komutları](#temel-terminal-komutlar%C4%B1)
  - [Kurulum Komutları](#kurulum-komutlar%C4%B1)
    - [Dpkg - Debian Paket Kurma](#dpkg---debian-paket-kurma)
    - [Tar dosyalarının kurulumları](#tar-dosyalar%C4%B1n%C4%B1n-kurulumlar%C4%B1)
    - [AppImage Uzantılı Dosyaların Kurulumu](#appimage-uzant%C4%B1l%C4%B1-dosyalar%C4%B1n-kurulumu)
    - [Run Uzantılı Dosyaların Kurulumu](#run-uzant%C4%B1l%C4%B1-dosyalar%C4%B1n-kurulumu)
  - [Kısayol oluşturma](#k%C4%B1sayol-olu%C5%9Fturma)
    - [Desktop kısayolu oluşturma](#desktop-k%C4%B1sayolu-olu%C5%9Fturma)
  - [Terminalde Yazdırma İşlemleri (Echo)](#terminalde-yazd%C4%B1rma-i%CC%87%C5%9Flemleri-echo)
    - [Değişkeni Ekrana Basma](#de%C4%9Fi%C5%9Fkeni-ekrana-basma)
    - [Komut Çıktısını Ekrana Basma](#komut-%C3%A7%C4%B1kt%C4%B1s%C4%B1n%C4%B1-ekrana-basma)
    - [Çıktıları Gizleme](#%C3%A7%C4%B1kt%C4%B1lar%C4%B1-gizleme)
    - [Ekran Yerine Dosyaya Basma](#ekran-yerine-dosyaya-basma)
  - [Terminalde For Döngüsü (For Loop)](#terminalde-for-d%C3%B6ng%C3%BCs%C3%BC-for-loop)
    - [Her Dizine For Döngüsü](#her-dizine-for-d%C3%B6ng%C3%BCs%C3%BC)
      - [Alt Dizinler Dahil Değil](#alt-dizinler-dahil-de%C4%9Fil)
      - [Alt Dizinler Dahil](#alt-dizinler-dahil)
  - [Donanım Komutları](#donan%C4%B1m-komutlar%C4%B1)
- [Linux Kısayolları](#linux-k%C4%B1sayollar%C4%B1)
  - [Uygulama Kısayolları](#uygulama-k%C4%B1sayollar%C4%B1)
  - [Panel Kısayolları](#panel-k%C4%B1sayollar%C4%B1)
  - [Ubuntu için Ekran Görüntüsü ve Kaydı Kısayolları](#ubuntu-i%C3%A7in-ekran-g%C3%B6r%C3%BCnt%C3%BCs%C3%BC-ve-kayd%C4%B1-k%C4%B1sayollar%C4%B1)
- [Linux Değişkenleri](#linux-de%C4%9Fi%C5%9Fkenleri)
  - [Temel Değişkenler](#temel-de%C4%9Fi%C5%9Fkenler)
  - [Komut Çıktısını Ele Alma](#komut-%C3%A7%C4%B1kt%C4%B1s%C4%B1n%C4%B1-ele-alma)
- [Linux Temel Dosyaları](#linux-temel-dosyalar%C4%B1)
- [Faydalı Uygulamalar](#faydal%C4%B1-uygulamalar)
  - [Temel Araçların Kurulumu (Flameshot, Font, Gnome Tweaaks, Unrar)](#temel-ara%C3%A7lar%C4%B1n-kurulumu-flameshot-font-gnome-tweaaks-unrar)
    - [Flameshot Hakkında Notlar](#flameshot-hakk%C4%B1nda-notlar)
  - [Sistem Bakım Aracı Kurulumu (Stacer)](#sistem-bak%C4%B1m-arac%C4%B1-kurulumu-stacer)
    - [Paket Yöneticisi Üzerinden Stacer Kurulumu](#paket-y%C3%B6neticisi-%C3%BCzerinden-stacer-kurulumu)
  - [Tarayıcı Kurulumu (Chrome)](#taray%C4%B1c%C4%B1-kurulumu-chrome)
    - [Chrome Gnome Eklentisi](#chrome-gnome-eklentisi)
    - [Gnome Eklentileri](#gnome-eklentileri)
      - [Ubuntu Üstteki Çubuğu Gizleme](#ubuntu-%C3%BCstteki-%C3%A7ubu%C4%9Fu-gizleme)
      - [Dash to Dock ile MacOS Durum Çubuğu Görünümü](#dash-to-dock-ile-macos-durum-%C3%A7ubu%C4%9Fu-g%C3%B6r%C3%BCn%C3%BCm%C3%BC)
      - [Dast to Panel](#dast-to-panel)
      - [Emoji Selector (Emoji Klavyesi)](#emoji-selector-emoji-klavyesi)
  - [Gedit Eklentileri](#gedit-eklentileri)
    - [Çoklu İmleç Desteği (Multi Cursor)](#%C3%A7oklu-i%CC%87mle%C3%A7-deste%C4%9Fi-multi-cursor)
  - [Yazılım Araçları Kurulumu (VsCode ve Git)](#yaz%C4%B1l%C4%B1m-ara%C3%A7lar%C4%B1-kurulumu-vscode-ve-git)
  - [Miniconda3 Kurulumu](#miniconda3-kurulumu)
  - [Nodejs Kurulumu](#nodejs-kurulumu)
  - [Xampp Kurulumu](#xampp-kurulumu)
  - [Postgresql Kurulumu](#postgresql-kurulumu)
    - [Postgresql JDBC Driver Kurulumu](#postgresql-jdbc-driver-kurulumu)
  - [Wine Kurulumu](#wine-kurulumu)
  - [Terminal Üzerinden Markdown to PDF](#terminal-%C3%BCzerinden-markdown-to-pdf)
  - [Terminal Üzerinden Çevirici](#terminal-%C3%BCzerinden-%C3%A7evirici)
  - [Video Düzenleyici Kurulumu (Open Shot)](#video-d%C3%BCzenleyici-kurulumu-open-shot)
  - [Indirme Yöneticisi Kurulumu (Uget)](#indirme-y%C3%B6neticisi-kurulumu-uget)
  - [ADB & Fastboot (Android Tools) Kurulumu](#adb--fastboot-android-tools-kurulumu)
  - [League of Legends](#league-of-legends)
- [Faydalı Gelişmiş Bilgiler](#faydal%C4%B1-geli%C5%9Fmi%C5%9F-bilgiler)
  - [Window Manager Controls](#window-manager-controls)
  - [Uygulamaların Terminal Komutlarını öğrenme](#uygulamalar%C4%B1n-terminal-komutlar%C4%B1n%C4%B1-%C3%B6%C4%9Frenme)
  - [Grub Menüyü Atlama](#grub-men%C3%BCy%C3%BC-atlama)
  - [Kernel Güncelleme](#kernel-g%C3%BCncelleme)
  - [Bashrc Dosyası Yedeği](#bashrc-dosyas%C4%B1-yede%C4%9Fi)
- [Process İşlemleri](#process-i%CC%87%C5%9Flemleri)
  - [Process Id (PID) Bulma](#process-id-pid-bulma)

## Linux Kullanım Notları

- Dosya gezgini `nautilus` içerisin <kbd>CTRL</kbd> + <kbd>H</kbd> yapıldığında gizli dosyaları gösterir / gizler
- <kbd>CTRL</kbd> + <kbd>ALT</kbd> + <kbd>T</kbd> terminali açar

## Linux Terminali Notları

Linux işletim sistemindeki komutlardır. Terminal üzerinden kernel'a bildirilir.

### Terminal Numaları

Çok sık kullanılan ve faydalı olacak olan bir kaç terminal yöntemleri:

- Tüm terminal ön işlemleri `~/.bashrc` dosyasındadır.
- `alias` ile kendinize özgü komutlar oluşturabilirsiniz
  - sudo ile kullanılması için `alias sudo='sudo '` satırını `.bashrc` dosyanıza eklemeniz gerekmektedir
  - `echo "alias sudo='sudo '" >> ~/.bashrc`
  - Kaynak için [buraya](https://askubuntu.com/a/22043/898692) bakabilirsin
- `grep` komutu ile dosya araması yapabilirsiniz.
  - Kaynak için [buraya](https://stackoverflow.com/a/16957078/9770490) bakabilirsin.

| Yöntem                                            | Açıklama                                               |
| ------------------------------------------------- | ------------------------------------------------------ |
| `<komut> --help`                                  | Komutlar için yardım metni                             |
| <kbd>TAB</kbd>                                    | Kod tamamlama                                          |
| `cwd`                                             | Çalışma dizini yolu                                    |
| `-`                                               | Son çalışan dizine gitme                               |
| `~`                                               | Home dizini                                            |
| `<komut>; <komut>;`                               | Birden fazla komut işleme (birbirlerini beklemez)      |
| `<komut> && <komut>`                              | 1. komut çalışırsa 2.'yi işleme                        |
| `<komut> || <komut>`                              | 1. olmazsa 2. komutu işleme                            |
| `<komut> | <komut>`                               | İlk komutun sonucunu 2'ye aktarma (pipeline)           |
| <kbd>CTRL</kbd> + <kbd>W</kbd>                    | Kelime silme                                           |
| <kbd>CTRL</kbd> + <kbd>R</kbd> `<aranan_terim>`   | Önceki komutlarda arama yapma                          |
| <kbd>CTRL</kbd> + <kbd>Q</kbd>                    | Kitlenmiş terminali kurtarma                           |
| <kbd>CTRL</kbd> + <kbd>A</kbd>                    | Komutların satırının başına gelme                      |
| <kbd>CTRL</kbd> +<kbd>E</kbd>                     | Komut satırının sonuna gelme                           |
| `tail -f <dosya>`                                 | Dosyayı anlık olarak okuma                             |
| `cat` ve `less`                                   | Ufak ve büyük dosyaları okuma                          |
| `!$`                                              | Bir önce kullanılan değişkeni kullanma                 |
| `!!`                                              | Bir önceki komutu kullanma                             |
| `alias`                                           | Komut yönlendirme, yeni komut oluşturma                |
| <kbd>CTRL</kbd> + <kbd>ALT</kbd> + <kbd>E</kbd>   | Oluşturulan komutların (alias) karşılıklarını gösterme |
| <kbd>CTRL</kbd> + <kbd>SHIFT</kbd> + <kbd>C</kbd> | Kopyalama işlemi                                       |
| <kbd>CTRL</kbd> + <kbd>SHIFT</kbd> + <kbd>V</kbd> | Yapıştırma işlemi                                      |
| `yes | <komut_ya_da_script>`                      | İnteraktif veri isteyen işleme 'yes' verisi gönderme   |
| `grep <aranan_kelime>`                            | Kelime arama                                           |
| `<komut> | grep <aranan_kelime>`                  | Komut sonucunda kelime arama                           |


### Temel Terminal Komutları

Detalar için [buraya](https://gist.github.com/sayz/1130312/a45b548b82ee459e05a9159ec532224757a2ca56) tıklayarak, açıklamalara ulaşabilirsin.

- `clear` Terminali temizleme
- `sudo -s` Terminali root yapma `exit` rootlu terminali kapatma
- `sudo apt-get install <paket_adi>` Paket kurulumu
- `sudo apt-get install --fix-broken` Hatalı kurulumları veya gerekli bağımlılıkları kurma
- `sudo apt-get purge <paket_adi>` paketadi paketini kaldirma
- `sudo apt-get purge <paket_adi>*` Bulunan dizinde paket ile başlayan tüm paketleri kaldırma
- `sudo apt-get purge '<paket_adi>*'` paket ile başlayan tüm paketleri ve alt bileşenlerini kaldırma
- `sudo apt-cache search <paket_adi>` Depoda paketadi arama işlemi

### Kurulum Komutları

İndirdiğimiz dosyaları kurmak için gerkeli olan bir dize komutlar.

#### Dpkg - Debian Paket Kurma

- `sudo dpkq -i deb_uzantılı.deb`
- `sudo apt-get install --fix-broken` (kurulum için gerekli paketleri kurma)
- `sudo apt-get autoremove` (gereksizleri kaldırma)

#### Tar dosyalarının kurulumları

Tar.gz uzantılı dosyayı bulup, sağ tıklayıp, buraya çıkar diyoruz. Ya da terminal yardımıyla arşivi çıkarın

```bash
tar xzf dosya.tar.gz -C ./dizin
cd dizin
```

> Terminat komutlarını kullandıysanız, direk alttaki komutları uygulayabilirisiniz.

Ardından çıkarılan dosyaların olduğu dizine girip, alttaki komutları yazıyoruz.

```sh
./configure
make -j $(nproc --all)
sudo make install
```

#### AppImage Uzantılı Dosyaların Kurulumu

AppImage özelliği uygulamaları kurmadan çalıştırabilmemizi sağlar.

```sh
chmod a+x <appimage_dosyası>
./<appimage_dosyası>
```

#### Run Uzantılı Dosyaların Kurulumu

Run dosyaları kurulum dosyalarıdır bu sebeple yetkileri olmadan çalıştırılamaz.

```sh
chmod 0755 <run_dosyası>
./<run_dosyası>
```

### Kısayol oluşturma

Detaylar için [buraya](https://manpages.debian.org/stretch/coreutils/ln.1.en.html) tıklayabilirsin.

```bash
sudo ln -s /dosya/yolu/ dosyaAdi
```

- `ln` İki dosya arasında link oluşturma
- `-s` Statik link yerine sembolik link oluşturma
- `/dosya/yolu` Örneğin /home/$USER
- `dosyaAdi` Oluşturulacak kısayolun ismi

#### Desktop kısayolu oluşturma

Text editörü açıp

```bash
gedit dosya/yolu.desktop
```

Alttaki alanda gerekli yerleri doldurun.

```txt
#!/usr/bin/env xdg-open

[Desktop Entry]
Version=1.0
Type=Application
Terminal=false
Exec=command to run here
Name=visible name here
Comment=comment here
Icon=icon path here
```

Son olarak dosyanın bulunduğu dizinde terminali açıp, dosyayı güvenilir olarak işaretleyin (?)

```bash
chmod +x dosyadi.desktop
```

### Terminalde Yazdırma İşlemleri (Echo)

#### Değişkeni Ekrana Basma

```sh
echo $PYTHONPATH
```

#### Komut Çıktısını Ekrana Basma

```sh
echo $(pwd)
```

#### Çıktıları Gizleme

```sh
@Echo off
```

#### Ekran Yerine Dosyaya Basma

| Komut                            | Açıklama                                                      |
| -------------------------------- | ------------------------------------------------------------- |
| `echo "<metin>" > <dosya_yolu>`  | Verilen metni dosyanın üzerine yazma, yoksa dosyayı oluşturma |
| `echo "<metin>" >> <dosya_yolu>` | Verilen metni dosyaya ekleme                                  |

### Terminalde For Döngüsü (For Loop)

```sh
for f in *; do
    echo "-> $f"
done
```

#### Her Dizine For Döngüsü

##### Alt Dizinler Dahil Değil

```sh
for D in *; do
    if [ -d "${D}" ]; then
        echo "${D}"   # your processing here
    fi
done
```

```sh
for D in *; do [ -d "${D}" ] && my_command; done
```

```sh
for D in */; do my_command; done
```

##### Alt Dizinler Dahil

```sh
for D in `find . -type d`
do
    //Do whatever you need with D
done
```

### Donanım Komutları

- `nproc` İşlemci çekirdek sayısını gösterir.
- `uname -v` Kernel sürümünü gösterir
- `lspci` Donanum bilgilerini gösterir

## Linux Kısayolları

### Uygulama Kısayolları

| Kısayol                         | Açıklama                                     |
| ------------------------------- | -------------------------------------------- |
| <kbd>ALT</kbd> + <kbd>TAB</kbd> | Farklı uygulama türleri arasında hızlı geçiş |
| <kbd>ALT</kbd>+ <kbd>"</kbd>    | Aynı uygulama türleri arasında hızlı geçiş   |
| <kbd>ALT</kbd>+ <kbd>ESC</kbd>  | Son uygulamaya hızlı geçiş                   |

- <kbd>TAB</kbd>, <kbd>CAPS LOCK</kbd> tuşu üstündeki iki yönlü oku ifade eder.
- <kbd>"</kbd>, <kbd>TAB</kbd> üstündeki tuşu temsil eder.

### Panel Kısayolları

| Kısayol                                                   | Açıklama                |
| --------------------------------------------------------- | ----------------------- |
| <kbd>SUPER</kbd> + <kbd>`<sayı>`</kbd>                    | Uygulamarı çalıştırma   |
| <kbd>SUPER</kbd> + <kbd>SHIFT</kbd> + <kbd>`<sayı>`</kbd> | Uygulamayı gizleme      |
| <kbd>SUPER</kbd> + <kbd>CTRL</kbd> + <kbd>`<sayı>`</kbd>  | Uygulamayı yeniden açma |

- <kbd>`<sayı>`</kbd> Sayı tuşları

### Ubuntu için Ekran Görüntüsü ve Kaydı Kısayolları

Orjinal sayfayı görmek istiyorsan [buraya](https://help.ubuntu.com/stable/ubuntu-help/screen-shot-record.html) tıklayabilirsin.

| Kısayol                                                            | Açıklama                                          |
| ------------------------------------------------------------------ | ------------------------------------------------- |
| <kbd>PRINT SCREEN</kbd>                                            | Ekran görüntüsü alma                              |
| <kbd>ALT</kbd> + <kbd>PRINT SCREEN</kbd>                           | Üzerinde bulunduğumuz pencerenin görüntüsünü alma |
| <kbd>SHIFT</kbd>+ <kbd>PRINT SCREN</kbd>                           | Seçilecek alnın görüntüsünü alma                  |
| <kbd>CTRL</kbd> + <kbd>ALT</kbd> + <kbd>SHIFT</kbd> + <kbd>R</kbd> | Ekranı komple kayıt eder                          |

- <kbd>CTRL</kbd> tuşuna da basılırsa `$HOME/Pictures` ya da `HOME/Videos` dizinleri yerine panoya kayıt edilir.

> Ekran görüntüsü olarak [flameshot][flameshot], ekran kayıt edicisi olarak [simplescreenrecorder][simplescreenrecorder] uygulamları önerilir.

## Linux Değişkenleri

İşletim sisteminde terminal için değişkenler mevcuttur.

- `export <değişken_adı>=<değer1>:<değer2>:<$<değişken_adı2>` şeklinde yeni değişken oluşturabilirsin
  - Oluşturduğun değişken açık olan terminale özgü olacaktır

### Temel Değişkenler

- `$HOME` Kullanıcının dizini /home/user
- `$USER` Kullanıcı adı

### Komut Çıktısını Ele Alma

Alttaki şekilde bir komutun sonucunu değişken olarak alıp görebilirsin.

```bash
echo $(komut)
```

- `komut` Herhangi kullanılabilir komut (örn: nproc)
- Örnek Kullanım: `echo $(nproc)` İşlemcideki çekirdek sayısını gösterir

> Komutlar hakkında detaylı bilgi almak için [buraya](./Linux_Komutları.md) tıklayabilirsin.

## Linux Temel Dosyaları

| Yol                        | Açıklama              |
| -------------------------- | --------------------- |
| `~/.config/user-dirs.dirs` | Temel dosya dizinleri |

## Faydalı Uygulamalar

| Uygulama                | Açıklama                                             |
| ----------------------- | ---------------------------------------------------- |
| gnome-tweaks 🌟         | Gnome özelleştirme ayarları                          |
| unrar 🌟                | `.rar` uzantılı sıkıştırılmış dosyaları çıkarma      |
| flameshot 🌟            | Screenshot alma uygulaması lighthot gibi             |
| mailspring 🌟           | Mail yönetim uygulaması                              |
| vlc 🌟                  | En çok sevilen video oynatıcısı                      |
| Onlyoffice 🌟           | Office alternatifi sade ve şık arayüzü olan uygulama |
| kolourpaint 🌟          | Paint alternatifi resim düzenleyici                  |
| VsCode 🌟               | Çok fonksiyonel microsoft yapımı editör              |
| Chrome 🌟               | Google Chrome tarayıcı                               |
| Emoji Selector 👌       | Gnome eklentisi olarak indirilebilen emoji klavyesi  |
| stacer 🌟               | System Optimizer & Monitor                           |
| simplescreenrecorder 🌟 | Sade ekran kaydedicisi                               |
| zenkit 🌟               | Proje yönetim uygulaması                             |
| wine 🌟                 | Windows uygulamalarını çalıştırma                    |
| nomachine 🌟            | Uzaktan PC bağlantısı                                |
| copyq                   | Clipboard (pano) yöneticisi                          |
| gpick                   | Renk seçme uygulaması                                |
| dictd                   | Terminal üzerinden çeviri                            |
| retropie                | Atari oyunlarını içerisinde barındıran platform      |
| autocity                | Ses ile ilgili işlemleri barındıran uygulama         |
| OBS                     | Gelişmiş video kaydı hizmeti                         |
| kdenlive                | Windows media player alternatifi                     |
| Open Shot               | Video düzenleme                                      |
| uget                    | Download manager (idm alternatifi)                   |

### Temel Araçların Kurulumu (Flameshot, Font, Gnome Tweaaks, Unrar)

```sh
sudo apt install -y unrar, fonts-noto-color-emoji gnome-tweaks flameshot
```

#### Flameshot Hakkında Notlar

Kısayolları için [buraya](https://github.com/lupoDharkael/flameshot#keyboard-shortcuts) bakabilirsin.

| Komut                                       | Açıklama                                |
| ------------------------------------------- | --------------------------------------- |
| `flameshot full -p ~/Pictures/Screenshots/` | Tüm ekranın görüntüsünü path'e kaydetme |
| `flameshot gui`                             | Ekran görüntüsü alma arayüzünü açar     |
| `flameshot config`                          | Yapılandırma ayarları                   |

> Yapılandırma ayarlarından `General` sekmesi adı altında; `Show help message`'ın kapatılması, `Launch at startup`'ın açılması önerilir.

### Sistem Bakım Aracı Kurulumu (Stacer)

```sh
wget -O stacer.deb https://github.com/oguzhaninan/Stacer/releases/download/v1.0.9/stacer_1.0.9_amd64.deb
sudo dpkg -i stacer.deb
rm stacer.deb
```

#### Paket Yöneticisi Üzerinden Stacer Kurulumu

```sh
sudo add-apt-repository ppa:oguzhaninan/stacer -y
sudo apt-get update
sudo apt-get install stacer -y
```

### Tarayıcı Kurulumu (Chrome)

```sh
wget -O chrome.deb https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
sudo dpkg -i chrome.deb
rm chrome.deb
```

#### Chrome Gnome Eklentisi

Gnome özelleştirme eklentilerinin chrome üzeriinden yönetimini sağlar.

```sh
sudo apt install -y chrome-gnome-shell
google-chrome https://extensions.gnome.org/extension/1160/dash-to-panel/ https://extensions.gnome.org/extension/750/openweather/ https://extensions.gnome.org/extension/1162/emoji-selector/
```

#### Gnome Eklentileri

Gnome eklentileri ile ubuntu distronuzu özelleştirebilirsiniz.

- `sudo apt install chrome-gnome-shell` ile chrome için gnome çekirdeğini kurun
- [Chrome](https://chrome.google.com/webstore/detail/gnome-shell-integration/gphhapmejobijbbhgpjhcjognlahblep), [Firefox](https://addons.mozilla.org/en-US/firefox/addon/gnome-shell-integration/) veya [Opera](https://addons.opera.com/en/extensions/details/gnome-shell-integration/) için gnome eklentisini kurun

##### Ubuntu Üstteki Çubuğu Gizleme

Gnome eklentisini kurduktan sonra [buradan](https://extensions.gnome.org/extension/545/hide-top-bar/) eklentiyi `ON/OFF` ile açıp kapatabilirsiniz.

##### Dash to Dock ile MacOS Durum Çubuğu Görünümü

Tam ekranı kaplayan uzun görüntü yerine, içerdiği uygulama kadar yer kaplayan bir görüntü sağlar, [buradan](https://extensions.gnome.org/extension/307/dash-to-dock/) indirebilirsiniz.

- `Ubuntu Software` uygulamasını açın
- `Dash to Dock` yazıp aratın ev indirin
- `Extension Settings` kısmından özelleştirebilirsiniz

##### Dast to Panel

Windows 10 görev çubuğu izlenimi verir, [buraya](https://extensions.gnome.org/extension/1160/dash-to-panel/) tıklayarak erişebilirsiniz

##### Emoji Selector (Emoji Klavyesi)

Emoji klavyesi ile emojiyi panoya kopyalar, [buradan](https://extensions.gnome.org/extension/1162/emoji-selector/) indirebilirsiniz.

- <kbd>CTRL</kbd> + <kbd>V</kbd> ile yapıştırarak kullanabilirsiniz
- <kbd>SUPER</kbd> + <kbd>E</kbd> Emoji klavyesini açar

### Gedit Eklentileri

#### Çoklu İmleç Desteği (Multi Cursor)

```sh
sudo apt install gedit-plugin-multi-edit
```

| Kısayol                                           | AÇıklama                  |
| ------------------------------------------------- | ------------------------- |
| <kbd>CTRL</kbd> + <kbd>SHIFT</kbd> + <kbd>C</kbd> | *Mutli Edit*'i aktif etme |
| <kbd>CTRL</kbd> + <kbd>E</kbd>                    | İmleç (*cursor*) ekleme   |
| `Alan seçtikten sonra` + <kbd>ENTER</kbd>         | Sütun düzenleme           |
| <kbd>ESC</kbd>                                    | Geri çıkma karakteri      |

### Yazılım Araçları Kurulumu (VsCode ve Git)

```sh
wget -O code.deb https://az764295.vo.msecnd.net/stable/51b0b28134d51361cf996d2f0a1c698247aeabd8/code_1.33.1-1554971066_amd64.deb
sudo dpkg -i code.deb
rm code.deb

# Git Kurulumu
sudo apt install -y git
```

### Miniconda3 Kurulumu

```sh
# Uyarı notu
read -p "Çıkan ekranda özel bir ayarlama yapmayın, default değerleri tercih edin."

# Miniconda3 Kurulumu
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
bash ./Miniconda3-latest-Linux-x86_64.sh
rm Miniconda3-latest-Linux-x86_64.sh

# Miniconda3 komutlarını tanımlama
echo >> ~/.bashrc
echo "# Miniconda3 Komutları" >> ~/.bashrc
echo alias "alias conda_init='source ~/miniconda3/bin/activate'" >> ~/.bashrc
echo "Tanımlanan Miniconda3 komutları: conda_init"
```

### Nodejs Kurulumu

```sh
wget -qO- https://deb.nodesource.com/setup_11.x | sudo -E bash -
sudo apt-get install -y nodejs
```

### Xampp Kurulumu

```sh
# Bağlantı araçlarını kurma
sudo apt install net-tools

# Xammp indirme
wget https://downloadsapachefriends.global.ssl.fastly.net/7.3.4/xampp-linux-x64-7.3.4-0-installer.run?from_af=true

# Gerekli izinleri veerme ve kurma
chmod 0755 xampp-linux-x64-7.3.4-0-installer.run
sudo ./xampp-linux-x64-7.3.4-0-installer.run
rm xampp-linux-x64-7.3.4-0-installer.run

# Xammp komutlarını tanımlama
echo >> ~/.bashrc
echo "# Xampp Komutları" >> ~/.bashrc
echo alias xampp='sudo /opt/lampp/xampp' >> ~/.bashrc
echo alias mysql='sudo /opt/lampp/bin/mysql' >> ~/.bashrc
echo "Tanımlanan komutlar: xampp, mysql"
```

### Postgresql Kurulumu

```sh
sudo apt-get install postgresql
```

#### Postgresql JDBC Driver Kurulumu

```sh
sudo apt-get install libpostgresql-jdbc-java libpostgresql-jdbc-java-doc
echo "export CLASSPATH=$CLASSPATH:/usr/share/java/postgresql-42.2.5.jar" >> ~/.bashrc
```

### Wine Kurulumu

Resmi kaynak için [buraya](https://wiki.winehq.org/Ubuntu) bakabilirsin

```sh
# 32bit desteğini açma
sudo dpkg --add-architecture i386

# Güvenlik anahtarı ekleme
wget -nc https://dl.winehq.org/wine-builds/winehq.key
sudo apt-key add winehq.key
rm winehq.key

# Repoyu ekleme
sudo apt-add-repository 'deb https://dl.winehq.org/wine-builds/ubuntu/ cosmic main'
sudo apt update

# Sürüm seçimi
sudo apt install --install-recommends winehq-stable
# sudo apt install --install-recommends winehq-devel
# sudo apt install --install-recommends winehq-staging
```

### Terminal Üzerinden Markdown to PDF

Gerekli paketleri alttaki komutlarla kuruyoruz.

```sh
sudo apt-get install pandoc texlive-latex-base texlive-fonts-recommended texlive-extra-utils
```

Kullanım:

```sh
pandoc MANUAL.txt --pdf-engine=xelatex -o example13.pdf
```

### Terminal Üzerinden Çevirici

Terminal üzerinden çevrimdışı şekilde çeviri yapmak için:

```sh
sudo apt-get install dictd
sudo apt-get install dict-freedict-tur-eng
sudo apt-get install dict-freedict-eng-tur
```

Diğer dilleri kurmak için:

```sh
sudo apt-cache search "dict-freedict"
```

Kullanım şekli:

```sh
dict "word"
```

- `<metin>` Çevirilecek metin

### Video Düzenleyici Kurulumu (Open Shot)

```sh
sudo add-apt-repository ppa:openshot.developers/ppa
sudo apt update
sudo apt install openshot-qt
```

### Indirme Yöneticisi Kurulumu (Uget)

```sh
sudo add-apt-repository ppa:plushuang-tw/uget-stable
sudo apt-get update
sudo apt-get install uget
```

### ADB & Fastboot (Android Tools) Kurulumu

```sh
sudo apt-get install android-tools-adb android-tools-fastboot
adb version
```

### League of Legends

```sh
sudo snap install --edge leagueoflegends --devmode
```

## Faydalı Gelişmiş Bilgiler

### Window Manager Controls

Uygulamaların durumlarını kontrol eden `wmctrl` adlı komuttur.

- `wmctrl -xa <uygulama_komutu>` uygulama açıksa ekrana getirir.
- `wmctrl -xc <uygulama_komutu>` uygulamayı kibarca kapatma
- `wmctrl -lxG` açık olan uygulamalar hakkında bilgi basar.

### Uygulamaların Terminal Komutlarını öğrenme

Alttaki komutu yazdıktan sonra pencerenin üstüne tıklamanız yeterlidir.

```sh
xprop | grep WM_CLASS
```

### Grub Menüyü Atlama

- `sudo nano /etc/default/grub` ile grub yapılandırma dosyasını açın
- En alt kısmına `GRUB_HIDDEN_TIMEOUT=0` yazın ve `GRUB_TIMEOUT=0` yapın
- <kbd>CTRL</kbd> + <kbd>S</kbd> e basarak kaytıt edin, <kbd>CTRL</kbd> + <kbd>X</kbd> ile çıkış yapın
- `sudo update-grub` ile yine grub ayarlarını aktifleştirin

### Kernel Güncelleme

Kernel güncelleme yazım için [buraya](https://medium.com/@yyunussemree/linux-kernel-g%C3%BCncelleme-4ce3ce55de36) bakabilirsin.

### Bashrc Dosyası Yedeği

```sh
# ~/.bashrc: executed by bash(1) for non-login shells.
# see /usr/share/doc/bash/examples/startup-files (in the package bash-doc)
# for examples

# If not running interactively, don't do anything
case $- in
    *i*) ;;
      *) return;;
esac

# don't put duplicate lines or lines starting with space in the history.
# See bash(1) for more options
HISTCONTROL=ignoreboth

# append to the history file, don't overwrite it
shopt -s histappend

# for setting history length see HISTSIZE and HISTFILESIZE in bash(1)
HISTSIZE=1000
HISTFILESIZE=2000

# check the window size after each command and, if necessary,
# update the values of LINES and COLUMNS.
shopt -s checkwinsize

# If set, the pattern "**" used in a pathname expansion context will
# match all files and zero or more directories and subdirectories.
#shopt -s globstar

# make less more friendly for non-text input files, see lesspipe(1)
[ -x /usr/bin/lesspipe ] && eval "$(SHELL=/bin/sh lesspipe)"

# set variable identifying the chroot you work in (used in the prompt below)
if [ -z "${debian_chroot:-}" ] && [ -r /etc/debian_chroot ]; then
    debian_chroot=$(cat /etc/debian_chroot)
fi

# set a fancy prompt (non-color, unless we know we "want" color)
case "$TERM" in
    xterm-color|*-256color) color_prompt=yes;;
esac

# uncomment for a colored prompt, if the terminal has the capability; turned
# off by default to not distract the user: the focus in a terminal window
# should be on the output of commands, not on the prompt
#force_color_prompt=yes

if [ -n "$force_color_prompt" ]; then
    if [ -x /usr/bin/tput ] && tput setaf 1 >&/dev/null; then
    # We have color support; assume it's compliant with Ecma-48
    # (ISO/IEC-6429). (Lack of such support is extremely rare, and such
    # a case would tend to support setf rather than setaf.)
    color_prompt=yes
      else
    color_prompt=
    fi
fi

if [ "$color_prompt" = yes ]; then
    PS1='${debian_chroot:+($debian_chroot)}\[\033[01;32m\]\u@\h\[\033[00m\]:\[\033[01;34m\]\w\[\033[00m\]\$ '
else
    PS1='${debian_chroot:+($debian_chroot)}\u@\h:\w\$ '
fi
unset color_prompt force_color_prompt

# If this is an xterm set the title to user@host:dir
case "$TERM" in
xterm*|rxvt*)
    PS1="\[\e]0;${debian_chroot:+($debian_chroot)}\u@\h: \w\a\]$PS1"
    ;;
*)
    ;;
esac

# enable color support of ls and also add handy aliases
if [ -x /usr/bin/dircolors ]; then
    test -r ~/.dircolors && eval "$(dircolors -b ~/.dircolors)" || eval "$(dircolors -b)"
    alias ls='ls --color=auto'
    #alias dir='dir --color=auto'
    #alias vdir='vdir --color=auto'

    alias grep='grep --color=auto'
    alias fgrep='fgrep --color=auto'
    alias egrep='egrep --color=auto'
fi

# colored GCC warnings and errors
#export GCC_COLORS='error=01;31:warning=01;35:note=01;36:caret=01;32:locus=01:quote=01'

# some more ls aliases
alias ll='ls -alF'
alias la='ls -A'
alias l='ls -CF'

# Add an "alert" alias for long running commands.  Use like so:
#   sleep 10; alert
alias alert='notify-send --urgency=low -i "$([ $? = 0 ] && echo terminal || echo error)" "$(history|tail -n1|sed -e '\''s/^\s*[0-9]\+\s*//;s/[;&|]\s*alert$//'\'')"'

# Alias definitions.
# You may want to put all your additions into a separate file like
# ~/.bash_aliases, instead of adding them here directly.
# See /usr/share/doc/bash-doc/examples in the bash-doc package.

if [ -f ~/.bash_aliases ]; then
    . ~/.bash_aliases
fi

# enable programmable completion features (you don't need to enable
# this, if it's already enabled in /etc/bash.bashrc and /etc/profile
# sources /etc/bash.bashrc).
if ! shopt -oq posix; then
  if [ -f /usr/share/bash-completion/bash_completion ]; then
    . /usr/share/bash-completion/bash_completion
  elif [ -f /etc/bash_completion ]; then
    . /etc/bash_completion
  fi
fi

# Sudo ile yeni komutların kullanılmasını sağlar
# https://askubuntu.com/a/22043/898692
alias sudo='sudo '
```

## Process İşlemleri

| Komut   | Açıklama                 |
| ------- | ------------------------ |
| `pgrep` | PID (process id) Bulma   |
| `kill`  | PID öldürme, sonlandırma |

### Process Id (PID) Bulma

```sh
pgrep [option] <pattern>
```

<!--  Harici Bağlantılar  -->

[flameshot]: https://github.com/lupoDharkael/flameshot
[simplescreenrecorder]: https://www.maartenbaert.be/simplescreenrecorder/