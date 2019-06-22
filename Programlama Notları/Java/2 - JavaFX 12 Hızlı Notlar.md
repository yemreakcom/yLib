# JavaFX 12 Hızlı Notlar <!-- omit in toc -->

<!-- TODO: Gdirect link creator -->

## İçerikler <!-- omit in toc -->

## Hızlı Notlar

- İlk önce `Controller` clasına ekle sonra `Scene Builder` tarafında `fx:id`'ye eşle
- `drive.png` okunmuyor ama `google_drive.png` okunuyor
  - Refactor ile ismi yenilenirse de düzeliyor
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

- [JavaFX Executable File](https://www.youtube.com/watch?v=_KHCHiH2RZ0)
- [JavaFX Drag and Drop for Internal and External Communication](https://www.youtube.com/watch?v=f7KGXUrAH0g)
- [JavaFX Settings UI Design - Scene builder and Netbeans](https://youtu.be/gJYXctDSIl8?list=PLniX3R2-dwS90WpmHq-hD7g_3xnkTwB6w)
- [JPackage Tools](http://jdk.java.net/jpackage/)
