# Linux Giriş 

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

### 🐞 Linux BootMenu Gözükmeme Sorunu

- Ubuntu yükü olan USB ile ubuntuyu açın
- Alttaki komutlarla bootrepair'i kurun
- **Recommended Repair** butonuna tıklayın

```sh
sudo add-apt-repository ppa:yannubuntu/boot-repair
sudo apt-get update
sudo apt-get install -y boot-repair && boot-repair
```

> [RecoveringUbuntuAfterInstallingWindows](https://help.ubuntu.com/community/RecoveringUbuntuAfterInstallingWindows)

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
