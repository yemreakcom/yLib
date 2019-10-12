---
description: GitBook, GitHub dökümantasyonlarımızı daha güzel bir arayüz ve hızlı arama özelliği ile sunan yardımcı bir platformdur
---

# 📖 GitBook Notları

## 📌 Önemli Notlar

GitBook'a 🚙 geçiş yapmadan önce bilinmesi gerekenler

- Kaynakları (resim, PDF vs) GitHub üzerinden çekebilmekte
  - Kendi linkleri **.gitbook/assets** dizinindeki dosyalara yapılmakta
  - `{% file src="../../.gitbook/assets/örnek.pdf" %}` şeklindedir
    - 2 dizin içeride olan bir dosya için yazılmıştır
- GitHub ile 💫 senkronize çalışır 

### 💔 Desteklemedikleri

- Açılır menü yapısı olan `<detail>` formatı
- Buton yapısı olan `<kdb>` formatı
- Github submodule'leri
- Markdown (`md`) dışındaki dosyalar

### 💞 Ek Olarak Destekledikleri

- `SUMMARY.md` ile sol kenarda gösterilen dizin yapısını düzenleme
- `README.md`'yi otomatik olarak algılama
- Matematiksel formül formatı olarak bilinen `latex` formatını `$$a=1$$`
- `.bookignore` ile GitHub'dan aktarılmayacak dosyaları belirleme

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

Temel amacı githubdaki dosyalarımızın sitenin sol kısmında (navigation):

- Hangi isimle gösterileceği
- Hangi dosyaların veya klasörlerin görünür olacağı
- Hangi sırada gözükeceği

gibi sorulara çözüm bulmaktır.

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

## 👨‍💻 GitBook Scriptlerim

[YGitBookIntegration](https://github.com/yedhrab/YGitBookIntegration) repom ile 🐙 GitHub - GitBook 📖 entegrasyonunu sağlayabilirsin.

- `SUMMARY.md` oluşturma
- Markdown olmayan dosyalar için GitHub linkleri oluşturma
  - Markdown olmayan dosyalar GitBook'da gözükmez

> ⚙ Kişiselleştirmek istersen, [YPackage](https://pypi.org/project/ypackage/) üzerinde GitBook scriptlerim mevcuttur.

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
