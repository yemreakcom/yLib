# JavaFX 12 Hızlı Notlar 

## Proje Dizin Yapısı

JavaFX için önerilen dizin yapısı aşağıdaki gibidir. ([kaynak](https://stackoverflow.com/a/24948550/9770490))

- Çalışmaları gruplandırmak için `com/yemreak/myproject` yapısı kullanılmakta
  - Maven veya gradle yapısı olarak da geçmektedir
- `controllers`, FXML dosyalarını kontrol eden kodlar
- `services`, Harici hizmetler (veya tüm hizmetler)
  - Eğer çok fazla hizmet varsa, yerel hizmetleri farklı dizine alabilirsin
- `utility`, Dahili hizmetler
- `resources`, Tüm kod dışı kaynaklar (images, css, html vs.)
- `views`, FXML tasarımları

```
src/main
  ├──java/com/yemreak/myproject (ya da sadece myproject)
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

Dizinleri IDE üzerinden yapılandırak daha verimli çalışabilirsin.

- `Project Structure` - `Project Settings` - `Modules`
- `Source` sekmesinden `src/res` dizinini `Resources` olarak tanıt
- `out`, `lib` ve `res` dosyalarını `Excluded` olarak tanıt

![jetbrains_project_structures](../../res/jetbrains_project_structures.png)

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

## JPackage ile Çıkarma

- İlk olarak [buradan](https://jdk.java.net/jpackage/) JPackage'ı indirmen lazım.

> [MSPaint](https://wiki.ms-paint-i.de/developing#prerequesits) adlı yazılım JPackage ile çıkarılmış (?)

## Kod Notları

### Kod Tarafında CSS Değiştirme

```java
buttonDownload.setStyle("-fx-background-image: url('/images/verified.png')");
```

### Thread ile Kodlama

JavaFX'de oluşturulan Thread, FX'in threadına uyumsuz olarak ilerleyebilmekte, bu durumda `Not on FX application thread; currentThread = JavaFX Application Thread error?` hatası gelemektedir.

- FX (arayüzden) bağımsız Thread'lerdee sorun oluşmaz.
- Arayüzü bağımlı Thread'lerde `Platform.runAfter{() -> {}}` yapısı kullanılır
- Thread'i platformdan sonra başlat anlamına gelmektedir

```java
new Thread(() -> {
    Image resim = uzunSürenBirİşlem();
    imageView.setImage(resim); // Bu udurmda thread ile FX yapısı kesişir ve hata verir
}).start();

new Thread(() -> {
    Image resim = uzunSürenBirİşlem();
    Platform.runAfter(() -> imageView.setImage(resim)); // Yapısı ile FX hazır olduktan sonra işlem yapılır
}).start();
```

### CSS ile Stil Oluşturma

- Buton gibi alt öğrelere `.buton` css class'ı ile özellik tanımlayabilirsin
- Her eleman içinde bulunduğu panelin css özelliğini taşır

> - [CSS ile arkaplana resim ekleme]
> - [CSS ile özel buton ayarlama]
> - [How to refer to an anchor pane in css?]
> - [JavaFX Button with transparent background]

### FXML'de Kod Yapısı

```xml
<TextField prefWidth="50" text="${speedSlider.value}"/> <!-- Inline code -->
<Slider fx:id="speedSlider" orientation="HORIZONTAL" prefWidth="300"
        min="60" max="100000" blockIncrement="100"/>
```

> [Slider'a göre Label'ı güncelleme]

### Slider Listener (Kaydırmalı çubuğun değişikliğine göre tepki verme)

Silder objesinden herhangi bir özelliği (`...Property`) alıp ona uygun listener ekleyebiliriz.

```java
// Listener örneği
sliderQuality.valueProperty().addListener((observableValue, number, t1) -> {
    updateFileSize();
});
```

> [Slider'a göre Label'ı güncelleme]

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

### ImageView Resmi Değiştirme

Bu işlem için `resource` dizini **IntelliJ**'de işaretlemeniz gerekmektedir.

```java
import javafx.scene.image.Image;

// load an image in background, displaying a placeholder while it's loading
// (assuming there's an ImageView node somewhere displaying this image)
// The image is located in default package of the classpath
Image image1 = new Image("/flower.png", true);

// load an image and resize it to 100x150 without preserving its original
// aspect ratio
// The image is located in my.res package of the classpath
Image image2 = new Image("my/res/flower.png", 100, 150, false, false);

// load an image and resize it to width of 100 while preserving its
// original aspect ratio, using faster filtering method
// The image is downloaded from the supplied URL through http protocol
Image image3 = new Image("http://sample.com/res/flower.png", 100, 0, false, false);

// load an image and resize it only in one dimension, to the height of 100 and
// the original width, without preserving original aspect ratio
// The image is located in the current working directory
Image image4 = new Image("file:flower.png", 0, 100, false, false);
```

> Oracle'ın [resmi sitesinden](https://docs.oracle.com/javafx/2/api/javafx/scene/image/Image.html) alınmıştır.

### Dosya Sürükle Bırak İşlemleri

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
- [Listener Yönetimi](https://www.javacodegeeks.com/2015/01/dont-remove-listeners-use-listenerhandles.html)
- [JavaFX Jar çıkarma - Intellij]()

[slider'a göre label'ı güncelleme]: https://stackoverflow.com/a/40053895/9770490
[how to refer to an anchor pane in css?]: https://stackoverflow.com/a/28751561/9770490
[javafx button with transparent background]: https://stackoverflow.com/a/36566444/9770490
[css ile arkaplana resim ekleme]: https://stackoverflow.com/questions/9738146/javafx-how-to-set-scene-background-image
[css ile özel buton ayarlama]: https://stackoverflow.com/questions/10518458/javafx-create-custom-button-with-image
