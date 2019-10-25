---
description: Instagram üzerinden otomatik follow / unfollow işlemleri yapan botun kullanımı
---

# 🤖 Instagram Bot

## 🗽 Açıklama

![instabot](https://raw.githubusercontent.com/yedhrab/YInstaBot/master/res/instabot.png)

Botu `pip install yinstabot` komutu ile indirebilirsiniz.

* Çalışma dizini komutun çalıştırıldığı dizindir.
* Kullanıcı bilgileri [🤵 sessions](./sessions) dizinine kaydedilir

> ✨ [Instabot](https://github.com/instagrambot/instabot) projesinden yararlanılmıştır.

{% embed url="https://github.com/yedhrab/YInstaBot" %}

## 📑 Botun Kullanımı

Bot, `yinstabot <accounts.json yolu>` komutu ile önceden oluşturulmuş `accounts.json` dosyasının yolunu alarak çalışır.

| İsteğe bağlı parametreler | Açıklama |
| :--- | :--- |
| `--help` | Yardım metnin gösterir |
| `-nr` | Verileri güncellemeden çalışır |
| `-q` | Sessizce çalışır |

> 🙄 Henüz yapım aşamasında olduğundan gereksiz parametreleri de vardır

### 📂 `accounts.json` yapısı

```javascript
{
  "username": {
    "info": "Kişisel notunuz (önemli bir alan değildir)",
    "username": "kullaniciadi",
    "password": "şifre",
    "option": 1,
    "target_usernames": [
      "instagram",
      "facebook",
    ]
  },
  "username": {
    "info": "Kişisel notunuz (önemli bir alan değildir)",
    "username": "kullaniciadi",
    "password": "şifre",
    "option": 5,
    "target_usernames": [
      "instagram",
      "facebook",
    ]
  }
}
```

### 🔨 Option Değerleri

| Değer | Açıklama |
| :--- | :--- |
| 1 | `data` dizinindeki kullancı idlerini takip eder, seni takip etmeyenleri takipten çıkarır |
| 2 | Seni takip etmeyenleri takipten çıkarır |
| 3 | Herkesi takipten çıkarır |
| 4 | Sadece takip işlemi yapar |
| 5 | `target_usernames`'deki kişilerin paylaştığı resimleri beğenen kişilerin idlerini `data` dizininde dosyalarda saklar |

> `1`'in çalışması için `5` özelliğine sahip ayrı bir hesap tanımlanmazsa ilk hesap ile veri toplanması yapılır

## 🖤 Android'te Termux ile Kullanım

Android için [🖤 Termux](https://play.google.com/store/apps/details?id=com.termux&hl=en) uygulamasını indirin ve yükleyin, ardıntan alttaki komutları yazdıktan sonra 📑 Botun Kullanımı alanındakileri uygulayın.

```bash
# Gerekli araçların kurulumları
pkg install python
pip install yinstabo

# İsteğe bağlı paremetreler:
# --help  | Yardım metnin gösterir
# -nr    | Verileri güncellemeden çalışır
# -q    | Sessizce çalışır
yinstabot <accounts.json yolu>
```

## ⭐ Örnek Kullanım Çıktısı

![](../.gitbook/assets/image%20%2833%29.png)

## 🔗 Harici Bağlantılar

* [Instabot](https://github.com/instagrambot/instabot)
* [NeoInstabot](https://github.com/yurilaaziz/neo-instabot)
* [Instabot-py](https://github.com/instabot-py/instabot.py)

## 💖 Destek ve İletişim

Yardımcı olmak için _pull request_ atabilirsiniz 🤗

> **The** [**MIT License**](https://choosealicense.com/licenses/mit/) **© Yunus Emre Ak**

[![Github](https://drive.google.com/uc?id=1PzkuWOoBNMg0uOMmqwHtVoYt0WCqi-O5)](https://github.com/yedhrab) [![LinkedIn](https://drive.google.com/uc?id=1hvdil0ZHVEzekQ4AYELdnPOqzunKpnzJ)](https://www.linkedin.com/in/yemreak/) [![Website](https://drive.google.com/uc?id=1wR8Ph0FBs36ZJl0Ud-HkS0LZ9b66JBqJ)](https://yemreak.com) [![Mail](https://drive.google.com/uc?id=142rP0hbrnY8T9kj_84_r7WxPG1hzWEcN)](mailto::yedhrab@gmail.com?subject=YBilgiler%20%7C%20Github) [![Destek](https://drive.google.com/uc?id=1zyU7JWlw4sJTOx46gJlHOfYBwGIkvMQs)](https://gogetfunding.com/yemreak/)

[![Patreon](https://drive.google.com/uc?id=11YmCRmySX7v7QDFS62ST2JZuE70RFjDG)](https://www.patreon.com/yemreak/)

