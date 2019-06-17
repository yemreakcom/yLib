# React <!-- omit in toc -->

## İçerikler <!-- omit in toc -->

> `HOME` tuşu ile yukarı yönlenebilrsiniz.

- [Neden React](#Neden-React)
- [React Kullanımı](#React-Kullan%C4%B1m%C4%B1)
- [Temel Bilgiler](#Temel-Bilgiler)
- [Yazım Formatı](#Yaz%C4%B1m-Format%C4%B1)
  - [Return Yapısı](#Return-Yap%C4%B1s%C4%B1)
  - [Hook Yapısı (useSatate)](#Hook-Yap%C4%B1s%C4%B1-useSatate)
- [Ücretsiz React Çalışma Yerleri](#%C3%9Ccretsiz-React-%C3%87al%C4%B1%C5%9Fma-Yerleri)
- [Görsel Kaynaklar](#G%C3%B6rsel-Kaynaklar)
  - [Admin Paneli (Dashboard)](#Admin-Paneli-Dashboard)
- [Faydalı Bağlantılar](#Faydal%C4%B1-Ba%C4%9Flant%C4%B1lar)

Facebook'un çıkarmış olduğu bir web programlama framework'udür.

## Neden React

- Sanal bir DOM oluşturarak DOM üzerinden değişiklik olduğunda tüm kod sanal DOM'a aktarılır ardından sadece değişen kısımları DOM'a aktarır.
- DOM'a sadece değişenler aktarıldıkları için daha hızlı ve daha senkronize işlem yapılır

## React Kullanımı

**Online olarak:**

- [CodeSandbox] üzerinden çalışabilirsin

**Bilgisayarın üzerinden çalıştırmak için:**

- [Nodejs] kurulumunu gerektirir
- React'i basit olarak kurmak için [buraya][react kurulumu] bakabilirsin
- `npm init react-app my-app`

## Temel Bilgiler

| Terim            | Açıklama                                         |
| ---------------- | ------------------------------------------------ |
| Compoenent       | Her bir objeye verilen isim                      |
| `state = {}`     | Class componentlere özgü veriler                 |
| `probs = {}`     | Componentler arası veri aktarmak için kullanılır |
| `{<javascript>}` | Html içine js komutları ekleme                   |

## Yazım Formatı

- Yazı yapısı olarak **camelCase** tercih edilir
- React'a özgü html attribute'ları camelCase yazılır
  - `onclick` yerine `onClick` vs.
- Classlar'ın içinde `render()` olur ve `div` içinde html döndürmek zorundadır
- `()` kullanılırsa içerisindeki veri otomatik olarak **return** edilir
- Html içine javascriptler `{}` karakterleri arasına `<div>{"javascript_kodu"}</div>` yapısı ile eklenir
- `onClick` gibi metodların kullanımı `onClick={() => this.<func>()}` şeklindedir
- `{<func>()}` şeklinde kullanılırsa fonksiyon tıklanmadan, direkt olarak çalıştırılır
- `{() => {<func>()}}` şeklinde de kullanılabilir
  - `this` sadece class componentler için kullanılır, function componentler için gerek yoktur

### Return Yapısı

Alttaki iki yapı eşdeğerdir

```js
render()(
    <div>temp</div>
)

render () {
    return <div>temp</div>****
}
```

### Hook Yapısı (useSatate)

- React v16.8 ile gelen bir özelliktir
- Class componentler de olan ama function componentlerde olmayan state yapısı için:
  - `useState` kodu kullanılır
  - `const [<state>, <handler>] = useState(<value>)` formatında kullanımı vardır
  - Bu sayede function componentlerde de state'ler kullanılabilir hale gelmekte

## Ücretsiz React Çalışma Yerleri

- [Complete React Tutorial (with Redux)]
- [React, Redux & Firebase App Tutorial]
- [Best free react courses for tutorials]
- Kitap için [buraya][road to learn react]
- [Master React & Redux]
- [Ücretli kurs][react udemy - ücretli]
- [Başkalarının yaptığı demo'lu ve açık kaynaklı projeler][açık kaynak react projeleri]

## Görsel Kaynaklar

- [Daynight Animation](https://codepen.io/Catagen/pen/PqYdXR/)
- [Meterial UI](https://github.com/mui-org/material-ui)
  - Codesanbox üzerinden deneyebilirsin
  - Upload butonu da vardır
- [Material Kit] ✨
- [MDB Component]
  - `npm install mdbreact`
  - [Examples](https://mdbootstrap.com/docs/react/css/background-image/)
- [Shard UI]
- [Button Tasarımları][reactjs awesome button]
- [React Datepicker]
- [React Poper]

> Kaynaklar için [buradaki][react ui compenent framework] makeleye bakmanda fayda var

### Admin Paneli (Dashboard)

- [MDB Dasboard]

## Faydalı Bağlantılar

- [Dökümantasyon](https://reactjs.org/docs/getting-started.html)
- [Ana Kavramlar](https://reactjs.org/docs/hello-world.html)
- [Hosting](https://www.roast.io/for/react)
- [Online IDE](https://codesandbox.io/s/new)
- [React Instagram Klonu][react instagram clone]
- [React Instagram Klonu 2][react instagram clone 2]
- [Nodejs React ve Redux ile Medium Klonu][medium clone]
- [React ile yapılan uygulama örnekleri]

[react instagram clone]: https://github.com/yedehrab/React-Instagram-Clone-2.0
[react instagram clone 2]: https://github.com/hibiken/hackafy
[medium clone]: https://github.com/krissnawat/medium-clone-on-node
[reactjs awesome button]: https://caferati.me/demo/react-awesome-button
[master react & redux]: https://bahdcasts.com/courses/learn-react-redux
[complete react tutorial (with redux)]: https://www.youtube.com/playlist?list=PL4cUxeGkcC9ij8CfkAY2RAGb-tmkNwQHG
[best free react courses for tutorials]: https://designrevision.com/best-free-react-tutorials-courses/
[road to learn react]: ../res/the-road-to-learn-react.pdf
[react udemy - ücretli]: https://www.udemy.com/react-the-complete-guide-incl-redux/
[açık kaynak react projeleri]: https://react.rocks/
[react ile yapılan uygulama örnekleri]: https://madewithreact.com/
[codesandbox]: https://codesandbox.io/
[nodejs]: https://nodejs.org/en/download/
[react kurulumu]: https://github.com/facebook/create-react-app
[react datepicker]: https://reactdatepicker.com/#example-10
[react poper]: https://github.com/FezVrasta/react-popper
[mdb component]: https://mdbootstrap.com/docs/react/components/demo/
[shard ui]: https://designrevision.com/docs/shards-react/getting-started
[react, redux & firebase app tutorial]: https://www.youtube.com/playlist?list=PL4cUxeGkcC9iWstfXntcj8f-dFZ4UtlN3
[material kit]: https://demos.creative-tim.com/material-kit-react/#/
[react ui compenent framework]: https://www.codeinwp.com/blog/react-ui-component-libraries-frameworks/
[mdb dasboard]: https://mdbootstrap.com/previews/free-templates/react-admin-dashboard/
