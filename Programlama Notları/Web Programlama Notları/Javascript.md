# Javascript 

## Ön Bilgilendirme

Python ve Javascript en popüler diller arasındadır.

- Javascript kodlarım [YScripts] repomda tutulmaktadır ✨

> Aralarındaki kıyaslama için [buraya][python vs javascript] bakabilirisin.

## Değişken Tipleri

| Değişken | Açıklama                                 |
| -------- | ---------------------------------------- |
| `var`    | Her şey serbest 🎉                       |
| `let`    | Tekrardan tanımlanamaz, değiştirilebilir |
| `const`  | Tekrardan tanımlanmaz ve değiştirilmez   |

```js
var temp = 1;
var temp = 2;
let temp2;
temp2 = 4;
const temp3 = 5;
```

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
kosul ? "Doğru" : "Yanlış"; // Koşul sağlanırsa 'Doğru' sağlanmazsa 'Yanlış' döndürür
const sonuc = 1 > 2 ? "Doğru" : "Yanlış"; // sonuc = 'Yanlış'
```

### Dizilerde Koşul İşlemleri

**Dahili fonksiyon ile:**

```js
arr = [1, 2, 3];

arr.every(a => {
  return a > 1;
}); // Her biri 1'ten büyük mü? false
arr.some(a => {
  return a > 1;
}); // Herhangi biri 1'ten büyük mü? true
```

**Harici fonksiyon ile:**

```js
arr = [1, 2, 3];

function checkIndex(index) {
  return index > 1;
}

arr.every(checkIndex); // Her biri 1'ten büyük mü? false
arr.some(checkIndex); // Herhangi biri 1'ten büyük mü? true
```

## Tarih İşlemleri

Tarih işlemleri için `new Date()` kullanılır.

> Detaylar için [buraya][js date i̇şlemleri] bakabilirsin.

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
  ];

  // Değişken tarih oluşturma
  date = new Date();
  date.setDate(date.getDate() + offset);
  dateString = date.toLocaleDateString("tr");
  dayName = day[date.getDay()];

  return dateString + " " + dayName;
}
```

## HTML Elemanları

### HTML Elemanlarını Alma

```javascript
document.getElementById("id"); // HTML elemanı döndürür (object)
document.getElementsByTagName("tag_name"); // HTML elemanları dizisi döndürür (HTMLCollection)
document.getElementsByClassName("class_name"); // HTML elemanları dizisi döndürür (HTMLCollection)
document.getElementsByName("name"); // HTML elemanları dizisi döndürür (HTMLCollection)
// id'ler için '#' classlar için '.' kullanılır
document.querySelector("#content"); // İlk elemanı alma
document.querySelectorAll("span.style-scope.ytd-playlist-video-renderer"); // Hepsini alma
```

- `Id` _Kimlik verisi_
- `Tag` _a, div, i, p, input, article ..._
- `Class` _Css dosyasındaki classları ifade eden alanlar_
- `Name` _Inputlarda sıklıkla kullanınlan alanlar_

#### Query Selector ile HTML Elemanı Alma

Tek bir eleman alınmak isteniyorsa `querySelector(<işlem>)`, hepsi alınmak isteniyorsa `querySelectorAll(<işlem>)` komutu kullanılır

| İşlem                  | Seçilen                                            |
| ---------------------- | -------------------------------------------------- |
| `"#yemreak"`           | ID'si yemreak olan eleman                          |
| `".yemre"`             | `yemre` _class_'ına sahip olan elemanlar           |
| `"[href]"`             | `href` özelliği olan elemanlar                     |
| `"a[target='_blank']"` | `target`'i `_blank` olan linkler                   |
| `"p.active"`           | `active` _class_'ına sahip olan tüm _p_ elemanları |
| `"*"`                  | Her eleman                                         |
| `this`                 | Şuanki eleman                                      |

#### ID ile HTML Elemanı Alma

ID'ler eşsiz olduğundan 1 tane html elamanı bulunacaktır.

```js
document.getElementById("<id>"); // HTML elemanı döndürür (object)
```

**Örnek kullanım**:

```html
<div id="secondary" class="widget-area col-md-4" role="complementary"></div>
```

```js
const div_element = document.getElementById("secondary");
```

#### Class, Tag veya Name ile HTML Elemanları Alma

