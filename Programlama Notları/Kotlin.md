# Kotlin

## Değişkenler (Variables)

Değişkenler `var` ile tanımlanmaktadır.

- Değişkendir, atama yapılır
- `var x = 5`
- `var y = "Hello"`
- `y = "hi"` (olur)

### Obje Tanımlaması

```kt
object : Obje
object : CountDownTimer(1, 1){...}
object : Intent(...)
```

### Değişken Tanımlamalarında Ek Notlar

```kt
var sayi? = null  // Buradaki  ' ? ' değişkenin değerinin null da olabiliceğini ifade etmekte.
var kesin!!             // Buradaki '!!' değişkenin kesinlikle değerinin olacağını ifade etmekte.
val a = b?.lenght ?: -1 // b null değilse b'nin uzunluğunu ata aksi halde -1 ata (Elvis Operator)
lateinit var a : String // a'nın sonradan tanımlanacağını ifade eder.
```

## Sabitler (Constants)

Sabitler `val` ile tanımlanmaktadır.

- Sabit değişkendir, atama yapılamaz (`final` gibi)
- `val x = 5`
- `val y = "Hello"`
- `y = "hi"` (olmaz)

## Fonksiyonlar (Functions)

```kt
fun (var a : Int, val b : String?) : Int (return şekli) { ... }
```

## Diziler (Arrays)

`val dizi = arrayOfNulls<String>(10)`

- String : Değişken tipi
- 10 : Dizi boyutu
- dizi[0] = "Dizi 0"
- dizi[1] = "dizi 1" şeklinde tanımlanır.

> Not: val olan dizi değişkenimiz oluyor, dizi[0] val olmuyor, var oluyor. Atama yapılabiliyor.

`val sayıDizisi = intArrayOf(1, 2, 3, 4)`

- 1, 2, 3, 4 sırasıyla 0, 1 ,2 ,3. indexlerin değerleri
- sayıDizisi.set(2, 9)
  - 2 : index
  - 9 : index'e yerleşecek değer.

> (dizideki 3 değeri 9 olacak, yeni dizi : 1, 2, 9, 4)

### Boyutu Değiştirilebilen Diziler

`val liste = ArrayList<String>()`

- String : değişken tipi
- liste.add("liste1")
- liste.add("liste 2")
- liste.add("liste 2")
- liste.add(1, "Hello")
  - 1 : index
  - "Hello" değişkene atanan değer
  - liste'nin değerleri ["liste1", "Hello", "liste2", "liste2"]

### Her Elemanı Farklı Olan Diziler

`val küme = HashSet<Int>()`

- Int : Değişken tipi
- küme.add(2)
- küme.add(2) // 2 tane aynı değer olamaz bu kaydedilmez. (Set özelliği)
- küme.add(0, 3)
  - 0 : index
  - 3 : değer
  - küme'nin değerleri [3, 2]

`val harita= HashMap<String, Double>`

- String : Key (Konum bilgisi , anahtarı)
- Double : Değer
- harita.add("ilkdeger", 1.0)
- harita.add("ikincideger", 2.6)
- harita.get("ilkdeğer") // Verileri almak için yapılır.
  - ilkdeğer : anahtar değeri
- harita dizisinde
  - ilkdeğer indexinde 1.0
  - ikincideğer indexinde 2.6 var.

## IF Yapısı

```kt
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

## When Yapısı (Switch)

```kt
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

## Inheritance (Extend Olayı)

```kt
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

## Harici Bağlantılar

- [Video Dersi (Ücretli / Udemy)](https://www.udemy.com/android-o-mobil-uygulama-dersi-kotlin-java/)
- [Keywords and Operators](https://kotlinlang.org/docs/reference/keyword-reference.html)
- [Control Flows (if, while, for)](https://kotlinlang.org/docs/reference/control-flow.html)
- [Ranges (for 1..3)](https://kotlinlang.org/docs/reference/ranges.html)
- [Properties and Fields](https://kotlinlang.org/docs/reference/properties.html)
- [Diziler ve Kümeler (Alternatif)](https://www.mobilhanem.com/kotlin-dersleri-kotlin-diziler-array/)
- [When](http://www.baeldung.com/kotlin-when)
- [Enum Class](http://developine.com/enum-classes-in-kotlin-example/) / ([Resmi Site için](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-enum/index.html))
- [Sealed Class ve Enum Farkı](https://proandroiddev.com/kotlin-sealed-classes-enums-with-swag-d3c4b799bcd4)
  - Sealed Class daha gelişmiş.
- [Sealed Class  / Enum farkı 2](https://medium.com/@arturogdg/creating-enums-with-associated-data-in-kotlin-d9e2cdcf4a99)
- [Get / Set olayı (Properties and Fields)](https://kotlinlang.org/docs/reference/properties.html)
- [Reciever (Kullanışlıdır.)](https://stackoverflow.com/questions/45875491/what-is-a-receiver-in-kotlin)
- [Metodlarda lamda kullanımı ve örnekleri](https://medium.com/@dbottillo/kotlin-by-examples-methods-and-lambdas-25aef7544365)
