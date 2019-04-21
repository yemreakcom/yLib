# Anaconda <!-- omit in toc -->

Yapay zeka, veri analizi, makine öğrenimi gibi işlemler için gerekli olan paketleri hazır halde sunan ve onları yöneten bir uygulamadır.

> Anaconda ile yerel PC üzerinden çalışmak yerine, kurulumlarla uğraşmamak adına [Google Colab](https://colab.research.google.com/) hizmetini kullanabilirisin.

## İçerikler <!-- omit in toc -->

> `HOME` tuşu ile yukarı yönlenebilrsiniz.

- [Faydaları](#faydalar%C4%B1)
- [Anaconda Kurulumu](#anaconda-kurulumu)
- [Temel Condo Kullanımı](#temel-condo-kullan%C4%B1m%C4%B1)
  - [Conda Yardımcısını Güncelleme](#conda-yard%C4%B1mc%C4%B1s%C4%B1n%C4%B1-g%C3%BCncelleme)
  - [Conda ile Tüm Paketleri Güncelleme](#conda-ile-t%C3%BCm-paketleri-g%C3%BCncelleme)
  - [Conda ile Paket Sürümlerini Gösterme](#conda-ile-paket-s%C3%BCr%C3%BCmlerini-g%C3%B6sterme)
  - [Conda ile Yükleme İşlemleri](#conda-ile-y%C3%BCkleme-i%CC%87%C5%9Flemleri)
    - [Conda ile Belli Bir Sürümü İndirme](#conda-ile-belli-bir-s%C3%BCr%C3%BCm%C3%BC-i%CC%87ndirme)
- [Paket ve Kütüphane Kurulumları](#paket-ve-k%C3%BCt%C3%BCphane-kurulumlar%C4%B1)
  - [Numpy Kurulumu](#numpy-kurulumu)
  - [OpenCV Kurulumu](#opencv-kurulumu)
    - [Linux için OpenCV](#linux-i%C3%A7in-opencv)
  - [Tensorflow Kurulumu](#tensorflow-kurulumu)
    - [Sanal Ortama Tensorflow Kurulumu](#sanal-ortama-tensorflow-kurulumu)
  - [Tensorflow-GPU Kurulumu](#tensorflow-gpu-kurulumu)
    - [Sanal Ortama Tensorflow-GPU Kurulumu](#sanal-ortama-tensorflow-gpu-kurulumu)
  - [Keras Kurulumu](#keras-kurulumu)
  - [Tesseract Kurulumu](#tesseract-kurulumu)
  - [Selenium Kurulumu](#selenium-kurulumu)
  - [Pillow (Python Image Library) Kurulumu](#pillow-python-image-library-kurulumu)
- [Sanal Ortam İşlemleri](#sanal-ortam-i%CC%87%C5%9Flemleri)
  - [Sanal Ortam Oluşturma](#sanal-ortam-olu%C5%9Fturma)
    - [Belirli Python Sürümünde Ortam Oluşturma](#belirli-python-s%C3%BCr%C3%BCm%C3%BCnde-ortam-olu%C5%9Fturma)
  - [Sanal Ortamı Aktif Etme](#sanal-ortam%C4%B1-aktif-etme)
  - [Sanal Ortamı Pasif Etme](#sanal-ortam%C4%B1-pasif-etme)
  - [Sanal Ortamı Kaldırma](#sanal-ortam%C4%B1-kald%C4%B1rma)
- [Hata Notları](#hata-notlar%C4%B1)
  - [Conda SSL Hatası](#conda-ssl-hatas%C4%B1)
    - [Windows Üzerinden Ağ Sıfırlama](#windows-%C3%BCzerinden-a%C4%9F-s%C4%B1f%C4%B1rlama)
    - [Manuel OpenSSL Kurulumu](#manuel-openssl-kurulumu)
    - [Conda ile Networkx İndirme](#conda-ile-networkx-i%CC%87ndirme)
    - [SSL Ek Hata Linkleri](#ssl-ek-hata-linkleri)
- [PyCharm Üzerinden Anaconda](#pycharm-%C3%BCzerinden-anaconda)
  - [PyCharm Projeyi Derlemek için Yapılandırma Ayarlama](#pycharm-projeyi-derlemek-i%C3%A7in-yap%C4%B1land%C4%B1rma-ayarlama)
  - [PyCharm Üzerinden Sanal Conda Ortam Oluşturma](#pycharm-%C3%BCzerinden-sanal-conda-ortam-olu%C5%9Fturma)

## Faydaları

- NPM (node package manager) gibi sanal bir ortam oluşturup python kütüphanelerinin yönetimini sağlar.
  - `conda` komutu ve **Anaconda Promt** yardımıyla ile yönetimi sağlar.
- Veri bilimi ve yapay zeka konuları için sık kullanılan kütüphaneler ön yüklenmiş olarak gelir.
  - Tekrar indirmeye normal şartlar altında gerek kalmaz.

## Anaconda Kurulumu

- İndirmek için [buraya](https://hub.docker.com/r/continuumio/anaconda3/) tıklayabilirsin.
  - *Yükleme sırasında PATH'e eklemeyin* !
- Docker üzerine indirmek için [buraya](https://hub.docker.com/r/continuumio/anaconda3/) tıklayabilirsin
- Anaconda'yı windowsda kullanmak için **Anaconda Prompt**'u kullanman gerekmekte!
  - *Aksi halde değişik sorunlarla karşılaşırsınız. (SSL error vs.)*
- Dökümantasyonu için [buraya](https://docs.anaconda.com/) tıklayabilirsin.

## Temel Condo Kullanımı

Anaconda paket yönetim aracı `conda`'dır.

### Conda Yardımcısını Güncelleme

```sh
conda update -n base -c defaults conda
```

### Conda ile Tüm Paketleri Güncelleme

```sh
conda update --all
```

### Conda ile Paket Sürümlerini Gösterme

```sh
conda search <paket> --info
conda search tensorflow-gpu --info # Örnek
```

### Conda ile Yükleme İşlemleri

```sh
conda install <ayarlar> <framework | package | lib>
conda install -c <depo-ismi> <frameword vs.>

conda install -c conda-forge python-socketio # Örnek (dev olabilir)
conda install -c anaconda  flask # Örnek (stable olabilir)
```

#### Conda ile Belli Bir Sürümü İndirme

```sh
conda install -c <depo_ismi> <paket>=<versiyon>
conda install -c anaconda tensorflow-gpu=<versiyon> # Örnek
```

## Paket ve Kütüphane Kurulumları

Paket kurulumları `conda` komutu yardımıyla yapılır.

- Tüm bu işlemlerin **Anaconda Prompt** üzerinde yapıldığına emin olun!
- Sanal ortama yükleme yapılmadan önce sanal ortamın **aktif edilmesi** gerekmektedir!

### Numpy Kurulumu

```sh
conda install -c anaconda numpy
```

### OpenCV Kurulumu

```sh
conda install opencv
```

#### Linux için OpenCV

GTK ve FFMPEG support hatası gelmemesi adına bu şekilde indirme yapılmalıdır

```sh
pip install opencv-contrib-python
```

### Tensorflow Kurulumu

Anaconda'nın resmi sitesindeki açıklama için [buraya](https://www.anaconda.com/tensorflow-in-anaconda/) bakabilirsin.

- Bu kurulum CPU kurulumu olarak da geçmekte
- GPU kurulumu CPU'ya nazaran oldukça hızlı eğitim seçeneği sağlar
- GPU kurulumu için gereksinimleri sağlıyorsanız GPU kurulumu (tensorflow-gpu) yapmanız tavsiye edilir

> Daha yüksek verim için tensorflow için ortam oluşturun.

```sh
conda install -c conda-forge tensorflow
```

#### Sanal Ortama Tensorflow Kurulumu

Tensorflow için sanal ortam oluşturmak hız açısından daha faydalıdır.

```sh
conda create -n tensorflow-cpu tensorflow # Tensorflow ortamı oluşturma
conda activate tensorflow-cpu # Ortamı aktif etme
```

### Tensorflow-GPU Kurulumu

Anaconda'nın resmi sitesindeki açıklama için [buraya](https://www.anaconda.com/tensorflow-in-anaconda/) bakabilirsin.

- Bu kurulum GPU kurulumu olarak geçmekte
- GPU kurulumu CPU'ya nazaran oldukça hızlı eğitim seçeneği sağlar
- GPU kurulumu için gereksinimleri sağlamıyorsanız CPU kurulumu (tensorflow) yapmanız tavsiye edilir
  - Ekran kartınızın **NVIDIA olması ve desteklemesi** gerekmektedir  
  - Kontrol için [buraya](https://developer.nvidia.com/cuda-gpus) tıklayabilirsin

> Daha yüksek verim için tensorflow-gpu için ortam oluşturun

```sh
conda search tensorflow-gpu --info # Sürüme karar vermek için
conda install -c anaconda tensorflow-gpu=<versiyon> # Belirli sürümü indirme
conda install -c anaconda tensorflow-gpu=1.12.0 # Örnek
```

#### Sanal Ortama Tensorflow-GPU Kurulumu

Tensorflow için sanal ortam oluşturmak hız açısından daha faydalıdır.

```sh
conda create -n tensorflow-gpu tensorflow-gpu
conda activate tensorflow-gpu
```

### Keras Kurulumu

```sh
conda install -c conda-forge keras
```

### Tesseract Kurulumu

Resimden yazıyı çekmek için kullanılır.

```sh
conda install -c mcs07 tesseract
conda install -c jim-hart pytesseract
```

> [Pillow (Python Image Library)](#pillow-python-image-library) paketinin de indirimlesi gerekebilir.

### Selenium Kurulumu

Web siteleri üzerinde işlem yapmak için kullanılır.

```sh
conda install -c conda-forge selenium
conda install -c clinicalgraphics selenium-chromedriver
```

### Pillow (Python Image Library) Kurulumu

Python resim kütüphanesi resim işlemleri için kullanılır.

```sh
conda install -c anaconda pillow
```

## Sanal Ortam İşlemleri

Sanal ortamlar üzerine çalışmak istediğimiz projeler için kurulur ve gerekmediği vakit kaldırılır.

> Projelerin bağımlılıkları arasında çakışma olmasını engeller.

### Sanal Ortam Oluşturma

```sh
conda create -n <ortam_ismi>
conda create -n myenv # Örnek
```

#### Belirli Python Sürümünde Ortam Oluşturma

```sh
conda create -n <ortam_ismi> anaconda python=<versiyon>
conda create -n Tensorflow anaconda python=3.6 # Örnek
```

> Ortam *Anaconda3/env* dizinine kaydedilir.

### Sanal Ortamı Aktif Etme

```sh
conda activate <ortam_ismi>
conda activate myenv # Örnek
```

> Ortam seçildiğinde (base) yazan kısımda (`<ortam_ismi>`) yazar.

### Sanal Ortamı Pasif Etme

```sh
conda deactivate
```

### Sanal Ortamı Kaldırma

```sh
conda env remove -n <ortam_ismi>
conda env remove -n myenv # Örnek
```

> Anaconda Prompt `base` ortamına geri döner.

## Hata Notları

### Conda SSL Hatası

#### Windows Üzerinden Ağ Sıfırlama

Windows 10'daki  `Ağı Sıfırla` ayarını deneyin

- Ayarlar (*Options*)
- Ağ ve İnternet (*Network & Internet*)
- Durum sekmesi (*Status tab*)
- Sayfanın en altına bakın (*Ağı Sıfırla / Network Reset*)
- Şimdi Sıfırla (*Reset Now*)

> Bu işlem kaydedilmiş WI-FI şifrelerini de silecektir.

#### Manuel OpenSSL Kurulumu

Kurulum sayfasına gitmek için [buraya](https://slproweb.com/products/Win32OpenSSL.html) tıklayabilirsin.

> Kaynak için [buraya](https://github.com/conda/conda/issues/8046#issuecomment-450515815) tıklayabilirsin.

#### Conda ile Networkx İndirme

```sh
conda install -c anaconda networkx
```

#### SSL Ek Hata Linkleri

- [How to install the most recent version of OpenSSL on Windows 10 in 64 Bit](https://www.cloudinsidr.com/content/how-to-install-the-most-recent-version-of-openssl-on-windows-10-in-64-bit/)
- [Conda update failed: SSL error: [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed](https://stackoverflow.com/a/35804869/9770490)
- [Setting SSL Verify](https://github.com/ContinuumIO/anaconda-issues/issues/494#issuecomment-155097614)

## PyCharm Üzerinden Anaconda

### PyCharm Projeyi Derlemek için Yapılandırma Ayarlama

Çalıştırma butonu üzerinden (`SHIFT` + `F9`) projeyi çalıştırmak için:

- Derleme butonu yanındaki `seçme kutusuna` tıklayın
- `Edit Configuration`
- Sol üstten `+` butonuna basıns
  - `Python`
- `Script Path:` kısmından çalıştırmak istediğiniz **.py** uzantılı dosyayı seçin
- `OK`

### PyCharm Üzerinden Sanal Conda Ortam Oluşturma

- `CTRL` + `ALT` + `S` ile ayarlara girin
- `Project: imgtotext`
  - `Project: Interpeter`
- Sağ üstteki `ayarlar butonu`na tıklayın
  - `Add`
  - `Conda Enviroment`
  - `OK`
- `+` butonu ile ek paket kurulumu yapabilirsiniz (*İsteğe Bağlı*)
