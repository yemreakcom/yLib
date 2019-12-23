---
description: Kotlin'de koşullar
---

# 👮‍♂️ Koşullar \| Kotlin

## 🎆 IF Yapısı

```kotlin
if (index = 0){
        println("0")
        index++
}
else if (index = 1) {
          println("1")
}
else if (index = 1) {
          println("2")
}
else if (index = 1) {
          println("3")
}
else {
          println("İndex değeri bulunamadı")
}
```

## 🎇 When Yapısı \(Switch\)

```kotlin
when (index){
    0 -> {
          println("0")
          index++
    }
    1 -> println("1")
    2 -> println("2")
    3 -> println("3")
    else -> println("İndex değeri bulunamadı")
}
```

