# JQuery

Daha az kodla daha çok js işi yapmayı amaçlayan API.

## Temel Giriş

- `$` karakteri `document.querySelector()` komutuna karşılık gelir
- `$$` karakteri `document.querySelectorAll()` komutuna karşılık gelir
- Sayfadaki JQuery kontrolü için *console*'a `jQuery` yazıldığında tepki vermesi gerekir
- Jquery versiyonunu `$().jquery` komutuyla öğrenebilirsin.

> Kaynak için [buraya][JQuery Tek Eleman Seçme Sorunu] bakabilirsin.

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
| `"a[target='_blank']"` | `target`'i `_blank` olan linkler                   |
| `"p.active"`           | `active` *class*'ına sahip olan tüm *p* elemanları |
| `"*"`                  | Her eleman                                         |
| `this`                 | Şuanki eleman                                      |

## Harici Bağlantılar

- [JQuery Tek Eleman Seçme Sorunu]

[JQuery Tek Eleman Seçme Sorunu]: https://stackoverflow.com/a/14309038/9770490
[JQuery selector]: https://www.w3schools.com/jquery/jquery_selectors.asp
[JQuery seçim testi]: https://www.w3schools.com/jquery/trysel.asp