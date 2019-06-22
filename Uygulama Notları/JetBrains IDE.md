# Jetbrains IDEs <!-- omit in toc -->

> `HOME` tuşu ile yukarı yönlenebilrsiniz.

- [Kısayolar](#K%C4%B1sayolar)
  - [Kod Kısayolları](#Kod-K%C4%B1sayollar%C4%B1)
  - [Metin Kısayolları](#Metin-K%C4%B1sayollar%C4%B1)
  - [Debug Kısayolları](#Debug-K%C4%B1sayollar%C4%B1)
  - [Git Kısayolları](#Git-K%C4%B1sayollar%C4%B1)
  - [VsCode KeyMap](#VsCode-KeyMap)
- [Git Yönetimi](#Git-Y%C3%B6netimi)
- [Pluginler (Eklenti gibi)](#Pluginler-Eklenti-gibi)
- [Proje Yapılandırma](#Proje-Yap%C4%B1land%C4%B1rma)
  - [Interpreter (Derleyici) Değiştirme](#Interpreter-Derleyici-De%C4%9Fi%C5%9Ftirme)
  - [Configuration (Yapılandırma) Ayarları](#Configuration-Yap%C4%B1land%C4%B1rma-Ayarlar%C4%B1)
  - [Kaynak Kod Dosyalarını Belirtme](#Kaynak-Kod-Dosyalar%C4%B1n%C4%B1-Belirtme)
    - [Ek Ortam Değşkenleri Tanımlama](#Ek-Ortam-De%C4%9F%C5%9Fkenleri-Tan%C4%B1mlama)
    - [Ortam Değişkenleri Ayarlama Eklentisi](#Ortam-De%C4%9Fi%C5%9Fkenleri-Ayarlama-Eklentisi)
- [Faydalı Ayarlar](#Faydal%C4%B1-Ayarlar)
  - [Font Ayarları](#Font-Ayarlar%C4%B1)
  - [Dökümantasyon Önizle](#D%C3%B6k%C3%BCmantasyon-%C3%96nizle)
  - [Dictionaries](#Dictionaries)
  - [Spellcheck Kaldırma](#Spellcheck-Kald%C4%B1rma)
- [Karma Notlar](#Karma-Notlar)
- [Yapılacaklar](#Yap%C4%B1lacaklar)
- [Keymap (Kısayollar)](#Keymap-K%C4%B1sayollar)

## Kısayolar

Detaylar için [buraya](https://www.jetbrains.com/help/idea/mastering-keyboard-shortcuts.html) tıklayabilirsin.

> VsCode kısayollarını aktarmak için [buraya](https://plugins.jetbrains.com/plugin/12062-vs-code-keymap/versions) bakabilirsin.

- `CTRL` + `CTRL` Komut çalıştırma
- `SHIFT` + `SHIFT` Kod içerisinde arama yapma
- `CTRL` + `SHIFT` + `ALT` + `L` Code formatlama diyaloğu
- `CTRL` + `ALT` + `L` Tüm kodu otamatik formatlama
- `CTRL` + `ALT` `O` Import'ları optimize etme
- `CTRL` + `N` Classlar arasında dolanma
- `CTRL` + `F12` Üzerinde bulunduğumuz dosya üzerinde dolanma

### Kod Kısayolları

- `CTRL` + `SPACE` Kod tamamlama
  - 2 kez ard arda basılırsa **import edilmemiş** değişkenleri de gösterir ve otomatik dahil eder
- `CTRL` + `SHIFT` + `SPACE` İle akıllı kod önerileri sunar
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
- `SHIFT` + `F6` Yeniden adlandırma

### Debug Kısayolları

- `ALT` + `F8` Dobug modunda iken kod derleme arayüzü

### Git Kısayolları

- `CTRL` + `K` Commit
- `CTRL` + `SHIFT` + `K` Push

### VsCode KeyMap

- <kbd>CTRL</kbd> + <kbd>P</kbd>, Dosyalarda arama
  - <kbd>CTRL</kbd> + <kbd>TAB</kbd>, Arama ekranındaki sekmeyi değiştirme
- <kbd>ALT</kbd> + <kbd>SHIFT</kbd> + <kbd>A</kbd>, Seçilen alanı yorum satırına alma

## Git Yönetimi

- `JetBrain IDE` - `Check out from Version Control` - `Git`
  - _Url:_ Proje URL'idir. (Adress çubuğunda yazan metin)
  - _Directory:_ Proje yolunudur. (projenin/konumu)
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
- Derlemek istediğiniz dili | uygulamayı seçin (_Örn: Python | PyCharm için_)
- Dosya derleyeceksiniz _Script_ kısmına `dosyanın yolunu` yazın.
- _Python Interpreter_ kısmında yorumlayıcıyı seçin, ayarlanmadıysa `Interpreter (Derleyici) Değiştirme` aşamasında (üst aşamada) nasıl ayarlayacağınıza bakabilirsiniz.

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
  - _Font:_ `Consolas`
  - _Size:_ `12`
  - _Line spacing:_ `1.0`

### Dökümantasyon Önizle

Fareyle kodun üzerinize geldiğiniz _açıklamalarını_ ve dökümantasyonlarını gösterecektir.

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

## Keymap (Kısayollar)

- Comment with line Comment, <kbd>ALT</kbd> + <kbd>SHIFT</kbd> + <kbd>A</kbd>
- Extend Selection, <kbd>CTRL</kbd> + <kbd>D</kbd> (Kelime ve daha fazlasını seçme)
- Editör Tab - Close, <kbd>CTRL</kbd> + <kbd>W</kbd>
- Toggle Distraction Free mode, <kbd>CLTR</kbd> + <kbd>K</kbd>, <kbd>Z</kbd>
