# JavaFX ile GUI <!-- omit in toc -->

> As of JDK 11, the javafx.\* modules are no longer included as part of the JDK. They are now distributed separately as a standalone, unbundled release of OpenJFX. They are available either as maven artifacts for use with maven/gradle or as a standalone SDK that includes jmod files for use with jlink.

## İçerikler <!-- omit in toc -->

- [IntelliJ için JavaFx Kurulumu](#IntelliJ-i%C3%A7in-JavaFx-Kurulumu)
- [JavaFX Scene Builder](#JavaFX-Scene-Builder)
  - [Scene Builder Yapılandırması](#Scene-Builder-Yap%C4%B1land%C4%B1rmas%C4%B1)
- [JavaFX RunTime Images](#JavaFX-RunTime-Images)
- [Hata Notları](#Hata-Notlar%C4%B1)
  - [class com.sun.javafx.fxml.FXMLLoaderHelper (in unnamed module @0x24782c87) cannot access class com.sun.javafx.util.Utils (in module javafx.graphics) because module javafx.graphics:](#class-comsunjavafxfxmlFXMLLoaderHelper-in-unnamed-module-0x24782c87-cannot-access-class-comsunjavafxutilUtils-in-module-javafxgraphics-because-module-javafxgraphics)
  - [Error: Java FX Packager: Can not build artifact - fx: deploy is not available in this JDK](#Error-Java-FX-Packager-Can-not-build-artifact---fx-deploy-is-not-available-in-this-JDK)
- [Faydalı Bağlantılar](#Faydal%C4%B1-Ba%C4%9Flant%C4%B1lar)

<!-- TOOO: Burayı düzenle YToolsJava'deki gibi olsun-->

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

### Scene Builder Yapılandırması

[JFoenix] framework'ü kullanıldığından [Scene Builder]'ın library'lerine dahil edilmesi lazımdır.

- Sol üst kısımda **Library** sekmesinin en sağındaki <kbd>⚙</kbd> tıklayın
- <kbd>JAR/FXML Management</kbd> - <kbd>Add Library/FXML from file system</kbd> linkine tıklayın
- İndirdiğiniz [JFoenix] dosyasının `jar`'ını bulup, seçin.
- <kbd>Check All</kbd> ve <kbd>Built in</kbd> ayarları ile dahil edin.

> FXML dosyası ile Controller vs Resimlerin aynı package içerisinde olmaması durumunda **Scene Builder** öneri yapamaz 😢

## JavaFX RunTime Images

```bat
export PATH_TO_FX_MODS=path/to/javafx-jmods-12.0.1
$JAVA_HOME/bin/jlink --module-path $PATH_TO_FX_MODS:mods/production --add-modules hellofx --output jre
jre/bin/java -m hellofx/org.openjfx.MainApp
```

## Hata Notları

### class com.sun.javafx.fxml.FXMLLoaderHelper (in unnamed module @0x24782c87) cannot access class com.sun.javafx.util.Utils (in module javafx.graphics) because module javafx.graphics:

- Çıkan ekranda `VM Opitons` alanına alttaki metni kopyalayın:
  - `--module-path "C:\Program Files\Java\javafx-sdk-12.0.1\lib" --add-modules=javafx.controls,javafx.fxml`

### Error: Java FX Packager: Can not build artifact - fx: deploy is not available in this JDK

- **IntelliJ** üzerinde java ile gelen `fx:deploy` özelliği kaldırılmıştır (java 11+)
- Bu yüzden [buradan](https://openjfx.io/openjfx-docs/#modular) veya [jpackage](http://jdk.java.net/jpackage/) üzerinden kurulumlara bakabilirsin

> [Kaynak](https://github.com/openjfx/openjfx-docs/issues/90#issuecomment-477743330)

## Faydalı Bağlantılar

- [Drag Drop](https://www.youtube.com/watch?v=f7KGXUrAH0g)
- [Java Settings UI Design](https://www.youtube.com/watch?v=gJYXctDSIl8&list=PLniX3R2-dwS90WpmHq-hD7g_3xnkTwB6w&index=3)
- [Exe'ye çevirme](https://www.youtube.com/watch?v=iR85RRep-Po)

[intellij]: https://www.jetbrains.com/idea/download/#section=windows
[javafx sdk]: https://gluonhq.com/products/javafx/
[scene builder]: https://gluonhq.com/products/scene-builder/
[videom]: https://www.youtube.com/watch?v=1uDuWfPPL6s
