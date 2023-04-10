---
description: GitBook'u GitHub'tan farklı kılan yönler.
---

# 🌟 GitBook Farklılıkları

## 🚀 Önemli Ayrıcalıkları

* 🔍 Tüm dokümanda **kelimesi kelimesine arama özelliği** sayesinde aradığını çok rahat bulabilirsin
* 📑 **Online editörü** ile markdown yazmakla uğraşmana gerek kalmaz
* ✨ Dokümanlarını **daha görsel** bir arayüzde sunarsın
* 📂 **Tab yapısı** ile birden fazla notu daha görsel bir arayüzle sunabilirsin, üstelik arama özelliği ile
* 🎴 [**Embed**](https://docs.gitbook.com/editing-content/embeds) \*\*\*\* destekleri sayesinde **📺 video, 📃 makale, 👨‍💻 gist hatta 🎶 müzik** bile paylaşabilirsin
* 💫 Kaynakları (resim, PDF vs) **GitHub üzerinden otomatik** olarak bağlamaktadır

## 💔 Desteklemedikleri

* 😥 `###`'ten fazla markdown başlıkları
* 🙇‍♂️ Açılır menü yapısı olan `<detail>` formatı
* 🔘 Buton yapısı olan `<kdb>` formatı
* 📁 GitHub submodule yapısı (bu yapı yerine [ysubmodules](https://github.com/yedhrab/YPackage#-entegrasyon-scripti) kullanabilirsin)
* 🙄 Markdown (`md`) dışındaki dosyalar

{% hint style="info" %}
GitBook için yazmış [YPackage](https://github.com/yedhrab/YPackage#-entegrasyon-scripti) olduğum entegrasyon scriptim ilgini çekebilir
{% endhint %}

## 💞 Ek Olarak Destekledikleri

* 👀 Harici bağlantılar için ön izleme desteği
* 🔗 Anchor Link'ler için url değiştirme
* 📑 `SUMMARY.md` ile sol kenarda gösterilen dizin yapısını düzenleme
* 📄 `README.md`'yi otomatik olarak algılama
* 🧮 Matematiksel formül formatı olarak bilinen `latex` formatını `$$a=1$$`
  * 👌 `$$$$ a $$$$` yapısını da destekler
  * 💁‍♂️ Özetle `$` yerine `$$` kullanmanız gerekmekte
* 📜 `.bookignore` ile GitHub'dan aktarılmayacak dosyaları belirleme

## 💡 Bilmen Gerekenler

* 📂 Kendi dosya linklerini **.gitbook/assets** dizinindeki dosyalara yapılmakta
  * URL: \`

{% embed url="https://www.google.com/glass/start/" %}

\` \* 2 dizin içeride olan bir dosya için yazılmıştır \* Dosya: \`

\` şeklindedir \* İpucu: \`

{% hint style="info" %}
İpucu
{% endhint %}

\` \* Sayfa: \`

{% content-ref url="https://github.com/YEmreAk/YLib/blob/master/proje-yonetimi/gitbook/ozel-karakterli-sayfa/README.md" %}
[https://github.com/YEmreAk/YLib/blob/master/proje-yonetimi/gitbook/ozel-karakterli-sayfa/README.md](https://github.com/YEmreAk/YLib/blob/master/proje-yonetimi/gitbook/ozel-karakterli-sayfa/README.md)
{% endcontent-ref %}

\`

## 🔗 Harici Bağlantılar

* [Proje Dizin Yapısı](https://github.com/GitbookIO/gitbook/blob/master/docs/structure.md)
* [Sayfa ve İndeksleme](https://github.com/GitbookIO/gitbook/blob/master/docs/pages.md)
* [Değişkenler](https://github.com/GitbookIO/gitbook/blob/master/docs/templating/variables.md)
