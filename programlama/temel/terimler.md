---
description: Programlamada bilmen gereken terimler ve mimari yaklaşımlar
---

# 💎 Programlama Terimleri

## 🏰 Yazılım Mimarisi <a id="yazilimda-kullanilan-terimler"></a>

📉 Katmanlarda aşağıya doğru inildikçe karmaşıklık artar

{% hint style="success" %}
Bu özellik, katman adlandırmalarında **Soft, Hard** olarak belirtilmiştir.
{% endhint %}

| Katman | Açıklama |
| :--- | :--- |
| 👨‍💻 Software | Yazılım katmanıdır, son kullanıcının gördüğü \(oyunlar, uygulamalar\) |
| 🔌 Middleware | Ara katmandır, yazılım ile işletim sistemi arasındaki iletişim |
| 👨‍💼 Operation System | İşletim sistemi katmanıdır \(windows, Linux vs\) |
| 🕹️ Firmware | Donanımla ilgili yazılmış, yazılımları kapsar \(drivers, sürücüler\) |
| 🧱 Hardware | Donanım katmanıdır \(entegre devreler\) |

![](../../.gitbook/assets/image%20%28101%29.png)

> [What's the difference between hardware, firmware, and software?](https://www.quora.com/Whats-the-difference-between-hardware-firmware-and-software)

## 🌟 Sık Kullanılan Terimler <a id="ana-terimler"></a>

| Terim | Açıklama |
| :--- | :--- |
| 📚 Library | Özel bir iş için toplanmış metotlar fonksiyonlar \(ev için alet çantası\) |
| 🎇 Framework | Kapsamlı işler için toplanmış metotlar \(önceden yapılmış ev\) |
| ⛓️ ToolChain | Birden fazla teknolojiyi \(library veya framework\) kullanma |
| 💫 API | Uygulama ile karşılıkla haberleşme \(istek gönderip, karşılık alma\) |
| 🦄 Singleton | Tek seferlik tanımlanabilen uygulama türü |

## 💎 Kavramlar

### ⛓️ ToolChain

Aşağıdaki amaçlar için kullanılan yazılımdır.

* Genellikle başka bilgisayar programları yada programlar arasında ilişki kuran
* Karmaşık yazılım geliştirme görevlerini yapmak
* Yazılım ürünü oluşturmada programlama araçlarını ayarlamak

## 🏦 Yazılımda kullanılan terimler <a id="yazilimda-kullanilan-terimler"></a>

| Kavram | Türkçe Karşılığı | Ek Açıklama |
| :--- | :--- | :--- |
| Feed | Akış | Instagram'daki resim alanı, veya sitelerdeki ana verilerin alanı |
| Feature | Özellik | ​ |
| Bug | Hata - Sıkıntı | Yazılımın açılmaması gibi çeşitli sorunlar |
| Dev | Geliştirici | ​ |
| Script | Dile özgü kod | Belli bir de yazılan proje kadar iyi olmayan kod topluluğu |
| Code Snipped | Kod Parçası | 1-2 satırlık kodlardan oluşan kod parçası |
| Register | Yazmaç | ​ |
| Cache | Önbellek | Verileri hafızada tutup hızlı açmak için önbellek kullanılır |
| Cookie | Çerez | Bir siteye tekrardan girdiğimizde giriş bilgilerimiz gibi bilgileri koruması, çerezlerle sağlanır |
| Run | Çalıştırma | Yazılan kodu derleyici üzerinde çalıştırma |
| Debug | Hata Ayıklama | Kodu derleyici üzerinde adım adım gerekli yerlerde duracak şekilde çıktılarla çalıştırma |
| Banner | Afiş | ​ |
| Slider | Kayan Afiş | ​ |
| Namespace | İsim alanı | Aynı amaca hizmet eden özellikleri, sınıfları ve fonksiyonları aynı çatı altında toplama |
| Wild Card | ​ | `..` `.` `*` gibi terimleri içeren metne verilen isim |
| Hook | Kanca | Eylemler çalıştıklarında tetiklenen işlemler \(her tıklandığında yapılan eylem için onClick\(\) kullanılır\) |
| Overhead | Ek yük | İşin yapan işçiye harcanan enerji. \(Örn: kamyon yük kaldırmak için kendi ağırlığını da kaldırmalıdır\) \([kaynak](http://bilgisayarkavramlari.sadievrenseker.com/2011/01/03/overhead-ek-yuk/)\) |

## 🔂 Değişken Terimleri <a id="degisken-terimleri"></a>

| Kavram | Türkçe Karşılığı | Ek Açıklama |
| :--- | :--- | :--- |
| Flag | Bayrak | Varlık \(evet, hayır\) değeri tutan değişkenler - Boolean |
| Listener | Dinleyici | Bir olay gerçekleştiğinde tetiklenen metotlar |

## 📜 Raporlama \(Logging\) Seviyeleri <a id="raporlama-logging-seviyeleri"></a>

Aşağıya doğru inildikçe, ekrana basılan çıktı azalır.‌

* DEBUG
* INFO
* WARNING
* ERROR
* CRITICAL

## ✨ Versiyonlar

| 💎 Sürüm | 📝 Açıklama |
| :--- | :--- |
| Beta | Sadece toplu güncelleştirme alır \(6 haftada bir\) |
| Dev | Haftalık güncelleştirme alır Cannary'den daha stabildir |
| Cannary | Gecelik güncelleme alan, anlık gelişimi temsil eder |

