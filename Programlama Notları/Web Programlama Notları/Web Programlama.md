# Web Programlama <!-- omit in toc -->

> `HOME` tuşu ile yukarı yönlenebilrsiniz.

- [CSS Notları](#CSS-Notlar%C4%B1)
  - [Faydalı Linkler](#Faydal%C4%B1-Linkler)
  - [Arkaplaba Ortalanmış Resim Ekleme](#Arkaplaba-Ortalanm%C4%B1%C5%9F-Resim-Ekleme)
  - [Ekranın Tam Ortasına Alma](#Ekran%C4%B1n-Tam-Ortas%C4%B1na-Alma)
  - [İçeriklerini Merkeze konumlandırma](#%C4%B0%C3%A7eriklerini-Merkeze-konumland%C4%B1rma)
  - [Animasyon (Transition)](#Animasyon-Transition)
- [VsCode Eklentileri](#VsCode-Eklentileri)
  - [Code runner ek ayarı](#Code-runner-ek-ayar%C4%B1)
- [Web Automation (Web Otomasyaonu)](#Web-Automation-Web-Otomasyaonu)
- [Faydalı Araçlar](#Faydal%C4%B1-Ara%C3%A7lar)
- [İlham Verici Çalışmalar](#%C4%B0lham-Verici-%C3%87al%C4%B1%C5%9Fmalar)
- [Karma Linkler](#Karma-Linkler)

## CSS Notları

- `width: 1vw` Ekranın genişliğinin 100'de 1'ini temsil eder
- `height: 1vh` Ekranın yüksekliğinin 100'de 1'ini temsil eder
- `em, rem` Fonta oranla boyut belirtme

### Faydalı Linkler

- [Css Before After](https://www.youtube.com/watch?reload=9&v=9t6j2UQx0Dc)

### Arkaplaba Ortalanmış Resim Ekleme

```css
.add-image {
    background-image: url(url);
    background-size: cover; /* <------ */
    background-repeat: no-repeat;
    background-position: center center;
}
```

### Ekranın Tam Ortasına Alma

```css
.centered {
    position: fixed;
    top: 50%;
    left: 50%;
    /* bring your own prefixes */
    transform: translate(-50%, -50%);
}
```

### İçeriklerini Merkeze konumlandırma

```css
.centered-content {
    display: flex;
    align-items: center;
    justify-content: center;
}
```

### Animasyon (Transition)

Tüm eylemleri için animasyon

```css
transition: all 1.1s ease-in-out;
```

## VsCode Eklentileri

| Adı          | Açıklama                          |
| ------------ | --------------------------------- |
| Html Preview | Html kodlarını ön izlemeyi sağlar |
| Code Runner  | Editör'e çalıştır butonu ekler    |

### Code runner ek ayarı

HTML dosyalarını tarayıcı ile çalıştırmak için alttaki kodu vscode json ayarlarına eklemeniz gerekmekte.

```json
 "code-runner.executorMap": {
        "html": "start $fileName"
 }
```

## Web Automation (Web Otomasyaonu)

Web otomasyonu için selenium ide kullanılmaktadır.

- Chrome için eklentisini [buraya](https://chrome.google.com/webstore/detail/selenium-ide/mooikfkahbdckldjjndioackbalphokd) tıklayarak indirebilirsin.
- Örnek video için [buraya](https://www.youtube.com/watch?v=4I7xay_NV8A) bakabilirsin.

## Faydalı Araçlar

- [CSS Animasyonu Oluşturucu](http://animista.net)
- [CSS Gölgelendirme Oluşturucu](https://www.cssmatic.com/box-shadow)

## İlham Verici Çalışmalar

- [Karma Figürler ve Animasyonlar İçeren İlginç Site](https://iuri.is/)
- [CSS Animasyon Örnekleri](https://www.mockplus.com/blog/post/css-animation-examples)
- [Codepen Üzerindeki CSS Animasyon Örnekleri](https://webdesign.tutsplus.com/articles/15-inspiring-examples-of-css-animation-on-codepen--cms-23937)

## Karma Linkler

- [Netlify](https://app.netlify.com) & [Heroku](https://www.heroku.com/) ücretsiz github entegrasyonlu site sunucuları
- [CSS Psudo Sınıfları ve Elemanları](https://fatihhayrioglu.com/pseudo-siniflari-ve-pseudo-elementleri/) (_after, before vs._)
- [Responsive Circle](https://codeitdown.com/css-circles/) | Bootstrap
- [Resimden renk kodunu alma](https://html-color-codes.info/colors-from-image/)
- [JSON Place Holder for RESTAPI](https://jsonplaceholder.typicode.com/)
