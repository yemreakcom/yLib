# 1 - Linux Giriş <!-- omit in toc -->

## İçerikler <!-- omit in toc -->

- [Linux Nedir](#Linux-Nedir)
- [Birkaç Öneri Distro](#Birka%C3%A7-%C3%96neri-Distro)
- [Linux Kurulumu](#Linux-Kurulumu)
- [Linux Genel Kullanım Notları](#Linux-Genel-Kullan%C4%B1m-Notlar%C4%B1)
  - [Linux Temel Dosyaları](#Linux-Temel-Dosyalar%C4%B1)
  - [Linux Yapılandırma Ayarları](#Linux-Yap%C4%B1land%C4%B1rma-Ayarlar%C4%B1)
- [Linux Kısayolları](#Linux-K%C4%B1sayollar%C4%B1)
  - [Özel karakter Oluşturma (Compose Key)](#%C3%96zel-karakter-Olu%C5%9Fturma-Compose-Key)
  - [Pencere Kısayolları](#Pencere-K%C4%B1sayollar%C4%B1)
  - [Uygulama Kısayolları](#Uygulama-K%C4%B1sayollar%C4%B1)
  - [Panel Kısayolları](#Panel-K%C4%B1sayollar%C4%B1)
  - [Ubuntu için Ekran Görüntüsü ve Kaydı Kısayolları](#Ubuntu-i%C3%A7in-Ekran-G%C3%B6r%C3%BCnt%C3%BCs%C3%BC-ve-Kayd%C4%B1-K%C4%B1sayollar%C4%B1)
    - [Yapılandırma Ayalarını Dosyaya Aktarma](#Yap%C4%B1land%C4%B1rma-Ayalar%C4%B1n%C4%B1-Dosyaya-Aktarma)
    - [Yapılandırma Ayarlarını Dosyadan Alma](#Yap%C4%B1land%C4%B1rma-Ayarlar%C4%B1n%C4%B1-Dosyadan-Alma)
- [Faydalı Uygulamalar](#Faydal%C4%B1-Uygulamalar)
  - [Temel Araçların Kurulumu (Flameshot, Font, Gnome Tweaaks, Unrar)](#Temel-Ara%C3%A7lar%C4%B1n-Kurulumu-Flameshot-Font-Gnome-Tweaaks-Unrar)
    - [Flameshot Hakkında Notlar](#Flameshot-Hakk%C4%B1nda-Notlar)
  - [Sistem Bakım Aracı Kurulumu (Stacer)](#Sistem-Bak%C4%B1m-Arac%C4%B1-Kurulumu-Stacer)
    - [Paket Yöneticisi Üzerinden Stacer Kurulumu](#Paket-Y%C3%B6neticisi-%C3%9Czerinden-Stacer-Kurulumu)
  - [Tarayıcı Kurulumu (Chrome)](#Taray%C4%B1c%C4%B1-Kurulumu-Chrome)
    - [Chrome Gnome Eklentisi](#Chrome-Gnome-Eklentisi)
- [Gnome Eklentileri](#Gnome-Eklentileri)
  - [Ubuntu Üstteki Çubuğu Gizleme](#Ubuntu-%C3%9Cstteki-%C3%87ubu%C4%9Fu-Gizleme)
  - [Dash to Dock ile MacOS Durum Çubuğu Görünümü](#Dash-to-Dock-ile-MacOS-Durum-%C3%87ubu%C4%9Fu-G%C3%B6r%C3%BCn%C3%BCm%C3%BC)
  - [Dast to Panel](#Dast-to-Panel)
  - [Emoji Selector (Emoji Klavyesi)](#Emoji-Selector-Emoji-Klavyesi)
  - [Clipboard Indicator](#Clipboard-Indicator)
  - [EasyScreenCast](#EasyScreenCast)
  - [GS Connect](#GS-Connect)

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

## Linux Kurulumu

- Yukarıdaki distrolardan birini indirin
- [Rüfus](https://github.com/pbatard/rufus/releases/download/v3.5/rufus-3.5.exe) programını indirin (linux için etcher)
- En az 8Gb olan bir usb belleği takıp, rüfus programını çalıştırın
- Sırasıyla disk imajını, GPT / UEFI ayarını seçin, DD image ile başlatın

## Linux Genel Kullanım Notları

- Dosya gezgini `nautilus` içerisin <kbd>✲ Ctrl</kbd> + <kbd>H</kbd> yapıldığında gizli dosyaları gösterir / gizler
- <kbd>✲ Ctrl</kbd> + <kbd>⎇ Alt</kbd> + <kbd>T</kbd> terminali açar

### Linux Temel Dosyaları

| Yol                        | Açıklama              |
| -------------------------- | --------------------- |
| `~/.bashrc`                | Terminal ayaları      |
| `~/.config/user-dirs.dirs` | Temel dosya dizinleri |

### Linux Yapılandırma Ayarları

İşletim sistemi üzerinde yapmış olduğunuz değişikliklerin hepsi `dconf` komutu tarafından kontrol edilir.

## Linux Kısayolları

### Özel karakter Oluşturma (Compose Key)

Öncelikle aktif edilmesi lazımdır:

- Tweak (`sudo apt install gnome-tweaks`)
- Keyboard & Mouse
- Compose Key

Şimdilik [buradan](https://fsymbols.com/keyboard/linux/compose/) bakabilirsin

### Pencere Kısayolları

<!-- ↑←↓→ -->

| Kısayol                                                                   | Açıklama                          |
| ------------------------------------------------------------------------- | --------------------------------- |
| <kbd>✲ Ctrl</kbd> + <kbd>⎇ Alt</kbd> + <kbd>↑↓</kbd>                      | Çalışma alanları arasında geçiş   |
| <kbd>✲ Ctrl</kbd> + <kbd>⎇ Alt</kbd> + <kbd>⇧ Shift</kbd> + <kbd>↑↓</kbd> | Uygulamayı çalışma alanına taşıma |

### Uygulama Kısayolları

| Kısayol                             | Açıklama                                     |
| ----------------------------------- | -------------------------------------------- |
| <kbd>⎇ Alt</kbd> + <kbd>F2</kbd>    | Komut girme alanı                            |
| <kbd>⎇ Alt</kbd> + <kbd>⭾ Tab</kbd> | Farklı uygulama türleri arasında hızlı geçiş |
| <kbd>⎇ Alt</kbd>+ <kbd>"</kbd>      | Aynı uygulama türleri arasında hızlı geçiş   |
| <kbd>⎇ Alt</kbd>+ <kbd>ESC</kbd>    | Son uygulamaya hızlı geçiş                   |

- <kbd>⭾ Tab</kbd>, <kbd>CAPS LOCK</kbd> tuşu üstündeki iki yönlü oku ifade eder.
- <kbd>"</kbd>, <kbd>⭾ Tab</kbd> üstündeki tuşu temsil eder.

### Panel Kısayolları

| Kısayol                                                     | Açıklama                |
| ----------------------------------------------------------- | ----------------------- |
| <kbd>SUPER</kbd> + <kbd>`<sayı>`</kbd>                      | Uygulamarı çalıştırma   |
| <kbd>SUPER</kbd> + <kbd>⇧ Shift</kbd> + <kbd>`<sayı>`</kbd> | Uygulamayı yeniden açma |
| <kbd>SUPER</kbd> + <kbd>✲ Ctrl</kbd> + <kbd>`<sayı>`</kbd>  | Uygulamayı yeniden açma |

- <kbd>`<sayı>`</kbd> Sayı tuşları

### Ubuntu için Ekran Görüntüsü ve Kaydı Kısayolları

Orjinal sayfayı görmek istiyorsan [buraya](https://help.ubuntu.com/stable/ubuntu-help/screen-shot-record.html) tıklayabilirsin.

| Kısayol                                                                  | Açıklama                                          |
| ------------------------------------------------------------------------ | ------------------------------------------------- |
| <kbd>PRINT SCREEN</kbd>                                                  | Ekran görüntüsü alma                              |
| <kbd>⎇ Alt</kbd> + <kbd>PRINT SCREEN</kbd>                               | Üzerinde bulunduğumuz pencerenin görüntüsünü alma |
| <kbd>⇧ Shift</kbd>+ <kbd>PRINT SCREN</kbd>                               | Seçilecek alnın görüntüsünü alma                  |
| <kbd>✲ Ctrl</kbd> + <kbd>⎇ Alt</kbd> + <kbd>⇧ Shift</kbd> + <kbd>R</kbd> | Ekranı komple kayıt eder                          |

- <kbd>✲ Ctrl</kbd> tuşuna da basılırsa `$HOME/Pictures` ya da `HOME/Videos` dizinleri yerine panoya kayıt edilir.

> Ekran görüntüsü olarak [flameshot][flameshot], ekran kayıt edicisi olarak [simplescreenrecorder][simplescreenrecorder] uygulamları önerilir.

#### Yapılandırma Ayalarını Dosyaya Aktarma

Yapılandırma ayarlarını `dconf dump <dizin> > <dosya_ismi>` komutu ile dosyaya aktarabilrisiniz

- `<dizin>` Hangi dizinden itibaren yapılandırma verileri yedeklensin
  - `/` olursa tüm yapılandırma ayarlarını dahil eder
- `<dosya_ismi>` Ayarların yazılacağı dosya ismi
  - `dconf-settings.ini` yaparsanız, `dconf-settings.ini` isimli dosya oluşturup içine ayarları yazacaktır

#### Yapılandırma Ayarlarını Dosyadan Alma

Yapılandırma ayarlarını `dconf load <dizin> < <dosya_ismi>` komutu ile dosyaya aktarabilrisiniz

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
| gpick 🌟               | Renk seçme uygulaması (<kbd>SPACE</kbd> ile seçilir) |
| simplescreenrecorder   | Sade ekran kaydedicisi                               |
| zenkit                 | Proje yönetim uygulaması                             |
| wine                   | Windows uygulamalarını çalıştırma                    |
| nomachine              | Uzaktan PC bağlantısı                                |
| vlc                    | En çok sevilen video oynatıcısı                      |
| Onlyoffice             | Office alternatifi sade ve şık arayüzü olan uygulama |
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

> En iyi 19 gnome eklentisi için [buraya][best gnome extension] bakabilirsin.

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

- <kbd>✲ Ctrl</kbd> + <kbd>V</kbd> ile yapıştırarak kullanabilirsiniz
- <kbd>SUPER</kbd> + <kbd>E</kbd> Emoji klavyesini açar

### Clipboard Indicator

Pano'yu yönetme imkanı sağlar, [buradan](https://extensions.gnome.org/extension/779/clipboard-indicator/) indirebilirsin.

### EasyScreenCast

Ekranı paylaşma eklentisidir. Kurulum öncesi alttaki komutla gereksinimleri kurman gerekmektedir. Eklentiyi kurmak için [buraya](https://extensions.gnome.org/extension/690/easyscreencast/) tıklayabilirsin.

```sh
sudo apt-get install gir1.2-clutter-1.0 gir1.2-clutter-gst-3.0 gir1.2-gtkclutter-1.0
```

### GS Connect

Mobil cihaz ile bilgisayarı entegre etmeyi sağlar, [buradan][gs connect - extension] erişebilirsin.

[flameshot]: https://github.com/lupoDharkael/flameshot
[simplescreenrecorder]: https://www.maartenbaert.be/simplescreenrecorder/
[gs connect - extension]: https://extensions.gnome.org/extension/1319/gsconnect/
[best gnome extension]: https://www.ubuntupit.com/19-best-gnome-shell-extensions-ubuntu-gnome-desktop/
[best gnome applications]: https://www.maketecheasier.com/best-gnome-applications/
[best desktop environment]: https://www.ubuntupit.com/best-linux-desktop-environment-reviewed-and-compared/
