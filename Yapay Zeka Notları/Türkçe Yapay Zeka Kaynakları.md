# Türkçe Yapay Zeka Kaynakları <!-- omit in toc -->

Bu bir alıntılı içeriktir. Orjinali üzerinde ufak geliştirme yapmış bulunmaktayım.

> Orjinali için [buraya](https://github.com/deeplearningturkiye/turkce-yapay-zeka-kaynaklari) ziyaret edebilirsin.

## Giriş <!-- omit in toc -->

Bu sayfada Türkiye'de derin öğrenme (deep learning) ve makine öğrenmesi (machine learning) alanında yapılan çalışmaları (blog yazısı, video ders, bilimsel makale, kodlar, verisetleri) bulabilirsiniz.

Sayfa, **Deep Learning Türkiye*- topluluğu tarafından desteklenmektedir. Derin öğrenme ve makine öğrenmesiyle ilgili **çalışmalarınız var ise*- Deep Learning Türkiye topluluğuna katılmak için [başvuru formunu](https://docs.google.com/forms/d/e/1FAIpQLScUmwLsWTl-Xj5E4Ble2jtaSlezZ_gklQNA2fylYQ7KGH4DNQ/viewform) doldurabilirsiniz.

Bizi [LinkedIn](http://linkedin.com/company/deep-learning-turkiye), [Facebook](https://www.facebook.com/deeplearningtr/) ve [Twitter](https://twitter.com/deeplearningtr)'da takip edebilir, [Medium-Türkçe](https://medium.com/deep-learning-turkiye) ve [Medium-İngilizce](https://medium.com/deep-learning-turkey) platformunda da blog yazılarımızı okuyabilir, isterseniz katkı sağlayabilirsiniz:

Sayfaya yeni kaynak eklemek için: [Katkıda bulunma rehberi](contributing.md) adresindeki talimatları izleyin.

## İçerikler  <!-- omit in toc -->

> `HOME` tuşu ile yukarı yönlenebilrsiniz

- [TEMEL KONULAR](#temel-konular)
- [ALGORİTMALAR](#algori%CC%87tmalar)
  - [Algoritmalar için Püf Noktaları](#algoritmalar-i%C3%A7in-p%C3%BCf-noktalar%C4%B1)
  - [Yapay Sinir Ağları (Artificial Neural Networks)](#yapay-sinir-a%C4%9Flar%C4%B1-artificial-neural-networks)
  - [Evrişimli Sinir Ağları (Convolutional Neural Networks)](#evri%C5%9Fimli-sinir-a%C4%9Flar%C4%B1-convolutional-neural-networks)
  - [Kapsül Ağları (Capsule Networks)](#kaps%C3%BCl-a%C4%9Flar%C4%B1-capsule-networks)
  - [Çekişmeli Üretici Ağlar (Generative Adversarial Networks)](#%C3%A7eki%C5%9Fmeli-%C3%BCretici-a%C4%9Flar-generative-adversarial-networks)
  - [Otokodlayıcılar (Autoencoders)](#otokodlay%C4%B1c%C4%B1lar-autoencoders)
- [KULLANIM ALANLARI](#kullanim-alanlari)
  - [Doğal Dil İşleme (Natural Language Processing)](#do%C4%9Fal-dil-i%CC%87%C5%9Fleme-natural-language-processing)
  - [Siber Güvenlik (Cyber Security)](#siber-g%C3%BCvenlik-cyber-security)
  - [Bilgisayarlı Görü (Computer Vision)](#bilgisayarl%C4%B1-g%C3%B6r%C3%BC-computer-vision)
- [FRAMEWORKS](#frameworks)
  - [Caffe](#caffe)
  - [Keras](#keras)
  - [TensorFlow](#tensorflow)
  - [Deeplearning4j](#deeplearning4j)
  - [FANN](#fann)
- [DONANIM VE BULUT DESTEKLERİ](#donanim-ve-bulut-destekleri%CC%87)
  - [Donanım](#donan%C4%B1m)
    - [NVIDIA Titan Serisi](#nvidia-titan-serisi)
    - [NVIDIA Jetson TX Serisi](#nvidia-jetson-tx-serisi)
    - [Intel-Movidius Neural Compute Stick](#intel-movidius-neural-compute-stick)
  - [Bulut](#bulut)
    - [Google Colaboratory](#google-colaboratory)
  - [Derin öğrenme için sistem hazırlama ve Kurulum rehberleri](#derin-%C3%B6%C4%9Frenme-i%C3%A7in-sistem-haz%C4%B1rlama-ve-kurulum-rehberleri)
    - [Ekran kartı sürücüsü, Cuda ve Cudnn Kurulumu](#ekran-kart%C4%B1-s%C3%BCr%C3%BCc%C3%BCs%C3%BC-cuda-ve-cudnn-kurulumu)
    - [Microsoft Azure Notebook](#microsoft-azure-notebook)
- [BİLİMSEL MAKALELER](#bi%CC%87li%CC%87msel-makaleler)
  - [Genel (Review/Survey)](#genel-reviewsurvey)
  - [Bilgisayarlı Görü (Computer Vision) Makaleleri](#bilgisayarl%C4%B1-g%C3%B6r%C3%BC-computer-vision-makaleleri)
  - [Türkçe Doğal Dil İşleme](#t%C3%BCrk%C3%A7e-do%C4%9Fal-dil-i%CC%87%C5%9Fleme)
  - [Ses İşleme](#ses-i%CC%87%C5%9Fleme)
  - [Tahmin](#tahmin)
  - [Siber Güvenlik](#siber-g%C3%BCvenlik)
- [VERİSETLERİ](#veri%CC%87setleri%CC%87)
- [VİDEO DERSLER](#vi%CC%87deo-dersler)
  - [Genel](#genel)
  - [Yapay Sinir Ağları](#yapay-sinir-a%C4%9Flar%C4%B1)
  - [Yapay Zeka](#yapay-zeka)
  - [Bilgisayarlı Görü](#bilgisayarl%C4%B1-g%C3%B6r%C3%BC)
  - [IoT](#iot)
- [Framework](#framework)
  - [Keras Framework](#keras-framework)
  - [Julia](#julia)
  - [MatConvNet](#matconvnet)
- [Sunumlar](#sunumlar)
- [Github](#github)
  - [Doğal Dil İşleme](#do%C4%9Fal-dil-i%CC%87%C5%9Fleme)
  - [Arama Algoritmaları](#arama-algoritmalar%C4%B1)
  - [Github Bilgisayarlı Görü](#github-bilgisayarl%C4%B1-g%C3%B6r%C3%BC)
  - [Sinir Ağları](#sinir-a%C4%9Flar%C4%B1)
- [Bloglar](#bloglar)
- [Kitaplar](#kitaplar)
- [Yarışmalar](#yar%C4%B1%C5%9Fmalar)
- [Mobil Uygulamalar](#mobil-uygulamalar)
- [Düzenleyen](#d%C3%BCzenleyen)

## TEMEL KONULAR

- [Temel: Şu Kara Kutuyu Açalım: Yapay Sinir Ağları](https://medium.com/deep-learning-turkiye/%C5%9Fu-kara-kutuyu-a%C3%A7alim-yapay-sinir-a%C4%9Flar%C4%B1-7b65c6a5264a) (Merve Ayyüce Kızrak)
- [Motivasyon: Yapay Zeka ve Derin Öğrenmenin Hikayesi](https://medium.com/deep-learning-turkiye/motivasyon-yapay-zeka-ve-derin-%C3%B6%C4%9Frenme-48d09355388d) (Merve Ayyüce Kızrak)
- [Derin Öğrenme Başlangıç Seti - Donanım Ve Yazılım](http://www.ardamavi.com/2017/10/derin-ogrenme-baslangic-seti.html) (Arda Mavi)
- [Yapay Zeka - Düşünen Ve Üreten Makinelerin Doğuşu](http://www.ardamavi.com/2017/09/yapay-zekanin-gelecegi.html) (Arda Mavi)
- [İnsanda Ve Makinede Öğrenme](http://www.ardamavi.com/2017/07/insanda-ve-makinede-ogrenme.html) (Arda Mavi)
- [Bilgisayarda Görüntü Ve Sayı Dizileri](http://www.ardamavi.com/2017/07/bilgisyarda-goruntu-ve-sayi-dizileri.html) (Arda Mavi)
- [Derin Öğrenme 1](http://derindelimavi.blogspot.com.tr/2015/10/derin-ogrenme-1.html) (Birol Kuyumcu)
- [Derin Öğrenme 2](http://derindelimavi.blogspot.com.tr/2015/11/derin-ogrenme-2.html) (Birol Kuyumcu)
- [Derin Öğrenme 3](http://derindelimavi.blogspot.com.tr/2015/11/derin-ogrenme-3.html) (Birol Kuyumcu)
- [Derin Öğrenme , Yapay Zeka ve Bilgisayar Bilim](http://sayilarvekuramlar.blogspot.com/2015/12/bilgisayar-bilim-yapay-zeka.html) (Burak Bayramlı)
- [Makine Öğrenimi Eğlencelidir](https://medium.com/t%C3%BCrkiye/makine-%C3%B6%C4%9Frenimi-e%C4%9Flencelidir-2ad33ae37bea)(Özgür Şahin)
- [Makine Öğrenimi Eğlencelidir 2](https://medium.com/bili%C5%9Fim-hareketi/makine-%C3%B6%C4%9Frenimi-e%C4%9Flencelidir-2-k%C4%B1s%C4%B1m-6b464cbdf40c)(Atakan Yenel)
- [Makine Öğrenmesi Nedir?](https://medium.com/türkiye/makine-öğrenmesi-nedir-20dee450b56e) (Halil İbrahim Şafak)
- [Makine Öğrenmesi 101](https://veribilimcisi.com/makine-ogrenmesi/) (Seray Beşer)
- [Derin Öğrenme 101](https://veribilimcisi.com/derin-ogrenme-101/) (Seray Beşer)
- [Makine Öğrenmesi Matematiği](https://veribilimcisi.com/makine-ogrenmesi-matematigi/) (Seray Beşer)
- [Veri Bilimcisi Olma Rehberi](http://bilisim.io/2017/09/28/veri-bilimcisi-olma-rehberi/) (Şefik İlkin Serengil)
- [Python: Sıfırdan Uzmanlığa Programlama](https://www.udemy.com/python-sfrdan-uzmanlga-programlama-1/) (Kaan Can Yılmaz)
- [Data Science ve Python](https://www.udemy.com/data-science-sfrdan-uzmanlga-veri-bilimi-2/) (Kaan Can Yılmaz)
- [Data Visualization](https://www.udemy.com/data-visualization-adan-zye-veri-gorsellestirme-3/) (Kaan Can Yılmaz)
- [Makine Öğrenmesi](https://www.udemy.com/machine-learning-ve-python-adan-zye-makine-ogrenmesi-4/) (Kaan Can Yılmaz)

## ALGORİTMALAR

### Algoritmalar için Püf Noktaları

- [Derin Öğrenme Uygulamalarında En Sık kullanılan Hiper-parametreler](https://medium.com/deep-learning-turkiye/derin-ogrenme-uygulamalarinda-en-sik-kullanilan-hiper-parametreler-ece8e9125c4) (Necmettin Çarkacı)
- [Derin Öğrenme Uygulamalarında Başarım İyileştirme (Regularization) Yöntemleri](https://medium.com/@necmettin.carkaci/derin-öğrenme-uygulamalarında-başarım-iyileştirme-yöntemleri-regularization-fb521e64c30f) (Necmettin Çarkacı)

### Yapay Sinir Ağları (Artificial Neural Networks)

- [Yapay Sinir Ağlarına Giriş](http://www.ardamavi.com/2017/07/sinir-aglari.html) (Arda Mavi)
- [Yapay Sinir Ağları](http://www.akanesen.com/2017/09/yapay-sinir-aglar.html) (Birol Akan Esen)
- [Yapay Sinir Ağları Temel Kavramlar: Perceptron, Skor fonksiyonu ve Hata hesaplaması(loss function)](https://www.linkedin.com/pulse/derin-öğrenme-uygulamalarında-temel-kavramlar-skor-ve-çarkacı/) (Necmettin Çarkacı)
- [Nöral Ağlar: Geçmiş Hatalardan Dersler Çıkarmak](http://bilisim.io/2017/07/08/noral-aglar-gecmis-hatalardan-dersler-cikarmak/) (Şefik İlkin Serengil)
- [Nöral Ağlar Öğrenme Algoritması Anlama Kılavuzu: Geri Yayılım Algoritması](http://bilisim.io/2017/07/11/noral-aglar-ogrenme-algoritmasi-anlama-kilavuzu-geri-yayilim-algoritmasi/) (Şefik İlkin Serengil)
- [Yapay Sinir Ağları (Neural Network)](https://veribilimcisi.com/2017/08/13/yapay-sinir-aglari/) (Seray Beşer)
- [Algılayıcı (Perceptron (P))](https://veribilimcisi.com/2017/08/13/yapay-sinir-aglari/#PERCEPTRON%20-%20ALGILAYICI) (Seray Beşer)
- [İleri Beslemeli (Feed Forward (FF))](https://veribilimcisi.com/2017/09/26/ileri-beslemeli-sinir-aglari-feedforward-neural-network/) (Seray Beşer)
- [Tekrarlayan Sinir Ağı (Recurrent Neural Network (RNN))](https://veribilimcisi.com/2017/09/26/tekrarlayan-sinir-aglari-recurrent-neural-network/) (Seray Beşer)
- [Derin İleri Beslemeli (Deep Feed Forward (DFF))](https://veribilimcisi.com/2017/09/26/derin-ileri-beslemeli-sinir-aglari-deep-feedforward-network/) (Seray Beşer)
- [Uzun / Kısa Süreli Bellek (Long / Short Term Memory (LSTM))](https://veribilimcisi.com/2017/09/26/uzun-kisa-sureli-bellek-long-short-term-memory/) (Seray Beşer)
- [Yarıçapsal Temelli Ağ (Radial Basis Network (RBF))](https://veribilimcisi.com/2017/09/26/yaricapsal-temelli-ag-radial-basis-network/) (Seray Beşer)
- [Kapılı Tekrarlayan Hücre (Gated Recurrent Unit (GRU))](https://veribilimcisi.com/2017/09/26/kapili-tekrarlayan-hucre-gated-recurrent-unit/) (Seray Beşer)
- [Otomatik Kodlayıcı (Auto Encoder (AE))](https://veribilimcisi.com/2018/06/04/otomatik-kodlayici-auto-encoder/) (Seray Beşer)
- [Varyasyonel Otomatik Kodlayıcı (Variational AE (VAE))](https://veribilimcisi.com/2018/06/04/varyasyonel-otomatik-kodlayici-variational-autoencoder/) (Seray Beşer)
- [Gürültü Giderici Otomatik Kodlayıcı (Denoising AE (DAE))](https://veribilimcisi.com/2018/06/04/gurultu-giderici-otomatik-kodlayici-denoising-autoencoder/) (Seray Beşer)
- [Seyrek Otomatik Kodlayıcı (Sparse AE (SAE))](https://veribilimcisi.com/2018/06/04/seyrek-otomatik-kodlayici-sparse-autoencoder/) (Seray Beşer)
- [Markov Zinciri (Markov Chain (MC))](https://veribilimcisi.com/2017/09/26/markov-zinciri-markov-chain/) (Seray Beşer)
- [Hopfield Ağı (Hopfield Network (HN))](https://veribilimcisi.com/2017/09/26/hopfield-agi-hopfield-network/) (Seray Beşer)
- [Boltzmann Makinesi (Boltzmann Machine (BM))](https://veribilimcisi.com/2017/09/26/boltzmann-makinesi-boltzmann-machine/) (Seray Beşer)
- [Kısıtlı Boltzmann Makinesi (Restricted BM (RBM))](https://veribilimcisi.com/2017/09/26/kisitli-boltzmann-makinesi-restricted-boltzmann-machine-rbm/) (Seray Beşer)
- [Derin İnanç Ağı (Deep Belief Network (DBN))](https://veribilimcisi.com/2017/09/26/derin-inanc-agi-deep-belief-network/) (Seray Beşer)
- [Konvolüsyonel Sinir Ağı (Convolutional Neural Network (CNN))](https://veribilimcisi.com/2017/09/26/konvolusyonel-sinir-agi-convolutional-neural-network/) (Seray Beşer)

### Evrişimli Sinir Ağları (Convolutional Neural Networks)

- [Derin Bir Karşılaştırma: Inception ve Res-Net Verisyonları](http://www.ayyucekizrak.com/blogdetay/yapay-zeka-ve-derin-ogrenme-yazi-dizisi/derin-bir-karsilastirma-inception-ve-res-net-versiyonlari) (Bağlantı güncellenecek!) (Merve Ayyüce Kızrak)
- [Derine Daha Derine: Evrişimli Sinir Ağları](https://medium.com/deep-learning-turkiye/deri%CC%87ne-daha-deri%CC%87ne-evri%C5%9Fimli-sinir-a%C4%9Flar%C4%B1-2813a2c8b2a9) (Merve Ayyüce Kızrak)
- [Evrişimli Sinir Ağlarına Giriş](http://www.ardamavi.com/2017/07/convolutional-networks.html) (Arda Mavi)
- [Tensorflow Tabanlı Keras ile MNIST Veriseti Üzerinde Çalışma](http://erdoganb.com/2017/04/kerastensorflow-ile-rakamlari-tanima-mnist-dataset/) (Erdoğan Bavaş)
- [Konvolüsyonel Nöral Ağlara Kısa Bir Giriş](http://bilisim.io/2018/01/07/konvolusyonel-noral-aglara-kisa-bir-giris/) (Şefik İlkin Serengil)
- [Öğrenim Transferi: Keras ile Inception V3 kullanımı](http://bilisim.io/2018/01/22/ogrenim-transferi-keras-ile-inception-v3-kullanimi/) (Şefik İlkin Serengil)

### Kapsül Ağları (Capsule Networks)

- [Yapay Zekada Büyük Yenilik: Kapsül Ağları (Capsule Networks)](https://medium.com/deep-learning-turkiye/yapay-zekan%C4%B1n-yeni-ve-%C3%A7ekici-mimarisi-kaps%C3%BCl-a%C4%9F%C4%B1na-uygulamal%C4%B1-bir-bak%C4%B1%C5%9F-ef7310e3d847) (Merve Ayyüce Kızrak)

### Çekişmeli Üretici Ağlar (Generative Adversarial Networks)

- [Generative Adversarial Networks — GAN nedir ? ( Türkçe )](https://medium.com/@mubuyuk51/generative-adversarial-networks-gan-nedir-t%C3%BCrk%C3%A7e-5819fe9c1fa7) (Muhammed Buyukkınacı)

### Otokodlayıcılar (Autoencoders)

- [Yapay Nöral Ağlar: Autoencoder'lar](https://www.farukeroglu.org/2018/06/yapay-noral-aglar-autoencoder.html) (Faruk Eroğlu)
- [Otomatik Kodlayıcı (Autoencoder)](https://veribilimcisi.com/2018/06/04/otomatik-kodlayici-auto-encoder/) (Seray Beşer)
- [Gürültü Giderici Otomatik Kodlayıcı (Denoising Autoencoder)](https://veribilimcisi.com/2018/06/04/gurultu-giderici-otomatik-kodlayici-denoising-autoencoder/) (Seray Beşer)
- [Seyrek Otomatik Kodlayıcı (Sparse Autoencoder)](https://veribilimcisi.com/2018/06/04/seyrek-otomatik-kodlayici-sparse-autoencoder/) (Seray Beşer)
- [Varyasyonel Otomatik Kodlayıcı (Variational Autoencoder)](https://veribilimcisi.com/2018/06/04/varyasyonel-otomatik-kodlayici-variational-autoencoder/) (Seray Beşer)

## KULLANIM ALANLARI

### Doğal Dil İşleme (Natural Language Processing)

- [Keras ile Duygu Analizi](http://derindelimavi.blogspot.com.tr/2017/10/keras-ile-duygu-analizi.html) (Birol Kuyumcu)
- [Türkçe Metin İşlemede İlk Adımlar](http://www.veridefteri.com/2017/11/20/turkce-metin-islemede-ilk-adimlar/) (İlker Birbil)

### Siber Güvenlik (Cyber Security)

- [Derin Ögrenme Teknolojileri Kullanarak Dağıtık Hizmet Dışı Bırakma Saldırılarının Tespit Edilmesi
](https://ocatak.github.io/papers/poster_foc.pdf) (Ferhat Özgür Çatak, Ahmet Fatih Mustaçoglu)

### Bilgisayarlı Görü (Computer Vision)

- [Optik Karakter Tanıma, Yazı Tanıma (Optical Character Recognition -OCR-)](https://burakbayramli.github.io/dersblog/algs/ocr/optik_karakter_tanima_yazi_tanima__optical_character_recognition_ocr_.html) (Burak Bayramlı)
- [YOLO: Gerçek Zamanlı Nesne Tespiti Kütüphanesi (Darknet) Kurulumu](http://blog.yavuzz.com/post/gercek-zamanli-nesne-tespiti-kutuphanesi-darknet-kurulumu) (Yavuz Kömeçoğlu)
- [YOLO'da Kendi Özel Kişi yada Nesnemizin Algılanmasını Nasıl Sağlarız?](http://blog.yavuzz.com/post/yolo-da-kendi-ozel-nesnemizin-algilanmasini-nasil-saglariz) (Yavuz Kömeçoğlu)
- [Görüntü Tanıyan Mobil Uygulama Nasıl Geliştirilir?](https://medium.com/deep-learning-turkiye/g%C3%B6r%C3%BCnt%C3%BC-tan%C4%B1yan-mobil-uygulama-nas%C4%B1l-geli%C5%9Ftirilir-33760f7d827) (Özgür Şahin)
- [10 Dakikada Görüntü Sınıflandıran Mobil Uygulama Geliştirin](https://medium.com/nsistanbul/10-dakikada-g%C3%B6r%C3%BCnt%C3%BC-s%C4%B1n%C4%B1fland%C4%B1ran-mobil-uygulama-geli%C5%9Ftirin-7567371839b0) (Özgür Şahin)

## FRAMEWORKS

### Caffe

- [Caffe Kılavuzu - Tüm detaylarıyla Caffe ile çalışma rehberi](https://www.slideshare.net/bluekid/caffe-klavuzu) (Birol Kuyumcu)
- [Pratik Caffe Kullanımı](https://www.slideshare.net/bluekid/pratik-caffe) (Birol Kuyumcu)
- [Caffe Fine Tuning: Caffe'yi Kendi Verisetiniz ile Kullanma](http://blog.yavuzz.com/post/caffe-fine-tuning) (Yavuz Kömeçoğlu)
- [Windows İşletim Sistemi için Caffe Kurulumu](http://mesutpiskin.com/blog/windows-icin-caffe-kurulumu.html) (Mesut Pişkin)

### Keras

- [Keras'a Giriş-1](http://derindelimavi.blogspot.com.tr/2017/01/keras-giris-1.html) (Birol Kuyumcu)
- [Keras'a Giriş-2 ( LSTM )](http://derindelimavi.blogspot.com.tr/2017/03/kerasa-giris-2-lstm.html) (Birol Kuyumcu)
- [Keras Türkçe Dokümantasyon](https://github.com/kemalcanbora/keras_turkish_doc) (Kemalcan Bora)
- [Keras Kurulumu](http://ibrahimdelibasoglu.blogspot.com.tr/2017/08/python-tensorflow-ile-keras-derin.html) (İbrahim Delibaşoğlu)
- [Keras ile Sonar Verisi Sınıflandırma](http://ibrahimdelibasoglu.blogspot.com.tr/2017/09/keras-ile-derin-ogrenmeye-giris-snflama.html) (İbrahim Delibaşoğlu)

### TensorFlow

- [TensorFlow ile Derin Öğrenmeye Giriş](https://emredurukn.github.io/2016/11/02/tensorflow-ile-derin-ogrenmeye-giris.html) (Emre Durukan)
- [Tensorflow'u Anlamak](https://mcemilg.github.io/general/2017/11/23/tensorflow/) (M.Cemil Güney)
- [Tensorflow Türkçe Eğitim Dökümanları](https://github.com/Aelvangunduz/tensorflow_tutorials) (Ayse Elvan Aydemir)
- [Tensorflow 101](https://veribilimcisi.com/tensorflow-101/) (Seray Beşer)
- [PyTorch ile Derin Öğrenmeye Giriş: Kurulum](https://medium.com/@ozgungenc/pytorch-ile-derin-%C3%B6%C4%9Frenmeye-giri%C5%9F-kurulum-2194a06ce0c) (Özgün Genç)

### Deeplearning4j

- [Deeplearning4j ile Derin Öğrenmeye Giriş](http://mesutpiskin.com/blog/deeplearning4j-ile-derin-ogrenmeye-giris.html) (Mesut Pişkin)
- [Deeplearning4j Mimarisi](http://mesutpiskin.com/blog/deeplearning4j-mimarisi-ve-kurulum.html) (Mesut Pişkin)
- [Deeplearning4j ile Yapay Sinir Ağları](http://mesutpiskin.com/blog/yapay-sinir-agi-derin-ogrenme.html) (Mesut Pişkin)

### FANN

- [FANN Tool Kılavuzu](https://www.slideshare.net/bluekid/fann-tool-klavuzu) (Birol Kuyumcu)

## DONANIM VE BULUT DESTEKLERİ

### Donanım

#### NVIDIA Titan Serisi

#### NVIDIA Jetson TX Serisi

#### Intel-Movidius Neural Compute Stick

- [INTEL-Movidius Neural Compute Stick Nedir ve Nasıl Kullanılır](https://medium.com/deep-learning-turkiye/intel-movidius-neural-compute-stick-nedir-ve-nas%C4%B1l-kullan%C4%B1l%C4%B1r-85fc9af6dc26) (Merve Ayyüce Kızrak)
- [Raspberry Pi 3 üzerinde Intel Movidius Neural Compute Stick ile Derin Öğrenme Uygulamaları Çalıştırma](http://blog.yavuzz.com/post/raspberry-pi-3-uzerinde-intel-movidius-neural-compute-stick-ile-derin-ogrenme-uygulamalari-calistirma) (Yavuz Kömeçoğlu)

### Bulut

#### Google  Colaboratory

- [Google Colab ile Ücretsiz GPU Kullanımı](https://medium.com/deep-learning-turkiye/google-colab-ile-%C3%BCcretsiz-gpu-kullan%C4%B1m%C4%B1-30fdb7dd822e) (Fuat)

### Derin öğrenme için sistem hazırlama ve Kurulum rehberleri

#### Ekran kartı sürücüsü, Cuda ve Cudnn Kurulumu

- [NVIDIA GPU Sürücüsü, CUDA ve cudNN Kurulum Rehberi](https://github.com/earcz/NVIDIA-GPU-Surucusu-ve-CUDA-Yukleme) (Ender Ayhan Rencüzoğulları)

#### Microsoft Azure Notebook

## BİLİMSEL MAKALELER

### Genel (Review/Survey)

- [Derin Öğrenme Yöntemleri ve Uygulamaları Hakkında Bir İnceleme](http://dergipark.gov.tr/download/article-file/394923) (Abdulkadir Şeker, Banu Diri, Hasan Hüseyin Balık )

### Bilgisayarlı Görü (Computer Vision) Makaleleri

- [MARVEL: A Large-Scale Image Dataset for Maritime Vessels](https://link.springer.com/chapter/10.1007/978-3-319-54193-8_11) (Erhan Gündoğdu, Berkan Solmaz, Veysel Yücesoy, Aykut Koç)
- [Face Recognition Classifier Based on Dimension Reduction in Deep Learning Properties](http://ieeexplore.ieee.org/document/7960368/) (Ahmet Bilgiç, Onur Can Kurban, Tülay Yıldırım)
- [Signature recognition application based on deep learning](http://ieeexplore.ieee.org/abstract/document/7960454/) (Nurullah Çalık, Onur Can Kurban, Ali Rıza Yılmaz, Lütfiye Durak Ata, Tülay Yıldırım)
- [On identifying leaves: A comparison of CNN with classical ML methods](http://ieeexplore.ieee.org/abstract/document/7960257/) (Mohamed Abbas Hedjazi, Ikram Kourbane, Yakup Genç)
- [On identifying leaves: A comparison of CNN with classical ML methods](https://web.cs.hacettepe.edu.tr/~aykut/papers/ieee-tmm17.pdf) (Çağdaş Bak, Aysun Koçak, Erkut Erdem, Aykut Erdem)
- [Exploiting Convolution Filter Patterns for Transfer Learning](https://arxiv.org/abs/1708.06973) (Mehmet Aygün, Yusuf Aytar, Hazım Kemal Ekenel)
- [The Unconstrained Ear Recognition Challenge](https://arxiv.org/abs/1708.06997) (Žiga Emeršič, Dejan Štepec, Vitomir Štruc, Peter Peer, Anjith George, Adil Ahmad, Elshibani Omar, Terrance E. Boult, Reza Safdari, Yuxiang Zhou, Stefanos Zafeiriou, Dogucan Yaman, Fevziye I. Eyiokur, Hazim K. Ekenel)
- [Combining LiDAR Space Clustering and Convolutional Neural Networks for Pedestrian Detection](https://arxiv.org/abs/1710.06160) (Damien Matti, Hazım Kemal Ekenel, Jean-Philippe Thiran)
- [Combining Multiple Views for Visual Speech Recognition](http://avsp2017.loria.fr/wp-content/uploads/2017/07/AVSP2017_paper_25.pdf) (Marina Zimmermann, Mostafa Mehdipour Ghazi, Hazım Kemal Ekenel, Jean-Philippe Thiran)
- [A Computer Vision System to Localize and Classify Wastes on the Streets](https://infoscience.epfl.ch/record/231365/files/A-Computer-Vision-System%20to-Localize-and-Classify-Wastes-on-the-Streets.pdf) (Mohammad Saeed Rad,Andreas von Kaenel, Andre Droux, Francois
Tieche, Nabil Ouerhani, Hazım Kemal Ekenel, Jean-Philippe Thiran)

### Türkçe Doğal Dil İşleme

- [Linguistic Features in Turkish Word Representations](http://ieeexplore.ieee.org/abstract/document/7960223/) (Onur Güngör, Eray Yıldız)
- [Morphological Embeddings for Named Entity Recognition in Morphologically Rich Languages](https://arxiv.org/abs/1706.00506) (Onur Güngör, Eray Yıldız, Suzan Üsküdarlı, Tunga Güngör)
- [Zemberek Parser for python3.x](https://github.com/kemalcanbora/zemberek_parser)  (Kemalcan Bora)
- [A Morphology-Aware Network for Morphological Disambiguation](https://arxiv.org/pdf/1702.03654.pdf) (Eray Yıldız, Çağlar Tırkaz, H. Bahadır Şahin, Mustafa Tolga Eren, Ozan Sönmez)
- [Automatically Annotated Turkish Corpus for Named Entity Recognition and Text Categorization using Large-Scale Gazetteers](https://arxiv.org/pdf/1702.02363.pdf) (H. Bahadır Şahin, Çağlar Tırkaz, Eray Yıldız, Mustafa Tolga Eren, Ozan Sönmez)
- [Türkçe ve Doğal Dil İşleme](http://dergipark.gov.tr/download/article-file/207207) (Kemal Oflazer)
- [Turkish and its challenges for language processing](https://link.springer.com/article/10.1007/s10579-014-9267-2) (Kemal Oflazer)
- [Zemberek Docker REST Sunucusu](https://github.com/cbilgili/zemberek-nlp-server) (Canbey Bilgili)

### Ses İşleme

- [A musical information retrieval system for Classical Turkish Music makams
](http://journals.sagepub.com/doi/abs/10.1177/0037549717708615?journalCode=simb) (Merve Ayyüce Kızrak, Bülent Bolat)

### Tahmin

- [Intraday prediction of Borsa Istanbul using convolutional neural networks and feature correlations](http://www.sciencedirect.com/science/article/pii/S0950705117304252) (Hakan Gündüz, Yusuf Yaslan, Zehra Çataltepe)

### Siber Güvenlik

- [Derin Ögrenme Teknolojileri Kullanarak Dağıtık Hizmet Dışı Bırakma Saldırılarının Tespit Edilmesi
](https://ocatak.github.io/papers/poster_foc.pdf) (Ferhat Özgür Çatak, Ahmet Fatih Mustaçoglu)
- [CPP-ELM: Cryptographically Privacy-Preserving Extreme Learning Machine for Cloud Systems](http://www.atlantis-press.com/journals/ijcis/25885040) (Ferhat Özgür Çatak, Ahmet Fatih Mustaçoglu)

## VERİSETLERİ

- [İşaret Dili İle Rakamlar Veriseti](https://github.com/ardamavi/Sign-Language-Digits-Dataset) (Türkiye Ankara Ayrancı Anadolu Lisesi - Zeynep Dikle & Arda Mavi)
- [Marvel: A Large-Scale Image Dataset for Maritime Vessels](https://github.com/avaapm/marveldataset2016) (Erhan Gündoğdu, Berkan Solmaz, Veysel Yücesoy, Aykut Koç)
- [Yıldız Teknik Üniversitesi Kemik Doğal Dil İşleme Grubu Verisetleri](http://www.kemik.yildiz.edu.tr/?id=28) (YTÜ Kemik Doğal Dil İşleme Grubu)
- [TTC-3600: A new benchmark dataset for Turkish text categorization](https://github.com/denopas/TTC-3600) (Deniz Kılınç, Akın Özçift, Fatma Bozyigit, Pelin Yıldırım, Fatih Yücalar, Emin Borandag)
- [Turkish Sentiment Dataset](http://www.baskent.edu.tr/~msert/research/datasets/SentimentDatasetTR.html) (Ahmet Hayran, Mustafa Sert)
- [English/Turkish Wikipedia Named-Entity Recognition and Text Categorization Dataset](https://data.mendeley.com/datasets/cdcztymf4k/1) (H. Bahadır Şahin, Çağlar Tırkaz, Eray Yıldız, Mustafa Tolga Eren, Ozan Sönmez)
- [Turkish NLP Dataset](https://tscorpus.com)(Sezer, B., Sezer, T. 2013. TS Corpus: Herkes İçin Türkçe Derlem. Proceedings 27th National Linguistics Conference. May, 3-4 Mayıs 2013. Antalya, Kemer: Hacettepe University, English Linguistics Department. pp: 217-225)
- [1B Tokens Turkish Corpus and Turkish word vectors and analogical reasoning task pairs](https://github.com/onurgu/linguistic-features-in-turkish-word-representations/releases)(Onur Gungor, Eray Yildiz, "Linguistic Features in Turkish Word Representations", SIU, Antalya, 2017)
- [Turkish Language Resources compiled by Deniz Yüret](http://www.denizyuret.com/2006/11/turkish-resources.html)
- [METU-Sabanci Turkish treebank](https://web.itu.edu.tr/gulsenc/treebanks.html)
- [SemEval-2016 ABSA Telecom Tweets-Turkish: Test Data-Phase A (Subtask 1)](http://metashare.ilsp.gr:8080/repository/browse/semeval-2016-absa-telecom-tweets-turkish-test-data-phase-a-subtask-1/5343e408ba0811e5ab4f842b2b6a04d71f53ece5fa7a4dd286e99e539ac3e27f/)
- [SemEval-2016 ABSA Restaurant Reviews-Turkish: Train Data (Subtask 1)](http://metashare.ilsp.gr:8080/repository/browse/semeval-2016-absa-restaurant-reviews-turkish-train-data-subtask-1/ff5dad70676311e5bf9c842b2b6a04d71fa7fa3ba4504a228dafe0c24560585b/)
- [Turkish Paraphrase Corpus (TuPC)](https://osf.io/wp83a/)(Eyecioglu, Asli, and Bill Keller. "ASOBEK at SemEval-2016 Task 1: Sentence Representation with Character N-gram Embeddings for Semantic Textual Similarity." SemEval@ NAACL-HLT. 2016.)
- [Turkish WordNet (KeNet)](http://haydut.isikun.edu.tr/kenet.html)(Sasmaz, E., R. Ehsani, O. T. Yildiz, "Hypernym extraction from Wikipedia and Wiktionary", SIU, Antalya, Turkey, 2017)
- [Parkinson Speech Dataset with Multiple Types of Sound Recordings Data Set](https://archive.ics.uci.edu/ml/datasets/Parkinson%2BSpeech%2BDataset%2Bwith%2B%2BMultiple%2BTypes%2Bof%2BSound%2BRecordings#)(Erdogdu Sakar, B., Isenkul, M., Sakar, C.O., Sertbas, A., Gurgen, F., Delil, S., Apaydin, H., Kursun, O., 'Collection and Analysis of a Parkinson Speech Dataset with Multiple Types of Sound Recordings', IEEE Journal of Biomedical and Health Informatics, vol. 17(4), pp. 828-834, 2013.)
- [Turkiye Student Evaluation Data Set](http://archive.ics.uci.edu/ml/datasets/turkiye+student+evaluation#)(Gunduz, G. & Fokoue, E. (2013).)
- [Combined Cycle Power Plant Data Set](http://archive.ics.uci.edu/ml/datasets/combined+cycle+power+plant)(Pınar Tüfekci, Prediction of full load electrical power output of a base load operated combined cycle power plant using machine learning methods, International Journal of Electrical Power & Energy Systems, Volume 60, September 2014, Pages 126-140, ISSN 0142-06)
- [Dermatology Data Set](http://archive.ics.uci.edu/ml/datasets/dermatology)(G. Demiroz, H. A. Govenir, and N. Ilter, "Learning Differential Diagnosis of Eryhemato-Squamous Diseases using Voting Feature Intervals", Aritificial Intelligence in Medicine, 1998-2004)
- [Arrhythmia Data Set](https://archive.ics.uci.edu/ml/datasets/arrhythmia)(H. Altay Guvenir, Burak Acar, Gulsen Demiroz, Ayhan Cekin "A Supervised Machine Learning Algorithm for Arrhythmia Analysis." Proceedings of the Computers in Cardiology Conference, Lund, Sweden, 1997.)
- [Artificial Characters Data Set](https://archive.ics.uci.edu/ml/datasets/Artificial+Characters)( H. Altay Guvenir et al, 1992)
- [Turkish Natural Language Processing Toolkit- embedded in Zemberek](http://www.aliok.com.tr/projects/2014-10-02-trnltk.html)
- [235.000 Turkish Product Reviews](https://github.com/fthbrmnby/turkish-text-data)
- [ODP TR-30 Turkish Search Result Clustering Dataset](https://github.com/faraday/odp-tr30) (Ç. Çallı, 2010)
- [Modacruz ve Zara'da bulunan kıyafetlerin dataseti](https://github.com/kemalcanbora/flora_fashion_scraping) (Kemalcan Bora)

## VİDEO DERSLER

### Genel

- [Ankara Deep Learning - Derin Öğrenme Etkinliği 1](https://youtu.be/K74rzKSsGs8) (Ferhat Kurt) {96 dakika}
- [ODTÜ Görüntü Analizi Uygulama ve Araştırma Merkezi (OGAM) Yaz Okulu 2016](http://obayo.ogam.metu.edu.tr/videolar) (ODTÜ)

### Yapay Sinir Ağları

- [Neural Network 1 : Eğitime ve Kavramlara Giriş](https://youtu.be/B5MmXmMMuvI) (Dr. Sadi Evren SEKER @BilgisayarKavramlari) {23 dakika}
- [Neural Network 2: Perceptron Kavramı ve Öğrenme](https://youtu.be/5Lo_HUDtxtw) (Dr. Sadi Evren SEKER @BilgisayarKavramlari) {13 dakika}
- [Neural Network 3: Çok Katmanlı Yapay Sinir Ağları](https://youtu.be/qrmaixHBrzU) (Dr. Sadi Evren SEKER @BilgisayarKavramlari) {13 dakika}
- [Yapay Sinir Ağlarının Matematiği ve 18 Satırda Matematik Olarak Kodlanması](https://www.youtube.com/watch?v=icrcbqPNrNE/) (Mehmet Burak Sayıcı)

### Yapay Zeka

- [Yapay Zeka (Artificial Intelligence) - Oynatma Listesi](https://www.youtube.com/playlist?list=PLh9ECzBB8tJOtaD6DFxqRdP7QHIaBFcbW) (Dr. Sadi Evren SEKER @BilgisayarKavramlari) {48 Video}
- [Yapay Zeka ve Deep Learning](https://www.youtube.com/watch?v=qk1RjRLIAq4) (Merve Ayyüce Kızrak) {68 dakika}
- [Yapay Zeka Çağı | TEDxMETUAnkara](https://www.youtube.com/watch?v=d4kQVyAEsqA) (Dr. Şeyda Ertekin) {18 dakika}

### Bilgisayarlı Görü

- [Uzaktan Algılanmış Görüntülerin Piksel Düzeyinde Sınıflandırılması Bölüm 1/2](https://www.youtube.com/watch?v=Y087JVjzw-Y) (Erhan Abdullah (Erchan Aptoula) @Data İstanbul) {60 dakika}
- [Uzaktan Algılanmış Görüntülerin Piksel Düzeyinde Sınıflandırılması Bölüm 2/2](https://www.youtube.com/watch?v=EAYNMnMBqnA) (Erhan Abdullah (Erchan Aptoula) @Data İstanbul) {30 dakika}
- [Derin Öğrenmeye Derinlemesine Dalış](https://www.youtube.com/watch?v=zJPW6Lyf_Xs) (Şefik İlkin Serengil @Softtech Sahnesi) {52 dakika}
- [Makine Öğrenmesi Çağında Hayatta Kalma Rehberi](https://youtu.be/P2MwuGpRgSQ) (Şefik İlkin Serengil @İstanbul Coding Talks) {84 dakika}
- [Derin Öğrenme: Dünü, Bugünü, Yarını](https://www.youtube.com/watch?v=ITCD2Z4jT8w) (Şefik İlkin Serengil @Bilgisayar Mühendisleri Odası) {100 dakika}
- [Keras ile Convolutional Neural Networks](https://www.youtube.com/watch?v=RNWjwdEQHOQ&list=PLRRY18KNZTgUyaxSRvExF7zNsIpaehl5e/) (Mehmet Burak Sayıcı)
- [Keras ile Convolutional Neural Networks](https://www.youtube.com/watch?v=RNWjwdEQHOQ&list=PLRRY18KNZTgUyaxSRvExF7zNsIpaehl5e/) (Mehmet Burak Sayıcı)

### IoT

- [IoT ve Derin Öğrenme Etkinliği](https://youtu.be/fqf6m3R4psQ) (Ferhat Kurt) {82 dakika}

## Framework

### Keras Framework

- [Keras Video Eğitim Serisi](https://www.youtube.com/watch?v=RNWjwdEQHOQ&list=PLRRY18KNZTgUyaxSRvExF7zNsIpaehl5e) (Mehmet Burak Sayıcı) {21 video, artmakta}

### Julia

- [Julia ve Knet ile Derin Öğrenmeye Giriş](https://youtu.be/3TR3Rx-Esis) (Doç. Dr. Deniz Yuret) {104 dakika}

### MatConvNet

- [MatConvNet ve Matlab ile Derin Öğrenmeye Giriş](https://www.youtube.com/watch?v=nRVQQNw4Kh4&t=8s) (Ahmet Gökhan POYRAZ) {5 Video, eklemeler yapılacaktır}

## Sunumlar

- [Bozkırda Yapay Öğrenme Yaz Okulu 2017 - Sunumları](http://goo.gl/o2H9hA) (HUCVL)
- [ODTü Görüntü Analizi Uygulama ve Araştırma Merkezi (OGAM) Yaz Okulu 2016 - Sunumları](https://obayo.ogam.metu.edu.tr/sunumlar) (ODTÜ)
- [ODTü Görüntü Analizi Uygulama ve Araştırma Merkezi (OGAM) Yaz Okulu 2016 - Videoları](http://obayo.ogam.metu.edu.tr/videolar) (ODTÜ)
- [Deep Learning Türkiye - İstatistiksel Dil İşleme - Prof. Dr. Kemal Oflazer - Sunumları](https://drive.google.com/drive/folders/1w0L5r_C0BA1VLP8uA2iPNl90F8lXkMuc?usp=sharing) (DLTR)

## Github

### Doğal Dil İşleme

- [Zemberek Parser for Python3](https://github.com/kemalcanbora/zemberek_parser)  (Kemalcan Bora)
- [Turkish Word Embeddings with 900k data](https://github.com/savasy/TurkishWordEmbeddings) (Savas Y)
- [A finite-state morphological analyzer for Turkish](https://github.com/coltekin/TRmorph) (Çağrı Çöltekin)
- [Keras ile Türkçe Anlam Analizi(Olumlu - Olumsuz)](https://github.com/zekikus/Turkce-Anlam-Analizi) (Zeki Kuş)

### Arama Algoritmaları

- [C ile Ağaçlarda Bilgisiz/Bilmeden Arama Algoritmaları](https://github.com/Enes1313/Uninformed-Search-Strategies)  (Enes AYDIN)

### Github Bilgisayarlı Görü

- [CNN ile Görüntü Sınıflandırma](https://github.com/mesutpiskin/CaffeClassification) (Mesut Pişkin)
- [Gerçek Zamanlı Cinsiyet Tespiti](https://github.com/mesutpiskin/GenderClassification) (Mesut Pişkin)
- [Duygu-Duygu ve Cinsyet Tanıma](https://github.com/ayyucekizrak/Duygu-Cinsiyet_Tanima-Emotion-Gender_Recognition) (Merve Ayyüce Kızrak-Yavuz Kömeçoğlu)
- [CNN(Tensorflow) ile CIFAR10 Veri Setinin Sınıflandırılması ve Parametre Analizi](https://github.com/zekikus/Tensorflow-CNN-with-CIFAR10-Dataset) (Zeki Kuş)
- [CNN ile FashionMNIST Veri Setinin Sınıflandırılması](https://github.com/zekikus/Tensorflow-CNN-with-FashionMNIST-Dataset) (Zeki Kuş)
- [CNN(Keras) ile CIFAR10 Veri Setinin Sınıflandırılması](https://github.com/zekikus/Keras-CNN-with-CIFAR10-Dataset) (Zeki Kuş)

### Sinir Ağları

- [Geri Beslemeli Yapay Sinir Ağı ile Karakter Tanıma](https://github.com/mesutpiskin/ANNCharacterRecognition) (Mesut Pişkin)
- [Cpp ile Yapay Sinir Ağları](https://github.com/Enes1313/Cpp-ile-YSA)  (Enes AYDIN)
- [Makine Ogrenmesi](https://github.com/SerayBeser/Makine-Ogrenmesi) (Seray Beşer)

## Bloglar

- [veridefteri.com](http://veridefteri.com/)
- [zekimakine.com](http://zekimakine.com/)
- [veribilimcisi.com](https://veribilimcisi.com/)
- [alpslabel.wordpress.com](https://alpslabel.wordpress.com//)
- [makineogrenimi.wordpress.com](https://makineogrenimi.wordpress.com)
- [devhunteryz.wordpress.com](https://devhunteryz.wordpress.com)

## Kitaplar

- [Yapay Öğrenme - Ethem Alpaydın](http://www.idefix.com/Kitap/Yapay-Ogrenme/Ethem-Alpaydin/Bilim/Populer-Bilim/urunno=0000000362293)
- [OpenCv Görüntü İşleme ve Yapay Öğrenme - Birol Kuyumcu](http://www.kitapyurdu.com/kitap/opencv-goruntu-isleme-ve-yapay-ogrenme/376463.html)
- [Yapay Zeka - Vasif Vagifoğlu Nabiyev](http://www.dr.com.tr/Kitap/Yapay-Zeka-Problemler-Yontemler-Algoritma-/Vasif-Vagifoglu-Nabiyev/Bilim/Populer-Bilim/urunno=0000000435115)

## Yarışmalar

- [Kaggle Yarışma Deneyimim ve Gözlemlerim](https://burakozdemir.co.uk/article/kaggle-yarisma-deneyimim-ve-gozlemlerim) (Burak Özdemir)
- [Kaggle BNP Paribas 93. Derece (Top %3) Yöntem ve Kod](https://datanoord.wordpress.com/2016/05/05/kaggle-bnp-paribas-93-derece-top-3-yontem-ve-kod/) (Ayşe Elvan Aldemir)

## Mobil Uygulamalar

- [Görme Engelliler için Para Okuyucu](https://itunes.apple.com/tr/app/para-okuyucu/id1334298365?l=tr&mt=8) (Özgür Şahin)
- [VisionDict](https://itunes.apple.com/tr/app/visiondict/id1299943619?mt=8) (Kadir Mert Barutçuoğlu)

## Düzenleyen

Yunus Emre

- [Github](https://github.com/yedehrab)
- [GitLab](https://gitlab.com/yedehrab)

> Yardım veya destek için [iletişime](mailto::yyunussemree@gmail.com) geçebilrsiniz 😇