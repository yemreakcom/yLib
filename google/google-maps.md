---
description: Google haritalar hakkındaki notlarım
---

# 📍 Google Maps

## 👨‍💻 URL Yapısı

* 🐣 Google haritalar üzerinde alttaki URL yapısı ile konum paylaşabilirsiniz
* 📍 Konumu gösteren raptiye de olacaktır

```markup
http://www.google.com/maps/place/<lat>,<lng>/@<lat>,<lng>,<zoom>z
```

| 💎 Parametre | 📝 Açıklama |
| :--- | :--- |
| `lat` | Latitude \(enlem\) |
| `lng` | Longitude \(boylam\) |
| `zoom` | Yakınlık değeri \[1-20\] arası |

{% hint style="info" %}
‍🧙‍♂ Detaylı bilgi için [Google map zoom parameter in url not working](https://stackoverflow.com/questions/32806084/google-map-zoom-parameter-in-url-not-working) sorusuna bakabilirsin.
{% endhint %}

