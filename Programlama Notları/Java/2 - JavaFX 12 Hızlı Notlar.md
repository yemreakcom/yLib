# JavaFX 12 Hızlı Notlar <!-- omit in toc -->

<!-- TODO: Gdirect link creator -->

## İçerikler <!-- omit in toc -->

- [Proje Dizin Yapısı](#Proje-Dizin-Yap%C4%B1s%C4%B1)
  - [Dosyaları Yapılandırma](#Dosyalar%C4%B1-Yap%C4%B1land%C4%B1rma)
- [Hızlı Notlar](#H%C4%B1zl%C4%B1-Notlar)
- [Kod Notları](#Kod-Notlar%C4%B1)
  - [Çerçeveleri Kaldırma](#%C3%87er%C3%A7eveleri-Kald%C4%B1rma)
  - [Arkaplanı Transparant Yapma](#Arkaplan%C4%B1-Transparant-Yapma)
  - [Clipboard (Pano) İşlemleri](#Clipboard-Pano-%C4%B0%C5%9Flemleri)
- [Dosya Sürükle Bırak İşlemleri](#Dosya-S%C3%BCr%C3%BCkle-B%C4%B1rak-%C4%B0%C5%9Flemleri)
- [Listeners (Eylem Yönetimi)](#Listeners-Eylem-Y%C3%B6netimi)
  - [Ekranı Taşıma İşlemi](#Ekran%C4%B1-Ta%C5%9F%C4%B1ma-%C4%B0%C5%9Flemi)
- [Harici Bağlantılar](#Harici-Ba%C4%9Flant%C4%B1lar)

## Proje Dizin Yapısı

JavaFX için önerilen dizin yapısı aşağıdaki gibidir. ([kaynak](https://stackoverflow.com/a/24948550/9770490))

- `controllers`, FXML dosyalarını kontrol eden kodlar
- `services`, Harici hizmetler (veya tüm hizmetler)
  - Eğer çok fazla hizmet varsa, yerel hizmetleri farklı dizine alabilirsin
- `utility`, Dahili hizmetler
- `resources`, Tüm kod dışı kaynaklar (images, css, html vs.)
- `views`, FXML tasarımları

```
src/main
  ├──java/com/yemreak
     ├── controllers
        ├──Screen1controller.java
        ├──Screen2controller.java
     ├── services
        ├──Service1.java
     ├── applications
        ├── SaveProducts.java
  ├──resources
     ├──views
        ├──screen1.fxml
        ├──screen2.fxml
     ├──css
        ├──style.css
     ├──images
        ├──img1.jpg
        ├──img2.jpg
```

<!-- TODO: Sonradan kendi projemi ekleyebilirim -->

> Örnek olacak [proje](https://github.com/badarshahzad/JFX-Browser) için buraya bakabilirsin

### Dosyaları Yapılandırma

- `Project Structure` - `Project Settings` - `Modules`
- `Source` sekmesinden `src/res` dizinini `Resources` olarak tanıt
- `out`, `lib` ve `res` dosyalarını `Excluded` olarak tanıt

![jetbrains_project_structures](../../res/jetbrains_project_structures.png)

The above implementation can be considered for a `Maven` project.

For a simple project, you can view a [structure here](https://github.com/TheItachiUchiha/MediaPlayerFX). It is a maven project!

> [Kaynak](https://stackoverflow.com/a/24948550)

## Hızlı Notlar

- İlk önce `Controller` clasına ekle sonra `Scene Builder` tarafında `fx:id`'ye eşle
- `drive.png` okunmuyor ama `google_drive.png` okunuyor
  - Refactor ile ismi yenilenirse de düzeliyor
  - Resimlerin herbiri **src dizinininin altında** olmalı
- Üst üste tasarımlar için tasarım yapacağın paneli `Hierarchy` kısmından en alta alırsan, diğerlerinin üstüne gelir ve karışmaz
- Ya da visible değerini `false` yaparsın
- En alta alınan program çalıştığında ilk görülendir
- [Arkaplanı görünmez yapma](https://stackoverflow.com/a/48404925/9770490)

## Kod Notları

### Çerçeveleri Kaldırma

```java
primaryStage.initStyle(StageStyle.TRANSPARENT);
```

### Arkaplanı Transparant Yapma

- İlk olarak `.fxml` dosyasındaki gerekli objeye `style="-fx-background-color: transparent ;"` özelliği ekleyin
- Ardından kod tarafında alttaki düzeltmeyi yapın

```java
primaryStage.setScene(new Scene(root));
primaryStage.getScene().setFill(Color.TRANSPARENT);
```

### Clipboard (Pano) İşlemleri

```java
private void putClipboard(String clipboardString) {
    StringSelection stringSelection = new StringSelection(clipboardString);
    Clipboard clipboard = Toolkit.getDefaultToolkit().getSystemClipboard();
    clipboard.setContents(stringSelection, null);
}

String getClipboard() throws IOException, UnsupportedFlavorException {
    Clipboard clipboard = Toolkit.getDefaultToolkit().getSystemClipboard();
    return (String) clipboard.getData(DataFlavor.stringFlavor);
}
```

## Dosya Sürükle Bırak İşlemleri

```java
@FXML
private ImageView imageView;

@FXML
void handleDragOver(DragEvent event) {
    if (event.getDragboard().hasFiles()) {
        event.acceptTransferModes(TransferMode.ANY);
    }
}

@FXML
void handleDragDropped(DragEvent event) throws FileNotFoundException {
    List<File> files = event.getDragboard().getFiles();
    Image img = new Image(new FileInputStream(files.get(0)));
    imageView.setImage(img);
}
```

## Listeners (Eylem Yönetimi)

### Ekranı Taşıma İşlemi

```java
public class Main extends Application {

    private double xOffset;
    private double yOffset;

    @Override
    public void start(Stage primaryStage) throws Exception{
        Parent root = FXMLLoader.load(getClass().getResource("sample.fxml"));

        primaryStage.setTitle("Hello World");
        primaryStage.setScene(new Scene(root));
        primaryStage.show();

        root.setOnMousePressed(mouseEvent -> {
            xOffset = mouseEvent.getSceneX();
            yOffset = mouseEvent.getSceneY();
        });

        root.setOnMouseDragged(mouseEvent -> {
            primaryStage.setX(mouseEvent.getScreenX() - xOffset);
            primaryStage.setY(mouseEvent.getScreenY() - yOffset);
        });
    }


    public static void main(String[] args) {
        launch(args);
    }
}
```

## Harici Bağlantılar

- [JavaFX ImageView'i Dosya İle Değiştirme](https://stackoverflow.com/questions/7830951/how-can-i-load-computer-directory-images-in-javafx)
- [JavaFX Executable File](https://www.youtube.com/watch?v=_KHCHiH2RZ0)
- [JavaFX Drag and Drop for Internal and External Communication](https://www.youtube.com/watch?v=f7KGXUrAH0g)
- [JavaFX Settings UI Design - Scene builder and Netbeans](https://youtu.be/gJYXctDSIl8?list=PLniX3R2-dwS90WpmHq-hD7g_3xnkTwB6w)
- [JPackage Tools](http://jdk.java.net/jpackage/)
