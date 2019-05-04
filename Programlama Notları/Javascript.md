# Javascript <!-- omit in toc -->

<!-- TODO Javascript DOM'u taşınabilir -->

## İçerikler <!-- omit in toc -->

> `HOME` tuşu ile yukarı yönlenebilrsiniz.

- [String İşlemleri](#string-i%CC%87%C5%9Flemleri)
- [HTML Elemanları](#html-elemanlar%C4%B1)
  - [HTML Elemanlarını Alma](#html-elemanlar%C4%B1n%C4%B1-alma)
    - [ID ile HTML Elemanı Alma](#id-ile-html-eleman%C4%B1-alma)
    - [Class, Tag veya Name ile HTML Elemanları Alma](#class-tag-veya-name-ile-html-elemanlar%C4%B1-alma)
  - [HTML elemanının alt elemanlarını alma](#html-eleman%C4%B1n%C4%B1n-alt-elemanlar%C4%B1n%C4%B1-alma)
  - [HTMLCollection'u array'e dönüştürmek](#htmlcollectionu-arraye-d%C3%B6n%C3%BC%C5%9Ft%C3%BCrmek)
  - [HTML Attribute Alma](#html-attribute-alma)
  - [HTML Elemanının Konumunu Alma](#html-eleman%C4%B1n%C4%B1n-konumunu-alma)
- [Beklemeli İşlemler](#beklemeli-i%CC%87%C5%9Flemler)
  - [Senkronize Bekleme (Sync)](#senkronize-bekleme-sync)
    - [Zamanlayıcı (setTimeout)](#zamanlay%C4%B1c%C4%B1-settimeout)
  - [Asenktron Bekleme (Async)](#asenktron-bekleme-async)
    - [Promise Yapısı ile Bekletme](#promise-yap%C4%B1s%C4%B1-ile-bekletme)
    - [Promise ile Beklemeli Metod İşleme](#promise-ile-beklemeli-metod-i%CC%87%C5%9Fleme)
  - [Sayfa İşlemleri](#sayfa-i%CC%87%C5%9Flemleri)
  - [Input İşlemleri](#input-i%CC%87%C5%9Flemleri)
- [Dosya İndirme](#dosya-i%CC%87ndirme)
  - [Çoklu Dosya İndirme](#%C3%A7oklu-dosya-i%CC%87ndirme)
  - [MIME - Internet Media Types](#mime---internet-media-types)
- [HTTP İstekleri](#http-i%CC%87stekleri)
- [Objedeki Değer ile Anahtarını Bulma](#objedeki-de%C4%9Fer-ile-anahtar%C4%B1n%C4%B1-bulma)
- [Harici Kaynaklar](#harici-kaynaklar)

## String İşlemleri

| İşlem             | Açıklama                                                         |
| ----------------- | ---------------------------------------------------------------- |
| `trim()`          | Boşluk, satır atlatma gibi özel karakterlerin tekrarını kaldırır |
| `split(<ayrıac>)` | Metni ayıraca göre parçalama                                     |

- `<ayırac>` Metnin parçalara ayırmak için belirleyici
  - Örn: `' '` ile boşluklu metinler ayrıştırılıp, yeni bir diziye atanır

## HTML Elemanları

### HTML Elemanlarını Alma

```javascript
document.getElementById('id'); // HTML elemanı döndürür (object)
document.getElementsByTagName('tag_name');  // HTML elemanları dizisi döndürür (HTMLCollection)
document.getElementsByClassName('class_name'); // HTML elemanları dizisi döndürür (HTMLCollection)
document.getElementsByName('name');  // HTML elemanları dizisi döndürür (HTMLCollection)
// id'ler için '#' classlar için '.' kullanılır
document.querySelector("#content") // İlk elemanı alma
document.querySelectorAll("span.style-scope.ytd-playlist-video-renderer") // Hepsini alma
```

- `Id` *Kimlik verisi*
- `Tag` *a, div, i, p, input, article ...*
- `Class` *Css dosyasındaki classları ifade eden alanlar*
- `Name` *Inputlarda sıklıkla kullanınlan alanlar*

#### ID ile HTML Elemanı Alma

ID'ler eşsiz olduğundan 1 tane html elamanı bulunacaktır.

```js
document.getElementById('<id>'); // HTML elemanı döndürür (object)
```

**Örnek kullanım**:

```html
<div id="secondary" class="widget-area col-md-4" role="complementary">
```

```js
const div_element = document.getElementById('secondary');
```

#### Class, Tag veya Name ile HTML Elemanları Alma

*Class*, *tag* ve *name* özellikleri birden fazla *html* elemanında olabileceğinden, *HTMLCollection* objesi döndürür.

```js
document.getElementsByTagName('tag_name');  // HTML elemanları dizisi döndürür (HTMLCollection)
document.getElementsByClassName('class_name'); // HTML elemanları dizisi döndürür (HTMLCollection)
document.getElementsByName('name');  // HTML elemanları dizisi döndürür (HTMLCollection)
```

### HTML elemanının alt elemanlarını alma

```js
document.getElementById('id').childNodes;
```

- `Id` *Kimlik verisi*
- `document.getElementById('id')` *HTMLElemanı*

### HTMLCollection'u array'e dönüştürmek

```javascript
const array = [...htmlCollection] // array: Array objesidir
array.forEach(element => { // Arraydeki her bir elemanı işleme
    // element.method()
});
```

### HTML Attribute Alma

*Tag* özellikleri olarak geçer. Örn; src, href, data-thumb-url, ...

> <a class="" href="" ...> </a> Tag içindeki kısımlar (class, href)

```javascript
document.getElementById('id').getAttribute('attribute') // Özelliğin değerini döndürür (string)
```

### HTML Elemanının Konumunu Alma

```js
document.getElementById('id').getBoundingClientRect();
```

- `Id` *Kimlik verisi*

## Beklemeli İşlemler

İki farklı bekleme şekli vardır:

| Bekleme Türü | Açıklama                                          |
| ------------ | ------------------------------------------------- |
| syncronize   | Bekleme anında tüm program durur                  |
| asyncronize  | Bekleme anında sadece belli bir kod parçası durur |

### Senkronize Bekleme (Sync)

*Senkronize* bekleme işlemleri, yani sırayla çalışan bekleme işlemleri alttaki fonksyionlarla sağlanır:

> Senkronize beklemelerde, bekleme durumunda hiç bir kod parçası çalışmaz.

```js
setTimeout(metod, ms_gecikme, varsa_parametreler); // Gecikmeli olarak metodu başlatır
setInterval(metod, ms_gecikme, varsa_parametreler) // Gecikmeli olarak metodu tekrarlar
```

- `metod` Fonksiyon
- `ms_gecikme` Milisaniye türünden gecikme değeri
  - Örn: `1000` değer 1s'ye denk gelir
- `varsa_parametreleri` Fonksiyonun parametreleri
  - Sırayla yazılarak verilir
  - Metod çalıştığında verilen parametreler ile çalıştırılır

#### Zamanlayıcı (setTimeout)

Kaynak için [buraya](https://www.w3schools.com/jsref/met_win_settimeout.asp) tıklayabilirsin.

```js
setTimeout(func, delay); // Temel kullanım
setTimeout(function(){ alert('Hello'); }, 2000); // Fonksiyonu içeride tanımlama
setTimeout(help, 2000); // Fonksiyonu dışarıda tanımlama
setTimeout(function(){ help(1); help(2); }, 2000); // Paremetreli fonksyion kullanma

clearTimeout(); // Zamanlayıcıları temizleme
```

- `func` Paremetresiz fonksiyon
- `delay` Gecikme süresi (ms)

### Asenktron Bekleme (Async)

Beklemeli işlemlerde `await`, `promise` yapısı kullanılır.

- `await` barındıran fonksiyonların `async` özelliğini taşımaları lazımdır
- `async` özelliği olan fonksiyonlar `await func()` şeklinde kullanılır
  - `await` işlemi bitene kadar bekle anlamı taşımaktadır
  - `await` deyimi kullanıldığı için bu deyimi içeren fonksiyon da `async` özelliği taşımalıdır

Bu konuda hakkında yazılmış bir medium yazısına [buradan][Wait Function] erişebilirsin.

#### Promise Yapısı ile Bekletme

```js
function wait(ms) {
    return new Promise(
        (r, j) => setTimeout(r, ms)
    )
}

function method() {
    console.log("done")
}

// Promise Yapısı ile çalışma
const prom = wait(2000)
prom.then(metod)

// Await yapısı ile çalışma
await wait(2000)
method()
```

#### Promise ile Beklemeli Metod İşleme

```js
function startDelayed(method, ms) {
    new Promise(
        (r, j) => setTimeout(r, ms)
    ).then(method)
}
```

```js
async function startDelayed(method, ms) {
    await new Promise((r, j) => setTimeout(r, ms));
    return method();
}
```

### Sayfa İşlemleri

```js
window.scrollBy(x, y); // Verilen değer kadar kayma
window.scrollTo(x, y); // Verilen değere gitme

window.scrollBy(5, 100); // Örnek kaydırma
window.scrollTo(5, 100); // Örnek atlama
```

- `x` Yatay konum
- `y` Dikey konum

```js
function pageScroll() {
    window.scrollBy(0,1);
    scrolldelay = setTimeout(pageScroll,10); // 10ms de bir kaydırma
}
```

### Input İşlemleri

```js
document.getElementById(<input_id>).value = <val>
document.getElementById(<input_id>).value = <val>
document.getElementById(<button_id>).click()
```

- `<input_id>` Input alanlarının id değerleri
- `val` Girilecek değer metni
- `<button_id>` Giriş butonu id değeri

## Dosya İndirme

```js
function download(filename, text, mime='text/plain') {
    const link = document.createElement("a");

    if (mime.includes("json")) {
        text = JSON.stringify(text)
    }

    link.download = filename;
    link.href = `data:${mime};charset=utf-8,${encodeURIComponent(text)}`;
    link.style.display = 'none';

    document.body.appendChild(link);
    link.click();
    document.body.removeChild(link);

    delete link;
}
```

### Çoklu Dosya İndirme

```js
function downladUrlArrayWithKey(array, key) {
    array.forEach(element => {
        const url = element[key];
        const fileName = url.split("/").pop();

        download(url, fileName);  
        sleep(100); // Bekleme olmazsa chrome her dosyayı indirmiyor
    });
}

function sleep(milliseconds) {
    var start = new Date().getTime();
    for (var i = 0; i < 1e7; i++) {
        if ((new Date().getTime() - start) > milliseconds){
            break;
        }
    }
}
```

### MIME - Internet Media Types

Hepsi için [buraya](https://www.freeformatter.com/mime-types-list.html) bakabilirsin, sık kullanılanlar aşağıda listelenmiştir.

| Extension  | Kind of document                               | MIME Type                                                                                                                            |
| ---------- | ---------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------ |
| .aac       | AAC audio                                      | audio/aac                                                                                                                            |
| .abw       | AbiWord document                               | application/x-abiword                                                                                                                |
| .arc       | Archive document (multiple files embedded)     | application/x-freearc                                                                                                                |
| .avi       | AVI: Audio Video Interleave                    | video/x-msvideo                                                                                                                      |
| .azw       | Amazon Kindle eBook format                     | application/vnd.amazon.ebook                                                                                                         |
| .bin       | Any kind of binary data                        | application/octet-stream                                                                                                             |
| .bmp       | Windows OS/2 Bitmap Graphics                   | image/bmp                                                                                                                            |
| .bz        | BZip archive                                   | application/x-bzip                                                                                                                   |
| .bz2       | BZip2 archive                                  | application/x-bzip2                                                                                                                  |
| .csh       | C-Shell script                                 | application/x-csh                                                                                                                    |
| .css       | Cascading Style Sheets (CSS)                   | text/css                                                                                                                             |
| .csv       | Comma-separated values (CSV)                   | text/csv                                                                                                                             |
| .doc       | Microsoft Word                                 | application/msword                                                                                                                   |
| .docx      | Microsoft Word (OpenXML)                       | application/vnd.openxmlformats-officedocument.wordprocessingml.document                                                              |
| .eot       | MS Embedded OpenType fonts                     | application/vnd.ms-fontobject                                                                                                        |
| .epub      | Electronic publication (EPUB)                  | application/epub+zip                                                                                                                 |
| .gif       | Graphics Interchange Format (GIF)              | image/gif                                                                                                                            |
| .htm.html  | HyperText Markup Language (HTML)               | text/html                                                                                                                            |
| .ico       | Icon format                                    | image/vnd.microsoft.icon                                                                                                             |
| .ics       | iCalendar format                               | text/calendar                                                                                                                        |
| .jar       | Java Archive (JAR)                             | application/java-archive                                                                                                             |
| .jpeg .jpg | JPEG images                                    | image/jpeg                                                                                                                           |
| .js        | JavaScript                                     | text/javascript                                                                                                                      |
| .json      | JSON format                                    | application/json                                                                                                                     |
| .jsonld    | JSON-LD format                                 | application/ld+json                                                                                                                  |
| .mid .midi | Musical Instrument Digital Interface (MIDI)    | audio/midi audio/x-midi                                                                                                              |
| .mjs       | JavaScript module                              | text/javascript                                                                                                                      |
| .mp3       | MP3 audio                                      | audio/mpeg                                                                                                                           |
| .mpeg      | MPEG Video                                     | video/mpeg                                                                                                                           |
| .mpkg      | Apple Installer Package                        | application/vnd.apple.installer+xml                                                                                                  |
| .odp       | OpenDocument presentation document             | application/vnd.oasis.opendocument.presentation                                                                                      |
| .ods       | OpenDocument spreadsheet document              | application/vnd.oasis.opendocument.spreadsheet                                                                                       |
| .odt       | OpenDocument text document                     | application/vnd.oasis.opendocument.text                                                                                              |
| .oga       | OGG audio                                      | audio/ogg                                                                                                                            |
| .ogv       | OGG video                                      | video/ogg                                                                                                                            |
| .ogx       | OGG                                            | application/ogg                                                                                                                      |
| .otf       | OpenType font                                  | font/otf                                                                                                                             |
| .png       | Portable Network Graphics                      | image/png                                                                                                                            |
| .pdf       | Adobe Portable Document Format (PDF)           | application/pdf                                                                                                                      |
| .ppt       | Microsoft PowerPoint                           | application/vnd.ms-powerpoint                                                                                                        |
| .pptx      | Microsoft PowerPoint (OpenXML)                 | application/vnd.openxmlformats-officedocument.presentationml.presentation                                                            |
| .rar       | RAR archive                                    | application/x-rar-compressed                                                                                                         |
| .rtf       | Rich Text Format (RTF)                         | application/rtf                                                                                                                      |
| .sh        | Bourne shell script                            | application/x-sh                                                                                                                     |
| .svg       | Scalable Vector Graphics (SVG)                 | image/svg+xml                                                                                                                        |
| .swf       | Small web format (SWF) or Adobe Flash document | application/x-shockwave-flash                                                                                                        |
| .tar       | Tape Archive (TAR)                             | application/x-tar                                                                                                                    |
| .tif .tiff | Tagged Image File Format (TIFF)                | image/tiff                                                                                                                           |
| .ttf       | TrueType Font                                  | font/ttf                                                                                                                             |
| .txt       | Text, (generally ASCII or ISO 8859-n)          | text/plain                                                                                                                           |
| .vsd       | Microsoft Visio                                | application/vnd.visio                                                                                                                |
| .wav       | Waveform Audio Format                          | audio/wav                                                                                                                            |
| .weba      | WEBM audio                                     | audio/webm                                                                                                                           |
| .webm      | WEBM video                                     | video/webm                                                                                                                           |
| .webp      | WEBP image                                     | image/webp                                                                                                                           |
| .woff      | Web Open Font Format (WOFF)                    | font/woff                                                                                                                            |
| .woff2     | Web Open Font Format (WOFF)                    | font/woff2                                                                                                                           |
| .xhtml     | XHTML                                          | application/xhtml+xml                                                                                                                |
| .xls       | Microsoft Excel                                | application/vnd.ms-excel                                                                                                             |
| .xlsx      | Microsoft Excel (OpenXML)                      | application/vnd.openxmlformats-officedocument.spreadsheetml.sheet                                                                    |
| .xml       | XML                                            | application/xml if not readable from casual users (RFC 3023, section 3) text/xml if readable from casual users (RFC 3023, section 3) |
| .xul       | XUL                                            | application/vnd.mozilla.xul+xml                                                                                                      |
| .zip       | ZIP archive                                    | application/zip                                                                                                                      |
| .3gp       | 3GPP audio/video container                     | video/3gpp, audio/3gpp if it doesn't contain video                                                                                   |
| .3g2       | 3GPP2 audio/video container                    | video/3gpp2 audio/3gpp2 if it doesn't contain video                                                                                  |
| .7z        | 7-zip archive                                  | application/x-7z-compressed"                                                                                                         |

## HTTP İstekleri

```js
// https://stackoverflow.com/questions/247483/http-get-request-in-javascript
// https://medium.freecodecamp.org/here-is-the-most-popular-ways-to-make-an-http-request-in-javascript-954ce8c95aaa
function httpGet(theUrl) {
    var xmlHttp = new XMLHttpRequest();
    xmlHttp.open("GET", theUrl, false); // false for synchronous request
    xmlHttp.send(null);
    return xmlHttp.responseText;
}
```

## Objedeki Değer ile Anahtarını Bulma

```js
function getKeyByValue(object, value) {
  return Object.keys(object).find(key => object[key] === value);
}
```

## Harici Kaynaklar

- [Wait Function]
- [Sayfanın en altına inmek]

[Wait Function]: https://hackernoon.com/lets-make-a-javascript-wait-function-fa3a2eb88f11
[Sayfanın en altına inmek]: https://stackoverflow.com/a/11715670