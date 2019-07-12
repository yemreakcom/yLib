# CNN

## İçerikler

## CNN Nedir

Görüntü işleme kullanılan DNN yapısıdır.

## Terimler

| Terim   | AÇıklama                              |
| ------- | ------------------------------------- |
| Kernel  | Filtre                                |
| Strike  | Kernel'ın yer değiştirme uzunluğu (1) |
| Pooling | CNN'i küçülten filtreler              |

## Pooling

CNN üzerinde belli değerde kernel dolaştırma (max pool filtre boyutu kadar alanda max pixeli bulur)

## MaxPooling

Kernel'ı dolaştırarak en yük pixel değerini alır

- 2x2 kernel için boyut yarıya iner
- nxn için `boyut / n` boyutuna geçer
