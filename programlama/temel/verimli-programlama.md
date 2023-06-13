---
description: Yazılan kodların çalışmasından sonraki en önemli özelliği verimli olmasıdır 😅
---

# 📈 Verimli Programlama

## 🔍 Diziden eleman bulma <a href="#diziden-eleman-bulma" id="diziden-eleman-bulma"></a>

* Dizi öncelikle sıralanır
  * Sırasız dizilerin karmaşıklığı $$O(N) = N\log(N)$$
  * Sıralı olunca $$O(N) = N$$
  * Örnek sırala küçükten büyüğe olabilir
* Ardından eleman aranır
* Eğer eleman bakılan indeksten küçükse arama sonlandırılır
  * Sıralı olduğu için ileride de olmayacaktır
  * Eleman bulunamamıştır
* Binary arama yöntemi de oldukça hızlıdır

![Sıralı vs sırasız arama](<../../.gitbook/assets/image (91).png>)

![Binary vs sıralı ve sırasız](<../../.gitbook/assets/image (113).png>)

## 🎡 Tekrarlı ya da Hafıza ile Fonksiyon İşlemleri <a href="#tekrarli-ya-da-hafiza-ile-fonksiyon-islemleri" id="tekrarli-ya-da-hafiza-ile-fonksiyon-islemleri"></a>

Hafıza (_memory_), tekrarlı işlemler (_recursive_) ile çalışan fonksiyonlara nazaran daha **hızlıdır**.‌

![Tekrarlı fonksyionlar](<../../.gitbook/assets/image (74).png>)

## 📦 Hazır Paketlerin Hız Avantajı

Yazılım ekipleri tarafından oluşturulan paketler, optimize edildiğinden el yazımı işlemlere nazaran daha hızlı çalışır.

![Hazır paketlerin hız avantajı](<../../.gitbook/assets/image (55).png>)
