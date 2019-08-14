# Windows Subsystem for Linux (WSL) <!-- omit in toc -->

## İçerikler <!-- omit in toc -->

- [Terminel Sesini Kapatma](#Terminel-Sesini-Kapatma)
- [Linux Uygulamalarını WSL Üzerinde Çalıştırma](#Linux-Uygulamalar%C4%B1n%C4%B1-WSL-%C3%9Czerinde-%C3%87al%C4%B1%C5%9Ft%C4%B1rma)
- [WSL'i Ubuntu'nun Son Sürümüne Güncelleme](#WSLi-Ubuntunun-Son-S%C3%BCr%C3%BCm%C3%BCne-G%C3%BCncelleme)

## Terminel Sesini Kapatma

- `sudo nano /etc/inputrc` ile girdi dosyasını yetki ile açın
- `set bell-style none` satırını yorum satırı olmaktan kaldırın
- <kbd>✲ Ctrl</kbd> + <kbd>O</kbd> ile düzenlemeyi kaydedin
- <kbd>✲ Ctrl</kbd> + <kbd>X</kbd> ile çıkın

## Linux Uygulamalarını WSL Üzerinde Çalıştırma

- İlk olarak [vcxsrv] dosyasını indirin (~ 37.8MB)
- `echo "export DISPLAY=localhost:0.0" >> ~/.bashrc` komutunu yazın
- `sudo apt install dbus-x11` ile gereksinimleri indirin
  - Alttaki komutlara gerekirse yapılmalıdır
  - `sudo service dbus start` [kaynak](https://github.com/Microsoft/WSL/issues/2016#issuecomment-435091497)
  - `export $(dbus-launch)` [kaynak](https://github.com/Microsoft/WSL/issues/2016#issuecomment-462595967)

## WSL'i Ubuntu'nun Son Sürümüne Güncelleme

```sh
# Güncelleme ön hazırlığı
sudo apt update && sudo apt dist-upgrade
sudo apt install update-manager-core

# # Prompt=normal olarak ayarlayın CTRL+O ve CTRL+X ile kaydedin
sudo nano /etc/update-manager/release-upgrades

sudo sed -i 's/bionic/disco/g' /etc/apt/sources.list # Bionic'i Disco yapmak

# Minimalist güncelleme
sudo sed -i 's/^/#/' /etc/apt/sources.list.d/*.list # 3.parti yazılımları kaldırma (PPA)
sudo apt update
sudo apt upgrade
sudo apt dist-upgrade # Tam yükseltme

# Sonucu görme
lsb_release  -a
```

```text
Distributor ID: Ubuntu
Description:    Ubuntu 19.04
Release:        19.04
Codename:       disco
```

> [Kaynak](https://www.linuxbabe.com/ubuntu/upgrade-ubuntu-18-04-18-10-to-ubuntu-19-04)
