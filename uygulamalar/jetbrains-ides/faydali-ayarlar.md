# ⚙️ Faydalı Ayarlar

## ⌨️ VS Code Keymap

* 🚀 VS Code kısayollarını JetBrains üzerinde kullanmanızı sağlar
* 🔌 Plugins alanına `VS Code Keymap` yazarak indirebilirsiniz

## 🌌 Editör Kaydırması

* JetBrains varsayılan olarak son satırdan aşağısına inmez
* Son satırı en üst satıra kadar kaydırabilmek için alttaki ayarı kullanın
* Settings -&gt; Editor -&gt; Virtual Space -&gt; Show virtual space at file bottom

{% hint style="info" %}
🧙‍♂️ Detaylar için [Scroll Past End Of File](https://intellij-support.jetbrains.com/hc/en-us/community/posts/205814379/comments/205997989) bağlantısına bakabilirsin
{% endhint %}

## 🔤 Font Ayarları

Editör üzerindeki `==`, `=>`, `->`, `<=` gibi karakteri birleştiren hoş bir yazı tipidir

* ✲ Ctrl + ⎇ Alt + `S` yaptıktan sonra `Editor | Font` kısmında
  * _Font:_ `Consolas`
  * _Size:_ `12`
  * _Line spacing:_ `1.0`
  * `Enable Font Ligatures`

{% hint style="info" %}
🚀 FiraCode'u [buradan](https://github.com/tonsky/FiraCode#solution) indirebilirsin
{% endhint %}

## 🕵️‍♂️ Dokümantasyon Ön İzleme

Fareyle kodun üzerinize geldiğinizde açıklamalarını ve dokümantasyonları gösterecektir.

*  ✲ Ctrl + ⎇ Alt + `S` yaptıktan sonra
* 👇  `Editor | General | Other` başlığı altında 
* 👁️ `Show quick documentation on mouse move` kısmını seçin 
* 🕐 Süreyi `500` yapın.

![](../../.gitbook/assets/image%20%2894%29.png)

## 📖 Türkçe Kontrolü Tanımlama

Dillere özgü sözlükleri indirmek için [buraya](https://drive.google.com/open?id=1UAGLGvwv_zLBzH7zH1oGRvYhzzP67M4k) tıklayabilirsin.

* ✲ Ctrl + ⎇ Alt + `S` yaptıktan sonra `Editor | Spelling | Dictionaries | Custom Dictionaries` başlığı altında `+` butonuna basıp `.dic` uzantılı sözlük dosyanı ekleyin.

{% hint style="warning" %}
📢 Sözlüğün çalışabilmesi için `hunspell` eklentisini indirmeniz gerekmekte. Plugin kurma detayı için [buraya](https://www.jetbrains.com/help/idea/managing-plugins.html) tıklayabilirsin.
{% endhint %}

## 🧐 Spellcheck Kaldırma

* ✲ Ctrl + ⎇ Alt + `S` yaptıktan sonra `Editor | Inspection | Spelling | Typo | Process comments` ile yorum satırlarını kontrol etmesini kaldırabilirsin.

