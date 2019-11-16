---
description: Kotlin üzerinde fonksiyon ve sınıflar
---

# 💠 Fonksiyon ve Class'lar

## 💠 Fonksiyonlar \(Functions\)

```kotlin
fun (var a : Int, val b : String?) : Int (return şekli) { ... }
```

## 🍏 Inheritance \(Extend Olayı\)

```kotlin
class Sum:Div() { // : ile extend ediyoruz ve Div'in başına open yazıyoruz.
        fun sum(a: Int, b:Int):Int {
            return a + b
        }
    }

open class Div{
    fun div(a: Int, b:Int):Int {
        return a / b
    }
}
```

