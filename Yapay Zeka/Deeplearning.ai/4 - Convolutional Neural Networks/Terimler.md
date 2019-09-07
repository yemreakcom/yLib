# Terimler <!-- omit in toc -->

⚠ Kişisel çevirileri içerir.

## İçerikler <!-- omit in toc -->

- [Eğitim Süreci](#E%C4%9Fitim-S%C3%BCreci)
  - [Convolutional Neural Network](#Convolutional-Neural-Network)
  - [Resudial Network](#Resudial-Network)

## Eğitim Süreci

### Convolutional Neural Network

| Terim                     | Açıkama                                                                         |
| ------------------------- | ------------------------------------------------------------------------------- |
| _translation inverience_  | Değişiklikten bağımsız, (kaydırma, döndürme vs)                                 |
| _feature detector_        | Özellik algılayıcı                                                              |
| _feature map_             | Özelliklerin haritasi (pixel haritası)                                          |
| _parameter sharing_       | Özellik algıyıcı için belirlenen parametrelerin diğer alanlarda da kullanılması |
| _sparsity of connections_ | Her katmandaki her çıktının **az sayıdaki** girdi (input) değerine              |

### Resudial Network

| Terim                          | Açıklama                                                                                           |
| ------------------------------ | -------------------------------------------------------------------------------------------------- |
| _gradient descent_             | Dereceli alçalma (dağın tepe noktasından aşağı iniş)                                               |
| _pooling_                      | Ortaklama (max pooling, avg pooling)                                                               |
| _channel_                      | Renk sayısı (kanalı)                                                                               |
| _vanishing gradient_           | Gradyan değerlerinin (nöronların `a`) ilerleyen katmanlarda etisini yitirmesi                      |
| _main path_                    | Klasik sinir ağları ilerleme yapısı (Z -> A -> Z -> A)                                             |
| _short circle skip conections_ | ResNet (Residual Network) ile $a_l$ değerinin sonraki aktivasyon işlemine eklenmesine verilen isim |
