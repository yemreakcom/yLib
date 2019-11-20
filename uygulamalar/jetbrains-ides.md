# 🥦 Jetbrains IDEs

## Proje Dizinlerini yapılandırma

Projeledeki dizinlerin ne işe yaradığını derleyiciye bildiren ayardır.

* `Project Structure` - `Project Settings` - `Modules`
* `Source` sekmesinden dizinleri yapılandırabilirsin
  * `Sources` Modül ya da paketlerin dizinlerinin tanımlandığı yerdir
    * `src/java/com/yemreak` dizini kaynak kod dizini olsun:
    * `package controllers` yazıldığın `src/java/com/yemreak/controllers` dizinine bakılır
  * `Resources` kaynak dosyaları \(resim vs.\)
    * `Resources` dizinleri `Sources` dizinlerinin alt dizinleri olamaz
    * `src/resources` kaynak dizini olsun:
    * `getResource("/images/yemreak.jpg")` yazıldığında `src/resources/images/yemreak.jpg` yoluna bakılır
* `Excluded` dışlanan, bağımsız dosyalar

![](../.gitbook/assets/image%20%2811%29.png)

## Kısayolar

Detaylar için [buraya](https://www.jetbrains.com/help/idea/mastering-keyboard-shortcuts.html) tıklayabilirsin.

> VsCode kısayollarını aktarmak için [buraya](https://plugins.jetbrains.com/plugin/12062-vs-code-keymap/versions) bakabilirsin.

* ✲ Ctrl + ✲ Ctrl Komut çalıştırma
* ⇧ Shift + ⇧ Shift Kod içerisinde arama yapma
* ✲ Ctrl + ⇧ Shift + ⎇ Alt + `L` Code formatlama diyaloğu
* ✲ Ctrl + ⎇ Alt + `L` Tüm kodu otamatik formatlama
* ✲ Ctrl + ⎇ Alt `O` Import'ları optimize etme
* ✲ Ctrl + `N` Classlar arasında dolanma
* ✲ Ctrl + `F12` Üzerinde bulunduğumuz dosya üzerinde dolanma

### Kod Kısayolları

* ✲ Ctrl + `SPACE` Kod tamamlama
  * 2 kez ard arda basılırsa **import edilmemiş** değişkenleri de gösterir ve otomatik dahil eder
* ✲ Ctrl + ⇧ Shift + `SPACE` İle akıllı kod önerileri sunar
* ⎇ Alt + `F7` Projedeki kullanım alanını gösterir
* ✲ Ctrl + `Q` Dökümanı hızlı önizleme
  * **import** edilen modüller için kullanışlıdır
* ✲ Ctrl + `B` ya da ✲ Ctrl'ye basılı tutup fare ile tıklama, tanımlandığı alana gönderir
* ✲ Ctrl + ⎇ Alt + `V` Seçilen kısmı değişkene atama

### Metin Kısayolları

* ✲ Ctrl + `X` Satırı kesme
* ✲ Ctrl + `D` Satırı hemen altına kopyalam \(dublicate\)
* ✲ Ctrl + ⇧ Shift + `/` Yorum satırına çevirme
* ✲ Ctrl + ⇧ Shift + `YON TUSLARI` İmlecin üzerinde durduğu metni taşıma
* ⇧ Shift + `F6` Yeniden adlandırma

### Debug Kısayolları

* ⎇ Alt + `F8` Dobug modunda iken kod derleme arayüzü
* ✲ Ctrl + ENTER, Sonucu derleme

### Git Kısayolları

* ✲ Ctrl + `K` Commit
* ✲ Ctrl + ⇧ Shift + `K` Push

### VsCode KeyMap

* ✲ Ctrl + P, Dosyalarda arama
  * ✲ Ctrl + ⭾ Tab, Arama ekranındaki sekmeyi değiştirme
* ⎇ Alt + ⇧ Shift + A, Seçilen alanı yorum satırına alma

## Git Yönetimi

* `JetBrain IDE` - `Check out from Version Control` - `Git`
  * _Url:_ Proje URL'idir. \(Adress çubuğunda yazan metin\)
  * _Directory:_ Proje yolunudur. \(projenin/konumu\)
* `Test` & `Clone`

## Pluginler \(Eklenti gibi\)

Plugin kurma detayı için [buraya](https://www.jetbrains.com/help/idea/managing-plugins.html) tıklayabilirsin.

* ✲ Ctrl + ⎇ Alt + `S` kısmından `Plugin` sekmesinde istediğiniz iklentileri bulabilirsiniz.

## Proje Yapılandırma

### Interpreter \(Derleyici\) Değiştirme

Sanal environment gibi durumlarda system yerine onların derleyicisini kullanma

* ✲ Ctrl + ⎇ Alt + `S` yaptıktan sonra `Project: <project name> | Project Interpreter` sayfasında `Ayarlar Butonu | Add` kısmına basarak derleyicinizi değiştirebilirsiniz.

### Configuration \(Yapılandırma\) Ayarları

> Projenizi IDE üzerinde çalıştırabilmek için bu ayarı yapmanız gerekmekte.

* Sağ üst kısımdaki yeşin `Run` butonunun solundaki alandan `Edit Configuration`ı seçin.
* Sol üst köşedeki `+` butonuna basın
* Derlemek istediğiniz dili \| uygulamayı seçin \(_Örn: Python \| PyCharm için_\)
* Dosya derleyeceksiniz _Script_ kısmına `dosyanın yolunu` yazın.
* _Python Interpreter_ kısmında yorumlayıcıyı seçin, ayarlanmadıysa `Interpreter (Derleyici) Değiştirme` aşamasında \(üst aşamada\) nasıl ayarlayacağınıza bakabilirsiniz.

### Kaynak Kod Dosyalarını Belirtme

* `Project` kısmından dizine sağ tıklayın
* `Mark Directory as` alanından `Source` yazısına tıklayın

> Otomatik olarak dizin yolu, ortam değişkenlerine eklenecektir

#### Ek Ortam Değşkenleri Tanımlama

* Üst sekmeden `Run` kısmına gelin
* `Edit Configuration` yazısına tıklaıyn
* Yapılandırma ayarınızı seçin
  * Yoksa `+` ile yeni bir tane oluşturun
* `Environment Variables` kısmında en sağdaki dosya simgesine tıklayın
* `+` ile yeni ortam değişkeninizi ekletin

> Windows için cmd ortam değişkeni ayarlama yapısı `set name=value;value` şeklindedir.

#### Ortam Değişkenleri Ayarlama Eklentisi

Eklenti sitesi için [buraya](https://github.com/ashald/EnvFile/blob/develop/README.md) bakabilirsin.

## Faydalı Ayarlar

### Font Ayarları

* ✲ Ctrl + ⎇ Alt + `S` yaptıktan sonra `Editor | Font` kısmında
  * _Font:_ `Consolas`
  * _Size:_ `12`
  * _Line spacing:_ `1.0`

### Dökümantasyon Önizle

Fareyle kodun üzerinize geldiğiniz _açıklamalarını_ ve dökümantasyonlarını gösterecektir.

* ✲ Ctrl + ⎇ Alt + `S` yaptıktan sonra `Editor | General | Other` başlığı altında `Show quick documentation on mouse move` kısmını seçin ve süreyi `500` yapın.

### Dictionaries

Dillere özgü sözlükleri indirmek için [buraya](https://drive.google.com/open?id=1UAGLGvwv_zLBzH7zH1oGRvYhzzP67M4k) tıklayabilirsin.

* ✲ Ctrl + ⎇ Alt + `S` yaptıktan sonra `Editor | Spelling | Dictionaries | Custom Dictionaries` başlığı altında `+` butonuna basıp `.dic` uzantılı sözlük dosyanı ekleyin.

> Sözlüğün çalışabilmesi için `hunspell` plugin'ini indirmeniz gerekmekte. Plugin kurma detayı için [buraya](https://www.jetbrains.com/help/idea/managing-plugins.html) tıklayabilirsin.

### Spellcheck Kaldırma

* ✲ Ctrl + ⎇ Alt + `S` yaptıktan sonra `Editor | Inspection | Spelling | Typo | Process comments` ile yorum satırlarını kontrol etmesini kaldırabilirsin.

## Karma Notlar

* [Şifre değiştirme](https://stackoverflow.com/a/37959112)
* [DataGrip](https://www.jetbrains.com/datagrip/)

> Sayfa başındaki işaretçilere yönlenmek için [buraya]() tıklayabilirsin.

## Keymap \(Kısayollar\)

* Comment with line Comment, ⎇ Alt + ⇧ Shift + A
* Extend Selection, ✲ Ctrl + D \(Kelime ve daha fazlasını seçme\)
* Editör Tab - Close, ✲ Ctrl + W
* Toggle Distraction Free mode, CLTR + K, Z

## IDE Ortam Değişkenleri

* Oluşturmak için: `Preferences (File -> Settings) -> Appearance & Behavior -> Path Variables`
* Kullanmak için: `${<değişken_ismi>}`
* `$MODULE_DIR$`, projenin dizini
  * src, out vs.. içeren dizin

