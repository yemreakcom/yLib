---
description: Daha az javascript kodu ile daha çok js yapmayı amaçlayan API
---

# 🔶 JQuery

## JQuery Kurulumu

### Tarayıcı Consoluna Kurulum

```javascript
async function loadScript(url) {
  let response = await fetch(url);
  let script = await response.text();
  eval(script);
}

let scriptUrl = 'https://ajax.googleapis.com/ajax/libs/jquery/3.4.0/jquery.min.js'
loadScript(scriptUrl);
```

## Temel Giriş

* `$ veya $$` karakteri `document.querySelectorAll()` komutuna karşılık gelir
* Sayfadaki JQuery kontrolü için _console_'a `jQuery` yazıldığında tepki vermesi gerekir
* Jquery versiyonunu `$().jquery` komutuyla öğrenebilirsin.

> Ek bilgi için [buraya](https://stackoverflow.com/a/14309038/9770490) bakabilirsin.

## HTML Seçme İşlemleri

Tüm seçme işlemleri `$(<işlem>)` ve `$$(<işlem>)` komutu ile yapılır.

* Ana kaynak için [buraya](https://www.w3schools.com/jquery/jquery_selectors.asp) bakabilirsin
* Online olarak test etmek için [buraya](https://www.w3schools.com/jquery/trysel.asp) bakabilirsin

> Alttaki işlemler _Chrome DOM_'unda gömülü gelen işlemlerdir, ek işlemler için sitenin _jQuery_'i içermesi lazımdır

| İşlem | Seçilen |
| :--- | :--- |
| `"#yemreak"` | ID'si yemreak olan eleman |
| `".yemre"` | `yemre` _class_'ına sahip olan elemanlar |
| `"[href]"` | `href` özelliği olan elemanlar |
| `"[attribute=value]"` | Özelliğe göre eleman alma |
| `"a[target='_blank']"` | `target`'i `_blank` olan linkler |
| `"p.active"` | `active` _class_'ına sahip olan tüm _p_ elemanları |
| `"*"` | Her eleman |
| `this` | Şuanki eleman |

## Temel Metodlar

| İşlem | Seçilen |
| :--- | :--- |
| `.each(func(index) => {} )` | Her eleman için döngü \(index olduğuna dikkat\) |

## Harici Bağlantılar

* [JQuery Tek Eleman Seçme Sorunu](https://stackoverflow.com/a/14309038/9770490)

