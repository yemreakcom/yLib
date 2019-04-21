# Yapay Zeka Notları <!-- omit in toc -->

Python ile derin öğrenme notlarımı bu alanda derleyeceğim.

> `HOME` tuşu ile yukarı yönlenebilrsiniz.

- [Cloud Destekleri](#cloud-destekleri)
- [Derin Öğrenme Notları](#derin-%C3%B6%C4%9Frenme-notlar%C4%B1)
  - [Aktivasyon Fonksiyonları](#aktivasyon-fonksiyonlar%C4%B1)
  - [Aktivasyon Fonksiyonlarının Özellikleri](#aktivasyon-fonksiyonlar%C4%B1n%C4%B1n-%C3%B6zellikleri)
- [Kaynaklar](#kaynaklar)
  - [Araştırmacılar Web Siteleri](#ara%C5%9Ft%C4%B1rmac%C4%B1lar-web-siteleri)
  - [GitHub Kaynakları](#github-kaynaklar%C4%B1)
    - [Firmalar](#firmalar)
    - [Karma](#karma)
  - [Derin Öğrenme Kaynakları](#derin-%C3%B6%C4%9Frenme-kaynaklar%C4%B1)
  - [Motivasyon](#motivasyon)

## Cloud Destekleri

[Buraya](https://github.com/discdiver/deep-learning-cloud-providers/blob/master/list.md) ve [buraya](https://towardsdatascience.com/maximize-your-gpu-dollars-a9133f4e546a) tıklayarak makine öğrenimi için bulut hizmetlerine bakabilirsin.

- [Paperspace](https://www.paperspace.com/ml)

## Derin Öğrenme Notları

> Her zaman yapılacak iş: Girişler ile ağırlıkları çarp, sabit değişken (sapma) ile topla ve aktivasyon uygula!

![Aktivatör Fonksiyonu](https://cdn-images-1.medium.com/max/600/1*FLoEcD4bWRw6Zno32uFwuw.png)

- Aktivasyon fonksiyonu kullanılmayan bir sinir ağı sınırlı öğrenme gücüne sahip bir doğrusal bağlanım (linear regression) gibi davranacaktır.

- Birden fazla dereceye sahip olan fonksiyonlara doğrusal olmayan fonksiyonlar deriz

- Ağırlıklar ile ilgili hata değerlerini hesaplamak için yapay sinir ağında hatanın geriye yayılımı algoritması uygulanmaktadır.  (Backward Propagation)

### Aktivasyon Fonksiyonları

> Aktivasyon fonksiyonu tüm bu bilgiler ve sizin yapay öğrenme modelinizin gereksinimlerine göre karar vermeniz gereken kritik bir optimizasyon problemidir.

- Sigmoid Fonksiyonu
- ReLU (Rectified Linear Unit) Fonksiyonu
  - Derin öğrenme modelleri denemelere bu fonksiyon ile başlanması tavsiye edilir.
  - Hız bakımından avantajlıdır. Gradyanların ölmesi gibi bir problemi vardır.
  - Genellikle çıkış değil ara katmanlarda kullanılır.
- Softmax Fonksiyonu
  - Genelde çıkış için kullanılır.
- Basamak (Step) Fonksiyonu
- Doğrusal (Linear) Fonksiyon
- Hiperbolik Tanjant Fonksiyonu
- Sızıntı (Leaky) ReLU Fonksiyonu
- Swish (A Self-Gated/Kendinden Geçitli) Fonksiyonu

### Aktivasyon Fonksiyonlarının Özellikleri

> (0, 1) arasıdan olan fonksyionlar **olasılıksal*- fonksiyonlardır.

![Aktivasyon Fonkisyonlarının Özellikleri](https://cdn-images-1.medium.com/max/800/1*lI22JpQMrlx777AOhzvjcw.png)

## Kaynaklar

### Araştırmacılar Web Siteleri

- [NVIDIA AI](https://www.nvidia.com/en-us/research/ai-playground/#)

### GitHub Kaynakları

#### Firmalar

- [NVIDIA](https://github.com/NVIDIA)

#### Karma

- [DeepLeague](https://github.com/farzaa/DeepLeague)

### Derin Öğrenme Kaynakları

- [Derin Öğrenme İçin Aktivasyon Fonksiyonlarının Karşılaştırılması](https://medium.com/deep-learning-turkiye/derin-%C3%B6%C4%9Frenme-i%C3%A7in-aktivasyon-fonksiyonlar%C4%B1n%C4%B1n-kar%C5%9F%C4%B1la%C5%9Ft%C4%B1r%C4%B1lmas%C4%B1-cee17fd1d9cd)

### Motivasyon

- [Yapay zeka GauGAN, çizimleri tabloya dönüştürmeyi öğrendi!](https://www.youtube.com/watch?v=1iMmenHFdCE)
- [AYNA DÜNYALAR](https://www.youtube.com/watch?v=-3DvuLtuf1U)