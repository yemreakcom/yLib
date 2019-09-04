# 📖 GitBook Notları

## Entagrasyon Yönetimi

### Karşılama Ekranı

Markdown dosyasının en tepesine `description` alanı oluşturulur.

```md
---
description: İçeriği açıklayan kısa not
---

# İçerik Başlığı
...
```

### `Summary.md` Dosyası

<details>
<summary>Basit örnek</summary>

```md
# Summary

* [Part I](part1/README.md)
    * [Writing is nice](part1/writing.md)
    * [GitBook is nice](part1/gitbook.md)
* [Part II](part2/README.md)
    * [We love feedback](part2/feedback_please.md)
    * [Better tools for authors](part2/better_tools.md)
```

</details>


<details>
<summary>Linkleri parçalara ayırma</summary>

```md
# Summary

### Part I

* [Part I](part1/README.md)
    * [Writing is nice](part1/README.md#writing)
    * [GitBook is nice](part1/README.md#gitbook)
* [Part II](part2/README.md)
    * [We love feedback](part2/README.md#feedback)
    * [Better tools for authors](part2/README.md#tools)
```

</details>

<details>
<summary>Çok fazla parçalı örnek</summary>

```md
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

</details>

## 🔗 Harici Bağlantılar

- [Proje Dizin Yapısı](https://github.com/GitbookIO/gitbook/blob/master/docs/structure.md)
- [Sayfa ve İndeksleme](https://github.com/GitbookIO/gitbook/blob/master/docs/pages.md)
- [Değişkenler](https://github.com/GitbookIO/gitbook/blob/master/docs/templating/variables.md)
