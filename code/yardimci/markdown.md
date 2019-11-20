---
description: GitHub README gibi alanlarda kullanılan derlenebilir yazım formatıdır
---

# 📑 Markdown

## 🧱 Temel Formatlar

* `*[metin]*` Metni italik \(eğik\) yazma
* `**[metin]**` Metni bold \(kalın\) yazma
* 2 kez SPACE karakteri ile **satır** atlatabilirsiniz
* \ Karakteri ile karakterleri biçimlendirmeden uzak tutabilirsin `\\`
* \` karakteri ile `<code>` etiketli metin yazabilirsin
  * Metni biçimlendirmeden uzak tutar
* `-` ile maddesel yapı oluşturabilirsin.
* `$ $` karakterleri arasına **latex** \(matematiksel formül\) yazabilirsin
  * `$$` ile çok satırlı matematiksel formül yazabilirsin
* `<kbd>Buton</kbd>` ile Buton oluşturabilirsiniz
  * Temel butonların kullanım örnekleri:
    * Tab ⭾
    * ❖ Win
    * ⇧ Shift
    * ⇪ Caps Lock
    * ⇭ NumLock
    * ↩ Enter
    * ▤ Menu
    * ⎋ Esc
    * ⌫ Backspace
    * ⌦ Del
    * ⎀ Insert
    * ↑ ↓ ← → Arrow
    * ✲ Ctrl
    * ⎇ Alt
  * Daha fazlası için [buraya](http://xahlee.info/comp/unicode_computing_symbols.html) bakabilirsin

## 🔗 Bağlantı Verme

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

> Kaynak için [buraya](https://css-tricks.com/snippets/html/mailto-links/) tıklayabilirsin

### ⭐ Başlık Linkleri Oluşturma

> `<a name="link_ismi"></a>` ile başlıklarına `#` ön eki ile erişebileceğin bağlantılar oluşturabilirsin.

