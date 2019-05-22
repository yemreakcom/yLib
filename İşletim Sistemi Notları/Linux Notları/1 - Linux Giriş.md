# 1 - Linux Giriş <!-- omit in toc -->

## İçerikler <!-- omit in toc -->

- [Linux Nedir](#linux-nedir)
- [Birkaç Öneri Distro](#birka%C3%A7-%C3%B6neri-distro)
- [Linux Genel Kullanım Notları](#linux-genel-kullan%C4%B1m-notlar%C4%B1)
  - [Linux Temel Dosyaları](#linux-temel-dosyalar%C4%B1)
  - [Linux Yapılandırma Ayarları](#linux-yap%C4%B1land%C4%B1rma-ayarlar%C4%B1)
- [Linux Kısayolları](#linux-k%C4%B1sayollar%C4%B1)
  - [Uygulama Kısayolları](#uygulama-k%C4%B1sayollar%C4%B1)
  - [Panel Kısayolları](#panel-k%C4%B1sayollar%C4%B1)
  - [Ubuntu için Ekran Görüntüsü ve Kaydı Kısayolları](#ubuntu-i%C3%A7in-ekran-g%C3%B6r%C3%BCnt%C3%BCs%C3%BC-ve-kayd%C4%B1-k%C4%B1sayollar%C4%B1)
    - [Yapılandırma Ayalarını Dosyaya Aktarma](#yap%C4%B1land%C4%B1rma-ayalar%C4%B1n%C4%B1-dosyaya-aktarma)
    - [Yapılandırma Ayarlarını Dosyadan Alma](#yap%C4%B1land%C4%B1rma-ayarlar%C4%B1n%C4%B1-dosyadan-alma)
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
  - [Clipboard Indicator](#clipboard-indicator)
  - [EasyScreenCast](#easyscreencast)
  - [GS Connect](#gs-connect)

## Linux Nedir

Açık kaynak olan **Unix** tabanlı işletim sistemidir.

- Linux işletim sistemlerinde **python** gömülü olarak gelir, temel dili **bash** veya **shell** olarak geçmektedir.
- Farklı linux dağıtımlarına **distro** denir.

## Birkaç Öneri Distro

| Distro                                     | İyi Yanı                                 | Kötü Yanı                           |
| ------------------------------------------ | ---------------------------------------- | ----------------------------------- |
| [ubuntu](https://www.ubuntu.com/)          | Çok fazla kaynak ve bilgi desteği vardır | Arayüz tasarımı hususunda geridedir |
| [deepin](https://www.deepin.org/)          | Çok şık bir arayüz tasarımına sahiptir   | Donanım ve bilgi desteği zayıftır   |
| [elementary OS](http://www.elementary.io/) | Mac OS Temalı                            |
| Manjaro                                    | Hız ve verimlilik                        | Linux bilgisi gerektirir            |

## Linux Genel Kullanım Notları

- Dosya gezgini `nautilus` içerisin <kbd>CTRL</kbd> + <kbd>H</kbd> yapıldığında gizli dosyaları gösterir / gizler
- <kbd>CTRL</kbd> + <kbd>ALT</kbd> + <kbd>T</kbd> terminali açar

### Linux Temel Dosyaları

| Yol                        | Açıklama              |
| -------------------------- | --------------------- |
| `~/.bashrc`                | Terminal ayaları      |
| `~/.config/user-dirs.dirs` | Temel dosya dizinleri |

### Linux Yapılandırma Ayarları

İşletim sistemi üzerinde yapmış olduğunuz değişikliklerin hepsi `dconf` komutu tarafından kontrol edilir.

## Linux Kısayolları

### Uygulama Kısayolları

| Kısayol                         | Açıklama                                     |
| ------------------------------- | -------------------------------------------- |
| <kbd>ALT</kbd> + <kbd>F2</kbd>  | Komut girme alanı                            |
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

#### Yapılandırma Ayalarını Dosyaya Aktarma

Yapılandırma ayarlarını `dconf dump <dizin> > <dosya_ismi>`  komutu ile dosyaya aktarabilrisiniz

- `<dizin>` Hangi dizinden itibaren yapılandırma verileri yedeklensin
  - `/` olursa tüm yapılandırma ayarlarını dahil eder
- `<dosya_ismi>` Ayarların yazılacağı dosya ismi
  - `dconf-settings.ini` yaparsanız, `dconf-settings.ini` isimli dosya oluşturup içine ayarları yazacaktır

#### Yapılandırma Ayarlarını Dosyadan Alma

Yapılandırma ayarlarını `dconf load <dizin> < <dosya_ismi>`  komutu ile dosyaya aktarabilrisiniz

- `<dizin>` Hangi dizinden itibaren yapılandırma verileri yedeklensin
  - `/` olursa tüm yapılandırma ayarlarını dahil eder
- `<dosya_ismi>` Ayarların alınacağı dosya ismi
  - `dconf-settings.ini` yaparsanız, `dconf-settings.ini` isimli dosya dosyadan ayarları okuyup sisteme kaydeder

## Faydalı Uygulamalar

| Uygulama               | Açıklama                                             |
| ---------------------- | ---------------------------------------------------- |
| gnome-tweaks 🌟        | Gnome özelleştirme ayarları                          |
| unrar 🌟               | `.rar` uzantılı sıkıştırılmış dosyaları çıkarma      |
| flameshot 🌟           | Screenshot alma uygulaması lighthot gibi             |
| Emoji Selector 👌      | Gnome eklentisi olarak indirilebilen emoji klavyesi  |
| Clipboard Indicator 📄 | Pano (kopyalama geçmişi) kontrolü                    |
| Chrome 🌟              | Google Chrome tarayıcı                               |
| mailspring 🌟          | Mail yönetim uygulaması                              |
| kolourpaint 🌟         | Paint alternatifi resim düzenleyici                  |
| VsCode 🌟              | Çok fonksiyonel microsoft yapımı editör              |
| stacer 🌟              | System Optimizer & Monitor                           |
| simplescreenrecorder   | Sade ekran kaydedicisi                               |
| zenkit                 | Proje yönetim uygulaması                             |
| wine                   | Windows uygulamalarını çalıştırma                    |
| nomachine              | Uzaktan PC bağlantısı                                |
| vlc                    | En çok sevilen video oynatıcısı                      |
| Onlyoffice             | Office alternatifi sade ve şık arayüzü olan uygulama |
| copyq                  | Clipboard (pano) yöneticisi                          |
| gpick                  | Renk seçme uygulaması                                |
| dictd                  | Terminal üzerinden çeviri                            |
| retropie               | Atari oyunlarını içerisinde barındıran platform      |
| autocity               | Ses ile ilgili işlemleri barındıran uygulama         |
| OBS                    | Gelişmiş video kaydı hizmeti                         |
| kdenlive               | Windows media player alternatifi                     |
| Open Shot              | Video düzenleme                                      |
| uget                   | Download manager (idm alternatifi)                   |

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

## Gnome Eklentileri

Gnome eklentileri ile ubuntu distronuzu özelleştirebilirsiniz.

- `sudo apt install chrome-gnome-shell` ile chrome için gnome çekirdeğini kurun
- [Chrome](https://chrome.google.com/webstore/detail/gnome-shell-integration/gphhapmejobijbbhgpjhcjognlahblep), [Firefox](https://addons.mozilla.org/en-US/firefox/addon/gnome-shell-integration/) veya [Opera](https://addons.opera.com/en/extensions/details/gnome-shell-integration/) için gnome eklentisini kurun

> En iyi 19 gnome eklentisi için [buraya][Best Gnome Extension] bakabilirsin.

### Ubuntu Üstteki Çubuğu Gizleme

Gnome eklentisini kurduktan sonra [buradan](https://extensions.gnome.org/extension/545/hide-top-bar/) eklentiyi `ON/OFF` ile açıp kapatabilirsiniz.

### Dash to Dock ile MacOS Durum Çubuğu Görünümü

Tam ekranı kaplayan uzun görüntü yerine, içerdiği uygulama kadar yer kaplayan bir görüntü sağlar, [buradan](https://extensions.gnome.org/extension/307/dash-to-dock/) indirebilirsiniz.

- `Ubuntu Software` uygulamasını açın
- `Dash to Dock` yazıp aratın ev indirin
- `Extension Settings` kısmından özelleştirebilirsiniz

### Dast to Panel

Windows 10 görev çubuğu izlenimi verir, [buraya](https://extensions.gnome.org/extension/1160/dash-to-panel/) tıklayarak erişebilirsiniz

### Emoji Selector (Emoji Klavyesi)

Emoji klavyesi ile emojiyi panoya kopyalar, [buradan](https://extensions.gnome.org/extension/1162/emoji-selector/) indirebilirsiniz.

- <kbd>CTRL</kbd> + <kbd>V</kbd> ile yapıştırarak kullanabilirsiniz
- <kbd>SUPER</kbd> + <kbd>E</kbd> Emoji klavyesini açar

### Clipboard Indicator

Pano'yu yönetme imkanı sağlar, [buradan](https://extensions.gnome.org/extension/779/clipboard-indicator/) indirebilirsin.

### EasyScreenCast

Ekranı paylaşma eklentisidir. Kurulum öncesi alttaki komutla gereksinimleri kurman gerekmektedir. Eklentiyi kurmak için [buraya](https://extensions.gnome.org/extension/690/easyscreencast/) tıklayabilirsin.

```sh
sudo apt-get install gir1.2-clutter-1.0 gir1.2-clutter-gst-3.0 gir1.2-gtkclutter-1.0
```

### GS Connect

Mobil cihaz ile bilgisayarı entegre etmeyi sağlar, [buradan][GS Connect - Extension] erişebilirsin.

[flameshot]: https://github.com/lupoDharkael/flameshot
[simplescreenrecorder]: https://www.maartenbaert.be/simplescreenrecorder/

[GS Connect - Extension]: https://extensions.gnome.org/extension/1319/gsconnect/

[Best Gnome Extension]: https://www.ubuntupit.com/19-best-gnome-shell-extensions-ubuntu-gnome-desktop/
[Best Gnome Applications]: https://www.maketecheasier.com/best-gnome-applications/
[Best Desktop Environment]: https://www.ubuntupit.com/best-linux-desktop-environment-reviewed-and-compared/