_Class_, _tag_ ve _name_ özellikleri birden fazla _html_ elemanında olabileceğinden, _HTMLCollection_ objesi döndürür.

```js
document.getElementsByTagName("tag_name"); // HTML elemanları dizisi döndürür (HTMLCollection)
document.getElementsByClassName("class_name"); // HTML elemanları dizisi döndürür (HTMLCollection)
document.getElementsByName("name"); // HTML elemanları dizisi döndürür (HTMLCollection)
```

### HTML elemanının alt elemanlarını alma

```js
document.getElementById("id").childNodes;
```

- `Id` _Kimlik verisi_
- `document.getElementById('id')` _HTMLElemanı_

### HTMLCollection'u array'e dönüştürmek

```javascript
const array = [...htmlCollection]; // array: Array objesidir
array.forEach(element => {
  // Arraydeki her bir elemanı işleme
  // element.method()
});
```

### HTML Attribute Alma

_Tag_ özellikleri olarak geçer. Örn; src, href, data-thumb-url, ...

> <a class="" href="" ...> </a> Tag içindeki kısımlar (class, href)

```javascript
document.getElementById("id").getAttribute("attribute"); // Özelliğin değerini döndürür (string)
```

### HTML Elemanının Konumunu Alma

```js
document.getElementById("id").getBoundingClientRect();
```

- `Id` _Kimlik verisi_

### ID'si Olan Elemanları Alma

```js
elems = article.querySelectorAll("*[id]");
ids = [];
for (let i = 0; i < elems.length; i++) {
  ids.push(elems[i].id);
}
```

