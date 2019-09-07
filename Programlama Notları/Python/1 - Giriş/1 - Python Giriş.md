# Python Giriş <!-- omit in toc -->

## Python ile Programlamaya Hazırlanma

Python ve Javascript en popüler diller arasındadır.

- Python kodlarının uzatıları `.py` şeklindedir.
- Windows için `.pyw` uzantılı python dosyaları `start` (veya `pythonw`) komutu ile çalıştırılabilmekte
- Python komutunu ve pip ile indiklerinizi terminal üzerinden görebilmek için aşağıdakileri ortam değişkenlerine kaydetmeniz gerekmekte
  - `python.exe`'nin yolunu
  - `pip` ile indirilen terminal üzerinden derlenebilir komutlar için de _Scripts_ yolunu
  - `pip install` komutu ile indirilen script'ler scripts dizinine gider
  - Python'ı `exe` yapmak için [auto-py-exe](https://github.com/brentvollebregt/auto-py-to-exe) aracını kullanabiilirsin

> Aralarındaki kıyaslama için [buraya][python vs javascript] bakabilirisin.

## Ek Kaynaklar

- Ek başlangıç yazısı için [buraya][python türkçe başlangıç] bakabilirsin
- Kod yeteneklerini test etmek için [buraya][python hackerrank] bakabilirsin

## Yazım Kuralları

Orjinal dökümantasyon için [buraya](https://www.python.org/dev/peps/pep-0008/) bakabilirsin.

- Her python dosyasına **modül** denir
  - `import` ile dahil edilirler
  - `.` ile içlerine erişilir
- Class isimleri için **camel case** yazım kuralı geçerlidir
  - Boşluk karakteri **harfi büyüterek** temsil edilir
  - `camelCase`
- Geri kalanlar için **snake case** yazım kuralı geçerlidir
  - Boşluk karakteri `_` ile temsil edilir
  - `snake_case`
- Girintiler (`\t` karakteri) `{}` işlevi görür
- `:` karakteri ile yeni bir scope (alt alan) açılır
  - `for`, `def` gibi döngü veya metod işlemlerinde kullanırlır
- Metotlar arasında 2 satır bırakılır
- Metodların en son satırları boş olmalıdır (return için)
- Kodun en son satırı boş olmalıdır (End of File)
- _Private_ metodlar `_` ile başlar
  - `_add`, `_is_ prime`
- Özel metodlar (_"dunder"_) `__` ile başlar ve biter
  - `__init__`, `__add__`

> Daha fazla bilgi için harici linklerdeki [Should I use underscores or camel case for Python?](https://www.quora.com/Should-I-use-underscores-or-camel-case-for-Python) bağlantısına tıklayabilirsin.

## Modül Dökümantasyon Örneği

```python
'''
Xenotix Python Keylogger for Windows
====================================
Coded By: Ajin Abraham <ajin25@gmail.com>
Website: http://opensecurity.in/xenotix-python-keylogger-for-windows/
GitHub: https://github.com/ajinabraham/Xenotix-Python-Keylogger

FEATURES
========
1.STORE LOGS LOCALLY
2.SEND LOGS TO GOOGLE FORMS
3.SEND LOGS TO EMAIL
4.SEND LOGS TO FTP

MINIMUM REQUIREMENTS
===================
Python 2.7: http://www.python.org/getit/
pyHook Module: http://sourceforge.net/projects/pyhook/
pyrhoncom Module: http://sourceforge.net/projects/pywin32/
pyHook Module -
Unofficial Windows Binaries for Python Extension Packages: http://www.lfd.uci.edu/~gohlke/pythonlibs/

NOTE: YOU ARE FREE TO COPY,MODIFY,REUSE THE SOURCE CODE FOR EDUCATIONAL PURPOSE ONLY.
'''
```

## Çok Satırlı Kod Yazma

Çok satırlı kod yazmak için `\` karakterini koyup <kbd>ENTER</kbd>'a basarak alt satırdan devam edebilirsin

- Alttaki iki komut birbirine eşdeğerdir

```python
python 'train.py' \
      --train_dir="/{MODELIN_CIKTI_DIZINI_YOLU}" \
      --pipeline_config_path="/{YAPILANDIRMA_DOSYASI_YOLU}" \
      {'--logtostderr' if logdir else ''}

python 'train.py' --train_dir="/{MODELIN_CIKTI_DIZINI_YOLU}" --pipeline_config_path="/{YAPILANDIRMA_DOSYASI_YOLU}" {'--logtostderr' if logdir else ''}
```

## Dökümantasyon PyDoc

- `'''` ile fonksiyonların üstüne dökümantasyon (açıklama) eklenir
- `#` ile koda yorum eklenir

```python
def func(a):
  """ 1 Değeri döndürür """
  return 1 # Döndürme keywordu
```

> [PyDoc videosu](https://www.youtube.com/watch?v=Y6TgbyfKCNM)

## UTF-8 ve Script Bildirimleri

Her python scriptinin en üstüne alttaki metni yazın

```sh
#!/usr/bin/python
# -*- coding: utf-8 -*-
```

[python türkçe başlangıç]: https://github.com/fuatbeser/python-notlarim/blob/master/python_turkce_baslangic.ipynb
[python hackerrank]: https://www.hackerrank.com/domains/python
[python vs javascript]: https://www.educba.com/python-vs-javascript/

## 🧪 Python Terminalinde Kod Tamamlama

Pyreadline modülünü kurarak `pip install pyreadline` bu işlemi yapabilirsin.

### 🐞 AttributeError: module 'readline' has no attribute 'redisplay' Hatası

- 📋 Hata metninde en sonda verilen dosya yolunu kopyala 
  - Örnek dosya yolu: `...\Python\3.6.1\Lib\rlcompleter.py`
- Dosyayı herhangi bir metin düzenleyicisi ile aç 📑
  - VsCode kullanıyorsan alttaki komutu (**kendi dosya yolunla**) cmd'ye kopyalayabilirisin 👇 
  - `code ...\Python\3.6.1\Lib\rlcompleter.py`
- 👀 Açılan dosyada hata notunda yer alan `line 80`'e, yani 80. satıra bak 
- Oradaki satırları (`79`'dan başlıyor) alttaki gibi değiştirdikten sonra sorunsuz çalışacak 🚀

```py
...
if _readline_available:                     ## Eski kodlar ##
    if hasattr(readline, 'redisplay'):      # if _readline_available:
        readline.insert_text('\t')          #     readline.insert_text('\t')
        readline.redisplay()                #     readline.redisplay()
    return ''                               # return ''
...
```

> ⚠ Bu işlemden sonra python terminalini baştan açmayı unutma
