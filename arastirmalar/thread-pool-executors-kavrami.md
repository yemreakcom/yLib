---
description: >-
  Java, Kotlin ThreadPoolExecuter, Executors kavramları ve birden fazla thread
  ile işlerin yönetimi multithreding
---

# 🧵 Thread Pool \(Executors\) Kavramı

## 👀 Thread Pool Nasıl Çalışır

* 🚄 Yapılacak işler **Task Queue** içerisinde sıraya alınır
* 🦄 Her iş, **tek tek** oluşturulan **Thread Pool** üzerindeki boş bulunan _thread_ üzerinde tamamlanır
* 💦 Tamamlanan işlerden sonra _thread_ serbest bırakılır, **Task Queue** üzerinden yeni iş alınır 

![](../.gitbook/assets/thread_pool.png)

## ⭐ Thread Pool Türleri

| 💎 Tür | 📝 Açıklama |
| :--- | :--- |
| ⚡ Fixed | Sabit sayıda _thread_ ile havuz oluşturulur, boşta _thread_ yoksa işler bekletilir |
| 🤹‍♂️ Cached | Lazım oldukça _thread_ oluşturulur, Uzun süreli işlemlerde kullanılmaz, sistemin kaldıramayacağı kadar _thread_ oluşturulabilir |
| 🕐 Scheduled |  |

## 🔗 Faydalı Kaynaklar

{% embed url="https://howtodoinjava.com/java/multi-threading/java-thread-pool-executor-example/" %}

