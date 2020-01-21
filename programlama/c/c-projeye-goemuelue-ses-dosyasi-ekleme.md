---
description: Projeye dahili ses dosyaları ekleme
---

# 🎶 C\# Projeye Gömülü Ses Dosyası Ekleme

## 🗽 Açıklama

Öncelikle bu yazıda, Windows Form App.'da \(C\#'da\) ses dosyasını `.exe` dosyası içine **gömülü** olarak yerleştirmesi ve kullanılması ele alınacaktır. Yani ses dosyalarını, programın yanında **ek dosyalar olarak değil de programın içine yerleşik olmasının** nasıl sağlanacağına değinilecektir

## 📁 Ses Dosyasının Dahil Edilmesi

* Türkçe: `Proje` -  `<Proje Adın> Özellikleri` - `Kaynaklar` - `Kaynak Ekle` - `Mevcut Dosya Ekle`
* İngilizce:  `Project` - `Properties`  - `Resources tab` -  `Add Resource` -  `Add Existing File`

![](../../.gitbook/assets/image%20%286%29.png)



## 🔉 Waw harici Ses Dosylarının Yönetimi

`waw` dışındaki ses dosyalarını çalıştırmak için **Windows Media Player** referansını projemize dahil etmemiz lazım.

* `Proje` -&gt; `Başvuru Ekle` -&gt; `COM` -&gt; `Windows Media Player` \("wmp.dll" olmasına dikkat edin\)
* Ek olarak, `.waw` için `SoundPlayer`, diğer uzantılar için `WindowsMediaPlayer` türünden değişkenimizi oluşturuyorz.
* `WindowsMediaPlayer wmp = new WindowsMediaPlayer();`

![](../../.gitbook/assets/image%20%2896%29.png)

## 👨‍💻 Kod Parçası

```text
string fileName = Path.Combine(Environment.GetFolderPath(Environment.SpecialFolder.ApplicationData), "<istediğiniz isim>.<dosya uzantısı>");
File.WriteAllBytes(fileName, Properties.Resources.<ses dosyası ismi>);
wmp.URL = fileName;
wmp.controls.play(); // Sesi çalıştırma
wmp.controls.stop(); // Sesi durdurma
```

![](../../.gitbook/assets/image%20%2873%29.png)

## 💡 Kod Açıklaması

* Karşı bilgisayarda oluşturulacak dosyanın yolunu string'e atıyoruz. \(`"sound.mp3"` istediğiniz isim olabilir\)
* Dosya yolu ve ses dosyamızı kullanarak dosyayı oluşturuyoruz. \(`"bensound_memories"` ses dosyamın adı\)
* `.waw` için `SoundPlayer.URL` diğer ses dosyaları için `wmp.URL`'ye oluşturduğumuz dosyanın yolunu gönderiyoruz, bu sayede player o müziği bulacaktır.
* Müziği başlatma
* Müziği kapatma