> [Cross-reference \(named anchor\) in markdown](https://stackoverflow.com/a/7335259/9770490)

### 🔪 Satır içi Bağlantı \(Inline Link\)

`[metin](url)` yapısı ile metne _inline link_ verebilirsin. [Test](https://yemreak.com)

> _Dynamic link_'te `[]` kullanıldığına dikkat ediniz.

### 🌠 Dinamik Bağlantı \(Dynamic Link\)

Alttaki yapı ile metne _dynamic link_ verebilirsin. [Test](https://www.yemreak.com)

```text
[Test][test]

- [test]: https://www.yemreak.com "Açıklama Metni"
```

> _Inline link_'te `()` kullanıldığına dikkat ediniz.

### 🎨 Resim Bağlantısı

`![resim_açıklaması][resim_urli]` yapısı ile yazına resim yerleştirebilirsin.

> GIF'i de destekler

## 📊 Tablo Oluşturma

```text
| Tables   |      Are      |   Cool |
| -------- | :-----------: | -----: |
| col 1 is | left-aligned  | \$1600 |
| col 2 is |   centered    |   \$12 |
| col 3 is | right-aligned |    \$1 |
```

| Tables | Are | Cool |
| :--- | :---: | ---: |
| col 1 is | left-aligned | $1600 |
| col 2 is | centered | $12 |
| col 3 is | right-aligned | $1 |

## 📋 Açılır Menü Oluşturma

* `details` etiketi ile açılır menü oluşturulur
* `summary` kısmı görünen metindir

> `summary` alanında sonra boş satır olmazsa içerisindeki markdown işlenmez, olduğu gibi gözükür

```text
<details>
<summary>Görünen metin</summary>

- Detaylar

</details>
```

Görünen metin - Detaylar

## 🔢 Matematik Denklemleri

Detaylı bilgi için [buraya](https://csrgxtu.github.io/2015/03/20/Writing-Mathematic-Fomulars-in-Markdown/) bakabilirsin.

* Latex listesi için [buraya](https://oeis.org/wiki/List_of_LaTeX_mathematical_symbols) bakabilirsin
* Latex sembolleri için [buraya](https://artofproblemsolving.com/wiki/index.php/LaTeX:Symbols) bakabilirsin

> Online editör için [buraya](https://www.codecogs.com/latex/eqneditor.php) bakabilirsin.

### 🧬 Formül Yapısı

$$z^{[1] (i)} = W^{[1]} x^{(i)} + b^{[1]}\tag{1}$$ $$a^{[1] (i)} = \tanh(z^{[1] (i)})\tag{2}$$ $$z^{[2] (i)} = W^{[2]} a^{[1] (i)} + b^{[2]}\tag{3}$$ $$\hat{y}^{(i)} = a^{[2] (i)} = \sigma(z^{ [2] (i)})\tag{4}$$ $$y^{(i)}_{prediction} = \begin{cases} 1 & \mbox{if } a^{[2](i)} > 0.5 \\ 0 & \mbox{otherwise } \end{cases}\tag{5}$$ $$J = - \frac{1}{m} \sum\limits_{i = 0}^{m} \large\left(\small y^{(i)}\log\left(a^{[2] (i)}\right) + (1-y^{(i)})\log\left(1- a^{[2] (i)}\right) \large \right) \small \tag{6}$$

```text
$$z^{[1] (i)} =  W^{[1]} x^{(i)} + b^{[1]}\tag{1}$$
$$a^{[1] (i)} = \tanh(z^{[1] (i)})\tag{2}$$
$$z^{[2] (i)} = W^{[2]} a^{[1] (i)} + b^{[2]}\tag{3}$$
$$\hat{y}^{(i)} = a^{[2] (i)} = \sigma(z^{ [2] (i)})\tag{4}$$
$$y^{(i)}_{prediction} = \begin{cases} 1 & \mbox{if } a^{[2](i)} > 0.5 \\ 0 & \mbox{otherwise } \end{cases}\tag{5}$$
$$J = - \frac{1}{m} \sum\limits_{i = 0}^{m} \large\left(\small y^{(i)}\log\left(a^{[2] (i)}\right) + (1-y^{(i)})\log\left(1- a^{[2] (i)}\right)  \large  \right) \small \tag{6}$$
```

## ✨ Sık Kullanılan Rozetler \(Badge\)

Rozet yapımı için [buraya](https://shields.io/) bakabilirsin.

* [Vscode Rozetleri](https://vsmarketplacebadge.apphb.com/)

![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)

![licanse apache](https://img.shields.io/hexpm/l/plug.svg?style=plastic)

![quality](https://img.shields.io/ansible/quality/432.svg)

![status](https://img.shields.io/nodeping/status/jkiwn052-ntpp-4lbb-8d45-ihew6d9ucoei.svg)

## 🆚 VsCode için Markdown

### 📖 VsCode için Markdown Snippets

```javascript
{
  // Place your snippets for markdown here. Each snippet is defined under a snippet name and has a prefix, body and
  // description. The prefix is what is used to trigger the snippet and the body will be expanded and inserted. Possible variables are:
  // $1, $2 for tab stops, $0 for the final cursor position, and ${1:label}, ${2:another} for placeholders. Placeholders with the
  // same ids are connected.
  // Example:
  // "Print to console": {
  //     "prefix": "log",
  //     "body": [
  //         "console.log('$1');",
  //         "$2"
  //     ],
  //     "description": "Log output to console"
  // }
  "Markdown için buton etiketi": {
    "prefix": "kbd",
    "body": "<kbd>$1</kbd>$0",
    "description": "Buton tanımlama"
  },
  "Markdown omit in toc": {
    "prefix": "omit",
    "body": "$0",
    "description": "ToC dışında tutma metni"
  }
}
```

### 🔌 VsCode için Faydalı Eklentiler

| Eklenti | Açıklama |
| :--- | :--- |
| [Markdown All in One](https://marketplace.visualstudio.com/items?itemName=yzhang.markdown-all-in-one) | Markdown için gerekli tüm içeriklere, kısayollara ve formatlayıcıya sahip |
| [markdownlint](https://marketplace.visualstudio.com/items?itemName=DavidAnson.vscode-markdownlint) | Markdown hatalarının altını çizme ve uyarma |
| [Markdown PDF](https://marketplace.visualstudio.com/items?itemName=yzane.markdown-pdf) | Markdown'u PDF'e çevirme |
| [ToDo Tree](https://marketplace.visualstudio.com/items?itemName=Gruntfuggly.todo-tree) | Yapılacakları derleme ve arayüzde sunma |
| [Paste Image](https://marketplace.visualstudio.com/items?itemName=mushan.vscode-paste-image) | Panodan resim kopyalama |

### 🧾 Markdown to PDF

* PDF oluşumu için yeni sayfaya geçmek için `md` dosyasına `<div class="page"/>` satırını yazman gerekmekte
  * Yaklaşık **40** satırda bir yeni sayfaya geçmek mantıklı
  * Bu sayda metnini otomatik ekleyen script yazılabilir
* Dökümanda _latex_ varsa, `md` dosyasının en altında, latex scipt'ini eklemen gerekmektedir
  * Aksi halde _latex_ yapısı derlenmez.

```markup
<script
  type="text/javascript"
  src="http://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML"
></script>
<script type="text/x-mathjax-config">
  MathJax.Hub.Config({ tex2jax: {inlineMath: [['$', '$']]}, messageStyle: "none" });
</script>
```

#### ✍ PDF için Markdown Imzam

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

#### 🌠 PDF için Özelleştirmem

* Css dosyamı [buradan](https://github.com/yedhrab/YWiki/tree/169abadfd1b8862c004399268f6ca1f9f9359d61/1%20-%20Programlama%20Notları/res/markdown-pdf.css) indirebilirsin
* VsCode üzerinden ayarlara `"markdown-pdf.styles"` komutu ile `css` dosyasının yolunu belirtin
* Link: `http://tiny.cc/yek86y`

\`\`

#### 🔨 PDF için VsCode Ayarları

```javascript
{
  // Markdown PDF ayarları
  "markdown-pdf.outputDirectory": "Dökümanlar",
  "markdown-pdf.styles": ["http://tiny.cc/yek86y"],
  "markdown-pdf.headerTemplate": "<div style=\"width: 100%; font-size: 7px; margin: 0 auto; font: Segoe UI Light; text-align: center;\"><div style=\"float: left; width: 33.33%;\"><a style='text-decoration: none; font: Risque; color: red;' href='https://gogetfunding.com/yemreak/'>Destek ❤</a></div><div style=\"float: left; width: 33.33%;\"><a style='text-decoration: none; color: navy;' href='https://www.yemreak.com'>Yunus Emre Ak ©</a></div><div style=\"float: left; font-size: 7px; width: 33.33%; color: gainsboro;\"><span class='date'></span></div></div>",
  "markdown-pdf.footerTemplate": "<div style=\"width: 100%; font-size: 7px; margin: 0 auto; font: Segoe UI Light\"> <div style=\"float: left; width: 20%; text-align: center\"><a style=\"text-decoration: none; display: inline-block; color: dodgerblue;\" href=\"https://yemreak.com\">Website</a></div><div style=\"float: left; width: 20%; text-align: center\"><a style=\"text-decoration: none; display: inline-block; color: dodgerblue;\" href=\"https://github.com/yedhrab \">Github</a></div><div style=\"float: left; width: 20%; text-align: center\"><span class=\"pageNumber \">3 </span> / <span class=\"totalPages \"> 5</span></div><div style=\"float: left; width: 20%; text-align: center\"><a style=\"text-decoration: none; display: inline-block; color: dodgerblue;\" href=\"https://www.linkedin.com/in/yemreak/\">LinkedIn</a></div><div style=\"float: left; width: 20%; text-align: center\"><a style=\"text-decoration: none; display: inline-block; color: dodgerblue;\" href=\"mailto::yedhrab@gmail.com?subject=YPDF%20%7C%20Github\">İletişim</a></div></div>"
}
```

#### 🐞 PDF'te Emoji Fontlarının Gözükmemesi

```bash
sudo apt install fonts-noto-color-emoji
```

#### 🐞 PDF Dosya Boyutu Sorunu

Dosya boyutunu düşürmek için:

* Emojilerin kaldırılması 😢 \(~ 7MB\)
* Chromium \(~ 3MB\)

> Emoji sorunu sadece linux'ta var.

## 💎 Markdown Regexleri

### 🔗 Tüm Linkleri Bulma

```python
\[([^\[]+)\](\(.*\)) # Tüm linkleri bulma (https://regex101.com/r/m9dndl/6)
```

{% hint style="info" %}
🧐 Detaylı bilgi için [Regex to match markdown links](https://davidwells.io/snippets/regex-match-markdown-links) bağlantısına bakabilirsin.
{% endhint %}

### 💫 Statik linkleri dinamik yapma

```javascript
// node main.js test.md result.md

var fs = require('fs')
fs.readFile(process.argv[2], 'utf8', function (err, markdown) {
    if (err) {
        return console.log(err);
    }
    var counter = 1;
    var matches = {};
    var matcher = /\[.*?\]\((.*?)\)/g;
    while (match = matcher.exec(markdown)) {
        if (!matches[match[1]]) matches[match[1]] = counter++;
    }
    console.log(matches);
    Object.keys(matches).forEach(function(url) {
        var r = new RegExp("(\\[.*?\\])\\(" + url + "\\)", "g");
        markdown = markdown.replace(r, "$1[" + matches[url] + "]");
        markdown += "\n[" + matches[url] + "]: " + url;
    });

    fs.writeFile(process.argv[3], markdown, 'utf8', function (err) {
        if (err) return console.log(err);
    });

});
```

{% hint style="info" %}
🧐 Detaylı bilgi için [Convert markdown links from inline to reference](https://stackoverflow.com/questions/30917399/convert-markdown-links-from-inline-to-reference) bağlantısına bakabilirsin.
{% endhint %}

## 🔗 Faydalı Siteler

| Site | Açıklama |
| :--- | :--- |
| [Url Encoder](https://www.urlencoder.org/) | Link URL'leri oluşturma |
| [StackEdit](https://stackedit.io) | Çevrimiçi markdown editörü |

* [Mastering Markdown](https://guides.github.com/features/mastering-markdown/)
* [Markdown Cheat Sheet](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet)
* [https://html.com/attributes/a-href/](https://html.com/attributes/a-href/)
* [Markdown and Visual Studio Codes](https://code.visualstudio.com/docs/languages/markdown)

