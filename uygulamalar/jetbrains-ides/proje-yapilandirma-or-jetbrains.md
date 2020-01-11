# 🏗️ Proje Yapılandırma \| JetBrains

## 📂 Dizinlerini yapılandırma

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

![](../../.gitbook/assets/image%20%2816%29.png)

## 💫 Interpreter \(Derleyici\) Değiştirme

Sanal environment gibi durumlarda system yerine onların derleyicisini kullanma

* ✲ Ctrl + ⎇ Alt + `S` yaptıktan sonra `Project: <project name> | Project Interpreter` sayfasında `Ayarlar Butonu | Add` kısmına basarak derleyicinizi değiştirebilirsiniz.

## 🔨 Configuration \(Yapılandırma\) Ayarları

> Projenizi IDE üzerinde çalıştırabilmek için bu ayarı yapmanız gerekmekte.

* Sağ üst kısımdaki yeşin `Run` butonunun solundaki alandan `Edit Configuration`ı seçin.
* Sol üst köşedeki `+` butonuna basın
* Derlemek istediğiniz dili \| uygulamayı seçin \(_Örn: Python \| PyCharm için_\)
* Dosya derleyeceksiniz _Script_ kısmına `dosyanın yolunu` yazın.
* _Python Interpreter_ kısmında yorumlayıcıyı seçin, ayarlanmadıysa `Interpreter (Derleyici) Değiştirme` aşamasında \(üst aşamada\) nasıl ayarlayacağınıza bakabilirsiniz.

## 📝 Kaynak Kod Dosyalarını Belirtme

* `Project` kısmından dizine sağ tıklayın
* `Mark Directory as` alanından `Source` yazısına tıklayın

> Otomatik olarak dizin yolu, ortam değişkenlerine eklenecektir

## 🌄 IDE Ortam Değişkenleri

* Oluşturmak için: `Preferences (File -> Settings) -> Appearance & Behavior -> Path Variables`
* Kullanmak için: `${<değişken_ismi>}`
* `$MODULE_DIR$`, projenin dizini
  * src, out vs.. içeren dizin

## 🌃 Ek Ortam Değişkenleri Tanımlama

* Üst sekmeden `Run` kısmına gelin
* `Edit Configuration` yazısına tıklaıyn
* Yapılandırma ayarınızı seçin
  * Yoksa `+` ile yeni bir tane oluşturun
* `Environment Variables` kısmında en sağdaki dosya simgesine tıklayın
* `+` ile yeni ortam değişkeninizi ekletin

> Windows için cmd ortam değişkeni ayarlama yapısı `set name=value;value` şeklindedir.

## 🔌 Ortam Değişkenleri Ayarlama Eklentisi

Eklenti sitesi için [buraya](https://github.com/ashald/EnvFile/blob/develop/README.md) bakabilirsin.

