# DOM - Javascript <!-- omit in toc -->

<!-- TODO Javascript DOM'u buraya aktarılacak -->

## İçerikler <!-- omit in toc -->

- [Beklemeli İşlemler](#beklemeli-i%CC%87%C5%9Flemler)
  - [Basit Geciktirme Metodları](#basit-geciktirme-metodlar%C4%B1)
  - [Promise Yapısı ile Bekletme](#promise-yap%C4%B1s%C4%B1-ile-bekletme)
  - [Promise ile Beklemeli Metod İşleme](#promise-ile-beklemeli-metod-i%CC%87%C5%9Fleme)
- [HTTP İstekleri](#http-i%CC%87stekleri)
- [Dosya İndirme](#dosya-i%CC%87ndirme)
  - [Çoklu Dosya İndirme](#%C3%A7oklu-dosya-i%CC%87ndirme)
  - [MIME - Internet Media Types](#mime---internet-media-types)
- [HTML Elemanları](#html-elemanlar%C4%B1)
  - [HTML Elemanlarını Alma](#html-elemanlar%C4%B1n%C4%B1-alma)
    - [ID ile HTML Elemanı Alma](#id-ile-html-eleman%C4%B1-alma)
    - [Class, Tag veya Name ile HTML Elemanları Alma](#class-tag-veya-name-ile-html-elemanlar%C4%B1-alma)
- [Harici Kaynaklar](#harici-kaynaklar)

## Beklemeli İşlemler

Bu konuda hakkında yazılmış bir medium yazısına [buradan][Wait Function] erişebilirsin.

### Basit Geciktirme Metodları

```js
setTimeout(metod, ms_gecikme); // Gecikmeli olarak metodu başlatır
```

### Promise Yapısı ile Bekletme

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

### Promise ile Beklemeli Metod İşleme

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

## HTML Elemanları

### HTML Elemanlarını Alma

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

## Harici Kaynaklar

- [Wait Function]

[Wait Function]: https://hackernoon.com/lets-make-a-javascript-wait-function-fa3a2eb88f11