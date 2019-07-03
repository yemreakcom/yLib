# Java Dosya İşlemleri <!-- omit in toc -->

## İçerikler <!-- omit in toc -->

- [Kullanıcı Dizinleri](#Kullan%C4%B1c%C4%B1-Dizinleri)
- [Silme İşlemleri](#Silme-%C4%B0%C5%9Flemleri)
- [Clipboard (Pano) İşlemleri](#Clipboard-Pano-%C4%B0%C5%9Flemleri)
- [Seçilini Olanı Kopyalama](#Se%C3%A7ilini-Olan%C4%B1-Kopyalama)

## Kullanıcı Dizinleri

Tüm OS'larda çalışır.

```java
System.getProperty("user.home"); // Kullanıcı dizini
System.getProperties() // Tüm sistem bilgileri
System.getenv(); // Sistem değişkenleri
```

## Silme İşlemleri

```java
File file = new File(<dosyaYolu>); // Dosyayı tanımlama
file.delete(); // Silinirse true döndürür
```

> Tüm işlemler için [buraya](https://www.journaldev.com/830/java-delete-file-directory) bakabilirsin.

## Clipboard (Pano) İşlemleri

```java
Clipboard clipboard = Toolkit.getDefaultToolkit().getSystemClipboard(); // Panoyu alma
clipboard.getAvailableDataFlavors(); // Panodakileri liste olarak alma
```

## Seçilini Olanı Kopyalama

```java
private void pasteSelectionContent() {
  try {
    Clipboard systemSelection = Toolkit.getDefaultToolkit().getSystemSelection();
    if(systemSelection != null) {
      injectStringAsKeyStrokes((String) systemSelection.getData(DataFlavor.stringFlavor));
    }
  }
  catch(Exception ignore) {
  }
}
```
