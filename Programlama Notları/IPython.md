# IPython <!-- omit in toc -->

<!-- TODO: Google Colab notlarını buraya taşı -->

## İçerikler <!-- omit in toc -->

- [Temel Bilgiler](#temel-bilgiler)
- [Hızlı Notlar](#h%c4%b1zl%c4%b1-notlar)
  - [Google Colab için Çalışma Ortamını Yapılandırma](#google-colab-i%c3%a7in-%c3%87al%c4%b1%c5%9fma-ortam%c4%b1n%c4%b1-yap%c4%b1land%c4%b1rma)
- [Terminal İşlemleri](#terminal-%c4%b0%c5%9flemleri)
  - [Terminal İşlemleri Örneği](#terminal-%c4%b0%c5%9flemleri-%c3%96rne%c4%9fi)
  - [İşletim Sistemi Bilgileri](#%c4%b0%c5%9fletim-sistemi-bilgileri)
- [Magic Function](#magic-function)
- [Form Oluşturma İşlemleri (GUI)](#form-olu%c5%9fturma-%c4%b0%c5%9flemleri-gui)
- [Drive İşlemleri](#drive-%c4%b0%c5%9flemleri)
  - [Drive Dosyalarını Dosya Sistemine Bağlama](#drive-dosyalar%c4%b1n%c4%b1-dosya-sistemine-ba%c4%9flama)
  - [Drive Dosyalarına Erişme](#drive-dosyalar%c4%b1na-eri%c5%9fme)
- [I / O (Giriş / Çıkış) İşlemleri](#i--o-giri%c5%9f--%c3%87%c4%b1k%c4%b1%c5%9f-%c4%b0%c5%9flemleri)
  - [Dosya Upload Etme](#dosya-upload-etme)
  - [Dosya İndirme](#dosya-%c4%b0ndirme)
  - [Dizin İndirme](#dizin-%c4%b0ndirme)
    - [Dizin İndirme Arayüzü](#dizin-%c4%b0ndirme-aray%c3%bcz%c3%bc)
  - [Bilgisayar Kamerasına Erişme](#bilgisayar-kameras%c4%b1na-eri%c5%9fme)
- [Progress Bar](#progress-bar)
- [Harici Bağlantılar](#harici-ba%c4%9flant%c4%b1lar)

## Temel Bilgiler

- Tüm python özelliklerini destekler, python'a ek özellikler barındırır.
- _Jupyter Notebook_ ve _Google Colab_ gibi platformlarda kulanılır

> Bu yazı _Google Colab_'ı temel almıştır.

## Hızlı Notlar

| Operatör           | Açıklama                                         |
| ------------------ | ------------------------------------------------ |
| `!`                | Komut terminal üzerinde çalıştırılır             |
| `%`                | Tüm os üzerinde kalıcı komutlar (Magic function) |
| `#`                | Yorum satırı                                     |
| `#@`               | Form komutları                                   |
| `\<satir_atlatma>` | Satır atlatmak için kullanılır                   |
| `<func>??`         | Fonksiyonun kodlarını gösterir                   |

### Google Colab için Çalışma Ortamını Yapılandırma

**Ekran Kartını Aktif Etme:**

- Change Run Time
  - TPU
  - GPU

## Terminal İşlemleri

- Terminal komutları **unix** komutlarıdır
- Terminal işlemlerinin her biri `!` ön eki ile başlamalıdır.

| İşlem                   | Açıklama                                               |
| ----------------------- | ------------------------------------------------------ |
| `!echo {<python_kodu>}` | Python kodunun return değerini kullanma                |
| `!echo $<py_degiskeni>` | Tek kelimelik değişken (veya ortam değişkeni) kullanma |
| `!cd`                   | Sadece o satır için terminal dizini değiştirme         |
| `%cd`                   | Terminalin dizinini değiştirme                         |
| `!kill -9 -1`           | Sistemi sıfırlama                                      |

- Python değişkenlerini terminal komutunda kullanamk için:
  - `{<python_kodu>}` Arasına python komutu yazılır, return değeri kullanılır
  - `$` tek kelimelik değişkenlerin kullanımı

> `!` (terminal) komutların en ufak yazım hatası, `{}` gibi operatörler ile python komutlarının alınmasını engeller.

### Terminal İşlemleri Örneği

```py
TEMP = 'gecici'
!echo {gecici} # Python değişkenini kullanma
!echo {gecici.split('i')[0]} # Python kod parçası kullanma

!echo $PYTHONPATH # Ortam değşkenini kullanma
```

### İşletim Sistemi Bilgileri

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

## Magic Function

| Func                                | Açıklama                                        |
| ----------------------------------- | ----------------------------------------------- |
| `%%bash`                            | Kod bloğunun `bash` türünden olacağını belirtir |
| `%%timeit`                          | Blokta geçen süreyi hesaplar                    |
| `%%expect_exception AttributeError` | Hatayı fırlatır, run error engeller             |

## Form Oluşturma İşlemleri (GUI)

- Form komutları `#@` ile başlar

```py
#@title ## Model Kullanma Aracı { vertical-output: true, display-mode: "form" }

#@markdown - Markdown örneği
#@markdown     - Madde1

#@markdown - Markdown örneği
#@markdown     - Madde2

str_obj = "ssd" #@param {type:"string"}
list_obj = "train" #@param ["model_main", "train", "export_inference_graph"]
slider = 20000 #@param {type:"slider", min:100, max:20000, step:100}
bool_obj = False #@param {type:"boolean"}
```

![colab_form_ex](../res/colab_form_ex.png)

## Drive İşlemleri

### Drive Dosyalarını Dosya Sistemine Bağlama

**Normal Bağlama:**

```py
from google.colab import drive
drive.mount('/content/gdrive')
```

**Kontrollü bağlama:**

```py
if 'mount' not in globals() or not mount:
    from google.colab import drive
    drive.mount('/content/gdrive')
    mount = True
```

### Drive Dosyalarına Erişme

```py
with open('/content/gdrive/My Drive/foo.txt', 'w') as f:
  f.write('Hello Google Drive!')
!cat /content/gdrive/My\ Drive/foo.txt
```

## I / O (Giriş / Çıkış) İşlemleri

Resmi [Google Colab dökümanına][i/0 ipython] bakmanda fayda var

### Dosya Upload Etme

```py
from google.colab import files

uploaded = files.upload()

for fn in uploaded.keys():
  print('User uploaded file "{name}" with length {length} bytes'.format(
      name=fn, length=len(uploaded[fn])))
```

### Dosya İndirme

```py
from google.colab import files

with open('example.txt', 'w') as f:
  f.write('some content')

files.download('example.txt')
```

### Dizin İndirme

```py
zipped_file = "/content/file.zip"
folder_to_zip = "/content/Folder_To_Zip"
!zip -r "{zipped_file}" "{folder_to_zip}"

from google.colab import files
files.download(zipped_file)
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

## Progress Bar

```py
from IPython.display import HTML, display
import time

def progress(value, max=100):
    return HTML("""
        <progress
            value='{value}'
            max='{max}',
            style='width: 100%'
        >
            {value}
        </progress>
    """.format(value=value, max=max))

out = display(progress(0, 100), display_id=True)
for ii in range(101):
    time.sleep(0.02)
    out.update(progress(ii, 100))

```

> [Kaynak](https://stackoverflow.com/questions/46939393/how-do-i-use-updatable-displays-on-colab)

## Harici Bağlantılar

- [Overview of Colaboratory Features](https://colab.research.google.com/notebooks/basic_features_overview.ipynb)
- [External data: Drive, Sheets, and Cloud Storage](https://colab.research.google.com/notebooks/io.ipynb)
- [Styled table outputs](https://colab.research.google.com/drive/1oXkzlM0lPbDC8saNRUnkGOjpKCTiDHvM)
- [Mardown Guide](https://colab.research.google.com/notebooks/markdown_guide.ipynb)
- [Froms](https://colab.research.google.com/notebooks/forms.ipynb)
- [Magic Command](https://ipython.readthedocs.io/en/stable/interactive/magics.html)
- [Resetting VM](https://stackoverflow.com/questions/49001921/how-to-restart-virtual-machine)
- [Interacting with Shell](http://mmcdan.github.io/posts/interacting-with-the-shell-via-jupyter-notebook/)

[i/0 ipython]: https://colab.research.google.com/notebooks/io.ipynb
