# Python Harici Linkler

## İçeriklr <!-- omit in toc -->

- [Python Harici Linkler](#Python-Harici-Linkler)
  - [PDF İşlemleri](#PDF-%C4%B0%C5%9Flemleri)
  - [Veri Bilimi](#Veri-Bilimi)
  - [Karma](#Karma)
  - [Lisans ve Teferruatlar](#Lisans-ve-Teferruatlar)

## PDF İşlemleri

PDF işlemleri için [pdfkit] modülü kullanılır.

- `pip install pdfkit` ile modülü indirin
- Modül için gerekli [wkhtmltopdf] aracını indirin
- İndirdiğiniz aracın içerisindeki `wkhtmltopdf.exe` dosyasının yolunu bulun
  - İleride yapılandırma ayarı için kullanılacaktır
- İşlemler sırasında python kodunun çalıştırıldığı yola dikkat edin

> Farklı bir modül için [buraya][python for pdf] bakabilirsin

```py
import pdfkit

path_wkthmltopdf = r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe'
config = pdfkit.configuration(wkhtmltopdf=path_wkthmltopdf)

pdfkit.from_file('file.html', 'out.pdf', configuration=config)
```

## Veri Bilimi

- [HTML to PDF](https://pypi.org/project/pdfkit/)

## Karma

- [String işlemleri](https://sites.google.com/site/egitimbilgileri/home/a---python---twisted---qt/03---string-islemleri)
- [Learn Python Programming](https://www.programiz.com/python-programming)
- [Python Türkçe Başlangıç](https://github.com/fuatbeser/python-notlarim/blob/master/python_turkce_baslangic.ipynb)
- [Should I use underscores or camel case for Python?](https://www.quora.com/Should-I-use-underscores-or-camel-case-for-Python)
- [Top 10 Python Libs 2017](https://tryolabs.com/blog/2017/12/19/top-10-python-libraries-of-2017/)
- [Tensorflow Object Detection API](https://buildmedia.readthedocs.org/media/pdf/tensorflow-object-detection-api-tutorial/latest/tensorflow-object-detection-api-tutorial.pdf)
- [Dosyadak Belli Satırı Değiştirme](https://stackoverflow.com/a/2081880/9770490)
- [How do I list all files of a directory](https://stackoverflow.com/questions/3207219/how-do-i-list-all-files-of-a-directory)
- [Replace single backslash with double backslash](https://stackoverflow.com/questions/17327202/python-replace-single-backslash-with-double-backslash)
- [What does `if __name__ == '__main__':` do?](https://stackoverflow.com/questions/419163/what-does-if-name-main-do)
- [Gitignore yapılandırması](https://github.com/martinohanlon/flightlight/issues/1)
- [Ekranın Video Görüntüsünü Yakalama](https://stackoverflow.com/a/51643195/9770490)
- [Putting a simple if-then-else statement on one line](https://stackoverflow.com/a/2802748/9770490)
- [Can python get the screen shot of a specific window?](https://stackoverflow.com/a/48669645/9770490)
- [Get window position & size with python](https://stackoverflow.com/a/7142360/9770490)
- [Python inactive screen capture](https://stackoverflow.com/a/52314641/9770490)
- [Computer Screen Recording using Python & OpenCV](https://www.youtube.com/watch?v=GWdrL8dt1xQ)
- [How can I code OpenCV to use GPU using Python?](https://www.quora.com/How-can-I-code-OpenCV-to-use-GPU-using-Python)
- [Google Keep to Text](https://github.com/HardFork/KeepToText)
- [Python ile QuickDraw Projesi][quick draw]
- [7 Top Python GUI Frameworks][7 top python gui frameworks]
- [Python **init**.py Dosyası][python __init__.py dosyası]
- [How to listen Key combination? - Pynput](https://github.com/moses-palmer/pynput/issues/20#issuecomment-290649632)
- [Python keylogger](https://nitratine.net/blog/post/python-keylogger/)
- [Exe'ye çevirme işlemi](https://nitratine.net/blog/post/convert-py-to-exe/)

## Lisans ve Teferruatlar

Bu yazı **MIT** lisanslıdır. Lisanslar hakkında bilgi almak için [buraya](https://choosealicense.com/licenses/) bakmanda fayda var.

- [Github](https://github.com/yedhrab)
- [Website](https://yemreak.com)
- [LinkedIn](https://www.linkedin.com/in/yemreak/)

> Yardım veya destek için [iletişime](mailto::yedhrab@gmail.com?subject=YBilgiler%20%7C%20Github) geçebilrsiniz 🤗

~ Yunus Emre Ak

[quick draw]: https://github.com/vietnguyen91/QuickDraw
[7 top python gui frameworks]: https://insights.dice.com/2017/08/07/7-top-python-gui-frameworks/
[python __init__.py dosyası]: https://stackoverflow.com/questions/448271/what-is-init-py-for
[python for pdf]: https://towardsdatascience.com/python-for-pdf-ef0fac2808b0
[wkhtmltopdf]: https://github.com/wkhtmltopdf/wkhtmltopdf/releases
[pdfkit]: https://pypi.org/project/pdfkit/
