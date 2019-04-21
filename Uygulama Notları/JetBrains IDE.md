# Jetbrains IDEs <!-- omit in toc -->

> `HOME` tuşu ile yukarı yönlenebilrsiniz.

- [Kısayolar](#k%C4%B1sayolar)
  - [Kod Kısayolları](#kod-k%C4%B1sayollar%C4%B1)
  - [Metin Kısayolları](#metin-k%C4%B1sayollar%C4%B1)
  - [Debug Kısayolları](#debug-k%C4%B1sayollar%C4%B1)
  - [Git Kısayolları](#git-k%C4%B1sayollar%C4%B1)
- [Git Yönetimi](#git-y%C3%B6netimi)
- [Pluginler (Eklenti gibi)](#pluginler-eklenti-gibi)
- [Proje Yapılandırma](#proje-yap%C4%B1land%C4%B1rma)
  - [Interpreter (Derleyici) Değiştirme](#interpreter-derleyici-de%C4%9Fi%C5%9Ftirme)
  - [Configuration (Yapılandırma) Ayarları](#configuration-yap%C4%B1land%C4%B1rma-ayarlar%C4%B1)
  - [Kaynak Kod Dosyalarını Belirtme](#kaynak-kod-dosyalar%C4%B1n%C4%B1-belirtme)
    - [Ek Ortam Değşkenleri Tanımlama](#ek-ortam-de%C4%9F%C5%9Fkenleri-tan%C4%B1mlama)
    - [Ortam Değişkenleri Ayarlama Eklentisi](#ortam-de%C4%9Fi%C5%9Fkenleri-ayarlama-eklentisi)
- [Faydalı Ayarlar](#faydal%C4%B1-ayarlar)
  - [Font Ayarları](#font-ayarlar%C4%B1)
  - [Dökümantasyon Önizle](#d%C3%B6k%C3%BCmantasyon-%C3%B6nizle)
  - [Dictionaries](#dictionaries)
  - [Spellcheck Kaldırma](#spellcheck-kald%C4%B1rma)
- [Karma Notlar](#karma-notlar)
- [Yapılacaklar](#yap%C4%B1lacaklar)

## Kısayolar

Detaylar için [buraya](https://www.jetbrains.com/help/idea/mastering-keyboard-shortcuts.html) tıklayabilirsin.

- `CTRL` + `CTRL` Komut çalıştırma
- `SHIFT` + `SHIFT` Kod içerisinde arama yapma
- `CTRL` + `SHUFT` + `ALT` + `L` Açık olan dosyayı formatlama / biçimlendirme
- `CTRL` + `ALT` + `L` Tüm kodu otamatik derleme
- `CTRL` + `ALT` `O` Import'ları optimize etme
- `CTRL` + `N` Classlar arasında dolanma
- `CTRL` + `F12` Üzerinde bulunduğumuz dosya üzerinde dolanma

### Kod Kısayolları

- `CTRL` + `SPACE` Kod tamamlama
  - 2 kez ard arda basılırsa **import edilmemiş** değişkenleri de gösterir ve otomatik dahil eder
- `ALT` + `F7` Projedeki kullanım alanını gösterir
- `CTRL` + `Q` Dökümanı hızlı önizleme
  - **import** edilen modüller için kullanışlıdır
- `CTRL` + `B` ya da `CTRL`'ye basılı tutup fare ile tıklama, tanımlandığı alana gönderir
- `CTRL` + `ALT` + `V` Seçilen kısmı değişkene atama

### Metin Kısayolları

- `CTRL` + `X` Satırı kesme
- `CTRL` + `D` Satırı hemen altına kopyalam (dublicate)
- `CTRL` + `SHIFT` + `/` Yorum satırına çevirme
- `CTRL` + `SHIFT` + `YON TUSLARI` İmlecin üzerinde durduğu metni taşıma
- `SHIFT`  + `F6` Yeniden adlandırma

### Debug Kısayolları

- `ALT` + `F8` Dobug modunda iken kod derleme arayüzü

### Git Kısayolları

- `CTRL` + `K` Commit
- `CTRL` + `SHIFT` + `K` Push

## Git Yönetimi

- `JetBrain IDE` - `Check out from Version Control` - `Git`
  - *Url:* Proje URL'idir. (Adress çubuğunda yazan metin)
  - *Directory:* Proje yolunudur. (projenin/konumu)
- `Test` & `Clone`

## Pluginler (Eklenti gibi)

Plugin kurma detayı için [buraya](https://www.jetbrains.com/help/idea/managing-plugins.html) tıklayabilirsin.

- `CTRL` + `ALT` + `S` kısmından `Plugin` sekmesinde istediğiniz iklentileri bulabilirsiniz.

## Proje Yapılandırma

### Interpreter (Derleyici) Değiştirme

Sanal environment gibi durumlarda system yerine onların derleyicisini kullanma

- `CTRL` + `ALT` + `S` yaptıktan sonra `Project: <project name> | Project Interpreter` sayfasında `Ayarlar Butonu | Add` kısmına basarak derleyicinizi değiştirebilirsiniz.

### Configuration (Yapılandırma) Ayarları

> Projenizi IDE üzerinde çalıştırabilmek için bu ayarı yapmanız gerekmekte.

- Sağ üst kısımdaki yeşin `Run` butonunun solundaki alandan `Edit Configuration`ı seçin.
- Sol üst köşedeki `+` butonuna basın
- Derlemek istediğiniz dili | uygulamayı seçin (*Örn: Python | PyCharm için*)
- Dosya derleyeceksiniz *Script* kısmına `dosyanın yolunu` yazın.
- *Python Interpreter* kısmında yorumlayıcıyı seçin, ayarlanmadıysa `Interpreter (Derleyici) Değiştirme` aşamasında (üst aşamada) nasıl ayarlayacağınıza bakabilirsiniz.

### Kaynak Kod Dosyalarını Belirtme

- `Project` kısmından dizine sağ tıklayın
- `Mark Directory as` alanından `Source` yazısına tıklayın

> Otomatik olarak dizin yolu, ortam değişkenlerine eklenecektir

#### Ek Ortam Değşkenleri Tanımlama

- Üst sekmeden `Run` kısmına gelin
- `Edit Configuration` yazısına tıklaıyn
- Yapılandırma ayarınızı seçin
  - Yoksa `+` ile yeni bir tane oluşturun
- `Environment Variables` kısmında en sağdaki dosya simgesine tıklayın
- `+` ile yeni ortam değişkeninizi ekletin

> Windows için cmd ortam değişkeni ayarlama yapısı `set name=value;value` şeklindedir.

#### Ortam Değişkenleri Ayarlama Eklentisi

Eklenti sitesi için [buraya](https://github.com/ashald/EnvFile/blob/develop/README.md) bakabilirsin.

## Faydalı Ayarlar

### Font Ayarları

- `CTRL` + `ALT` + `S` yaptıktan sonra `Editor | Font` kısmında
  - *Font:* `Consolas`
  - *Size:* `12`
  - *Line spacing:* `1.0`

### Dökümantasyon Önizle

Fareyle kodun üzerinize geldiğiniz *açıklamalarını* ve dökümantasyonlarını gösterecektir.

- `CTRL` + `ALT` + `S` yaptıktan sonra `Editor | General | Other` başlığı altında `Show quick documentation on mouse move` kısmını seçin ve süreyi `500` yapın.

### Dictionaries

Dillere özgü sözlükleri indirmek için [buraya](https://drive.google.com/open?id=1UAGLGvwv_zLBzH7zH1oGRvYhzzP67M4k) tıklayabilirsin.

- `CTRL` + `ALT` + `S` yaptıktan sonra `Editor | Spelling | Dictionaries | Custom Dictionaries` başlığı altında `+` butonuna basıp `.dic` uzantılı sözlük dosyanı ekleyin.

> Sözlüğün çalışabilmesi için `hunspell` plugin'ini indirmeniz gerekmekte. Plugin kurma detayı için [buraya](https://www.jetbrains.com/help/idea/managing-plugins.html) tıklayabilirsin.

### Spellcheck Kaldırma

- `CTRL` + `ALT` + `S` yaptıktan sonra `Editor | Inspection | Spelling | Typo | Process comments` ile yorum satırlarını kontrol etmesini kaldırabilirsin.

## Karma Notlar

- [Şifre değiştirme](https://stackoverflow.com/a/37959112)
- [DataGrip](https://www.jetbrains.com/datagrip/)

> Sayfa başındaki işaretçilere yönlenmek için [buraya](#Y%C3%B6nlendirme) tıklayabilirsin.

## Yapılacaklar

- [x] PyCharm Env Variable
  - [Link1](https://stackoverflow.com/a/42708476/9770490)