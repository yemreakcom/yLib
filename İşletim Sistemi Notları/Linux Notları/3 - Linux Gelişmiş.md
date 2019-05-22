# Linux Gelişmiş <!-- omit in toc -->

## İçerikler <!-- omit in toc -->

- [Çalışma Alanlarını Bağımsızlaştırma (Isolate Workspace)](#%C3%A7al%C4%B1%C5%9Fma-alanlar%C4%B1n%C4%B1-ba%C4%9F%C4%B1ms%C4%B1zla%C5%9Ft%C4%B1rma-isolate-workspace)
- [Dosya İzinleri](#dosya-i%CC%87zinleri)
  - [İzin Kodu Hesaplama](#i%CC%87zin-kodu-hesaplama)
  - [Dizine ve Alt Dizinlerine Okuma ve Yazma İzni Verme](#dizine-ve-alt-dizinlerine-okuma-ve-yazma-i%CC%87zni-verme)
- [Desktop kısayolu oluşturma](#desktop-k%C4%B1sayolu-olu%C5%9Fturma)
  - [Whatsapp Kısayolu](#whatsapp-k%C4%B1sayolu)
    - [Whatsapp İkonu Ekleme](#whatsapp-i%CC%87konu-ekleme)
    - [Wmctrl ile Kısayol Oluşturma](#wmctrl-ile-k%C4%B1sayol-olu%C5%9Fturma)
- [Window Manager Controls](#window-manager-controls)
- [Uygulamaların Terminal Komutlarını öğrenme](#uygulamalar%C4%B1n-terminal-komutlar%C4%B1n%C4%B1-%C3%B6%C4%9Frenme)
- [Herhangi bir Uygulama için Kısayol Oluşturma](#herhangi-bir-uygulama-i%C3%A7in-k%C4%B1sayol-olu%C5%9Fturma)
  - [Uygulama için `WM_CLASS` metnini tanımlama](#uygulama-i%C3%A7in-wmclass-metnini-tan%C4%B1mlama)
  - [Herhangi bir uygulamanın `WM_CLASS` metnini alma](#herhangi-bir-uygulaman%C4%B1n-wmclass-metnini-alma)
  - [Kısayolu oluşturma](#k%C4%B1sayolu-olu%C5%9Fturma)
- [Grub Menüyü Atlama](#grub-men%C3%BCy%C3%BC-atlama)
- [Donanım Komutları](#donan%C4%B1m-komutlar%C4%B1)
- [Silinen Yerel Dosyaları Kurtarma](#silinen-yerel-dosyalar%C4%B1-kurtarma)
- [Process İşlemleri](#process-i%CC%87%C5%9Flemleri)
  - [Process Id (PID) Bulma](#process-id-pid-bulma)
- [Bashrc Dosyası Yedeği](#bashrc-dosyas%C4%B1-yede%C4%9Fi)
- [Kernel Güncelleme](#kernel-g%C3%BCncelleme)
- [Harici Bağlantılar](#harici-ba%C4%9Flant%C4%B1lar)

## Çalışma Alanlarını Bağımsızlaştırma (Isolate Workspace)

Bu işlem için `isolate workspaces` ayarını dash, dock ya da panel ayarlarında aktif hale getirmemiz lazım.

> Panel için `dock` yazan kısma `panel` yazıp komutu kullanın.

```sh
gsettings set org.gnome.shell.extensions.dash-to-dock isolate-workspaces true
```

## Dosya İzinleri

Dosya izinleri `chmod <parametre> <izin_no> <dosya_veya_dizin>` komutuyla yapılır.

| Parametmerler | Açılımı   | Anlamı                               |
| ------------- | --------- | ------------------------------------ |
| `-R`          | Recursive | Dizin ve alt dizinlerini de ele alır |

### İzin Kodu Hesaplama

İzin kodu, aşağıdaki formattaki kod yapısıdır.

- Sırasıyla `owner`, `group`, `others` basamaklarına alttaki yetkilerin toplamının atanmasıdır
  - `4` Read (okuma)
  - `2` Write (yazma)
  - `1` Execute (çalıştırma)
  - `0` No permission (izin yok)

```sh
mkdir temp
sudo chmod 777 temp # Her gruba tüm yekileri verme
sudo chmod 751 temp # Oner: Hepsi Group: Read & Write Others: Execute
sudo chmod 000 temo # Hiç yetki yok
sudo chmod -R 777 temp # Dizine ve altdizinlere herkes için tam yetki verme
```

> `Root` her şeye erişebilir.

### Dizine ve Alt Dizinlerine Okuma ve Yazma İzni Verme

Alttaki komutla dizine ve alt dizinlerine herkes için okuma ve yazma erişimi verebilirsin.

```sh
sudo chmod -R 757 /opt/lampp/htdocs/wordpress/
```

## Desktop kısayolu oluşturma

Text editörü açıp

```sh
gedit dosya/yolu.desktop
```

Alttaki alanda gerekli yerleri doldurun.

```ini
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

> Detaylı bilgi için [buraya][Linux desktop entry oluşturma] bakabilirsin.

### Whatsapp Kısayolu

Text editörü açıp;

```sh
sudo -H gedit /usr/share/applications/whatsapp-webapp.desktop
```

açılan yere alttaki verileri kopyalayın;

```ini
#!/usr/bin/env xdg-open
[Desktop Entry]
Name=WhatsApp
GenericName=WhatsApp
Comment=WhatsApp desktop webapp
#Exec=webapp-container --store-session-cookies --webappUrlPatterns=https?://*.whatsapp.com/* --user-agent-string='Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36' https://web.whatsapp.com %u
Exec=/opt/google/chrome/google-chrome --app=https://web.whatsapp.com/
Terminal=false
Type=Application
StartupNotify=true
MimeType=text/plain;
# Alttaki alana ikon yolunuzu kopyalayın
# Icon=
Categories=Network;Application;
Keywords=WhatsApp;webapp;
X-Ubuntu-Gettext-Domain=WhatsApp
StartupWMClass=web.whatsapp.com
```

#### Whatsapp İkonu Ekleme

İlk olarak [buradaki][Whatsapp Svg] ikonu indirin.

- İndirdiğiniz dosyanın yolunu kopyalayın
- `gedit /usr/share/applications/whatsapp-webapp.desktop` komutu ile dosyayı tekrar açın
- İçerisinde `Icon=` olan satırın başındaki `#` karkterini silin ve yolu kopyalayın
  - Örn: `Icon=/home/yemreak/Pictures/Ikons/Svg/whatsapp-webapp.svg`

#### Wmctrl ile Kısayol Oluşturma

Alttaki komut ile wapp açıksa gösterme, kapalıysa oluşturmayı sağlayabilirsin.

```sh
bash -c "wmctrl -xa web.whatsapp.com || /opt/google/chrome/google-chrome --app=https://web.whatsapp.com/"
```

## Window Manager Controls

Uygulamaların durumlarını kontrol eden `wmctrl` adlı komuttur.

- `wmctrl -xa <uygulama_komutu>` uygulama açıksa ekrana getirir.
- `wmctrl -v <uygulama>` Uygulama varsa 1 döndürür
- `wmctrl -xc <uygulama_komutu>` uygulamayı kibarca kapatma
- `wmctrl -lxG` açık olan uygulamalar hakkında bilgi basar.

## Uygulamaların Terminal Komutlarını öğrenme

Alttaki komutu yazdıktan sonra pencerenin üstüne tıklamanız yeterlidir.

```sh
xprop | grep WM_CLASS
```

## Herhangi bir Uygulama için Kısayol Oluşturma

### Uygulama için `WM_CLASS` metnini tanımlama

To do this, you need to make desktop app.

- Terminale `sudo -H gedit /usr/share/applications/<appname>.desktop` komutunu yazın
- Açılan dosyada gerekli bilgileri, [buradaki][Linux desktop entry oluşturma] bilgiden de yararlanarak doldurun
- Örnek dosya içeriği aşağıdaki gibi olacaktır

```ini
#!/usr/bin/env xdg-open
[Desktop Entry]
Name=WhatsApp
GenericName=WhatsApp
Comment=WhatsApp desktop webapp
Exec=/opt/google/chrome/google-chrome --app=https://web.whatsapp.com/
Terminal=false
Type=Application
StartupNotify=true
MimeType=text/plain;
# Alttaki alana ikon yolunuzu kopyalayın
# Icon=
Categories=Network;Application;
Keywords=WhatsApp;webapp;
X-Ubuntu-Gettext-Domain=WhatsApp
StartupWMClass=web.whatsapp.com
```

### Herhangi bir uygulamanın `WM_CLASS` metnini alma

- Terminal üzerinde `xprop | grep WM_CLASS` komutu ile `WM_CLASS` metnini alabiliriz
- Komutu yazıp <kbd>ENTER</kbd>'a bastıktan sonra kısayolunu oluşturmak istediğimiz uygulamaya tıklıyoruz
- Yandaki gibi bir çıktı gelecektir `WM_CLASS(STRING) = "gnome-terminal-server", "Gnome-terminal`
- `gnome-terminal-server` olan metni <kbd>CTRL</kbd> + <kbd>SHIFT</kbd> + <kbd>C</kbd> ile kopyalıyoruz

### Kısayolu oluşturma

- <kbd>SUPER</kbd> tuşuna basıp arama yerine `shortcut` yazıyoruz
- Açılan pencerenin en altındaki `+` butonuna tıklayarak kısayol ekliyoruz
- **name** alanına herhangi bir isim giriyoruz
- Ardından **command** alanına `bash -c "wmctrl -xa <wm_class> || <wm_class>` yazıyoruz
- Son olarak klavye kısayolunu atıyoruz ve kaydediyoruz

## Grub Menüyü Atlama

- `sudo nano /etc/default/grub` ile grub yapılandırma dosyasını açın
- En alt kısmına `GRUB_HIDDEN_TIMEOUT=0` yazın ve `GRUB_TIMEOUT=0` yapın
- <kbd>CTRL</kbd> + <kbd>S</kbd> e basarak kaytıt edin, <kbd>CTRL</kbd> + <kbd>X</kbd> ile çıkış yapın
- `sudo update-grub` ile yine grub ayarlarını aktifleştirin

## Donanım Komutları

- `nproc` İşlemci çekirdek sayısını gösterir.
- `uname -v` Kernel sürümünü gösterir
- `lspci` Donanum bilgilerini gösterir

## Silinen Yerel Dosyaları Kurtarma

Home dizinin yanlışlıkla (ya da bilinçli 🧐) `rm -rf *` komutu uygulanması durumunda bu sorun meydana gelir. İster en alttaki script ile isterseniz talimatlarla sorunu çözebilirsiniz.

- `cd ~` ile `Home` dizinine gelin ve dizinlerinizi oluşturun
- `gedit ~/.config/user-dirs.dirs` ile dizinleri ayarların
- `xdg-user-dirs-update` komutu ile dizinleri güncelleyin

```sh
cd ~
mkdir Downloads Templates Shares Documents Musics Pictures Videos Desktop
echo '# This file is written by xdg-user-dirs-update' > ~/.config/user-dirs.dirs
echo '# If you want to change or add directories, just edit the line you are' >> ~/.config/user-dirs.dirs
echo '# interested in. All local changes will be retained on the next run.' >> ~/.config/user-dirs.dirs
echo '# Format is XDG_xxx_DIR="$HOME/yyy", where yyy is a shell-escaped' >> ~/.config/user-dirs.dirs
echo '# homedir-relative path, or XDG_xxx_DIR="/yyy", where /yyy is an' >> ~/.config/user-dirs.dirs
echo '# absolute path. No other format is supported.' >> ~/.config/user-dirs.dirs
echo '# YEmreAk' >> ~/.config/user-dirs.dirs
echo 'XDG_DOWNLOAD_DIR="$HOME/Downloads"' >> ~/.config/user-dirs.dirs
echo 'XDG_TEMPLATES_DIR="$HOME/Templates"' >> ~/.config/user-dirs.dirs
echo 'XDG_PUBLICSHARE_DIR="$HOME/Shares"' >> ~/.config/user-dirs.dirs
echo 'XDG_DOCUMENTS_DIR="$HOME/Documents"' >> ~/.config/user-dirs.dirs
echo 'XDG_MUSIC_DIR="$HOME/Musics"' >> ~/.config/user-dirs.dirs
echo 'XDG_PICTURES_DIR="$HOME/Pictures"' >> ~/.config/user-dirs.dirs
echo 'XDG_VIDEOS_DIR="$HOME/Videos"' >> ~/.config/user-dirs.dirs
echo 'XDG_DESKTOP_DIR="$HOME/Desktop"' >> ~/.config/user-dirs.dirs
xdg-user-dirs-update
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

## Bashrc Dosyası Yedeği

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

## Kernel Güncelleme

Kernel güncelleme yazım için [buraya][Kernel Güncelleme] bakabilirsin.

## Harici Bağlantılar

- [Windows yanına linux kurulduğunda windows saatinin bozulması]
- [Linux desktop entry oluşturma]
- [Uygulamalar için neden sudo -h kullanılmalı]
- [Ubuntu soluk renk]
- [Ubuntu 19.04 yenilikleri]

[Kernel Güncelleme]: https://medium.com/@yyunussemree/linux-kernel-g%C3%BCncelleme-4ce3ce55de36
[Windows yanına linux kurulduğunda windows saatinin bozulması]: https://www.howtogeek.com/323390/how-to-fix-windows-and-linux-showing-different-times-when-dual-booting/
[Linux desktop entry oluşturma]: https://askubuntu.com/a/282187
[Whatsapp Svg]: res/whatsapp-webapp.svg
[Uygulamalar için neden sudo -h kullanılmalı]: https://askubuntu.com/questions/270006/why-should-users-never-use-normal-sudo-to-start-graphical-applications

[Ubuntu soluk renk]: https://askubuntu.com/questions/621964/colors-on-display-are-washed-out#
[Ubuntu 19.04 yenilikleri]: https://itsfoss.com/ubuntu-19-04-release-features/