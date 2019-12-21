---
description: Markdown regexleri ile metinleri ayrıştırma ve anlama
---

# 💎 Markdown Regexleri

## 🔗 Tüm Linkleri Bulma

```python
\[([^\[]+)\](\(.*\)) # Tüm linkleri bulma (https://regex101.com/r/m9dndl/6)
```

{% hint style="info" %}
🧐 Detaylı bilgi için [Regex to match markdown links](https://davidwells.io/snippets/regex-match-markdown-links) bağlantısına bakabilirsin.
{% endhint %}

## 💫 Statik Linkleri Dinamik Yapma

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

