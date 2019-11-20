---
description: GitBook - GitHub entegrasyonu hakkında bilgiler
---

# 💫 GitBook Entagrasyon Yönetimi

## 🙋‍♂️ Karşılama Ekranı

Markdown dosyasının en tepesine `description` alanı oluşturulur.

```text
---
description: İçeriği açıklayan kısa not
---

# İçerik Başlığı
...
```

## 📃 `Summary.md` Dosyası

Temel amacı GitHub'daki dosyalarımızın sitenin sol kısmında \(navigation\):

* Hangi isimle gösterileceği
* Hangi dosyaların veya klasörlerin görünür olacağı
* Hangi sırada gözükeceği

gibi sorulara çözüm bulmaktır.

**👶 Basit Örnek:**

```text
# Summary

* [Part I](part1/README.md)
    * [Writing is nice](part1/writing.md)
    * [GitBook is nice](part1/gitbook.md)
* [Part II](part2/README.md)
    * [We love feedback](part2/feedback_please.md)
    * [Better tools for authors](part2/better_tools.md)
```

**🔗 Linkleri parçalara ayırma:**

```text
# Summary

### Part I

* [Part I](part1/README.md)
    * [Writing is nice](part1/README.md#writing)
    * [GitBook is nice](part1/README.md#gitbook)
* [Part II](part2/README.md)
    * [We love feedback](part2/README.md#feedback)
    * [Better tools for authors](part2/README.md#tools)
```

**🤯 Çok fazla parçalı örnek:**

```text
# Summary

### Part I

* [Writing is nice](part1/writing.md)
* [GitBook is nice](part1/gitbook.md)

### Part II

* [We love feedback](part2/feedback_please.md)
* [Better tools for authors](part2/better_tools.md)

----

* [Last part without title](part3/title.md)
```

## 👨‍💻 GitBook Scriptlerim

[YGitBookIntegration](https://github.com/yedhrab/YGitBookIntegration) repom ile 🐙 GitHub - GitBook 📖 entegrasyonunu sağlayabilirsin.

* `SUMMARY.md` oluşturma
* Markdown olmayan dosyalar için GitHub linkleri oluşturma
  * Markdown olmayan dosyalar GitBook'da gözükmez

{% hint style="info" %}
Kişiselleştirmek istersen, [📦 YPackage](https://pypi.org/project/ypackage/) üzerinde GitBook scriptlerim mevcuttur.
{% endhint %}

