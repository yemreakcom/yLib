---
description: Pixhawk Firmware kaynak kodlarının derlenmesi
---

# 👨‍💻 Kodlarını Derleme

## 🌄 Linux Sanal Ortamını Hazırlama

PixHawk kodları Linux ortamını önermekte ve desteklemektedir

* Sorunsuz ve etkili çalışma adına Linux ortamı seçilmelidir
* Windows üzerinden WSL ile Linux kullanılabilir
* Alttaki bağlantı üzerinden Ubuntu'yu bilgisayarınıza subsystem olarak kurun

{% embed url="https://windows.yemreak.com/diger-notlar/windows-subsystem-for-linux-wsl" %}

{% hint style="warning" %}
📢 Alttaki işlemlerin her biri **Ubuntu terminali üzerinden** yapılmalıdır.
{% endhint %}

### 🔗 Alakalı Bağlantı

{% embed url="https://wiki.yemreak.com/isletim-sistemi-notlari/linux-notlari/linux-gelismis\#linuxta-varsayilan-olarak-python3-kullanma" %}

## ‍⏬ PixHawk Kodlarının İndirilmesi

Ubuntu terminaliniz üzerinden alttaki komut ile projeyi indirin ve ardından proje dizinine girin

```bash
 git clone https://github.com/PX4/Firmware.git
 cd Firmware
```

## 📦 Gerekli Paketlerin Kurulumu

* Windows terminalinden `bash` komutu ile Linux terminalinize geçin
* Terminal üzerinden alttaki komutlarla gereksinimleri kurun

```bash
sudo apt update # Sunucuları yenileme
sudo apt upgrade # Paketleri güncelleme
sudo apt install cmake build-essential # Derleme araçlarını yükleme
sudo apt-get install python3-pip astyle
pip install catkin_pkg numpy toml empy
```

{% hint style="info" %}
🧙‍♂️ Python2 ve python3 çakışmalarını engellemek için [👨‍🔧 Linux'ta Varsayılan Olarak Python3 Kullanma](https://wiki.yemreak.com/isletim-sistemi-notlari/linux-notlari/linux-gelismis#linuxta-varsayilan-olarak-python3-kullanma) alanına bakabilirsin.
{% endhint %}

## 🌃 VsCode Üzerinden Derleme

PixHawk VsCode üzerinden düzenlenebilecek şekilde Firmware kodlarını oluşturmuştur.

* VsCode'u Windows'a indirin
* Ubuntu'yu terminale `ubuntu`  yazıp veya arama yerinde aratıp açabilirsiniz
* Ubuntu üzerinden Firmware dizininde `code .` yazarak VsCode ile kaynak kodları açın

{% hint style="success" %}
VsCode yüklü ise terminalden `code .` komutu ile projeyi remote olarak VsCode ile açabilirsiniz
{% endhint %}

### 🔌 Eklentileri Ekleme

* Tüm gerekli eklentiler PixHawk tarafından ayarlanmıştır
* **Install All** butonu ile indirmeniz yeterli

![](../../.gitbook/assets/image%20%2845%29.png)

### 🚧 Build Etme

* Kaynak kodları kullanmak için onların **build** edilmesi gerekir
* Build işlemini **Status Bar** üzerinden yapabiliriz
* Veya `make px4_fmu-v4_default` komutu ile **NuttX / Pixhawk Based Boards** için derleyebiliriz

![](../../.gitbook/assets/image%20%2882%29.png)

{% hint style="warning" %}
📢 Build ederken herhangi bir sorunla karşılaştığınızda [📦 Gerekli Paketlerin Kurulumu]() alanındaki paketleri kurduğunuzdan emin olun
{% endhint %}

## 🔗 Ayrıntılı Açıklamalar

{% embed url="https://dev.px4.io/master/en/setup/vscode.html" %}

{% embed url="https://dev.px4.io/master/en/setup/building\_px4.html" %}

