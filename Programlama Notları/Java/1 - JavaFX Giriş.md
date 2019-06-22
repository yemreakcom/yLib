# JavaFX ile GUI <!-- omit in toc -->

## İçerikler <!-- omit in toc -->

- [IntelliJ için JavaFx Kurulumu](#IntelliJ-i%C3%A7in-JavaFx-Kurulumu)
- [JavaFX Scene Builder](#JavaFX-Scene-Builder)
- [JavaFX RunTime Images](#JavaFX-RunTime-Images)
- [Hata Notları](#Hata-Notlar%C4%B1)
- [Faydalı Bağlantılar](#Faydal%C4%B1-Ba%C4%9Flant%C4%B1lar)

## IntelliJ için JavaFx Kurulumu

JavaFX ve JFhoenix Material UI'ı kurulumunu anlatan videom için [buraya][videom] bakabilrisin 💁‍♂️

- İlk olarak [IntelliJ][intellij]'yi indirin
- Resmi sitesinden [JavaFX SDK][javafx sdk]'sını indirin
- İndirdiğiniz arşivdeki çıkartın
- Arşivdeki `javafx-sdk-12.0.1` dosyasını `C:\Program Files\Java` dizinine taşıyın
- GUI düzenleme aracı olan [Scene Builder][scene builder]'ı indirin
- IntelliJ üzerinden `File` - `Settings` - `Languages & Frameworks` - `JavaFx` kısmına [Scene Builder][scene builder]'ın yolunu yazın.
  - Örn: _C:\Program Files\SceneBuilder\SceneBuilder.exe_
- IntelliJ üzerinden `File` - `New` - `Project` - `JavaFX` - `Next` - `Finish` ile projenizi oluşturun
- Son olarak `File` - `Project Structure` - `Modules`
- Açılan ekranda `+` - `Library` - `Java`
- Çıkan ekran ile `C:\Program Files\Java\javafx-sdk-12.0.1\lib` kütüphanesini ekleyin
- `Run` - `Edit Configurations`
- Çıkan ekranda `VM Opitons` alanına alttaki metni kopyalayın:
  - `--module-path "C:\Program Files\Java\javafx-sdk-12.0.1\lib" --add-modules=javafx.controls,javafx.fxml`
- Artık `.fxml` uzantılı dosyalarda ekranın sol alt köşesinden `Scene Builder`'a tıklayarak GUI programlamaya başlayabilirsiniz ✨

> Not sizin sürümünüz ve yolunuz farklı ise ona göre ayalayın `<yol>\javafx-sdk-<version>\lib`

## JavaFX Scene Builder

- `View` - `Show Sample Controller Skeleton` ile Controller'a yazılacak kodu görebiliriz
- Sol alttaki alandan `Controller` içerisinde
  - `Controller Class` alanına `<package>.Controller` yazarak Controller class'ını görmesini sağlıyoruz
- Sol alttaki `code` alanındakiler Controller'a aktarılacaktır
- Her importta `javafx.scene` olması lazımdır
  - Image vs..
- Sağ taraftaki `code` alanındaki `fx:id` kısmında ismi yazacak (Controller'dan erişmek için)

## JavaFX RunTime Images

```bat
export PATH_TO_FX_MODS=path/to/javafx-jmods-12.0.1
$JAVA_HOME/bin/jlink --module-path $PATH_TO_FX_MODS:mods/production --add-modules hellofx --output jre
jre/bin/java -m hellofx/org.openjfx.MainApp
```

## Hata Notları

**class com.sun.javafx.fxml.FXMLLoaderHelper (in unnamed module @0x24782c87) cannot access class com.sun.javafx.util.Utils (in module javafx.graphics) because module javafx.graphics:**

- Çıkan ekranda `VM Opitons` alanına alttaki metni kopyalayın:
  - `--module-path "C:\Program Files\Java\javafx-sdk-12.0.1\lib" --add-modules=javafx.controls,javafx.fxml`

## Faydalı Bağlantılar

- [Drag Drop](https://www.youtube.com/watch?v=f7KGXUrAH0g)
- [Java Settings UI Design](https://www.youtube.com/watch?v=gJYXctDSIl8&list=PLniX3R2-dwS90WpmHq-hD7g_3xnkTwB6w&index=3)

[intellij]: https://www.jetbrains.com/idea/download/#section=windows
[javafx sdk]: https://gluonhq.com/products/javafx/
[scene builder]: https://gluonhq.com/products/scene-builder/
[videom]: https://www.youtube.com/watch?v=1uDuWfPPL6s
