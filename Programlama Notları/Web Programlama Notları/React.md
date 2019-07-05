# React <!-- omit in toc -->

<!-- TODO: Ract için özel yapı -->

## İçerikler <!-- omit in toc -->

> `HOME` tuşu ile yukarı yönlenebilrsiniz.

- [Neden React](#neden-react)
- [React Kullanımı](#react-kullan%C4%B1m%C4%B1)
- [Temel Kavramlar](#temel-kavramlar)
  - [Component Kavramı](#component-kavram%C4%B1)
  - [State Kavramı](#state-kavram%C4%B1)
  - [Props Kavramı](#props-kavram%C4%B1)
  - [Function Components ve Function Kavramı](#function-components-ve-function-kavram%C4%B1)
  - [State'lerde Immutable (Değişmezlik) Yapısı](#statelerde-immutable-de%C4%9Fi%C5%9Fmezlik-yap%C4%B1s%C4%B1)
  - [React ile Programlama Yapısı](#react-ile-programlama-yap%C4%B1s%C4%B1)
  - [Faydalı Metodlar](#faydal%C4%B1-metodlar)
  - [For veya Map Döngüsü İşlemleri](#for-veya-map-d%C3%B6ng%C3%BCs%C3%BC-i%CC%87%C5%9Flemleri)
  - [Hook Yapısı (useSatate)](#hook-yap%C4%B1s%C4%B1-usesatate)
- [Github Üzerinde Yayınlama](#github-%C3%BCzerinde-yay%C4%B1nlama)
- [React Bilgileri](#react-bilgileri)
  - [SVG alımı](#svg-al%C4%B1m%C4%B1)
  - [HTML Gösterme](#html-g%C3%B6sterme)
- [Ücretsiz React Çalışma Yerleri](#%C3%BCcretsiz-react-%C3%A7al%C4%B1%C5%9Fma-yerleri)
- [Görsel Kaynaklar](#g%C3%B6rsel-kaynaklar)
  - [Admin Paneli (Dashboard)](#admin-paneli-dashboard)
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
- React'i basit olarak kurmak için [buraya][react kurulumu] bakabilirsin
- `npm init react-app my-app`

## Temel Kavramlar

### Component Kavramı

- Tüm classlar `React.Component`'i extends etmek zorundadır
- `render(<html>)` ile html yorumlanır
  - `return` edilen html metni ekrana basılır
  - HTML verileri `<div>` arasında olmak zorundadır
- Oluşturulduklarında `constructer` metodları çalışır
- Css atama işlemlerinde `class` yerine `className` özelliği kullanılır
- React'e özgü özelliklerde **camelCase** yazım formatı vardır
  - Örn: `className`, `onClick`
- Javascript verileri `{<js>}` arasında kullanılır
- `onClick` metodu `{() => <func>}` şeklinde javascript fonksiyonları ile kullanılır
  - `{<func>()}` şeklinde kullanılırsa fonksiyon tıklanmadan, direkt olarak çalıştırılır
- `state`'i olmayan `props`'lar üzerinden çalışan componentlere **controlled component** denir

### State Kavramı

- Class component'e özgü verilerdir
- Private veriler olarak ele alınır
- Constructer içerisinde `super`'den sonra kullanılır
  - `super` olmak zorundadır
- `setState({<key>: <value>})` ile güncellenirler

```js
class Square extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      value: null
    };
  }

  render() {
    return (
      <button className="square" onClick={() => this.setState({ value: "X" })}>
        {this.state.value}
      </button>
    );
  }
}
```

### Props Kavramı

- `<Square value={i} />;` ile aktarılan veriler props verileridir
- `this.props` şeklinde kullanılır
- Constructer'a ihtiyaç duymaz
  - `super` default olarak tanımlanır

```jsx
class Square extends React.Component {
  render() {
    return (
      <button className="square" onClick={() => alert("click")}>
        {this.props.value}
      </button>
    );
  }
}
```

### Function Components ve Function Kavramı

- Fonksiyonlar html döndüren objelerdir
- `return` ile tek satır döndürülüyorsa paranteze gerek yoktur
- `return` çok satırlı dönüş değerleri için `()` içerisine yazılır
- `state` değişkeni olmadığından component'e göre daha kolay oluşturulur
- `onClick` kullanımı component'lere göre daha farklıdır
  - `this` deyimine ve `() => <func>()` yapısna gerek duymaz

```jsx
// Function Component
function Square(props) {
  return (
    <button className="square" onClick={props.onClick}>
      {props.value}
    </button>
  );
}

// Function
renderSquare(i) {
    return <Square value={this.state.squares[i]} />;
}

renderSquare(i) {
    return (
        <Square
        value={this.state.squares[i]}
        onClick={() => this.handleClick(i)}
        />
    );
}
```

### State'lerde Immutable (Değişmezlik) Yapısı

State'ler değişmeyen veriler barındırır ve fonksiyonlarda `slice()` işlemi ile kopyaları oluşturulup, onlar değiştirilir.

- Karmaşıklığı ortadan kaldırır, geri alma işlemlerinde eski veriye erişim kolay olur
- Değişikliği tespit etmesi kolaydır, kopyalanma işlemi değişkenin adresini değiştirecektir
- Tekrardan render edilme zamanı çok daha rahat belirlenir

### React ile Programlama Yapısı

- En alt birimden kodlamaya başlanır
- Duruma göre _component_'in _state_'leri bir üst birime aktarılır
- _component_'teki _state_'ler _props_ ile yenilenir
- Bu işlem olabilidiğince devam eder

### Faydalı Metodlar

| Method                                | Açıklama                              |
| ------------------------------------- | ------------------------------------- |
| `Array<num>.fill(<value>)`            | Dizi tanımlaması                      |
| `<arr>.slice()`                       | Diziyi kopyalama                      |
| `<arr>.concat([{}])`                  | Diziye obje dizisi ekleme (immutable) |
| `<arr>.map((<val>, <i>) => {<code>})` | Dizideki tüm elemanlara işlem yapma   |

> `<arr>.push` ile ekleme işlemi orjinal diziyi değiştirir (immutable olması bozulur)

### For veya Map Döngüsü İşlemleri

- Döngüsel işlemlerde react hangi objenin değiştiğine karar veremez
- Ayırt ediciliğin oluşması için `key` değeri verilir
- `key` değerinin _global_ olarak eşsiz olmasına gerek yoktur, _local_ olarak olması kafi
- `key` değerine `this.props.key` gibi işlemlerle erişilemez, rezerve edilmiş bir kelimedir
- `key={i}` ataması sağlıklı değildir, indekslerdeki kayıp durumunda sorun çıkarır

```jsx
const moves = history.map((step, move) => {
  const desc = move ? "Go to move #" + move : "Go to game start";
  return (
    <li key={move}>
      {" "}
      {/* Key kullanımı gerekir */}
      <button onClick={() => this.jumpTo(move)}>{desc}</button>
    </li>
  );
});
```

### Hook Yapısı (useSatate)

- React v16.8 ile gelen bir özelliktir
- Class componentler de olan ama function componentlerde olmayan state yapısı için:
  - `useState` kodu kullanılır
  - `const [<state>, <handler>] = useState(<value>)` formatında kullanımı vardır
  - Bu sayede function componentlerde de state'ler kullanılabilir hale gelmekte

## Github Üzerinde Yayınlama

- `package.json` dosyasına `"homepage":"https://yourusername.github.io/repository-name"` alnını ekleyin
- `npm install --save gh-pages` ile gh-pages'i yükleyin
- `package.json`'daki scripts'lere alttakileri ekleyin:
  - `"predeploy": "npm run build",`
  - `"deploy": "gh-pages -d build"`
- `npm run deploy` ile gh-pages'e aktarabilirsiniz 🚀

> [Netlify](https://www.netlify.com/) üzerinden yayınlar isen [daha fazla avataja](https://www.netlify.com/github-pages-vs-netlify/) sahipsin 🎈

## React Bilgileri

- React'ta dom komutları çalışır
- [React ile CSS Ayalarma Yolları](https://codeburst.io/4-four-ways-to-style-react-components-ac6f323da822)
- [Markdown dosyasını ekrana basma]
- [Upload İşlemleri]

### SVG alımı

- Svg dosyası oluşturulup içine svg ekleniir
  - `<svg> <g> ...`
- `jsx` dosyasından `import` edilir
- `img src={svg}` şeklinde kullanılır

### HTML Gösterme

```jsx
const html = "HTML verisi";

<section>
  <article dangerouslySetInnerHTML={{ __html: html }} />
</section>;
```

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
- [Frontend'de React Backend'de Nodejs Kullanma]
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
[frontend'de react backend'de nodejs kullanma]: https://www.freecodecamp.org/news/how-to-make-create-react-app-work-with-a-node-backend-api-7c5c48acb1b0/
[upload işlemleri]: https://medium.com/@ilonacodes/front-end-shorts-how-to-read-content-from-the-file-input-in-react-17f49b293909
[markdown dosyasını ekrana basma]: https://stackoverflow.com/a/42928796/9770490
