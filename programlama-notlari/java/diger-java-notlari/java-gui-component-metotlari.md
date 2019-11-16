---
description: 'Faydalı olabilecek component (frame, panel, label) Metot''ları'
---

# 💠 GUI Component Metotları

## Set \(Ayarlama\) Metodları

| Metod |  | Açıklama |
| :--- | :--- | :--- |
| `setSize(...);` |  | Componentler'in boyutunu ayarlar |
| `setLocation(...);` |  | Componentler'in çizileceği konumu ayarlar |
| `setBounds(...);` |  | Componentler'in boyutunu ve çizileceği konumu ayarlar |
| `setVisible(...);` |  | Componentler'in görünürlüğünü ayarlar |
| `setLayout(...);` |  | Componentler'in içine eklenen componentlerin \(panel, text, label\) eklenme yerleştirilme düzenini ayarlar |
| `setDefaultCloseOperation(...);` |  | Frame'de X butonuna basıldığında yapılacak eylemi ayarlar. 3 \(JFrame.EXIT\_ON\_CLOSE\) alırsa X'a basıldığında kapatır |
| `setLocationRelativeTo(...);` |  | Component'in ekrana çizilme konumu ayarlar. Null alırsa tam ortaya çizer |

## Get Metodları

| Metod | Açıklama |
| :--- | :--- |
| `getInsets()` | Çerçeve çizimi için harcanan değerleri döndürür |

## Diğer Metodlar

| Metod | Açıklama |
| :--- | :--- |
| `pack()` | Component'i alt öğelerine göre yeniden boyutlandırır. `frame.pack()` yapılırsa, içindeki öğelerin boyutuna göre minimum boyutu alır. |

