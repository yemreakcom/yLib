---
description: Google'ın sunduğu online kontrol edilebilir bilgisayar hizmeti
---

# 🟠 Google Colabrotory

## ❔ Nedir

* Kodlama dili [🐍 IPython](https://github.com/yedhrab/YWiki/tree/169abadfd1b8862c004399268f6ca1f9f9359d61/6%20-%20Uygulama%20&%20Yazılım/Programlama%20Notları/IPython/README.md) olarak geçmektedir, bağlantıya tıklarak detaylara erişebilirsin
* Colab üzerinde kullanılan komutların \(IPython\) dökümanı için [buraya](https://ipython.readthedocs.io/en/stable/index.html) bakabilirsin.

## ⚙ Google Colab Çalışma Ortamını Yapılandırma

### İşletim Sistemi Bilgileri

```text
!less /etc/os-release
```

```bash
NAME="Ubuntu"
VERSION="18.04.2 LTS (Bionic Beaver)"
ID=ubuntu
ID_LIKE=debian
PRETTY_NAME="Ubuntu 18.04.2 LTS"
VERSION_ID="18.04"
HOME_URL="https://www.ubuntu.com/"
SUPPORT_URL="https://help.ubuntu.com/"
BUG_REPORT_URL="https://bugs.launchpad.net/ubuntu/"
PRIVACY_POLICY_URL="https://www.ubuntu.com/legal/terms-and-policies/privacy-policy"
VERSION_CODENAME=bionic
UBUNTU_CODENAME=bionic
(END)^C
```

### Google Colab için Çalışma Ortamını Yapılandırma

Ekran kartını veya TPU'yu aktif ederek 📈 daha yüksek verim alabilirsin.

* Change Run Time
  * TPU
  * GPU

### Kernel'ı Sıfırlama

```python
!kill -9 -1
```

## Harici Bağlantılar

* [Overview of Colaboratory Features](https://colab.research.google.com/notebooks/basic_features_overview.ipynb)
* [External data: Drive, Sheets, and Cloud Storage](https://colab.research.google.com/notebooks/io.ipynb)
* [Styled table outputs](https://colab.research.google.com/drive/1oXkzlM0lPbDC8saNRUnkGOjpKCTiDHvM)
* [Mardown Guide](https://colab.research.google.com/notebooks/markdown_guide.ipynb)
* [Froms](https://colab.research.google.com/notebooks/forms.ipynb)
* [Magic Command](https://ipython.readthedocs.io/en/stable/interactive/magics.html)
* [Resetting VM](https://stackoverflow.com/questions/49001921/how-to-restart-virtual-machine)
* [Interacting with Shell](http://mmcdan.github.io/posts/interacting-with-the-shell-via-jupyter-notebook/)
* [Colab'ı Jupyter üzerinde Kendi PC'mizde Kullanma](https://research.google.com/colaboratory/local-runtimes.html)
* [https://dev.to/ikeyasu/how-to-use-google-colaboratory-with-local-runtime-4j1p](https://dev.to/ikeyasu/how-to-use-google-colaboratory-with-local-runtime-4j1p)

