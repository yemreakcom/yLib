# Python Verimli Kodlama Notlarım <!-- omit in toc -->

## İçerikler <!-- omit in toc -->

- [Değişkenlerin Değerlerini Bulma](#De%C4%9Fi%C5%9Fkenlerin-De%C4%9Ferlerini-Bulma)
- [Bağımlılıkları ve PythonPath'i Ayarlama](#Ba%C4%9F%C4%B1ml%C4%B1l%C4%B1klar%C4%B1-ve-PythonPathi-Ayarlama)
- [Medyan Alma](#Medyan-Alma)
- [Zaman Hesaplama Sorunu](#Zaman-Hesaplama-Sorunu)
- [Koşullu İç İçe For Döngüsü](#Ko%C5%9Fullu-%C4%B0%C3%A7-%C4%B0%C3%A7e-For-D%C3%B6ng%C3%BCs%C3%BC)

## Değişkenlerin Değerlerini Bulma

Değişkenin objelerini ve değerlerini öğrenmek için debug çok faydalıdır 🌟

- Debug modunda alt değişkenlere bakıp
- Kod içerisinde kullanabilirsin

## Bağımlılıkları ve PythonPath'i Ayarlama

Bu modülü ana projenizin başında `import` ederek pythonpath ayarlanmasını otomatize edebilirisiniz.

```py
import os.path as osp
import sys

def add_path(path):
    if path not in sys.path:
        sys.path.insert(0, path)

this_dir = osp.dirname(__file__)

# Add lib to PYTHONPATH
PATH = "lib" # Bu kısma oath'e alınacak dizinleri yazın
lib_path = osp.join(this_dir, PATH)
root_path = osp.join(this_dir)

add_path(lib_path)
add_path(root_path)
```

## Medyan Alma

```py
// super slow
[a, b, c].sort()[1]
```

```py
// fast
let max = Math.max(Math.max(a,b),c),
    min = Math.min(Math.min(a,b),c),
// the max and the min value cancel out because of the xor, the median remains
median = a^b^c^max^min;
```

> Hız farkı için [buraya](https://jsperf.com/fast-median-of-three) bakabilirsin

## Zaman Hesaplama Sorunu

- Keyword argument ile metod kullanıldığında zaman işlemlerinde sorun oluşmakta 🤔
- Keyword arguments fonksiyonlar tanımlandığında hesaplanır, bu yüzden time'lar birbirine eşit olabilecek kadar küçük olmakta

> [Stackoverflow'daki sorum](https://stackoverflow.com/q/56759000/9770490)

```py
from pynput import keyboard
import atexit
from time import time as get_time
from datetime import datetime

LOG_FILE = "keyLog.txt"
DELIM = "|"
TIME_LIMIT = 20 * 60

start_time = get_time()s
pressedKeys = []

def calculate_time():
    global start_time
    return get_time() - start_time

# calculate neden 0 veriyor 🤔
def save_to_file(passing_time = calculate_time()):
    global pressedKeys

    if passing_time is None:
        passing_time = calculate_time() # 0' vermiyor

    with open(LOG_FILE, "a+", encoding="utf-8") as file:
        lines = []
        lines.append(f"\n\n\n\n")
        lines.append(f"Tarih (Yıl-Ay-Gün Saat-Dakika-Saniye.): {datetime.now()}")
        lines.append(f"Geçen süre (s):                         {passing_time}")
        lines.append(f"Basılan karakter:                       {len(pressedKeys)}")
        lines.append(f"Saniye başı tuş basımı (key/s):         {len(pressedKeys) / passing_time}")
        lines.append(f"\n")
        lines.append("|".join(pressedKeys))

        file.write("\n".join(lines))

# Kapanma anında çalışacak metod
atexit.register(save_to_file)

# END ile işlemi sonlandırma
def on_press(key):
    global pressedKeys

    char = None
    try:
        char = key.char
    except AttributeError:
        char = str(key)

    pressedKeys.append(char)

    time = calculate_time()
    if time > TIME_LIMIT:
        save_to_file(time)


def on_release(key):
    print("")
    if key == keyboard.Key.end:
        # Stop listener
        return False

# Collect events until released
with keyboard.Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()

```

## Koşullu İç İçe For Döngüsü

Alttaki yapı yerine, bir sonraki yapıyı kullanarak daha **verimli ve anlaşılır** kod yazabilrisin 😊

- Döngüde fazladan kontrolü engelleriz
- Her seferin tüm değişkenlere bakmak yerine, ihtiyacımız olanlara bakarız

```py
KOSUL1 = 1
KOSUL2 = 1
KOSUL3 = 0

if KOSUL1 != 0 and "kosul1" in line:
    # yapılacaklar
    pass
elif KOSUL2 != 0 and "kosul2" in line:
    # yapılacaklar
    pass
elif KOSUL3 != 0 and "kosul3" in line:
    # yapılacaklar
    pass

```

```py
conditions = []
conditions.add(('kosul1:', KOSUL1)) if KOSUL1 != 0
conditions.add(('kosul2:', KOSUL2)) if KOSUL2 != 0
patteconditionsrns.add(('kosul3:', KOSUL3)) if KOSUL3 != 0

for condition in conditions:
    if condition[0] in line:
        # Yapılacak işlemler
        break
```
