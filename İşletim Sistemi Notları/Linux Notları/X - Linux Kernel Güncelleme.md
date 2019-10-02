---
description: Linux üzerinde can sıkan kernel güncelleme olayı
---


# 💎 Linux Kernel Güncelleme

## 🗽 Açıklama

- Bu yazı bir alıntı (türkçeleştirme) yazısıdır, orjinal halini görmek için [buraya](https://www.cyberciti.biz/tips/compiling-linux-kernel-26.html) tıklayabilirsin.

## ⤵ Güncel Kernel Dosyasının İndirilmesi

[🐧 The Linux Kernel Archives](https://www.kernel.org/) sitesi üzerinden en güncel kernel sürümünü indirin veya alttaki komut ile indirmeyi 🖤 terminal üzerinden yapın:

```sh
wget -O linux-5.3.2.tar.xz https://cdn.kernel.org/pub/linux/kernel/v5.x/linux-5.3.2.tar.xz
```

![](../../res/linux_kernel_archives.png)

## 📦 Kernel Kurulumu

### 🗃 Arşivden Çıkarma

İndirdiğiniz kernel dosyasının bulunduğu dizine girin. (Örn `cd ~/Downloads`)

**Ubuntu, Debian**:

```sh
xz -d -v linux-5.3.2.tar.xz # Ubuntu, Debian 
```

**Diğer**:

```sh
unzx -v linux-5.3.2.tar.xz
```

### ⚙ Yapılandırma Ayarları

```sh
cd linux-5.3.2
cp -v /boot/config-$(uname -r) .config
```

**Örnek Çıktı**:

```sh
'/boot/config-5.0.0-23-generic' -> '.config'
```

### 🧰 Geliştirici Araçlarının Kurulumu

```sh
sudo apt-get install build-essential libncurses-dev bison flex libssl-dev libelf-dev
```

### 👷‍ Kernel Yapılandırma

Kaynak kodların olduğu yerde aşağıdaki komuntlardan gerekli olanı yazıyoruz:

| Kod               | Açıklama                                         |
| ----------------- | ------------------------------------------------ |
| `make menuconfig` | Grafiksel arayüz ile yapılandırma                |
| `make xconfig`    | KDE Masaüstü ortamları için ideal yapılandırma   |
| `make gconfig`    | Gnome Masaüstü ortamları için ideal yapılandırma |

**Örnek komut kullanım şekli**:

```sh
make menuconfig
```

> Eğer make komutu bulunamadı hatası gelirse `sudo apt-get install make` ile indirmeniz gerekmekte

### ⚒ Kernel'i Derleme

Sıkıştırılmış kernel imajını derlemek için alttaki komutu yazın:

```sh
make -j $(nproc)
```

> `-j $(nproc)` komutu ile birden fazla işlemci çekirdeği kullanılır

### 🔆 Kernel Modüllerini Yükleme

```sh
sudo make modules_install
```

### ⏬ Kernel Yükleme

Alttaki komut ile aşağıdaki dosyaları `/boot` dizinine yükleyeceğiz

- initramfs-5.3.2.img
- System.map-5.3.2
- vmlinuz-5.3.2

```sh
sudo make install
```

## 👨‍🔧 Grub Yapılandırmasını Güncelleme

Grub2 yükleyicisinin yapılandırma ayarlarını yapmamız gerekmekte.

> Bu komutlar isteğe bağlıdır. make install işlemi bu işlemleri zaten yapmış olacaktır

```sh
sudo update-initramfs -c -k 5.3.2
sudo update-grub
```

## 🚀 İşlemleri Sonlandırma

- `reboot` ile sistemi yeniden başlatıyoruz
- Ardından `uname -mrs` ile linux kernel versiyonunu kontrol ediyoruz

**Örnek Çıktı**:

```sh
Linux 5.3.2 x86_64
```