- [ID'si olan elemanları alma](https://stackoverflow.com/a/7115033/9770490)

### Tüm H Değerlerini Alma

```js
document.querySelectorAll("h1, h2, h3, h4, h5, h6");
```

### Dom Elemanını Temizleme

```js
var elem = document.querySelector("#some-element");
elem.parentNode.removeChild(elem);
```

- [Removing an element from the DOM with vanilla JS]

### Dom Elemanın Altındaki Tüm Elemanları Temizleme

```js
var list = document.getElementById("mList");
   while (list.hasChildNodes()) {
      list.removeChild(list.firstChild);
   }
}
```

```js
var myNode = document.getElementById("foo");
while (myNode.firstChild) {
  myNode.removeChild(myNode.firstChild);
}
```

- [Remove all child elements of a DOM node in JavaScript]

## Sayfadaki URL'leri Alma

### Code for URL Extraction

```js
// URL'leri ekrana bastırma
urls = $$("a");
for (url in urls) console.log(urls[url].href);

// URL ve Anchor text'i renkli alma  (Chrome / Firefox)
var urls = $$("a");
for (url in urls) {
  console.log(
    "%c#" + url + " - %c" + urls[url].innerHTML + " -- %c" + urls[url].href,
    "color:red;",
    "color:green;",
    "color:blue;"
  );
}

// URL ve Anchor text'i alma (IE / EDGE)
var urls = $$("a");
for (url in urls) {
  console.log(
    "#" + url + " - " + urls[url].innerHTML + " -- " + urls[url].href
  );
}
```

> [How To Extract URLs From A Website In Chrome? (No Downloads Required)](https://www.youtube.com/watch?v=85GqVYeyn18)

## Beklemeli İşlemler

İki farklı bekleme şekli vardır:

| Bekleme Türü | Açıklama                                          |
| ------------ | ------------------------------------------------- |
| syncronize   | Bekleme anında tüm program durur                  |
| asyncronize  | Bekleme anında sadece belli bir kod parçası durur |

### Senkronize Bekleme (Sync)

_Senkronize_ bekleme işlemleri, yani sırayla çalışan bekleme işlemleri alttaki fonksyionlarla sağlanır:

> Senkronize beklemelerde, bekleme durumunda hiç bir kod parçası çalışmaz.

```js
setTimeout(metod, ms_gecikme, varsa_parametreler); // Gecikmeli olarak metodu başlatır
intervalID = setInterval(metod, ms_gecikme, varsa_parametreler); // Gecikmeli olarak metodu tekrarlar
clearInterval(intervalID); // Interval'ı sonlandırma
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
setTimeout(function() {
  alert("Hello");
}, 2000); // Fonksiyonu içeride tanımlama
setTimeout(help, 2000); // Fonksiyonu dışarıda tanımlama
setTimeout(function() {
  help(1);
  help(2);
}, 2000); // Paremetreli fonksyion kullanma

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

Bu konuda hakkında yazılmış bir medium yazısına [buradan][wait function] erişebilirsin.

#### Promise Yapısı ile Bekletme

```js
function wait(ms) {
  return new Promise((r, j) => setTimeout(r, ms));
}

function method() {
  console.log("done");
}

// Promise Yapısı ile çalışma
const prom = wait(2000);
prom.then(metod);

// Await yapısı ile çalışma
await wait(2000);
method();
```

#### Promise ile Beklemeli Metod İşleme

```js
function startDelayed(method, ms) {
  new Promise((r, j) => setTimeout(r, ms)).then(method);
}
```

```js
async function startDelayed(method, ms) {
  await new Promise((r, j) => setTimeout(r, ms));
  return method();
}
```

```js
async function startDelayed(method, ms, param) {
  await new Promise((r, j) => setTimeout(r, ms));
  return param ? method(param) : method();
}
```

```js
async function startAndWait(method, ms, param) {
  const result = param ? method(param) : method();
  await new Promise((r, j) => setTimeout(r, ms));
  return result;
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
  window.scrollBy(0, 1);
  scrolldelay = setTimeout(pageScroll, 10); // 10ms de bir kaydırma
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

> _Popup blocker_ gibi eklentiler varsa kapatılması gerekmektedir.

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
    if (new Date().getTime() - start > milliseconds) {
      break;
    }
  }
}
```

### `console.save` Metodu Oluşturma

```js
(function(console) {
  console.save = function(data, filename) {
    if (!data) {
      console.error("Console.save: No data");
      return;
    }

    if (!filename) filename = "console.json";

    if (typeof data === "object") {
      data = JSON.stringify(data, undefined, 4);
    }

    var blob = new Blob([data], { type: "text/json" }),
      e = document.createEvent("MouseEvents"),
      a = document.createElement("a");

    a.download = filename;
    a.href = window.URL.createObjectURL(blob);
    a.dataset.downloadurl = ["text/json", a.download, a.href].join(":");
    e.initMouseEvent(
      "click",
      true,
      false,
      window,
      0,
      0,
      0,
      0,
      0,
      false,
      false,
      false,
      false,
      0,
      null
    );
    a.dispatchEvent(e);
  };
})(console);

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

## Ses İşlemleri

<details>
<summary>Tuşa basıldığında ses çalma</summary>

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <title>JS Drum Kit</title>
    <link rel="stylesheet" href="style.css" />
  </head>
  <body>
    <div class="keys">
      <div data-key="65" class="key">
        <kbd>A</kbd>
        <span class="sound">clap</span>
      </div>
      <div data-key="83" class="key">
        <kbd>S</kbd>
        <span class="sound">hihat</span>
      </div>
      <div data-key="68" class="key">
        <kbd>D</kbd>
        <span class="sound">kick</span>
      </div>
      <div data-key="70" class="key">
        <kbd>F</kbd>
        <span class="sound">openhat</span>
      </div>
      <div data-key="71" class="key">
        <kbd>G</kbd>
        <span class="sound">boom</span>
      </div>
      <div data-key="72" class="key">
        <kbd>H</kbd>
        <span class="sound">ride</span>
      </div>
      <div data-key="74" class="key">
        <kbd>J</kbd>
        <span class="sound">snare</span>
      </div>
      <div data-key="75" class="key">
        <kbd>K</kbd>
        <span class="sound">tom</span>
      </div>
      <div data-key="76" class="key">
        <kbd>L</kbd>
        <span class="sound">tink</span>
      </div>
    </div>

    <audio data-key="65" src="sounds/clap.wav"></audio>
    <audio data-key="83" src="sounds/hihat.wav"></audio>
    <audio data-key="68" src="sounds/kick.wav"></audio>
    <audio data-key="70" src="sounds/openhat.wav"></audio>
    <audio data-key="71" src="sounds/boom.wav"></audio>
    <audio data-key="72" src="sounds/ride.wav"></audio>
    <audio data-key="74" src="sounds/snare.wav"></audio>
    <audio data-key="75" src="sounds/tom.wav"></audio>
    <audio data-key="76" src="sounds/tink.wav"></audio>

    <script>
      function removeTransitionEventListener(e) {
        if (e.propertyName !== "transform") return;
        this.classList.remove("playing");
      }

      function keyDownEventListener(e) {
        const audioElement = document.querySelector(
          `audio[data-key="${e.keyCode}"]`
        );

        const div = document.querySelector(`div[data-key="${e.keyCode}"]`);

        if (!audioElement || !div) return;

        // Oynama efekti ekleme
        div.classList.add("playing");

        // Playing always from start
        audioElement.currentTime = 0;
        audioElement.play();
      }

      // Tuşalara basıldığında listenerı aktif etme
      window.addEventListener("keydown", keyDownEventListener);

      // Efektleri kaldırma
      const keys = document.querySelectorAll(".key");
      keys.forEach(key =>
        key.addEventListener("transitionend", removeTransitionEventListener)
      );
    </script>
  </body>
</html>
```

</details>

## Harici Javascript Dosyası Ekleme

```js
async function loadScript(url) {
  let response = await fetch(url);
  let script = await response.text();
  eval(script);
}

let scriptUrl = "<url.js>";
loadScript(scriptUrl);
```

> [Kaynak](https://stackoverflow.com/a/44042421)

## Objedeki Değer ile Anahtarını Bulma

```js
function getKeyByValue(object, value) {
  return Object.keys(object).find(key => object[key] === value);
}
```

## `<div role=button>` Objelerine tıklama

```js
var e = document.createEvent("MouseEvents");
e.initMouseEvent("click", true, true, window, 0, 0, 0, 0, 0, false, false, false, false, 0, null);
$button[0].dispatchEvent(e);
```

## Latex Ayrıştırma

```html
<script
  type="text/javascript"
  src="http://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML"
></script>
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

### VsCode Nodejs için Debug Ayarı

```json
{
  "version": "0.2.0",
  "configurations": [
    {
      "type": "node",
      "request": "launch",
      "name": "Launch Program",
      "program": "${workspaceFolder}\\index.js",
      "outFiles": ["${workspaceRoot}/dist/**/**/*.js"]
    },
    {
      "type": "node",
      "request": "launch",
      "name": "Launch Current File",
      "program": "${file}",
      "outFiles": ["${workspaceRoot}/dist/**/**/*.js"]
    }
  ]
}
```

## Harici Kaynaklar

- [Wait Function]
- [Sayfanın en altına inmek]
- [Js Date İşlemleri]
- [Js gün işlemleri]
- [10 Js Extension for Vscode]
- [Js throws]

[python vs javascript]: https://www.educba.com/python-vs-javascript/
[wait function]: https://hackernoon.com/lets-make-a-javascript-wait-function-fa3a2eb88f11
[sayfanın en altına inmek]: https://stackoverflow.com/a/11715670
[js date i̇şlemleri]: https://www.w3schools.com/jsref/jsref_obj_date.asp
[js gün işlemleri]: https://stackoverflow.com/a/24998705/9770490
[10 js extension for vscode]: https://www.sitepoint.com/vs-code-extensions-javascript-developers/
[js throws]: https://www.w3schools.com/js/js_errors.asp
[quokka.js]: https://marketplace.visualstudio.com/items?itemName=WallabyJs.quokka-vscode
[prettier - code formatter]: https://marketplace.visualstudio.com/items?itemName=esbenp.prettier-vscode
[javascript (es6) code snippets]: https://marketplace.visualstudio.com/items?itemName=xabikos.JavaScriptSnippets
[babel javascript]: https://marketplace.visualstudio.com/items?itemName=mgmcdermott.vscode-language-babel
[npm intellisese]: https://marketplace.visualstudio.com/items?itemName=christian-kohler.npm-intellisense
[jshint]: https://marketplace.visualstudio.com/items?itemName=dbaeumer.jshint
[eslint]: https://marketplace.visualstudio.com/items?itemName=dbaeumer.vscode-eslint
[import cost]: https://marketplace.visualstudio.com/items?itemName=wix.vscode-import-cost
[yscripts]: https://github.com/yedhrab/YScripts
[remove all child elements of a dom node in javascript]: https://stackoverflow.com/a/3955238/9770490
[removing an element from the dom with vanilla js]: https://gomakethings.com/removing-an-element-from-the-dom-with-vanilla-js/
