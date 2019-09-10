# JQuery

Daha az kodla daha çok js işi yapmayı amaçlayan API.

## JQuery Kurulumu

### Tarayıcı Consoluna Kurulum

```js
async function loadScript(url) {
  let response = await fetch(url);
  let script = await response.text();
  eval(script);
}

let scriptUrl = 'https://ajax.googleapis.com/ajax/libs/jquery/3.4.0/jquery.min.js'
loadScript(scriptUrl);
```

## Temel Giriş

- `$ veya $$` karakteri `document.querySelectorAll()` komutuna karşılık gelir
- Sayfadaki JQuery kontrolü için *console*'a `jQuery` yazıldığında tepki vermesi gerekir
- Jquery versiyonunu `$().jquery` komutuyla öğrenebilirsin.

> Ek bilgi için [buraya][JQuery Tek Eleman Seçme Sorunu] bakabilirsin.

## HTML Seçme İşlemleri

Tüm seçme işlemleri `$(<işlem>)` ve `$$(<işlem>)` komutu ile yapılır.

- Ana kaynak için [buraya][JQuery selector] bakabilirsin
- Online olarak test etmek için [buraya][JQuery seçim testi] bakabilirsin

> Alttaki işlemler *Chrome DOM*'unda gömülü gelen işlemlerdir, ek işlemler için sitenin *jQuery*'i içermesi lazımdır

| İşlem                  | Seçilen                                            |
| ---------------------- | -------------------------------------------------- |
| `"#yemreak"`           | ID'si yemreak olan eleman                          |
| `".yemre"`             | `yemre` *class*'ına sahip olan elemanlar           |
| `"[href]"`             | `href` özelliği olan elemanlar                     |
| `"[attribute=value]"`  | Özelliğe göre eleman alma                          |
| `"a[target='_blank']"` | `target`'i `_blank` olan linkler                   |
| `"p.active"`           | `active` *class*'ına sahip olan tüm *p* elemanları |
| `"*"`                  | Her eleman                                         |
| `this`                 | Şuanki eleman                                      |

## Temel Metodlar

| İşlem                       | Seçilen                                       |
| --------------------------- | --------------------------------------------- |
| `.each(func(index) => {} )` | Her eleman için döngü (index olduğuna dikkat) |

## Harici Bağlantılar

- [JQuery Tek Eleman Seçme Sorunu]

[JQuery Tek Eleman Seçme Sorunu]: https://stackoverflow.com/a/14309038/9770490
[JQuery selector]: https://www.w3schools.com/jquery/jquery_selectors.asp
[JQuery seçim testi]: https://www.w3schools.com/jquery/trysel.asp
