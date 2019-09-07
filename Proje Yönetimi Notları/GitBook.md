# 📖 GitBook Notları

## 📌 Önemli Notlar

GitBook'a 🚙 geçiş yapmadan önce bilinmesi gerekenler

- Kaynakları (resim, PDF vs) GitHub üzerinden çeker, kendi sitesinde barındırmaz
- GitHub ile 💫 senkronize çalışır 

### 💔 Desteklemedikleri

- Açılır menü yapısı olan `<detail>` formatı
- Buton yapısı olan `<kdb>` formatı
- Github submodule'leri

### 💞 Ek Olarak Destekledikleri

- `SUMMARY.md` ile sol kenarda gösterilen dizin yapısını düzenleme
- `README.md`'yi otomatik olarak algılama
- Matematiksel formül formatı olarak bilinen `latex` formatını

## ⚙ Entagrasyon Yönetimi

### 🙋‍ Karşılama Ekranı

Markdown dosyasının en tepesine `description` alanı oluşturulur.

```md
---
description: İçeriği açıklayan kısa not
---

# İçerik Başlığı
...
```

### 🗂 `Summary.md` Dosyası

**Basit Örnek:**
```md
# Summary

* [Part I](part1/README.md)
    * [Writing is nice](part1/writing.md)
    * [GitBook is nice](part1/gitbook.md)
* [Part II](part2/README.md)
    * [We love feedback](part2/feedback_please.md)
    * [Better tools for authors](part2/better_tools.md)
```

**Linkleri parçalara ayırma:**
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

**Çok fazla parçalı örnek:**

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

## 🐞 Hata Çözümleri

### Github Export Sorunları

Aşağıdakı durumlarda bu tarz hatalar gelmektedir:

- `SUMMARY.md` yapısının düzgün olmaması
- Markdown formatında sorun oluşması

### Linklerin Güncel Olmama Sorunu

Sayfalardaki linkler veya içerikler, o sayfada değişiklik olmadığı sürece değişmez

- Sayfa linkleri eski commit'lere bağlı kalır
- Bunu engellemek için o sayfada bir değişiklik yapılması gerekir
- Değişiklik sonunda güncel commit'e bağlı linkler oluşacaktır

## 🔗 Harici Bağlantılar

- [Proje Dizin Yapısı](https://github.com/GitbookIO/gitbook/blob/master/docs/structure.md)
- [Sayfa ve İndeksleme](https://github.com/GitbookIO/gitbook/blob/master/docs/pages.md)
- [Değişkenler](https://github.com/GitbookIO/gitbook/blob/master/docs/templating/variables.md)
