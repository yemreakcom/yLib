# Markdowns <!-- omit in toc -->

Ek kaynak için [buraya](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet) tıklayabilirsin.

## İçerikler <!-- omit in toc -->

> `HOME` tuşu ile yukarı yönlenebilrsiniz.

- [Kullanım Örnekleri](#Kullan%C4%B1m-%C3%96rnekleri)
- [Temel Formatlar](#Temel-Formatlar)
- [Bağlantı Verme](#Ba%C4%9Flant%C4%B1-Verme)
  - [Satıriçi Bağlantı (Inline Link)](#Sat%C4%B1ri%C3%A7i-Ba%C4%9Flant%C4%B1-Inline-Link)
  - [Dinamik Bağlantı (Dynamic Link)](#Dinamik-Ba%C4%9Flant%C4%B1-Dynamic-Link)
  - [Resim Bağlantısı](#Resim-Ba%C4%9Flant%C4%B1s%C4%B1)
- [Tablo Oluşturma](#Tablo-Olu%C5%9Fturma)
- [Açılır Menü Oluşturma](#A%C3%A7%C4%B1l%C4%B1r-Men%C3%BC-Olu%C5%9Fturma)
- [Matematik Denklemleri](#Matematik-Denklemleri)
  - [Formül Yapısı](#Form%C3%BCl-Yap%C4%B1s%C4%B1)
- [Sık Kullanılan Rozetler (Badge)](#S%C4%B1k-Kullan%C4%B1lan-Rozetler-Badge)
- [VsCode için Markdown](#VsCode-i%C3%A7in-Markdown)
  - [VsCode için Markdown Snippets](#VsCode-i%C3%A7in-Markdown-Snippets)
  - [VsCode için Faydalı Eklentiler](#VsCode-i%C3%A7in-Faydal%C4%B1-Eklentiler)
  - [Markdown PDF](#Markdown-PDF)
    - [PDF için Markdown Imzam](#PDF-i%C3%A7in-Markdown-Imzam)
    - [PDF için Özelleştirmem](#PDF-i%C3%A7in-%C3%96zelle%C5%9Ftirmem)
    - [PDF için VsCode Ayarları](#PDF-i%C3%A7in-VsCode-Ayarlar%C4%B1)
    - [PDF'te Emoji Fontlarının Gözükmemesi](#PDFte-Emoji-Fontlar%C4%B1n%C4%B1n-G%C3%B6z%C3%BCkmemesi)
    - [PDF Dosya Boyutu Sorunu](#PDF-Dosya-Boyutu-Sorunu)
- [Faydalı Siteler](#Faydal%C4%B1-Siteler)
- [Harici Bağlantılar](#Harici-Ba%C4%9Flant%C4%B1lar)

## Kullanım Örnekleri

Detaylar için [buraya](https://guides.github.com/features/mastering-markdown/) tıklayabilirsin.

> HTML etiketlerini destekler.

## Temel Formatlar

- `*[metin]*` Metni italik (eğik) yazma
- `**[metin]**` Metni bold (kalın) yazma
- 2 kez <kbd>SPACE</kbd> karakteri ile **satır** atlatabilirsiniz
- \\ Karakteri ile karakterleri biçimlendirmeden uzak tutabilirsin `\\`
- \` karakteri ile `<code>` etiketli metin yazabilirsin
  - Metni biçimlendirmeden uzak tutar
- `-` ile maddesel yapı oluşturabilirsin.
- `$ $` karakterleri arasına **latex** (matematiksel formül) yazabilirsin
  - `$$` ile çok satırlı matematiksel formül yazabilirsin
- `<kbd>Buton</kbd>` ile <kbd>Buton</kbd> oluşturabilirsiniz
  - Özel butonlar: <kbd>Tab ⭾</kbd> <kbd>❖ Win</kbd> <kbd>⇧ Shift</kbd> <kbd>⇪ Caps Lock</kbd> <kbd>⇭ NumLock</kbd> <kbd>↩ Enter</kbd> <kbd>▤ Menu</kbd> <kbd>⎋ Esc</kbd> <kbd>⌫ Backspace</kbd> <kbd>⌦ Del</kbd> <kbd>⎀ Insert</kbd> <kbd>↑ ↓ ← → Arrow</kbd> <kbd>✲ Ctrl</kbd> <kbd>⎇ Alt</kbd>
  - Daha fazlası için [buraya](http://xahlee.info/comp/unicode_computing_symbols.html) bakabilirsin

## Bağlantı Verme

Link işlemleri için bilgiler. Kaynak için [buraya](https://css-tricks.com/snippets/html/mailto-links/) tıklayabilirsin.

| İstek            | Anahtar           |
| ---------------- | ----------------- |
| Site             | `https://<link>`  |
| Mail             | `mailto:<eposta>` |
| Telefon          | `tel:<numara>`    |
| Başlıklar arası  | `#<başlık>`       |
| Aynı dizinden    | `./<yol>`         |
| Bir üst dizinden | `../<yol>`        |

> Bağlantı verme işlemlerinde özel karakter kullanmak için kodlama yapmanız gerekmekte. Kodlama yapan online site için [buraya](https://www.urlencoder.org/) tıklaytabilirsin. Siteye yol verini kopyalayıp _encoded_ demeniz yeterli

- [Test](../Markdown#ba%C4%9Flant%C4%B1-verme) `[Test](../Markdown#ba%C4%9Flant%C4%B1-verme)`
- `%20` Boşluk karakteri

### Satıriçi Bağlantı (Inline Link)

`[metin](url)` yapısı ile metne _inline link_ verebilirsin. [Test](https://yemreak.com)

> _Dynamic link_'te `[]` kullanıldığına dikkat ediniz.

### Dinamik Bağlantı (Dynamic Link)

Alttaki yapı ile metne _dynamic link_ verebilirsin. [Test][test]

```md
[Test][test]

- [test]: https://www.yemreak.com
```

[test]: https://www.yemreak.com

> _Inline link_'te `()` kullanıldığına dikkat ediniz.

### Resim Bağlantısı

`![resim_açıklaması][resim_urli]` yapısı ile yazına resim yerleştirebilirsin.

> GIF'i de destekler

## Tablo Oluşturma

```markdown
| Tables   |      Are      |   Cool |
| -------- | :-----------: | -----: |
| col 1 is | left-aligned  | \$1600 |
| col 2 is |   centered    |   \$12 |
| col 3 is | right-aligned |    \$1 |
```

| Tables   |      Are      |   Cool |
| -------- | :-----------: | -----: |
| col 1 is | left-aligned  | \$1600 |
| col 2 is |   centered    |   \$12 |
| col 3 is | right-aligned |    \$1 |

## Açılır Menü Oluşturma

- `details` etiketi ile açılır menü oluşturulur
- `summary` kısmı görünen metindir

> `summary` alanında sonra boş satır olmazsa içerisindeki markdown işlenmez, olduğu gibi gözükür

```md
<details>
<summary>Görünen metin</summary>

- Detaylar

</details>
```

<details>
<summary>Görünen metin</summary>

- Detaylar

</details>

## Matematik Denklemleri

Detaylı bilgi için [buraya](https://csrgxtu.github.io/2015/03/20/Writing-Mathematic-Fomulars-in-Markdown/) bakabilirsin.

- Latex listesi için [buraya](https://oeis.org/wiki/List_of_LaTeX_mathematical_symbols) bakabilirsin
- Latex sembolleri için [buraya](https://artofproblemsolving.com/wiki/index.php/LaTeX:Symbols) bakabilirsin

> Online editör için [buraya](https://www.codecogs.com/latex/eqneditor.php) bakabilirsin.

### Formül Yapısı

$$z^{[1] (i)} =  W^{[1]} x^{(i)} + b^{[1]}\tag{1}$$
$$a^{[1] (i)} = \tanh(z^{[1] (i)})\tag{2}$$
$$z^{[2] (i)} = W^{[2]} a^{[1] (i)} + b^{[2]}\tag{3}$$
$$\hat{y}^{(i)} = a^{[2] (i)} = \sigma(z^{ [2] (i)})\tag{4}$$
$$y^{(i)}_{prediction} = \begin{cases} 1 & \mbox{if } a^{[2](i)} > 0.5 \\ 0 & \mbox{otherwise } \end{cases}\tag{5}$$
$$J = - \frac{1}{m} \sum\limits_{i = 0}^{m} \large\left(\small y^{(i)}\log\left(a^{[2] (i)}\right) + (1-y^{(i)})\log\left(1- a^{[2] (i)}\right)  \large  \right) \small \tag{6}$$

```latex
$$z^{[1] (i)} =  W^{[1]} x^{(i)} + b^{[1]}\tag{1}$$
$$a^{[1] (i)} = \tanh(z^{[1] (i)})\tag{2}$$
$$z^{[2] (i)} = W^{[2]} a^{[1] (i)} + b^{[2]}\tag{3}$$
$$\hat{y}^{(i)} = a^{[2] (i)} = \sigma(z^{ [2] (i)})\tag{4}$$
$$y^{(i)}_{prediction} = \begin{cases} 1 & \mbox{if } a^{[2](i)} > 0.5 \\ 0 & \mbox{otherwise } \end{cases}\tag{5}$$
$$J = - \frac{1}{m} \sum\limits_{i = 0}^{m} \large\left(\small y^{(i)}\log\left(a^{[2] (i)}\right) + (1-y^{(i)})\log\left(1- a^{[2] (i)}\right)  \large  \right) \small \tag{6}$$
```

## Sık Kullanılan Rozetler (Badge)

Rozet yapımı için [buraya](https://shields.io/) bakabilirsin.

- [Vscode Rozetleri](https://vsmarketplacebadge.apphb.com/)

![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)

![licanse apache](https://img.shields.io/hexpm/l/plug.svg?style=plastic)

![quality](https://img.shields.io/ansible/quality/432.svg)

![status](https://img.shields.io/nodeping/status/jkiwn052-ntpp-4lbb-8d45-ihew6d9ucoei.svg)

## VsCode için Markdown

### VsCode için Markdown Snippets

```json
{
  // Place your snippets for markdown here. Each snippet is defined under a snippet name and has a prefix, body and
  // description. The prefix is what is used to trigger the snippet and the body will be expanded and inserted. Possible variables are:
  // $1, $2 for tab stops, $0 for the final cursor position, and ${1:label}, ${2:another} for placeholders. Placeholders with the
  // same ids are connected.
  // Example:
  // "Print to console": {
  // 	"prefix": "log",
  // 	"body": [
  // 		"console.log('$1');",
  // 		"$2"
  // 	],
  // 	"description": "Log output to console"
  // }
  "Markdown için buton etiketi": {
    "prefix": "kbd",
    "body": "<kbd>$1</kbd>$0",
    "description": "Buton tanımlama"
  },
  "Markdown omit in toc": {
    "prefix": "omit",
    "body": "<!-- omit in toc -->$0",
    "description": "ToC dışında tutma metni"
  }
}
```

### VsCode için Faydalı Eklentiler

| Eklenti                                                                                               | Açıklama                                                                  |
| ----------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------- |
| [Markdown All in One](https://marketplace.visualstudio.com/items?itemName=yzhang.markdown-all-in-one) | Markdown için gerekli tüm içeriklere, kısayollara ve formatlayıcıya sahip |
| [markdownlint](https://marketplace.visualstudio.com/items?itemName=DavidAnson.vscode-markdownlint)    | Markdown hatalarının altını çizme ve uyarma                               |
| [Markdown PDF](https://marketplace.visualstudio.com/items?itemName=yzane.markdown-pdf)                | Markdown'u PDF'e çevirme                                                  |
| [ToDo Tree](https://marketplace.visualstudio.com/items?itemName=Gruntfuggly.todo-tree)                | Yapılacakları derleme ve arayüzde sunma                                   |
| [Paste Image](https://marketplace.visualstudio.com/items?itemName=mushan.vscode-paste-image)          | Panodan resim kopyalama                                                   |

### Markdown PDF

- PDF oluşumu için yeni sayfaya geçmek için `md` dosyasına `<div class="page"/>` satırını yazman gerekmekte
  - Yaklaşık **40** satırda bir yeni sayfaya geçmek mantıklı
  - Bu sayda metnini otomatik ekleyen script yazılabilir
- Dökümanda _latex_ varsa, `md` dosyasının en altında, latex scipt'ini eklemen gerekmektedir
  - Aksi halde _latex_ yapısı derlenmez.

```html
<script
  type="text/javascript"
  src="http://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML"
></script>
<script type="text/x-mathjax-config">
  MathJax.Hub.Config({ tex2jax: {inlineMath: [['$', '$']]}, messageStyle: "none" });
</script>
```

#### PDF için Markdown Imzam

```md
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

#### PDF için Özelleştirmem

- Css dosyamı [buradan](../res/markdown-pdf.css) indirebilirsin
- VsCode üzerinden ayarlara `"markdown-pdf.styles"` komutu ile `css` dosyasının yolunu belirtin
- Link: `http://tiny.cc/yek86y`

![PDF Css](../res/pdf_structure.png)

#### PDF için VsCode Ayarları

```json
{
  // Markdown PDF ayarları
  "markdown-pdf.outputDirectory": "Dökümanlar",
  "markdown-pdf.styles": ["http://tiny.cc/yek86y"],
  "markdown-pdf.headerTemplate": "<div style=\"width: 100%; font-size: 7px; margin: 0 auto; font: Segoe UI Light; text-align: center;\"><div style=\"float: left; width: 33.33%;\"><a style='text-decoration: none; font: Risque; color: red;' href='https://gogetfunding.com/yemreak/'>Destek ❤</a></div><div style=\"float: left; width: 33.33%;\"><a style='text-decoration: none; color: navy;' href='https://www.yemreak.com'>Yunus Emre Ak ©</a></div><div style=\"float: left; font-size: 7px; width: 33.33%; color: gainsboro;\"><span class='date'></span></div></div>",
  "markdown-pdf.footerTemplate": "<div style=\"width: 100%; font-size: 7px; margin: 0 auto; font: Segoe UI Light\"> <div style=\"float: left; width: 20%; text-align: center\"><a style=\"text-decoration: none; display: inline-block; color: dodgerblue;\" href=\"https://yemreak.com\">Website</a></div><div style=\"float: left; width: 20%; text-align: center\"><a style=\"text-decoration: none; display: inline-block; color: dodgerblue;\" href=\"https://github.com/yedhrab \">Github</a></div><div style=\"float: left; width: 20%; text-align: center\"><span class=\"pageNumber \">3 </span> / <span class=\"totalPages \"> 5</span></div><div style=\"float: left; width: 20%; text-align: center\"><a style=\"text-decoration: none; display: inline-block; color: dodgerblue;\" href=\"https://www.linkedin.com/in/yemreak/\">LinkedIn</a></div><div style=\"float: left; width: 20%; text-align: center\"><a style=\"text-decoration: none; display: inline-block; color: dodgerblue;\" href=\"mailto::yedhrab@gmail.com?subject=YPDF%20%7C%20Github\">İletişim</a></div></div>"
}
```

#### PDF'te Emoji Fontlarının Gözükmemesi

```sh
sudo apt install fonts-noto-color-emoji
```

#### PDF Dosya Boyutu Sorunu

Dosya boyutunu düşürmek için:

- Emojilerin kaldırılması 😢 (~ 7MB)
- Chromium (~ 3MB)

> Emoji sorunu sadece linux'ta var.

## Faydalı Siteler

| Site                                       | Açıklama                   |
| ------------------------------------------ | -------------------------- |
| [Url Encoder](https://www.urlencoder.org/) | Link URL'leri oluşturma    |
| [StackEdit](https://stackedit.io)          | Çevrimiçi markdown editörü |

## Harici Bağlantılar

- <https://html.com/attributes/a-href/>
- [Markdown and Visual Studio Codes](https://code.visualstudio.com/docs/languages/markdown)
