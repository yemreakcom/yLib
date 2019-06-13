# Javascript <!-- omit in toc -->

## İçerikler <!-- omit in toc -->

> `HOME` tuşu ile yukarı yönlenebilrsiniz.

- [Ön Bilgilendirme](#%C3%B6n-bilgilendirme)
- [String İşlemleri](#string-i%CC%87%C5%9Flemleri)
- [Koşul İşlemleri](#ko%C5%9Ful-i%CC%87%C5%9Flemleri)
  - [Tek Satırlı Koşul İşlemleri (Ternary If)](#tek-sat%C4%B1rl%C4%B1-ko%C5%9Ful-i%CC%87%C5%9Flemleri-ternary-if)
  - [Dizilerde Koşul İşlemleri](#dizilerde-ko%C5%9Ful-i%CC%87%C5%9Flemleri)
- [Tarih İşlemleri](#tarih-i%CC%87%C5%9Flemleri)
  - [Türkçe Tarih Alma](#t%C3%BCrk%C3%A7e-tarih-alma)
- [HTML Elemanları](#html-elemanlar%C4%B1)
  - [HTML Elemanlarını Alma](#html-elemanlar%C4%B1n%C4%B1-alma)
    - [Query Selector ile HTML Elemanı Alma](#query-selector-ile-html-eleman%C4%B1-alma)
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
  - [`console.save` Metodu Oluşturma](#consolesave-metodu-olu%C5%9Fturma)
  - [MIME - Internet Media Types](#mime---internet-media-types)
- [HTTP İstekleri](#http-i%CC%87stekleri)
- [Harici Javascript Dosyası Ekleme](#harici-javascript-dosyas%C4%B1-ekleme)
- [Objedeki Değer ile Anahtarını Bulma](#objedeki-de%C4%9Fer-ile-anahtar%C4%B1n%C4%B1-bulma)
- [Latex Ayrıştırma](#latex-ayr%C4%B1%C5%9Ft%C4%B1rma)
- [VsCode Eklentileri](#vscode-eklentileri)
- [Harici Kaynaklar](#harici-kaynaklar)

## Ön Bilgilendirme

Python ve Javascript en popüler diller arasındadır.

- Javascript kodlarım [YScripts] repomda tutulmaktadır ✨

> Aralarındaki kıyaslama için [buraya][Python vs Javascript] bakabilirisin.

## String İşlemleri

| İşlem             | Açıklama                                                         |
| ----------------- | ---------------------------------------------------------------- |
| `trim()`          | Boşluk, satır atlatma gibi özel karakterlerin tekrarını kaldırır |
| `split(<ayrıac>)` | Metni ayıraca göre parçalama                                     |

- `<ayırac>` Metnin parçalara ayırmak için belirleyici
  - Örn: `' '` ile boşluklu metinler ayrıştırılıp, yeni bir diziye atanır

## Koşul İşlemleri

```js
elems = [] // Herhangi sayılabilir bir obje
for (let i = 0; i < elems.lenght < i++) {
    elem = elems[i]
    // ...
}
```

### Tek Satırlı Koşul İşlemleri (Ternary If)

```js
kosul ? "Doğru" : "Yanlış" // Koşul sağlanırsa 'Doğru' sağlanmazsa 'Yanlış' döndürür
const sonuc = 1 > 2 ? "Doğru" : "Yanlış" // sonuc = 'Yanlış'
```

### Dizilerde Koşul İşlemleri

**Dahili fonksiyon ile:**

```js
arr = [1, 2, 3]

arr.every(a => {return a > 1}) // Her biri 1'ten büyük mü? false
arr.some(a => {return a > 1}) // Herhangi biri 1'ten büyük mü? true

```

**Harici fonksiyon ile:**

```js
arr = [1, 2, 3]

function checkIndex(index) {
    return index > 1
}

arr.every(checkIndex) // Her biri 1'ten büyük mü? false
arr.some(checkIndex) // Herhangi biri 1'ten büyük mü? true

```

## Tarih İşlemleri

Tarih işlemleri için `new Date()` kullanılır.

> Detaylar için [buraya][Js Date İşlemleri] bakabilirsin.

| Metod                             | Açıklama                              | Ek açıklama                         |
| --------------------------------- | ------------------------------------- | ----------------------------------- |
| `getDate()`                       | Gün verisini alır                     | Ayın 6'sı                           |
| `getDay()`                        | Gün ismini sayısal olarak verir       | Pazar için 0, Cumartesi için 6      |
| `setDate(<date> + <offset>)`      | Tarihi değiştirme                     | Bir sonraki veya önceki tarihi alma |
| `toLocaleDateString(<ülke_kodu>)` | Verilen ülkeye göre zaman metni verir | TR'ye göre için `"06.05.2019"`      |

- `<date>` Tarih objesi
  - Örn: `new Date()`
- `<offset>` Değişken sayı
  - Örn: 1 gün sonrası için `1`, 1 gün öncesi için `-1`
- `<ülke_kodu>` Ülkenin kodu
  - Örn: Tr için `"tr"`, Amerika için `"en-US"`

### Türkçe Tarih Alma

```js
/**
 * Bugüne kıyasla yeni bir gün verisi döndürür
 * @param {number} offset Sonrası ya da öncesi (`-1` 1 gün önce)
 */
function getDateTR(offset = 0) {
	// Günlerin türkçe karşılığı
	day = [
		"Pazar",
		"Pazartesi",
		"Salı",
		"Çarşamba",
		"Perşembe",
		"Cuma",
		"Cumartesi"
	]

	// Değişken tarih oluşturma
	date = new Date()
	date.setDate(date.getDate() + offset)
	dateString = date.toLocaleDateString("tr")
	dayName = day[date.getDay()]

	return dateString + " " + dayName
}
```

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

#### Query Selector ile HTML Elemanı Alma

Tek bir eleman alınmak isteniyorsa `querySelector(<işlem>)`, hepsi alınmak isteniyorsa `querySelectorAll(<işlem>)` komutu kullanılır

| İşlem                  | Seçilen                                            |
| ---------------------- | -------------------------------------------------- |
| `"#yemreak"`           | ID'si yemreak olan eleman                          |
| `".yemre"`             | `yemre` *class*'ına sahip olan elemanlar           |
| `"[href]"`             | `href` özelliği olan elemanlar                     |
| `"a[target='_blank']"` | `target`'i `_blank` olan linkler                   |
| `"p.active"`           | `active` *class*'ına sahip olan tüm *p* elemanları |
| `"*"`                  | Her eleman                                         |
| `this`                 | Şuanki eleman                                      |

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
- Bir fonksiyonda `await` beklemesi varsa onu kullanan fonksyionlar da o fonksiyonu `await` ile beklemelidir
  - Aksi halde asenkron olarak çalışır bekleme gerçekleşmez

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
async function startDelayed(method, ms, param) {
    await new Promise((r, j) => setTimeout(r, ms));
    return typeof param != "undefined" ? method(param) : method()
}
```

```js
async function startAndWait(method, ms, param) {
	const result = typeof param != "undefined" ? method(param) : method()
	await new Promise((r, j) => setTimeout(r, ms));
	return result
}
```

`

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

> *Popup blocker* gibi eklentiler varsa kapatılması gerekmektedir.

```js
function download(data, filename, mime = 'text/plain') {
        if (!data) {
            console.error("Veri olmadan indirme işlemi yapılmaz")
            return;
        }

        if (!data.includes("http")) {
            if (mime.includes("json") || typeof data === "object") {
                mime = "text/json"
                data = JSON.stringify(data)
            }
            data = `data:${mime};charset=utf-8,${encodeURIComponent(data)}`

            if (!filename) {
                filename = `template.${mime.split('/')[0]}`
            }
        }

        if (!filename) {
            filename = data.split('/').pop()
        }

        const link = document.createElement("a");

        link.download = filename;
        link.href = data
        link.style.display = 'none';

        document.body.appendChild(link);
        link.click();
        document.body.removeChild(link);

        delete link;
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

### `console.save` Metodu Oluşturma

```js
(function(console){

    console.save = function(data, filename){

        if(!data) {
            console.error('Console.save: No data')
            return;
        }

        if(!filename) filename = 'console.json'

        if(typeof data === "object"){
            data = JSON.stringify(data, undefined, 4)
        }

        var blob = new Blob([data], {type: 'text/json'}),
            e    = document.createEvent('MouseEvents'),
            a    = document.createElement('a')

        a.download = filename
        a.href = window.URL.createObjectURL(blob)
        a.dataset.downloadurl =  ['text/json', a.download, a.href].join(':')
        e.initMouseEvent('click', true, false, window, 0, 0, 0, 0, 0, false, false, false, false, 0, null)
        a.dispatchEvent(e)
    }
})(console)

// console.save(<url>, <filename>)
```

### MIME - Internet Media Types

Hepsi için [buraya](https://www.freeformatter.com/mime-types-list.html) bakabilirsin, sık kullanılanlar aşağıda listelenmiştir.

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

## Harici Javascript Dosyası Ekleme

```js
async function loadScript(url) {
  let response = await fetch(url);
  let script = await response.text();
  eval(script);
}

let scriptUrl = '<url.js>'
loadScript(scriptUrl);
```

> [Kaynak](https://stackoverflow.com/a/44042421)

## Objedeki Değer ile Anahtarını Bulma

```js
function getKeyByValue(object, value) {
  return Object.keys(object).find(key => object[key] === value);
}
```

## Latex Ayrıştırma

```html
<script type="text/javascript" src="http://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML"></script>
<script type="text/x-mathjax-config">
    MathJax.Hub.Config({ tex2jax: {inlineMath: [['$', '$']]}, messageStyle: "none" });
</script>
```

## VsCode Eklentileri

| Eklenti                          | Açıklama                                                                                |
| -------------------------------- | --------------------------------------------------------------------------------------- |
| [Quokka.js]                      | Anlık derleyici ve hata ayıklama ([video](https://www.youtube.com/watch?v=eyzO1xPI6_k)) |
| [Prettier - Code formatter]      | Kod formatlama ve güzelleştirme                                                         |
| [JavaScript (ES6) code snippets] | Kod kısayolları                                                                         |
| [Babel Javascript]               | ES6 tipinde yazmayı sağlar                                                              |
| [npm Intellisese]                | NPM modüllerini önerir                                                                  |
| [jshint]                         | Javascript imla kontrolcüsü                                                             |
| [Eslint]                         | JS için imla kontrolcüsü                                                                |
| [Import Cost]                    | Bellek kullanımını gösterir                                                             |

## Harici Kaynaklar

- [Wait Function]
- [Sayfanın en altına inmek]
- [Js Date İşlemleri]
- [Js gün işlemleri]
- [10 Js Extension for Vscode]
- [Js throws]

[Python vs Javascript]: https://www.educba.com/python-vs-javascript/

[Wait Function]: https://hackernoon.com/lets-make-a-javascript-wait-function-fa3a2eb88f11
[Sayfanın en altına inmek]: https://stackoverflow.com/a/11715670
[Js Date İşlemleri]: https://www.w3schools.com/jsref/jsref_obj_date.asp
[Js gün işlemleri]: https://stackoverflow.com/a/24998705/9770490
[10 Js Extension for Vscode]: https://www.sitepoint.com/vs-code-extensions-javascript-developers/
[Js throws]: https://www.w3schools.com/js/js_errors.asp

[Quokka.js]: https://marketplace.visualstudio.com/items?itemName=WallabyJs.quokka-vscode
[Prettier - Code formatter]: https://marketplace.visualstudio.com/items?itemName=esbenp.prettier-vscode
[JavaScript (ES6) code snippets]: https://marketplace.visualstudio.com/items?itemName=xabikos.JavaScriptSnippets
[Babel Javascript]: https://marketplace.visualstudio.com/items?itemName=mgmcdermott.vscode-language-babel
[npm Intellisese]: https://marketplace.visualstudio.com/items?itemName=christian-kohler.npm-intellisense
[jshint]: https://marketplace.visualstudio.com/items?itemName=dbaeumer.jshint
[Eslint]: https://marketplace.visualstudio.com/items?itemName=dbaeumer.vscode-eslint
[Import Cost]: https://marketplace.visualstudio.com/items?itemName=wix.vscode-import-cost

[YScripts]: https://github.com/yedhrab/YScripts
