# Google Colabrotory <!-- omit in toc -->

Colab üzerinde kullanılan komutların (IPython) dökümanı için [buraya](https://ipython.readthedocs.io/en/stable/index.html) bakabilirsin.

## İçerikler <!-- omit in toc -->

- [İşletim Sistemi Bilgileri](#%C4%B0%C5%9Fletim-Sistemi-Bilgileri)
- [Run Time Ayarları](#Run-Time-Ayarlar%C4%B1)
  - [Kernel'ı Sıfırlama](#Kernel%C4%B1-S%C4%B1f%C4%B1rlama)
- [Komut Parametreleri](#Komut-Parametreleri)
  - [Shell Komutları Kullanımı](#Shell-Komutlar%C4%B1-Kullan%C4%B1m%C4%B1)
- [Giriş / Çıkış İşlemleri](#Giri%C5%9F--%C3%87%C4%B1k%C4%B1%C5%9F-%C4%B0%C5%9Flemleri)
  - [Colab'a Dosya Upload Etme](#Colaba-Dosya-Upload-Etme)
  - [Colab'tan Dosya İndirme](#Colabtan-Dosya-%C4%B0ndirme)
  - [Colab'tan Dizin İndirme](#Colabtan-Dizin-%C4%B0ndirme)
    - [Dizin İndirme Arayüzü](#Dizin-%C4%B0ndirme-Aray%C3%BCz%C3%BC)
- [Colab Üzerinde Google Drive](#Colab-%C3%9Czerinde-Google-Drive)
  - [Drive Dosyalarını Dosya Sistemine Bağlama](#Drive-Dosyalar%C4%B1n%C4%B1-Dosya-Sistemine-Ba%C4%9Flama)
  - [Drive Dosyalarına Erişme](#Drive-Dosyalar%C4%B1na-Eri%C5%9Fme)
- [Colab Üzerinden Özel İşlemler](#Colab-%C3%9Czerinden-%C3%96zel-%C4%B0%C5%9Flemler)
  - [Bilgisayar Kamerasına Erişme](#Bilgisayar-Kameras%C4%B1na-Eri%C5%9Fme)
- [Harici Bağlantılar](#Harici-Ba%C4%9Flant%C4%B1lar)

## İşletim Sistemi Bilgileri

```ipynb
!less /etc/os-release
```

```sh
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

## Run Time Ayarları

- Change Run Time
  - TPU
  - GPU

### Kernel'ı Sıfırlama

```py
!kill -9 -1
```

## Komut Parametreleri

- `%` Magic Command
- `!` Command
- Python kodu

### Shell Komutları Kullanımı

Shell komutlarıyla:

- `{ }` arasında python kod parçları
- `$` Ortam değişkenleri

```sh
TEMP = 'gecici'
!echo {gecici} # Python değişkenini kullanma
!echo {gecici.split('i')[0]} # Python kod parçası kullanma

!echo $PYTHONPATH # Ortam değşkenini kullanma
```

## Giriş / Çıkış İşlemleri

### Colab'a Dosya Upload Etme

```py
from google.colab import files

uploaded = files.upload()

for fn in uploaded.keys():
  print('User uploaded file "{name}" with length {length} bytes'.format(
      name=fn, length=len(uploaded[fn])))
```

### Colab'tan Dosya İndirme

```py
from google.colab import files

with open('example.txt', 'w') as f:
  f.write('some content')

files.download('example.txt')
```

### Colab'tan Dizin İndirme

```py
!zip -r /content/file.zip /content/Folder_To_Zip

from google.colab import files
files.download("/content/file.zip")
```

#### Dizin İndirme Arayüzü

```py
#@title Dizin İndirme Arayüzü
INDIRILECEK_DIZININ_YOLU = "sample_data" #@param {type:"string"}

from google.colab import files

# Dizin adını alma
folder_name = INDIRILECEK_DIZININ_YOLU.split('/').pop()

# Gerekli dosyaları oluşturma
!cp -r "/{INDIRILECEK_DIZININ_YOLU}" "/content"
!zip -r '{folder_name}.zip'  "{folder_name}"

# İndirme işlemini başlatma
files.download(f'{folder_name}.zip')

# Geçici dosyaları temizleme
!rm -rf '{folder_name}.zip'
!rm -rf '{folder_name}'
```

## Colab Üzerinde Google Drive

Resmi dökümantasyon için [buraya](https://colab.research.google.com/notebooks/io.ipynb#scrollTo=XDg9OBaYqRMd) bakabilirsin.

### Drive Dosyalarını Dosya Sistemine Bağlama

```py
from google.colab import drive
drive.mount('/content/gdrive')
```

### Drive Dosyalarına Erişme

```py
with open('/content/gdrive/My Drive/foo.txt', 'w') as f:
  f.write('Hello Google Drive!')
!cat /content/gdrive/My\ Drive/foo.txt
```

## Colab Üzerinden Özel İşlemler

### Bilgisayar Kamerasına Erişme

```py
from IPython.display import display, Javascript
from google.colab.output import eval_js
from base64 import b64decode

def take_photo(filename='photo.jpg', quality=0.8):
  js = Javascript('''
    async function takePhoto(quality) {
      const div = document.createElement('div');
      const capture = document.createElement('button');
      capture.textContent = 'Capture';
      div.appendChild(capture);

      const video = document.createElement('video');
      video.style.display = 'block';
      const stream = await navigator.mediaDevices.getUserMedia({video: true});

      document.body.appendChild(div);
      div.appendChild(video);
      video.srcObject = stream;
      await video.play();

      // Resize the output to fit the video element.
      google.colab.output.setIframeHeight(document.documentElement.scrollHeight, true);

      // Wait for Capture to be clicked.
      await new Promise((resolve) => capture.onclick = resolve);

      const canvas = document.createElement('canvas');
      canvas.width = video.videoWidth;
      canvas.height = video.videoHeight;
      canvas.getContext('2d').drawImage(video, 0, 0);
      stream.getVideoTracks()[0].stop();
      div.remove();
      return canvas.toDataURL('image/jpeg', quality);
    }
    ''')
  display(js)
  data = eval_js('takePhoto({})'.format(quality))
  binary = b64decode(data.split(',')[1])
  with open(filename, 'wb') as f:
    f.write(binary)
  return filename
  ```

  ---

  ```py
  from IPython.display import Image
try:
  filename = take_photo()
  print('Saved to {}'.format(filename))
  
  # Show the image which was just taken.
  display(Image(filename))
except Exception as err:
  # Errors will be thrown if the user does not have a webcam or if they do not
  # grant the page permission to access it.
  print(str(err))
```

## Harici Bağlantılar

- [Overview of Colaboratory Features](https://colab.research.google.com/notebooks/basic_features_overview.ipynb)
- [External data: Drive, Sheets, and Cloud Storage](https://colab.research.google.com/notebooks/io.ipynb)
- [Styled table outputs](https://colab.research.google.com/drive/1oXkzlM0lPbDC8saNRUnkGOjpKCTiDHvM)
- [Mardown Guide](https://colab.research.google.com/notebooks/markdown_guide.ipynb)
- [Froms](https://colab.research.google.com/notebooks/forms.ipynb)
- [Magic Command](https://ipython.readthedocs.io/en/stable/interactive/magics.html)
- [Resetting VM](https://stackoverflow.com/questions/49001921/how-to-restart-virtual-machine)
- [Interacting with Shell](http://mmcdan.github.io/posts/interacting-with-the-shell-via-jupyter-notebook/)
- [Colab'ı Jupyter üzerinde Kendi PC'mizde Kullanma](https://research.google.com/colaboratory/local-runtimes.html)
- <https://dev.to/ikeyasu/how-to-use-google-colaboratory-with-local-runtime-4j1p>
