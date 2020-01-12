---
description: Kotlin üzerinde fonksiyon ve sınıflar
---

# 💠 Fonksiyon ve Class'lar \| Kotlin

## 💠 Fonksiyonlar \(Functions\)

```kotlin
fun (var a : Int, val b : String?) : Int (return şekli) { ... }
```

## 🚄 Variable Arguments \(...\)

```kotlin
fun <T> asList(vararg ts: T): List<T> {
    val result = ArrayList<T>()
    for (t in ts) // ts is an Array
        result.add(t)
    return result
}
```

{% hint style="info" %}
‍🧙‍♂ Detaylı bilgi için [Variable number of arguments \(Varargs\)](https://kotlinlang.org/docs/reference/functions.html#variable-number-of-arguments-varargs) alanına bakabilirsin.
{% endhint %}

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

