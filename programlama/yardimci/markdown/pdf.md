---
description: Markdown verilerini VSCode üzerinde PDF'e çevirme
---

# 🧾 Markdown to PDF

## 🔰 Markdown PDF Hakkında

* PDF oluşumu için yeni sayfaya geçmek için `md` dosyasına `<div class="page"/>` satırını yazman gerekmekte
  * Yaklaşık **40** satırda bir yeni sayfaya geçmek mantıklı
  * Bu sayda metnini otomatik ekleyen script yazılabilir

## 🧮 Latex Desteği

Dokümanda _latex_ varsa, `md` dosyasının en altına, latex scipt'ini eklemen gerekmektedir

```markup
<script
  type="text/javascript"
  src="http://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML"
></script>
<script type="text/x-mathjax-config">
  MathJax.Hub.Config({ tex2jax: {inlineMath: [['$', '$']]}, messageStyle: "none" });
</script>
```

{% hint style="info" %}
🧙‍♂️  Ek olarak buradaki yöntemi de deneyebilirsin.
{% endhint %}

## ✍ Markdown Imzam

```text
<!-- > *Yunus Emre Ak* ile çalışılmıştır. -->

Bu yazı **MIT** lisanslıdır. Lisanslar hakkında bilgi almak için [buraya](https://choosealicense.com/licenses/) bakmanda fayda var.

- Copyright © ~ _Yunus Emre AK_

<script type="text/javascript" src="http://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML"></script>
<script type="text/x-mathjax-config">
    MathJax.Hub.Config({ tex2jax: {inlineMath: [['$', '$']]}, messageStyle: "none" });
</script>

<br>
<br>
<br>
<br>
<br>

---

![PDF Yapısı Hakkında Bilgilendirme](https://bit.ly/2QmZtIc)

---

<div class="page"/>
```

## 🌠 Özelleştirmem

* Css dosyamı [buradan](https://github.com/yedhrab/YWiki/tree/169abadfd1b8862c004399268f6ca1f9f9359d61/1%20-%20Programlama%20Notları/res/markdown-pdf.css) indirebilirsin
* VsCode üzerinden ayarlara `"markdown-pdf.styles"` komutu ile `css` dosyasının yolunu belirtin
* Link: `http://tiny.cc/yek86y`

## 🔨 VsCode Ayarları

```javascript
{
  // Markdown PDF ayarları
  "markdown-pdf.outputDirectory": "Dökümanlar",
  "markdown-pdf.styles": ["http://tiny.cc/yek86y"],
  "markdown-pdf.headerTemplate": "<div style=\"width: 100%; font-size: 7px; margin: 0 auto; font: Segoe UI Light; text-align: center;\"><div style=\"float: left; width: 33.33%;\"><a style='text-decoration: none; font: Risque; color: red;' href='https://gogetfunding.com/yemreak/'>Destek ❤</a></div><div style=\"float: left; width: 33.33%;\"><a style='text-decoration: none; color: navy;' href='https://www.yemreak.com'>Yunus Emre Ak ©</a></div><div style=\"float: left; font-size: 7px; width: 33.33%; color: gainsboro;\"><span class='date'></span></div></div>",
  "markdown-pdf.footerTemplate": "<div style=\"width: 100%; font-size: 7px; margin: 0 auto; font: Segoe UI Light\"> <div style=\"float: left; width: 20%; text-align: center\"><a style=\"text-decoration: none; display: inline-block; color: dodgerblue;\" href=\"https://yemreak.com\">Website</a></div><div style=\"float: left; width: 20%; text-align: center\"><a style=\"text-decoration: none; display: inline-block; color: dodgerblue;\" href=\"https://github.com/yedhrab \">Github</a></div><div style=\"float: left; width: 20%; text-align: center\"><span class=\"pageNumber \">3 </span> / <span class=\"totalPages \"> 5</span></div><div style=\"float: left; width: 20%; text-align: center\"><a style=\"text-decoration: none; display: inline-block; color: dodgerblue;\" href=\"https://www.linkedin.com/in/yemreak/\">LinkedIn</a></div><div style=\"float: left; width: 20%; text-align: center\"><a style=\"text-decoration: none; display: inline-block; color: dodgerblue;\" href=\"mailto::yedhrab@gmail.com?subject=YPDF%20%7C%20Github\">İletişim</a></div></div>"
}
```

## 🐞 Emoji Fontlarının Gözükmemesi

```bash
sudo apt install fonts-noto-color-emoji
```

## 🐞 Dosya Boyutu Sorunu

Dosya boyutunu düşürmek için:

* Emojilerin kaldırılması 😢 \(~ 7MB\)
* Chromium \(~ 3MB\)

> Emoji sorunu sadece linux'ta var.

