---
description: GitBook'u GitHub'tan farklı kılan yönler.
---

# 🌟 GitBook Farklılıkları

## 📌 Önemli Notlar

GitBook'a 🚙 geçiş yapmadan önce bilinmesi gerekenler

* Kaynakları \(resim, PDF vs\) GitHub üzerinden çekebilmekte
* GitHub ile 💫 senkronize çalışır

> GitBook'da gömülü içerikler için [GitBook Embeds](https://docs.gitbook.com/content-editing/embeds) sayfasına bakabilirsin.

## 💔 Desteklemedikleri

* `###`'ten fazla markdown headerı
* Açılır menü yapısı olan `<detail>` formatı
* Buton yapısı olan `<kdb>` formatı
* GitHub submodule'leri
* Markdown \(`md`\) dışındaki dosyalar

## 💞 Ek Olarak Destekledikleri

* Harici bağlantılar için ön izleme desteği
* 🔗 Anchor Link'ler için url değiştirme
* `SUMMARY.md` ile sol kenarda gösterilen dizin yapısını düzenleme
* `README.md`'yi otomatik olarak algılama
* Matematiksel formül formatı olarak bilinen `latex` formatını `$$a=1$$`
  * `$$$$ a $$$$` yapısını da destekler
  * Özetle `$` yerine `$$` kullanmanız gerekmekte
* `.bookignore` ile GitHub'dan aktarılmayacak dosyaları belirleme
* Kendi linkleri **.gitbook/assets** dizinindeki dosyalara yapılmakta
  * URL: `{% embed url="https://www.google.com/glass/start/" %}`
    * 2 dizin içeride olan bir dosya için yazılmıştır
  * Dosya: `{% file src="../../.gitbook/assets/örnek.pdf" %}` şeklindedir
  * İpucu: `{% hint style="info" %} İpucu {% endhint %}`
  * Sayfa: `{% page-ref page="ozel-karakterli-sayfa/" %}`

## 🔗 Harici Bağlantılar

* [Proje Dizin Yapısı](https://github.com/GitbookIO/gitbook/blob/master/docs/structure.md)
* [Sayfa ve İndeksleme](https://github.com/GitbookIO/gitbook/blob/master/docs/pages.md)
* [Değişkenler](https://github.com/GitbookIO/gitbook/blob/master/docs/templating/variables.md)

