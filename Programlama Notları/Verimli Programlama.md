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

![img](C:\Users\Yedhrab\Documents\GitHub\YBilgiler\res\binary_sorted.png)

## Tekrarlı ya da Hafıza ile Fonksiyon İşlemleri

Hafıza (*memory*), tekrarlı işlemler (*recursive*) ile çalışan fonksiyonlara nazaran daha **hızlıdır**.

### Recursion

![1563709223590](C:\Users\Yedhrab\Documents\GitHub\YBilgiler\res\recursive_mem.png)

###  While  / For Döngüsü

![1563711892513](C:\Users\Yedhrab\Documents\GitHub\YBilgiler\res\while_mem.png)