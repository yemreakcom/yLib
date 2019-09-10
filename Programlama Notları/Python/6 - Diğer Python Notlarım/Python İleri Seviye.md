# Python İleri Seviye 

## Assertion (Kural Koyma)

Boolean değeri sağlanmazsa hata verir ve programı kapatır.

```python
assert <bool>, <açıklama>
```

- `<bool>` Kontrol değişkeni
  - _Örn: 0 > 5_
- `<açıklama>` Hatanın neden verildiğine dair metin
  - _Örn: Küçük bir değer girildi_

### Assertion Örnekleri

```python
def KelvinToFahrenheit(Temperature):
   assert (Temperature >= 0),"Colder than absolute zero!"
   return ((Temperature-273)*1.8)+32

print (int(KelvinToFahrenheit(505.78)))
print (KelvinToFahrenheit(-5))
```

```sh
451
Traceback (most recent call last):
  File "test.py", line 9, in <module>
    print KelvinToFahrenheit(-5)
  File "test.py", line 4, in KelvinToFahrenheit
    assert (Temperature >= 0),"Colder than absolute zero!"
AssertionError: Colder than absolute zero!
```

## Zaman İşlemlemleri (Time, Datetime)

```python
import time
from datetime import datetime

time.time() # Anlık süreyi saniye cinsinden verir
datetime.utcnow() # UTC formatında tarihi verir
datetime.now() # Yerel formatta tarihi verir (Türkiye)
datetime.now().strftime('%d-%b-%Y-%H:%M:%S') # Formatlı zaman bilgisi 26-Jun-2019-16:00:07
```

## Try / Except Yapısı

Olası hatalarda programın kapanmasını engelleyerek hata kontrolü sağlar.

```python
try:
    a = float("Ben sayı değilim")
except ValueError as err:
    print("Bu sayı değil", err)
```

## Dosya İşlemleri

Python üzerinde dosya işlemleri oldukça kolaydır ve `context manager` ile halledilir.

```python
with open(<dosya_ismi>, <erişim_modu>, encoding=<kodlama>) as file:
    # İşlemler
    pass
```

- `<dosya_ismi>` Dosya yolu veya ism
  - _Örn: "text.txt"_
- `<erişim_modu>` Okuma, yazma veya ekleme
  - _Örn: 'a', 'w', 'r', 'r+' ..._
- `<kodlama>` Dosya kodlama formatı
  - _Örn: 'utf-8'_

### Dosya Okuma

```python
file_str = ""
with open("README.md", "r", encoding="utf-8") as file:
    file_str = "".join(file.readlines())

```

```python
file_str = ""
with open("README.md", "r", encoding="utf-8") as file:
    for line in file:
        file_str += line

```

```python
with open(xml_path) as fp:
        for row, line in enumerate(fp):
            pass
```

```python
with open("README.md", "r", encoding="utf-8") as file:
    lines = list(file) # Tüm satırları liste olarak döndürür
    line = file.readline() # Tek bir satırı string olarak döndürür
    lines = file.readlines() # Tüm satırları liste olarak döndürür
```

## İşletim Sistemini Tespit Etme

```python
import platform as _platform
if _platform.system() == 'Windows':
    from. import _winmouse as _os_mouse
elif _platform.system() == 'Linux':
    from. import _nixmouse as _os_mouse
elif _platform.system() == 'Darwin':
    from. import _darwinmouse as _os_mouse
else:
    raise OSError("Unsupported platform '{}'".format(_platform.system()))
```

## Program Kapandığında İşlem Yapma (on Exit)

```python
import atexit

def exit_handler():
    print 'My application is ending!'

atexit.register(exit_handler)
```

