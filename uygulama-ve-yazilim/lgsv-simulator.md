---
description: LGSV otonom araç similasyonu
---

# 🚗 LGSV Simulator

## Simulasyonu Hakkında Bilgi

* Otonom araç eğitimleri için hazırlanmış bir similasyondur
* Resmi videosu için [buraya](https://www.youtube.com/watch?v=NgW1P75wiuA&) tıklayabilirsin.
* Windows ortamlarında linux ortamlarına göre daha verimlidir

> Yapılması gereken similasyon ortamının detaylarına erişmen için [buraya](https://github.com/yedhrab/YWiki/tree/169abadfd1b8862c004399268f6ca1f9f9359d61/6%20-%20Uygulama%20&%20Yazılım/resources/requirements.pdf) tıklayabilirsin

## Similasyonun Kurulumu

Resmi kurulum açıklamaları için [buraya](https://www.lgsvlsimulator.com/docs/getting-started/) tıklayabilirsin.

### Sistem Gereksinimleri

* 4 GHz Dual core CPU
* Nvidia GTX 1080 😢
* Windows 10 64 Bit

### Similasyonu Çalıştırma

* Similasyonu [buraya](https://github.com/lgsvl/simulator/releases/tag/2019.01) tıklayarak indirebilirsin
* İndirilen dosyayı çıkartın ve `.exe` uzantılı dosyayı çalıştırın

### Similasyonu Unity Düzenleyicinde Çalıştırma

* `Unity Editor 2018.2.4` sürümünü [windows](https://unity3d.com/get-unity/download/archive) \| [linux](https://beta.unity3d.com/download/fe703c5165de/public_download.html) için bulup indiriniz
* Git için büyük dosya desteğini `git lfs install` komutu ile aktif edin.
  * Git LFS uygulamasını [buraya](https://git-lfs.github.com/) tıklayarak indirebilirsin.
* `git clone https://github.com/lgsvl/simulator.git` komutu ile projeyi çalışma alanınıza kopyalayın
* Unity Editor uygulamasını çalıştırın
  * Kayıt veya giriş işlemlerini uygulayın
  * `Open` butonu ile **git kopyaladığımız projenin dizinine** gelip `select folder` butonuna tıklayın
* Similasyonu çalıştırın
  * Proje panelindeki sol alt kısımdan:
    * `Asset` -&gt; `Scenes` kısmına gelip
    * Yanında unity resmi olan `Menu` yazısına çift tıklıyoruz
    * Editör'ün en üstünde beliren `yeşil oynat butonuna` tıklıyoruz

## Similasyonda Harita İşlemleri

Resmi siteisndeki dökümantasyon için [buraya](https://www.lgsvlsimulator.com/docs/map-annotation/) bakabilirsin.

### Desteklenen Ortamlar ve Özellikler

* Harita üzerinde oluşturma, düzenleme harici kaynaklar ekleme gibi özellikleri similasyon desteklemektedir
* Şu anlık sadece **Windows** ortamında desteklenmektedir
* Örnek video için [buraya](https://www.youtube.com/watch?v=4aBlxCoa1DM) bakabilirsin.

### Harita Oluşturma

* Harita oluşturma aracı olan `MapToolUtilEdit` ile harita üzerinde işlemler yapabiliriz
* İlk olarak harita aracının açılacağı sahneyi açmalıyız
  * `Assets` -&gt; `Scenes` -&gt; `<Harita>`
    * `<harita_dosyası>` Scenes klasörü içinde unity logolu harita dosyaları
    * _Örn:_ `SmallMap`
* Ardından `Window` -&gt; `Map Tool Panel` ile harita aracını açabilirsin

## Harici Kaynaklar

* [Documentation](https://www.lgsvlsimulator.com/docs/getting-started/)
* [Map Annotions](https://www.youtube.com/watch?v=4aBlxCoa1DM)

