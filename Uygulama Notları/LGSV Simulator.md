# LGSV Simulator <!-- omit in toc -->

## İçerikler <!-- omit in toc -->

- [Simulasyonu Hakkında Bilgi](#simulasyonu-hakk%C4%B1nda-bilgi)
- [Similasyonun Kurulumu](#similasyonun-kurulumu)
  - [Sistem Gereksinimleri](#sistem-gereksinimleri)
  - [Similasyonu Çalıştırma](#similasyonu-%C3%A7al%C4%B1%C5%9Ft%C4%B1rma)
  - [Similasyonu Unity Düzenleyicinde Çalıştırma](#similasyonu-unity-d%C3%BCzenleyicinde-%C3%A7al%C4%B1%C5%9Ft%C4%B1rma)
- [Similasyonda Harita İşlemleri](#similasyonda-harita-i%CC%87%C5%9Flemleri)
  - [Desteklenen Ortamlar ve Özellikler](#desteklenen-ortamlar-ve-%C3%B6zellikler)
  - [Harita Oluşturma](#harita-olu%C5%9Fturma)
- [Örnek Resimleri](#%C3%B6rnek-resimleri)
- [Harici Kaynaklar](#harici-kaynaklar)
- [Yazar](#yazar)

## Simulasyonu Hakkında Bilgi

- Otonom araç eğitimleri için hazırlanmış bir similasyondur
- Resmi videosu için [buraya](https://www.youtube.com/watch?v=NgW1P75wiuA&) tıklayabilirsin.
- Windows ortamlarında linux ortamlarına göre daha verimlidir

> Yapılması gereken similasyon ortamının detaylarına erişmen için [buraya](resources/requirements.pdf) tıklayabilirsin

## Similasyonun Kurulumu

Resmi kurulum açıklamaları için [buraya](https://www.lgsvlsimulator.com/docs/getting-started/) tıklayabilirsin.

### Sistem Gereksinimleri

- 4 GHz Dual core CPU
- Nvidia GTX 1080 😢
- Windows 10 64 Bit

### Similasyonu Çalıştırma

- Similasyonu [buraya](https://github.com/lgsvl/simulator/releases/tag/2019.01) tıklayarak indirebilirsin
- İndirilen dosyayı çıkartın ve `.exe` uzantılı dosyayı çalıştırın

### Similasyonu Unity Düzenleyicinde Çalıştırma

- `Unity Editor 2018.2.4` sürümünü [windows](https://unity3d.com/get-unity/download/archive) | [linux](https://beta.unity3d.com/download/fe703c5165de/public_download.html) için bulup indiriniz
- Git için büyük dosya desteğini `git lfs install` komutu ile aktif edin.
  - Git LFS uygulamasını [buraya](https://git-lfs.github.com/) tıklayarak indirebilirsin.
- `git clone https://github.com/lgsvl/simulator.git` komutu ile projeyi çalışma alanınıza kopyalayın
- Unity Editor uygulamasını çalıştırın
  - Kayıt veya giriş işlemlerini uygulayın
  - `Open` butonu ile **git kopyaladığımız projenin dizinine** gelip `select folder` butonuna tıklayın
- Similasyonu çalıştırın
  - Proje panelindeki sol alt kısımdan:
    - `Asset` -> `Scenes` kısmına gelip
    - Yanında unity resmi olan `Menu` yazısına çift tıklıyoruz
    - Editör'ün en üstünde beliren `yeşil oynat butonuna` tıklıyoruz

![run-sim](resources/run_sim.jpg)

## Similasyonda Harita İşlemleri

Resmi siteisndeki dökümantasyon için [buraya](https://www.lgsvlsimulator.com/docs/map-annotation/) bakabilirsin.

### Desteklenen Ortamlar ve Özellikler

- Harita üzerinde oluşturma, düzenleme harici kaynaklar ekleme gibi özellikleri similasyon desteklemektedir
- Şu anlık sadece **Windows** ortamında desteklenmektedir
- Örnek video için [buraya](https://www.youtube.com/watch?v=4aBlxCoa1DM) bakabilirsin.

### Harita Oluşturma

- Harita oluşturma aracı olan `MapToolUtilEdit` ile harita üzerinde işlemler yapabiliriz
- İlk olarak harita aracının açılacağı sahneyi açmalıyız
  - `Assets` -> `Scenes` -> `<Harita>`
    - `<harita_dosyası>` Scenes klasörü içinde unity logolu harita dosyaları
    - *Örn:* `SmallMap`
- Ardından `Window` -> `Map Tool Panel` ile harita aracını açabilirsin

## Örnek Resimleri

![lamb_down](resources/lamb_down.jpg)

## Harici Kaynaklar

- [Documentation](https://www.lgsvlsimulator.com/docs/getting-started/)
- [Map Annotions](https://www.youtube.com/watch?v=4aBlxCoa1DM)

## Yazar

~ Yunus Emre

- [Github](https://github.com/yedhrab)
- [GitLab](https://gitlab.com/yedhrab)