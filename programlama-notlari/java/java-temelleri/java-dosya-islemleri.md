---
description: Verilerin saklanılması için olmazsa olmaz dosya işlemleri
---

# 📁 Java Dosya İşlemleri

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

## Clipboard \(Pano\) İşlemleri

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

