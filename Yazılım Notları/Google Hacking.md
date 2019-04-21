# Google Hacking

Google hacking, google da anahtar kelimeler kullanarak aradığımıza hızlı ulaşma tekniğinidir.

## Anahtar Kelimeler

Anahtarların kullanım şekli `<anahtar>:<değer>` şeklindedir.

> `:` karakteri sonrasında `boşluk` atılmaz.

| Anahtar   | Açıklama                      | Örnek                                | Örnek Açıklaması                                      |
| --------- | ----------------------------- | ------------------------------------ | ----------------------------------------------------- |
| filetype  | Dosya uzantısı                | `filetype:pdf Google hacking`        | Google hacking pdf'lerini listeler                    |
| site      | Verilen site içerisinde arama | `site:yemreak.com Ders Notları`      | Sitemdeki ders notları sayfasını listeler             |
| intitle   | Başlık içerisinde arama       | `intitle:index.of`                   | Sitelerin dizinlerini listeler                        |
| inurl     | Url'de arama                  | `intitle:index.of inurl:“/admin/”` | Admin dizini listelenmeye açık olan siteleri gösterir |
| numrange  | Sayı aralığında arama         | `numrange:99999-100000`
| daterange | Tarih aralığında arama        |
| cache     | Google önbelleğinde arama     | `cache:example.com`                  |

### Anahtar Kelime Kullanım Örnekleri

- `filetype:pdf Google hacking`
- `site:yemreak.com Ders Notları`

## Özel Karakterler

Özel karakter kullanımlarından sonra `boşluk` karakterinin **kullanılmadığına** dikkat edin.

| Operatör        | Kullanım Amacı                     | Örnek                            |
| --------------- | ---------------------------------- | -------------------------------- |
| `AND` ya da `+` | Anahtar kelimelerin her biri       | `web +application +security`     |
| `NOT` ya da `-` | Anahtar kelimlerini ayrımak        | `web application –security`      |
| `OR` ya da `|`  | Anahtar kelimelerden herhangi biri | `web application |security`      |
| `~`             | Benzeri anahtar kelimeler          | `web application ~security`      |
| `.`             | Belirsiz harfi belirtmek           | `.eb application security`       |
| `*`             | Belirsiz kelimeyi belirtmek        | `web * security`                 |
| `( )`           | Operatörleri gruplama              | `("web security" | websecurity)` |

## Harici Bağlantılar

- [Google Hacking Teknikleri](http://index-of.co.uk/Google/google-hacking.pdf)
- [Google Hacking: What is a Google Hack?](https://www.acunetix.com/websitesecurity/google-hacking/)
- [Google Hacking for Penetration Testers](http://www.mrjoeyjohnson.com/Google.Hacking.Filters.pdf)