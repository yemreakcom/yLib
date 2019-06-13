# React <!-- omit in toc -->

## İçerikler <!-- omit in toc -->

> `HOME` tuşu ile yukarı yönlenebilrsiniz.

- [Neden React](#neden-react)
- [React Kullanımı](#react-kullan%C4%B1m%C4%B1)
- [Temel Bilgiler](#temel-bilgiler)
- [Yazım Formatı](#yaz%C4%B1m-format%C4%B1)
  - [Return Yapısı](#return-yap%C4%B1s%C4%B1)
  - [Hook Yapısı (useSatate)](#hook-yap%C4%B1s%C4%B1-usesatate)
- [Ücretsiz React Çalışma Yerleri](#%C3%BCcretsiz-react-%C3%A7al%C4%B1%C5%9Fma-yerleri)
- [Görsel Kaynaklar](#g%C3%B6rsel-kaynaklar)
- [Faydalı Bağlantılar](#faydal%C4%B1-ba%C4%9Flant%C4%B1lar)

Facebook'un çıkarmış olduğu bir web programlama framework'udür.

## Neden React

- Sanal bir DOM oluşturarak DOM üzerinden değişiklik olduğunda tüm kod sanal DOM'a aktarılır ardından sadece değişen kısımları DOM'a aktarır.
- DOM'a sadece değişenler aktarıldıkları için daha hızlı ve daha senkronize işlem yapılır

## React Kullanımı

**Online olarak:**

- [CodeSandbox] üzerinden çalışabilirsin

**Bilgisayarın üzerinden çalıştırmak için:**

- [Nodejs] kurulumunu gerektirir
- React'i basit olarak kurmak için [buraya][React Kurulumu] bakabilirsin
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
- `onClick` gibi metodların kullanımı `onClick={() => this.<func>}` şeklindedir
  - `this` sadece class componentler için kullanılır, function componentler için gerek yoktur

### Return Yapısı

Alttaki iki yapı eşdeğerdir

```js
render()(
    <div>temp</div>
)

render () {
    return <div>temp</div>
}
```

### Hook Yapısı (useSatate)

- React v16.8 ile gelen bir özelliktir
- Class componentler de olan ama function componentlerde olmayan state yapısı için:
  - `useState` kodu kullanılır
  - `const [<state>, <handler>] = useState(<value>)` formatında kullanımı vardır
  - Bu sayede function componentlerde de state'ler kullanılabilir hale gelmekte

## Ücretsiz React Çalışma Yerleri

- [Master React & Redux]
- [Best free react courses for tutorials]
- Kitap için [buraya][Road to learn react]
- [Ücretli kurs][React Udemy - Ücretli]
- [Başkalarının yaptığı demo'lu ve açık kaynaklı projeler][Açık kaynak react projeleri]

## Görsel Kaynaklar

- [Button Tasarımları][Reactjs Awesome Button]

## Faydalı Bağlantılar

- [Dökümantasyon](https://reactjs.org/docs/getting-started.html)
- [Ana Kavramlar](https://reactjs.org/docs/hello-world.html)
- [Hosting](https://www.roast.io/for/react)
- [Online IDE](https://codesandbox.io/s/new)
- [React Instagram Klonu][React Instagram Clone]
- [React Instagram Klonu 2][React Instagram Clone 2]
- [Nodejs React ve Redux ile Medium Klonu][Medium Clone]
- [React ile yapılan uygulama örnekleri]

[React Instagram Clone]: https://github.com/yedehrab/React-Instagram-Clone-2.0
[React Instagram Clone 2]: https://github.com/hibiken/hackafy
[Medium Clone]: https://github.com/krissnawat/medium-clone-on-node
[Reactjs Awesome Button]: https://caferati.me/demo/react-awesome-button

[Master React & Redux]: https://bahdcasts.com/courses/learn-react-redux
[Best free react courses for tutorials]: https://designrevision.com/best-free-react-tutorials-courses/
[Road to learn react]: ../res/the-road-to-learn-react.pdf
[React Udemy - Ücretli]: https://www.udemy.com/react-the-complete-guide-incl-redux/
[Açık kaynak react projeleri]: https://react.rocks/
[React ile yapılan uygulama örnekleri]: https://madewithreact.com/

[CodeSandbox]: https://codesandbox.io/
[Nodejs]: https://nodejs.org/en/download/
[React Kurulumu]: https://github.com/facebook/create-react-app
