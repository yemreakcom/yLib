---
description: 'Markdown ile sayfa, resim veya başlık bağlantıları oluşturma'
---

# 🔗 Markdown ile Link

## 🧱 Temel İşlemler

Link işlemleri için bilgiler.

* Bağlantı verme işlemlerinde özel karakter kullanmak için kodlama yapmanız gerekmekte.
* Kodlama yapan online site için [buraya](https://www.urlencoder.org/) tıklayabilirsin. 
* Siteye yol verini kopyalayıp _encoded_ demeniz yeterli
  * `%20` Boşluk karakterini temsil eder

| İstek | Anahtar |
| :--- | :--- |
| Site | `https://<link>` |
| Mail | `mailto:<eposta>` |
| Telefon | `tel:<numara>` |
| Başlıklar arası | `#<başlık>` |
| Aynı dizinden | `./<yol>` |
| Bir üst dizinden | `../<yol>` |
| Dosyadaki başlığa | `../Markdown#ba%C4%9Flant%C4%B1-verme` |

{% hint style="info" %}
‍🧙‍♂ Detaylı bilgi için [Mailto Links](https://css-tricks.com/snippets/html/mailto-links/) alanına bakabilirsin
{% endhint %}

## ⭐ Başlık Linkleri Oluşturma

> `<a name="link_ismi"></a>` ile başlıklarına `#` ön eki ile erişebileceğin bağlantılar oluşturabilirsin.

> [Cross-reference \(named anchor\) in markdown](https://stackoverflow.com/a/7335259/9770490)

## 🔪 Satır içi Bağlantı \(Inline Link\)

`[metin](url)` yapısı ile metne _inline link_ verebilirsin. [Test](https://yemreak.com)

> _Dynamic link_'te `[]` kullanıldığına dikkat ediniz.

## 🌠 Dinamik Bağlantı \(Dynamic Link\)

Alttaki yapı ile metne _dynamic link_ verebilirsin. [Test](https://www.yemreak.com)

```text
[Test][test]

- [test]: https://www.yemreak.com "Açıklama Metni"
```

> _Inline link_'te `()` kullanıldığına dikkat ediniz.

## 🎨 Resim Bağlantısı

`![resim_açıklaması][resim_urli]` yapısı ile yazına resim yerleştirebilirsin.

> GIF'i de destekler

