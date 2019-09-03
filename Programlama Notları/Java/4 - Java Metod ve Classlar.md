# Java Method ve Classlar <!-- omit in toc -->

## Sayısı belirtilmemiş parametre kullanımı

Değişken tipinin yanına `...` yazılması ile ifade edilir.

- Çok sayıda tanımsız parametre gelebilir demektir
- For döngüleri ile ele alınır

```java
public void ornekMethod(String ... metinler) {
  for (String metin : metinler) {
    System.out.printf("%s ", metin);
  }
}
```

## Interface

Interface'ler metodlardan oluşan classlardır.

### Functional Interface

Tek metodtan oluşan interface'lerdir.

- Lambda expression `() -> {}` ile kullanılabilirler
- Metodlara parametre olarak metod göndermek için çok kullanışlıdır

```java
@FunctionalInterface
public interface ProcessEvent {

    void onOutputChanged(String param);

}

public static void executeCommand(ProcessEvent pe) {
    String param = "Selam";
        pe.onOutputChanged(param); // Gönderilen lambda expression'a param değişkenini atar
}

public static void main(String[] args) {
    executeCommand((param) -> { // Interface içerisinden gelen değişken () arasına yazılır
        System.out.println(param); // Ekrana hello basar
    })
}
```
