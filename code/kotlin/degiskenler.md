---
description: Kotlin'de değişkenler
---

# 💫 Değişkenler

## 💎 Değişkenler \(Variables\)

Değişkenler `var` ile tanımlanmaktadır.

* Değişkendir, atama yapılır
* `var x = 5`
* `var y = "Hello"`
* `y = "hi"` \(olur\)

### Obje Tanımlaması

```kotlin
object : Obje
object : CountDownTimer(1, 1){...}
object : Intent(...)
```

### Değişken Tanımlamalarında Ek Notlar

```kotlin
var sayi? = null  // Buradaki  ' ? ' değişkenin değerinin null da olabiliceğini ifade etmekte.
var kesin!!             // Buradaki '!!' değişkenin kesinlikle değerinin olacağını ifade etmekte.
val a = b?.lenght ?: -1 // b null değilse b'nin uzunluğunu ata aksi halde -1 ata (Elvis Operator)
lateinit var a : String // a'nın sonradan tanımlanacağını ifade eder.
```

## 🧱 Sabitler \(Constants\)

Sabitler `val` ile tanımlanmaktadır.

* Sabit değişkendir, atama yapılamaz \(`final` gibi\)
* `val x = 5`
* `val y = "Hello"`
* `y = "hi"` \(olmaz\)

