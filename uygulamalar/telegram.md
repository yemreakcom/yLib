---
description: Telegram mesajlaşma uygulaması hakkındaki notlarım
---

# 💌 Telegram

## 👀 Hızlı Bakış

* Whatapp alternatifi mesajlaşma uygulamasıdır, grup üye sayısı sınırsızdır
* Açık kaynak bir uygulama olduğundan yazılımlar ile erişebilen bir API hizmeti sunar
* API üzerinden kişisel botlar oluşturabilir ve kendi iş akışınızı geliştirebilirsiniz

{% hint style="info" %}
👨‍💻 Programlama işleri ile ilgilenenler için telegram ideal bir chat uygulamasıdır.
{% endhint %}

## 🤖 Bot Oluşturma

* Telegram üzerinden [BotFather](https://telegram.me/botfather) kanalına mesaj atmalısın 
* `/newbot` komutu ile bot oluşturma isteğinde bulun
* İlk önce botun için isim oluştur, bu isim türkçe karakter içerebilir ve uzun olabilir
* Ardından botun için eşsiz bir kullanıcı adı berlirlemen gerekir
* Bot oluşturulduktan sonra sana token bilgisi verilecek bu bilgiyi kopyalamalı ve saklamalısın
* Botuna erişmek için t.me/&lt;botkullanıcı\_adı bağlantısına bakmalısın

## 🆔 Bot için Chat ID Alma

* Chat ID, botunuza her mesaj atan kullanıcının id bilgisidir
* Chat ID ile istediğiniz kullanıcıya mesaj gönderebilirsiniz
* Chat ID değerini almak için .[https://api.telegram.org/botXXX:YYYY/getUpdates](https://api.telegram.org/botXXX:YYYY/getUpdates) bağlantısındaki
  * XXX:YYYY alanına daha önceden kopyaladığınız token bilginizi yapıştırın
  * Örneğin: `https://api.telegram.org/bot12345:TOKEN_DEVAMI/getUpdates` 
* Döndürülen JSON metninde id: alanı içerisinde Chat ID bilgisini alabilirsiniz

{% code title="Örnek JSON çıktısı" %}
```javascript
{
    "ok": true,
    "result": [
        {
            "update_id": 0,
            "message": {
                "message_id": 0,
                "from": {
                    "id": 0,
                    "is_bot": false,
                    "first_name": "",
                    "last_name": "",
                    "language_code": ""
                },
                "chat": {
                    "id": 0,
                    "first_name": "",
                    "last_name": "",
                    "type": ""
                },
                "date": 0,
                "text": ""
            }
        }
    ]
}
```
{% endcode %}

## 🔗 Harici Bağlantılar

* [5dk'da Telegram Bot'u Oluşturma](https://medium.com/@fatihsarhan/5-dk-da-telegram-botu-nasil-yapilir-1873f18bf59b)

