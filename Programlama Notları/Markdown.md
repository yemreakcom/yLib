# Markdowns <!-- omit in toc -->

Ek kaynak için [buraya](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet) tıklayabilirsin.

## İçerikler <!-- omit in toc -->

> `HOME` tuşu ile yukarı yönlenebilrsiniz.

- [Kullanım Örnekleri](#kullan%C4%B1m-%C3%B6rnekleri)
  - [Temel Formatlar](#temel-formatlar)
  - [Bağlantı Verme](#ba%C4%9Flant%C4%B1-verme)
    - [Satıriçi Bağlantı (Inline Link)](#sat%C4%B1ri%C3%A7i-ba%C4%9Flant%C4%B1-inline-link)
    - [Dinamik Bağlantı (Dynamic Link)](#dinamik-ba%C4%9Flant%C4%B1-dynamic-link)
    - [Resim Bağlantısı](#resim-ba%C4%9Flant%C4%B1s%C4%B1)
  - [Tablo Oluşturma](#tablo-olu%C5%9Fturma)
  - [Matematik Denklemleri](#matematik-denklemleri)
  - [Sık Kullanılan Rozetler](#s%C4%B1k-kullan%C4%B1lan-rozetler)
- [VsCode için Faydalı Eklentiler](#vscode-i%C3%A7in-faydal%C4%B1-eklentiler)
- [Faydalı Siteler](#faydal%C4%B1-siteler)
- [Harici Bağlantılar](#harici-ba%C4%9Flant%C4%B1lar)

## Kullanım Örnekleri

Detaylar için [buraya](https://guides.github.com/features/mastering-markdown/) tıklayabilirsin.

> HTML etiketlerini destekler.

### Temel Formatlar

- `*[metin]*` Metni italik (eğik) yazma
- `**[metin]**` Metni bold (kalın) yazma
- 2 kez <kbd>SPACE</kbd> karakteri ile **satır** atlatabilirsiniz
- \\ Karakteri ile karakterleri biçimlendirmeden uzak tutabilirsin `\\`
- \` karakteri ile `<code>` etiketli metin yazabilirsin
  - Metni biçimlendirmeden uzak tutar
- `-` ile maddesel yapı oluşturabilirsin.

### Bağlantı Verme

Link işlemleri için bilgiler. Kaynak için [buraya](https://css-tricks.com/snippets/html/mailto-links/) tıklayabilirsin.

| İstek            | Anahtar           |
| ---------------- | ----------------- |
| Site             | `https://<link>`  |
| Mail             | `mailto:<eposta>` |
| Telefon          | `tel:<numara>`    |
| Başlıklar arası  | `#<başlık>`       |
| Aynı dizinden    | `./<yol>`         |
| Bir üst dizinden | `../<yol>`        |

> Bağlantı verme işlemlerinde özel karakter kullanmak için kodlama yapmanız gerekmekte. Kodlama yapan online site için [buraya](https://www.urlencoder.org/) tıklaytabilirsin. Siteye yol verini kopyalayıp *encoded* demeniz yeterli

- [Test](../Markdown#ba%C4%9Flant%C4%B1-verme) `[Test](../Markdown#ba%C4%9Flant%C4%B1-verme)`
- `%20` Boşluk karakteri

#### Satıriçi Bağlantı (Inline Link)

`[metin](url)` yapısı ile metne *inline link* verebilirsin. [Test](https://yemreak.com)

> *Dynamic link*'te `[]` kullanıldığına dikkat ediniz.

#### Dinamik Bağlantı (Dynamic Link)

Alttaki yapı ile metne *dynamic link* verebilirsin. [Test][test]

```md
[Test][test]
- [test]: https://www.yemreak.com
```

[test]: https://www.yemreak.com

> *Inline link*'te `()` kullanıldığına dikkat ediniz.

#### Resim Bağlantısı

`![resim_açıklaması][resim_urli]` yapısı ile yazına resim yerleştirebilirsin.

### Tablo Oluşturma

```markdown
| Tables   |      Are      |  Cool |
| -------- | :-----------: | ----: |
| col 1 is | left-aligned  | $1600 |
| col 2 is |   centered    |   $12 |
| col 3 is | right-aligned |    $1 |
```

| Tables   |      Are      |  Cool |
| -------- | :-----------: | ----: |
| col 1 is | left-aligned  | $1600 |
| col 2 is |   centered    |   $12 |
| col 3 is | right-aligned |    $1 |

### Matematik Denklemleri

Detaylı bilgi için [buraya](https://csrgxtu.github.io/2015/03/20/Writing-Mathematic-Fomulars-in-Markdown/) bakabilirsin.

> Online editör için [buraya](https://www.codecogs.com/latex/eqneditor.php) bakabilirsin.

### Sık Kullanılan Rozetler

Rozet yapımı için [buraya](https://shields.io/) bakabilirsin.

![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)

![licanse apache](https://img.shields.io/hexpm/l/plug.svg?style=plastic)

![quality](https://img.shields.io/ansible/quality/432.svg)

![status](https://img.shields.io/nodeping/status/jkiwn052-ntpp-4lbb-8d45-ihew6d9ucoei.svg)

## VsCode için Faydalı Eklentiler

| Eklenti                                                                                               | Açıklama                                                                  |
| ----------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------- |
| [Markdown All in One](https://marketplace.visualstudio.com/items?itemName=yzhang.markdown-all-in-one) | Markdown için gerekli tüm içeriklere, kısayollara ve formatlayıcıya sahip |
| [markdownlint](https://marketplace.visualstudio.com/items?itemName=DavidAnson.vscode-markdownlint)    | Markdown hatalarının altını çizme ve uyarma                               |
| [Markdown PDF](https://marketplace.visualstudio.com/items?itemName=yzane.markdown-pdf)                | Markdown'u PDF'e çevirme                                                  |
| [ToDo Tree](https://marketplace.visualstudio.com/items?itemName=Gruntfuggly.todo-tree)                | Yapılacakları derleme ve arayüzde sunma                                   |
| [Paste Image](https://marketplace.visualstudio.com/items?itemName=mushan.vscode-paste-image)          | Panodan resim kopyalama                                                   |

## Faydalı Siteler

| Site                                       | Açıklama                   |
| ------------------------------------------ | -------------------------- |
| [Url Encoder](https://www.urlencoder.org/) | Link URL'leri oluşturma    |
| [StackEdit](https://stackedit.io)          | Çevrimiçi markdown editörü |

## Harici Bağlantılar

- <https://html.com/attributes/a-href/>
- [Markdown and Visual Studio Codes](https://code.visualstudio.com/docs/languages/markdown)