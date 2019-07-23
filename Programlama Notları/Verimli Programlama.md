# Verimli Programlama

## Diziden eleman bulma

- Dizi öncelikle sıralanır
  - Sırasız dizilerin karmaşıklığı $O(N) = N\log(N)$
  - Sıralı olunca $O(N) = N$
  - Örn: küçükten büyüğe
- Ardından eleman aranır
- Eğer eleman bakılan indeksten küçükse arama sonlandırılır
  - Sıralı olduğu için ileride de olmayacaktır
  - Eleman bulunamamıştır
- Binary arama yöntemi de oldukça hızlıdır

![img](..\res\prog_search_speed.png)

![img](..\res\binary_sorted.png)

## Tekrarlı ya da Hafıza ile Fonksiyon İşlemleri

Hafıza (_memory_), tekrarlı işlemler (_recursive_) ile çalışan fonksiyonlara nazaran daha **hızlıdır**.

### Recursion

![1563709223590](..\res\recursive_mem.png)

### While / For Döngüsü

![1563711892513](..\res\while_mem.png)
