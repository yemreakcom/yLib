# 🐍 Anaconda

Yapay zeka, veri analizi, makine öğrenimi gibi işlemler için gerekli olan paketleri hazır halde sunan ve onları yöneten bir uygulamadır.

> Anaconda ile yerel PC üzerinden çalışmak yerine, kurulumlarla uğraşmamak adına [Google Colab](https://colab.research.google.com/) hizmetini kullanabilirisin.

<!-- TODO İçerikleri kullanabilitesine göre sırala -->

## Faydaları

- NPM (node package manager) gibi sanal bir ortam oluşturup python kütüphanelerinin yönetimini sağlar.
  - `conda` komutu ve **Anaconda Promt** yardımıyla ile yönetimi sağlar.
- Veri bilimi ve yapay zeka konuları için sık kullanılan kütüphaneler ön yüklenmiş olarak gelir.
  - Tekrar indirmeye normal şartlar altında gerek kalmaz.

## Anaconda Kurulumu

Anaconda kurulurken beraberinde bir kaç modül daha kurmakta. Başlangıç aşamasındakiler için önerilir.

> Ne yaptığımı biliyorum diyorsan _Anaconda_ yerine **Miniconda** tavsiye edilir, minimalist bir yükleme sunar.

- İndirmek için [buraya](https://hub.docker.com/r/continuumio/anaconda3/) tıklayabilirsin.
  - _Yükleme sırasında PATH'e eklemeyin_ !
- Docker üzerine indirmek için [buraya](https://hub.docker.com/r/continuumio/anaconda3/) tıklayabilirsin
- Anaconda'yı windowsda kullanmak için **Anaconda Prompt**'u kullanman gerekmekte!
  - _Aksi halde değişik sorunlarla karşılaşırsınız. (SSL error vs.)_
- Dökümantasyonu için [buraya](https://docs.anaconda.com/) tıklayabilirsin.

## Miniconda Kurulumu

- İndirmek için [buraya](https://docs.conda.io/en/latest/miniconda.html) tıklayabilirsin.
- Linux için: `conda init` ile _conda_'yı _bash_'e dahil edebilir, `conda config --set auto_activate_base false` ile otomatik tanımlamayı kaldırabilirsin.
  - `~./bashrc` dosyasında değişiklikler yapılacaktır
  - Kaynak için [buraya](https://docs.anaconda.com/anaconda/install/silent-mode/#linux-macos) bakabilirsin.

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

### Conda ile Requirements Dosyası Oluşturma

`requirements.txt` dosyası sayesinde projeyi farklı ortamlara aktarmak istediğimizde, gerekli kurulumları hızlıca yapabiliriz.

```sh
conda list --export > requirements.txt
conda create --name <envname> --file requirements.txt # Dosyadan ortam oluşturma
```

> Kaynak için [buraya][requirements dosyası] bakabilirsin.

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

#### Requirements Dosyasına Uygun Sanal Ortam Oluşturma

```sh
conda create --name <ortam_ismi> --file requirements.txt
```

#### Belirli Python Sürümünde Ortam Oluşturma

```sh
conda create -n <ortam_ismi> anaconda python=<versiyon>
conda create -n Tensorflow anaconda python=3.6 # Örnek
```

> Ortam _Anaconda3/env_ dizinine kaydedilir.

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

Windows 10'daki `Ağı Sıfırla` ayarını deneyin

- Ayarlar (_Options_)
- Ağ ve İnternet (_Network & Internet_)
- Durum sekmesi (_Status tab_)
- Sayfanın en altına bakın (_Ağı Sıfırla / Network Reset_)
- Şimdi Sıfırla (_Reset Now_)

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

Çalıştırma butonu üzerinden (<kbd>⇧ Shift</kbd> + `F9`) projeyi çalıştırmak için:

- Derleme butonu yanındaki `seçme kutusuna` tıklayın
- `Edit Configuration`
- Sol üstten `+` butonuna basıns
  - `Python`
- `Script Path:` kısmından çalıştırmak istediğiniz **.py** uzantılı dosyayı seçin
- `OK`

### PyCharm Üzerinden Sanal Conda Ortam Oluşturma

- <kbd>✲ Ctrl</kbd> + <kbd>⎇ Alt</kbd> + `S` ile ayarlara girin
- `Project: imgtotext`
  - `Project: Interpeter`
- Sağ üstteki `ayarlar butonu`na tıklayın
  - `Add`
  - `Conda Enviroment`
  - `OK`
- `+` butonu ile ek paket kurulumu yapabilirsiniz (_İsteğe Bağlı_)

[requirements dosyası]: https://stackoverflow.com/a/45491091/9770490
