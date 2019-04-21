# Veri Kümeleri <!-- omit in toc -->

## İçerikler <!-- omit in toc -->

> `HOME` tuşu ile yukarı yönlenebilrsiniz.

- [Veri Kümeleri İndirme Araçları](#veri-k%C3%BCmeleri-i%CC%87ndirme-ara%C3%A7lar%C4%B1)
  - [axel](#axel)
  - [aria2](#aria2)
  - [wget](#wget)
    - [Wget Url'deki Tüm Resimleri İndirme](#wget-urldeki-t%C3%BCm-resimleri-i%CC%87ndirme)
- [Linkler](#linkler)
  - [Resim Veri Kümeleri](#resim-veri-k%C3%BCmeleri)
  - [Verilerdeki Etiketi Kaldırma](#verilerdeki-etiketi-kald%C4%B1rma)
  - [Karma Veri Kümeleri](#karma-veri-k%C3%BCmeleri)
- [Referanslar](#referanslar)

Yapay zeka için olmazsa olmaz olan veri kümeleri (dataset) hakkında bilgiler içermektedir.

## Veri Kümeleri İndirme Araçları

### axel

### aria2

Toplu olarak dosya indirmeyi sağlayan CLI tabanlı bir araçtır.

- [Dökümantasyon](https://aria2.github.io/manual/en/html/aria2c.html#id2)
- [İndirme sayfası](https://aria2.github.io/)

```sh
# Download from WEB:
aria2c http://example.org/mylinux.iso

# Download from 2 sources:
aria2c http://a/f.iso ftp://b/f.iso

# Download using 2 connections per host:
aria2c -x2 http://a/f.iso

# BitTorrent:
aria2c http://example.org/mylinux.torrent

# BitTorrent Magnet URI:
aria2c 'magnet:?xt=urn:btih:248D0A1CD08284299DE78D5C1ED359BB46717D8C'

# Metalink:
aria2c http://example.org/mylinux.metalink

# Download URIs found in text file:
aria2c -i uris.txt

# Download to dir
aria2c -i <file> -d <dir>
aria2c -i urls.txt -d downloads # örnek
```

### wget

Linux'un standart CLI yükleyicisidir

- Linux için kurulum gerektirmez.
- Kurulum sayfasına [buraya](https://eternallybored.org/misc/wget/) tıklayarak yönlenebilrsin.
  - [Windows x64](https://drive.google.com/open?id=1UULzjZVRpjVgDiDsVhLtWW7oggVfHFUK)

> `wget -h` ile komutlarına bakabilirsin

Temel kullanım: `wget <flag> <yol>`

| Flag | Açıklama          |
| ---- | ----------------- |
| `-i` | Dosya ile indirme |
| `-O` | Çıktı ismi        |
| `-d` | Çıktı dizini      |

#### Wget Url'deki Tüm Resimleri İndirme

```sh
wget -r -A jpg <url>
```

## Linkler

- [Kaggle](https://www.kaggle.com)
- [ABD açık veri](https://www.data.gov/)
- [COCO](http://cocodataset.org/)
- [Open Images](https://storage.googleapis.com/openimages/web/index.html)
- [Berkeley](https://bdd-data.berkeley.edu/)
  - Email : yoif4@alexbox.online
  - Password: Temp1234
- [Bosch Small Traffic Lights Dataset](https://hci.iwr.uni-heidelberg.de/node/6132/download/ce3ac63791d0a77612a4f8a857ec2a7b)
- [Türkçe Kelimeler](https://drive.google.com/open?id=1TOEqrRNmwJOa08F1lYgLz_HNL3WOppoA)
- [Deeplearning](http://deeplearning.net/datasets/)

### Resim Veri Kümeleri

- [ImageNet](http://www.image-net.org/index)
- [Getty](https://www.gettyimages.com/)
- [Usplash](https://unsplash.com/)

### Verilerdeki Etiketi Kaldırma

Açıklamalı video için [buraya](https://www.youtube.com/watch?v=zphUGNbs4Do) tıklayabilirsin.

### Karma Veri Kümeleri

- [Trafik Işıkları](https://www.kaggle.com/mbornoe/lisa-traffic-light-dataset/version/2)

## Referanslar

- [19 Ücretsiz Veri Kümesi Sitesi](https://www.springboard.com/blog/free-public-data-sets-data-science-project/)
- [17 Finans ve Ekonomik Veri Kümesi](https://gengo.ai/datasets/17-best-finance-economic-datasets-for-machine-learning/?utm_campaign=c&utm_medium=quora&utm_source=rei)
- [Step by Step TensorFlow Object Detection API Tutorial — Part 1: Selecting a Model](https://medium.com/@WuStangDan/step-by-step-tensorflow-object-detection-api-tutorial-part-1-selecting-a-model-a02b6aabe39e)
- [Step by Step TensorFlow Object Detection API Tutorial — Part 2: Converting Existing Dataset to TFRecord](https://medium.com/@WuStangDan/step-by-step-tensorflow-object-detection-api-tutorial-part-2-converting-dataset-to-tfrecord-47f24be9248d)