> [Doing something before program exit](https://stackoverflow.com/a/3850271/9770490)

## Thread

Thread modülü ile satır satır ilerleyen kod yerine karma ilerleyen kodlar yazılabilir.

- `threading` modülü kullanılır
- Eş zamanlı işlemler için [multiprocessing](#paralel-i%CC%87%C5%9Flemler-multiprocessing) tercih edilir

| Class     | Açıklama                                  |
| --------- | ----------------------------------------- |
| Thread    | Sırasız olarak bir fonksiyonu çalıştırma  |
| Timer     | Belirli saniyelerde fonksiyonu çalıştırma |
| Scheduler | Bir plana göre fonksiyonu çalıştırma      |

### Thread Yapısı

```python
import threading

def ela(fname, orig_dir, save_dir):
    """
    Paremetreli bir fonksiyon
    """
    pass

dirc = "Dizin"
for d in os.listdir(dirc):
    if d.endswith(".jpg") or d.endswith(".jpeg"):
        thread = threading.Thread(target=ela, args=[d, dirc, ela_dirc])
        threads.append(thread)
        thread.start()

# Join edilmez ise, arka planda çalışır, print yazısından sonra bitebiebilir
# Join edilirse threadlerin tamamlanmasını beklemiş oluruz.
for t in threads:
    t.join()

print("Finished!")
```

### Tekrarlayıcı Yapısı

```python
from time import sleep
from threading import Thread

def tekrarla(ne, bekleme):
    while True:
        print ne
        sleep(bekleme)

if __name__ == '__main__':
    dum = Thread(target = tekrarla, args = ("dum",1))
    tis = Thread(target = tekrarla, args = ("tis",0.5))
    ah = Thread(target = tekrarla, args = ("ah",3))

    dum.start()
    tis.start()
    ah.start()
```

```sh
dum
tis
ah

tis
dumtis

tis
dumtis

tis
ah
tisdum
```

### Zamanlayıcı Yapısı (Timer)

```python
import threading


def run_check():
    print("Fonksiyon çalıştı.")
    threading.Timer(5.0, run_check).start()


run_check()
```

### Bir Plana göre Fonksiyon Çalıştırma

```python
import sched, time
s = sched.scheduler(time.time, time.sleep)
def do_something(sc):
    print "Doing stuff..."
    # do your stuff
    s.enter(60, 1, do_something, (sc,))

s.enter(60, 1, do_something, (s,))
s.run()
```

## Paralel İşlemler (Multiprocessing)

Python'da eş zamanlı işler `thread` ile yapılamaz

> Kaynak için [buraya](https://stackoverflow.com/a/7207336/9770490) bakabilirsin.

### Multiprocessing Örneği

```python
from multiprocessing import Process


def func1():
    print('func1: starting')
    for i in range(10000000):
        pass
    print('func1: finishing')


def func2():
    print ('func2: starting')
    for i in range(10000000):
        pass
    print ('func2: finishing')


if __name__ == '__main__':
    p1 = Process(target=func1)
    p1.start()
    p2 = Process(target=func2)
    p2.start()
    p1.join() # Threadi çalıştırma (gecikmesini engellemek için)
    p2.join()

# func1: starting
# func2: starting
# func2: finishing
# func1: finishing
```

## Kod Parçaları (Code Snippet)

### PYTHONPATH Ayarlama

```python
# Tek başına çalışmak isterse
if __name__ == "__main__":
    import os
    import sys
    sys.path.append(os.getcwd())
```

### Ekran Görünüsünü Alma ve Kaydetme

```python
from PIL import ImageGrab as ig

import numpy as np
import time
import cv2

# Hata ayıklama ve bilgilendirme notlarını aktif edery
DEBUG = True

# Çıktı kaydını aktif etme
KEEP = False

# Yakalanacak ekranın konum bilgileri (x0, y0, x1, y1)
CAPTURE_AREA = (80, 101, 1111, 923)

# Yakalanan ekranın gösterilme boyutu (Varsayılan için 0 yapın)
WIDTH = 0
HEIGHT = 0

# FPS sayacını tanımlama
if DEBUG:
    frame_count = 0
    last_time = time.time()

out = cv2.VideoWriter(
    'output.avi',
    cv2.VideoWriter_fourcc(*'XVID'),
    5.0,
    (CAPTURE_AREA[2] - CAPTURE_AREA[0], CAPTURE_AREA[3] - CAPTURE_AREA[1])
) if KEEP else None

while True:
    screen = ig.grab(bbox=CAPTURE_AREA)
    screen_np = np.array(screen)

    # BGR tipindeki görüntüyü RGB yapıyoruz
    screen_np_RGB = cv2.cvtColor(screen_np, cv2.COLOR_BGR2RGB)

    # Gösterilecek ekranın boyutunu ayarlama
    screen_width = WIDTH if WIDTH != 0 else CAPTURE_AREA[2] - CAPTURE_AREA[0]
    screen_height = HEIGHT if WIDTH != 0 else CAPTURE_AREA[3] - CAPTURE_AREA[1]

    # Kaydedilen ekranı uygun boyutta görüntüleme
    cv2.imshow(
        'Ekran görüntüsü',
        cv2.resize(
            screen_np_RGB,
            (
                screen_width,
                screen_height
            )
        )
    )

    # Dosyaya yazma
    out.write(screen_np_RGB) if KEEP else None

    # 'q' tuşuna basıldığında çıkma işlemi
    if cv2.waitKey(25) & 0xFF == ord('q'):
        out.release() if KEEP else None
        cv2.destroyAllWindows()
        break

    # FPS bilgilerini hesaplama ve ekrana basma
    if DEBUG:
        frame_count += 1
        if time.time() - last_time >= 1:
            print('FPS: {}'.format(frame_count))
            frame_count = 0
            last_time = time.time()

```

### Kısayol ile Ekran Alanı Seçme

```python
def draw_dimension(hotkey="ctrl_l") -> tuple:
    """Ekrandan seçilen alanın koordinatlarını verir

    Keyword Arguments:
        hotkey {string} -- Klavye kısayolu (default: {None})

    Returns:
        tuple -- Seçilen alanın koordinatları `(x0, y0, x1, y1)`
    """

    # Farenin başlangıç ve bitiş konumları
    start_position, end_position = (0, 0)

    def listen_keyboard():
        with keyboard.Listener(on_press=on_press, on_release=on_release) as keyboard_listener:
            keyboard_listener.join()

    def on_press(key):
        # Başlangıç koordinatlarını oluşturma
        if key == keyboard.Key[hotkey]:
            nonlocal start_position
            start_position = mouse.Controller().position

    def on_release(key):
        # Bitiş koordinatlarını başlangıca ekleme
        if key == keyboard.Key[hotkey]:
            nonlocal end_position
            end_position = mouse.Controller().position

            # Dinleyiciyi kapatma
            return False

    print(
        f"Seçmek istediğiniz alanın başlangıç noktasına farenizi getirin ve {hotkey} tuşuna basılı tutarak farenizi alanın bitiş noktasına götürün.")

    listen_keyboard()
    return start_position + end_position

print(draw_dimension())
```

## Python ile System Komutları Çalıştırma

```py
import subprocess, os

# İstenilen dizine girme
os.chdir(os.path.dirname(__file__))

# Orjinal komut: git descript --always
print(subprocess.check_output(["git", "describe", "--always"]).strip().decode())
```

> [Get the current git hash in a Python script](https://stackoverflow.com/a/57683700/9770490)


### 🔗 Haric Bağlantılar

- [How to Run a Shell Command from Python and Get The Output?](https://cmdlinetips.com/2014/03/how-to-run-a-shell-command-from-python-and-get-the-output/)
