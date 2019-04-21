# Javascript <!-- omit in toc -->

Javascript DOM komutlarını özetleyen bir derlemedir.

## İçerikler <!-- omit in toc -->

> `HOME` tuşu ile yukarı yönlenebilrsiniz.

- [Temel Bilgiler](#temel-bilgiler)
  - [String İşlemleri](#string-i%CC%87%C5%9Flemleri)
- [DOM Bilgileri](#dom-bilgileri)
  - [Dosya İndirme İşlemleri](#dosya-i%CC%87ndirme-i%CC%87%C5%9Flemleri)
    - [Dosya İndrime](#dosya-i%CC%87ndrime)
    - [URI ile dosya indirme](#uri-ile-dosya-indirme)
    - [Çoklu URL ile indirme](#%C3%A7oklu-url-ile-indirme)
    - [JSON olarak indirme](#json-olarak-indirme)
    - [İndirme için Ek Notlar](#i%CC%87ndirme-i%C3%A7in-ek-notlar)
  - [HTML Elemanı Alma](#html-eleman%C4%B1-alma)
  - [HTML elemanının alt elemanlarını alma](#html-eleman%C4%B1n%C4%B1n-alt-elemanlar%C4%B1n%C4%B1-alma)
  - [HTMLCollection'u array'e dönüştürmek](#htmlcollectionu-arraye-d%C3%B6n%C3%BC%C5%9Ft%C3%BCrmek)
  - [HTML Attribute Alma](#html-attribute-alma)
  - [HTML Elemanının Konumunu Alma](#html-eleman%C4%B1n%C4%B1n-konumunu-alma)
  - [Sayfa İşlemleri](#sayfa-i%CC%87%C5%9Flemleri)
  - [Input İşlemleri](#input-i%CC%87%C5%9Flemleri)
  - [Zamanlayıcı](#zamanlay%C4%B1c%C4%B1)
- [Kod Notları](#kod-notlar%C4%B1)
  - [Objedeki Değer ile Anahtarını Bulma](#objedeki-de%C4%9Fer-ile-anahtar%C4%B1n%C4%B1-bulma)
- [Harici Bağlantılar](#harici-ba%C4%9Flant%C4%B1lar)

## Temel Bilgiler

- [For Each Kullanımı](https://stackoverflow.com/a/9329476)
- [Array](https://www.w3schools.com/js/js_arrays.asp)

> İndeksleme alanına yönelmek için [buraya](#%C4%B0ndeksleme) tıklayabilirsin.

### String İşlemleri

| İşlem    | Açıklama                                                         |
| -------- | ---------------------------------------------------------------- |
| `trim()` | Boşluk, satır atlatma gibi özel karakterlerin tekrarını kaldırır |

## DOM Bilgileri

Notların linklerine bakmak için [buraya](#Ek%20Notlar) tıklayabilirsin.

### Dosya İndirme İşlemleri

- Stackoverflow cevabı için [buraya](https://stackoverflow.com/a/14966131/9770490) tıklayın.
- URI için data tipleri için [buraya](https://developer.mozilla.org/en-US/docs/Web/HTTP/Basics_of_HTTP/Data_URIs) tıklayın.
- Gecikme işlemleri için [buraya](https://www.yazilimbilisim.net/javascript/javascript-zamanlayici-kullanimi/) tıklayın.
- **Chrome** `click()` metodunu  destekleyemeyebiliyor.. 😭 (*Edge kullanınız.* 😏)

> **Popup Blocker** gibi eklentiler ekliyse kapatmanız gerekmekte.

#### Dosya İndrime

```js
function download(filename, text, type='text/plain') {
  var element = document.createElement('a');
  element.setAttribute('href', `data:${type};charset=utf-8,${encodeURIComponent(text)}`);
  element.setAttribute('download', filename);

  element.style.display = 'none';
  document.body.appendChild(element);

  element.click();

  document.body.removeChild(element);
}
```

#### URI ile dosya indirme

Geçici HTMLElement ile bu işlemi yapabiliriz.

```js
function downloadURI(uri, name) {
    const link = document.createElement("a");

    link.download = name;
    link.href = uri;

    document.body.appendChild(link);

    link.click();

    document.body.removeChild(link);

    delete link;
}
```

> İndeksleme alanına yönelmek için [buraya](#%C4%B0ndeksleme) tıklayabilirsin.

#### Çoklu URL ile indirme

```js
function downloadArrayUrlWithKey(array, key) {
    array.forEach(element => {
        const url = element[key];
        const fileName = url.split("/").pop();

        downloadURI(url, fileName);  
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

> İndeksleme alanına yönelmek için [buraya](#%C4%B0ndeksleme) tıklayabilirsin.

#### JSON olarak indirme

Verilen json objesi istenen isimle indiren fonksiyon. Detayları için [buraya](https://stackoverflow.com/a/30800715) tıklayabilirsin.

```javascript
/**
 * JSON objesi indirme
 * @param {JSON} exportObj İndirilecek JSON objesi
 * @param {string} exportName İndirilen dosyanın ismi
 */
function downloadObjectAsJson(exportObj, exportName){
    var dataStr = "data:text/json;charset=utf-8," + encodeURIComponent(JSON.stringify(exportObj));
    var downloadAnchorNode = document.createElement('a');
    downloadAnchorNode.setAttribute("href",     dataStr);
    downloadAnchorNode.setAttribute("download", exportName + ".json");
    document.body.appendChild(downloadAnchorNode); // required for firefox
    downloadAnchorNode.click();
    downloadAnchorNode.remove();
}
```

**Kullanımı:**

```js
var exampleData = {
    "name" : "temp"
}

downloadObjectAsJson(exampleData, "champs.json");
```

> İndeksleme alanına yönelmek için [buraya](#%C4%B0ndeksleme) tıklayabilirsin.

#### İndirme için Ek Notlar

- [Dosya indirme](https://www.w3schools.com/jsref/prop_anchor_download.asp) | [URL ile indirme](https://stackoverflow.com/a/34694012)

> İndeksleme alanına yönelmek için [buraya](#%C4%B0ndeksleme) tıklayabilirsin.

### HTML Elemanı Alma

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

> İndeksleme alanına yönelmek için [buraya](#%C4%B0ndeksleme) tıklayabilirsin.

### HTML elemanının alt elemanlarını alma

```js
document.getElementById('id').childNodes;
```

- `Id` *Kimlik verisi*
- `document.getElementById('id')` *HTMLElemanı*

> İndeksleme alanına yönelmek için [buraya](#%C4%B0ndeksleme) tıklayabilirsin.

### HTMLCollection'u array'e dönüştürmek

```javascript
const array = [...htmlCollection] // array: Array objesidir
array.forEach(element => { // Arraydeki her bir elemanı işleme
    // element.method()
});
```

> İndeksleme alanına yönelmek için [buraya](#%C4%B0ndeksleme) tıklayabilirsin.

### HTML Attribute Alma

*Tag* özellikleri olarak geçer. Örn; src, href, data-thumb-url, ...

> <a class="" href="" ...> </a> Tag içindeki kısımlar (class, href)

```javascript
document.getElementById('id').getAttribute('attribute') // Özelliğin değerini döndürür (string)
```

> İndeksleme alanına yönelmek için [buraya](#%C4%B0ndeksleme) tıklayabilirsin.

### HTML Elemanının Konumunu Alma

```js
document.getElementById('id').getBoundingClientRect();
```

- `Id` *Kimlik verisi*

> İndeksleme alanına yönelmek için [buraya](#%C4%B0ndeksleme) tıklayabilirsin.

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

> İndeksleme alanına yönelmek için [buraya](#%C4%B0ndeksleme) tıklayabilirsin.

### Zamanlayıcı

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

## Kod Notları

### Objedeki Değer ile Anahtarını Bulma

```js
function getKeyByValue(object, value) {
  return Object.keys(object).find(key => object[key] === value);
}
```

## Harici Bağlantılar

- [Sayfanın en altına inmek](https://stackoverflow.com/a/11715670)
- [Debugging ES6 in Visual Studio Code](https://medium.com/@drcallaway/debugging-es6-in-visual-studio-code-4444db797954)
