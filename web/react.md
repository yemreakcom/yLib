---
description: React üzerine çalışmalarım ve bilgilerim.
---

# ⚛️ React

## Neden React

* Sanal bir DOM oluşturarak DOM üzerinden değişiklik olduğunda tüm kod sanal DOM'a aktarılır ardından sadece değişen kısımları DOM'a aktarır.
* DOM'a sadece değişenler aktarıldıkları için daha hızlı ve daha senkronize işlem yapılır

## React Kullanımı

**Online olarak:**

* [CodeSandbox](https://codesandbox.io/) üzerinden çalışabilirsin

**Bilgisayarın üzerinden çalıştırmak için:**

* [Nodejs](https://nodejs.org/en/download/) kurulumunu gerektirir
* React'i basit olarak kurmak için [buraya](https://github.com/facebook/create-react-app) bakabilirsin
* `npm init react-app my-app`

> [React IDE](https://github.com/reactide/reactide)

## Temel Kavramlar

### Component Kavramı

* Tüm classlar `React.Component`'i extends etmek zorundadır
* `render(<html>)` ile html yorumlanır
  * `return` edilen html metni ekrana basılır
  * HTML verileri `<div>` arasında olmak zorundadır
* Oluşturulduklarında `constructer` metodları çalışır
* Css atama işlemlerinde `class` yerine `className` özelliği kullanılır
* React'e özgü özelliklerde **camelCase** yazım formatı vardır
  * Örn: `className`, `onClick`
* Javascript verileri `{<js>}` arasında kullanılır
* `onClick` metodu `{() => <func>}` şeklinde javascript fonksiyonları ile kullanılır
  * `{<func>()}` şeklinde kullanılırsa fonksiyon tıklanmadan, direkt olarak çalıştırılır
* `state`'i olmayan `props`'lar üzerinden çalışan componentlere **controlled component** denir

### State Kavramı

* Class component'e özgü verilerdir
* Private veriler olarak ele alınır
* Constructer içerisinde `super`'den sonra kullanılır
  * `super` olmak zorundadır
* `setState({<key>: <value>})` ile güncellenirler

```javascript
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

* `<Square value={i} />;` ile aktarılan veriler props verileridir
* `this.props` şeklinde kullanılır
* Constructer'a ihtiyaç duymaz
  * `super` default olarak tanımlanır

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

* Fonksiyonlar html döndüren objelerdir
* `return` ile tek satır döndürülüyorsa paranteze gerek yoktur
* `return` çok satırlı dönüş değerleri için `()` içerisine yazılır
* `state` değişkeni olmadığından component'e göre daha kolay oluşturulur
* `onClick` kullanımı component'lere göre daha farklıdır
  * `this` deyimine ve `() => <func>()` yapısna gerek duymaz

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

#### Function Component Örnekleri

* Eğer js işlemi yoksa `{}` yerine `()` kullanılır
  * Bu sayede `return` işlemine gerek kalmaz
  * İçerisine yazılan direkt olarak return edilir

```jsx
// Buradaki authUser props'dan gelen anlamına gelir.
const Navigation = ({ authUser }) => (
  <div>{authUser ? <NavigationAuth /> : <NavigationNonAuth />}</div>
);
```

### State'lerde Immutable \(Değişmezlik\) Yapısı

State'ler değişmeyen veriler barındırır ve fonksiyonlarda `slice()` işlemi ile kopyaları oluşturulup, onlar değiştirilir.

* Karmaşıklığı ortadan kaldırır, geri alma işlemlerinde eski veriye erişim kolay olur
* Değişikliği tespit etmesi kolaydır, kopyalanma işlemi değişkenin adresini değiştirecektir
* Tekrardan render edilme zamanı çok daha rahat belirlenir

### React ile Programlama Yapısı

* En alt birimden kodlamaya başlanır
* Duruma göre _component_'in _state_'leri bir üst birime aktarılır
* _component_'teki _state_'ler _props_ ile yenilenir
* Bu işlem olabilidiğince devam eder

### Faydalı Metodlar

| Method | Açıklama |
| :--- | :--- |
| `Array<num>.fill(<value>)` | Dizi tanımlaması |
| `<arr>.slice()` | Diziyi kopyalama |
| `<arr>.concat([{}])` | Diziye obje dizisi ekleme \(immutable\) |
| `<arr>.map((<val>, <i>) => {<code>})` | Dizideki tüm elemanlara işlem yapma |

> `<arr>.push` ile ekleme işlemi orjinal diziyi değiştirir \(immutable olması bozulur\)

### For veya Map Döngüsü İşlemleri

* Döngüsel işlemlerde react hangi objenin değiştiğine karar veremez
* Ayırt ediciliğin oluşması için `key` değeri verilir
* `key` değerinin _global_ olarak eşsiz olmasına gerek yoktur, _local_ olarak olması kafi
* `key` değerine `this.props.key` gibi işlemlerle erişilemez, rezerve edilmiş bir kelimedir
* `key={i}` ataması sağlıklı değildir, indekslerdeki kayıp durumunda sorun çıkarır

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

### Hook Yapısı \(useSatate\)

* React v16.8 ile gelen bir özelliktir
* Class componentler de olan ama function componentlerde olmayan state yapısı için:
  * `useState` kodu kullanılır
  * `const [<state>, <handler>] = useState(<value>)` formatında kullanımı vardır
  * Bu sayede function componentlerde de state'ler kullanılabilir hale gelmekte

## Github Üzerinde Yayınlama

* `package.json` dosyasına `"homepage":"https://yourusername.github.io/repository-name"` alnını ekleyin
* `npm install --save gh-pages` ile gh-pages'i yükleyin
* `package.json`'daki scripts'lere alttakileri ekleyin:
  * `"predeploy": "npm run build",`
  * `"deploy": "gh-pages -d build"`
* `npm run deploy` ile gh-pages'e aktarabilirsiniz 🚀

> [Netlify](https://www.netlify.com/) üzerinden yayınlar isen [daha fazla avataja](https://www.netlify.com/github-pages-vs-netlify/) sahipsin 🎈

## React Bilgileri

* React'ta dom komutları çalışır
* [React ile CSS Ayalarma Yolları](https://codeburst.io/4-four-ways-to-style-react-components-ac6f323da822)
* [Markdown dosyasını ekrana basma](https://stackoverflow.com/a/42928796/9770490)
* \[Upload İşlemleri\]

### SVG alımı

* Svg dosyası oluşturulup içine svg ekleniir
  * `<svg> <g> ...`
* `jsx` dosyasından `import` edilir
* `img src={svg}` şeklinde kullanılır

### HTML Gösterme

```jsx
const html = "HTML verisi";

<section>
  <article dangerouslySetInnerHTML={{ __html: html }} />
</section>;
```

## Ücretsiz React Çalışma Yerleri

* [Complete React Tutorial \(with Redux\)](https://www.youtube.com/playlist?list=PL4cUxeGkcC9ij8CfkAY2RAGb-tmkNwQHG)
* [React, Redux & Firebase App Tutorial](https://www.youtube.com/playlist?list=PL4cUxeGkcC9iWstfXntcj8f-dFZ4UtlN3)
* [Best free react courses for tutorials](https://designrevision.com/best-free-react-tutorials-courses/)
* Kitap için [buraya](https://github.com/yedhrab/YWiki/tree/169abadfd1b8862c004399268f6ca1f9f9359d61/1%20-%20Programlama%20Notları/res/the-road-to-learn-react.pdf)
* [Master React & Redux](https://bahdcasts.com/courses/learn-react-redux)
* [Ücretli kurs](https://www.udemy.com/react-the-complete-guide-incl-redux/)
* [Başkalarının yaptığı demo'lu ve açık kaynaklı projeler](https://react.rocks/)

## Görsel Kaynaklar

* [Daynight Animation](https://codepen.io/Catagen/pen/PqYdXR/)
* [Meterial UI](https://github.com/mui-org/material-ui)
  * Codesanbox üzerinden deneyebilirsin
  * Upload butonu da vardır
* [Material Kit](https://demos.creative-tim.com/material-kit-react/#/) ✨
* [MDB Component](https://mdbootstrap.com/docs/react/components/demo/)
  * `npm install mdbreact`
  * [Examples](https://mdbootstrap.com/docs/react/css/background-image/)
* [Shard UI](https://designrevision.com/docs/shards-react/getting-started)
* [Button Tasarımları](https://caferati.me/demo/react-awesome-button)
* [React Datepicker](https://reactdatepicker.com/#example-10)
* [React Poper](https://github.com/FezVrasta/react-popper)

> Kaynaklar için [buradaki](https://www.codeinwp.com/blog/react-ui-component-libraries-frameworks/) makeleye bakmanda fayda var

### Admin Paneli \(Dashboard\)

* [MDB Dasboard](https://mdbootstrap.com/previews/free-templates/react-admin-dashboard/)

## ✨ React ile CSS Oluşturma

Oluşturulan stili `style = {myStyle}` şeklinde kullanabiliriz.

```jsx
const myStyle = {
  fontSize: 19,
  color: ...
}
// Eski yöntem
const myStyle = StyleSheed.create({
  fontSize: 19,
  color: ...
})
```

> [CSS Oluşturma Teknikleri](https://codeburst.io/4-four-ways-to-style-react-components-ac6f323da822)

### Tam Ekran Arkaplan Ayarlama

```jsx
const imgUrl = "images/bg.jpg"
const yStyle = {
  backgroundImage: `url(${imgUrl})`,
  backgroundPosition: "center",
  backgroundSize: "cover",
  backgroundRepeat: "no-repeat",
  WebkitTransition: "all", // note the capital 'W' here
  msTransition: "all" // 'ms' is the only lowercase vendor prefix
}
```

```css
.ystyle {
  background: url(images/bg.jpg) no-repeat center center fixed; 
  -webkit-background-size: cover;
  -moz-background-size: cover;
  -o-background-size: cover;
  background-size: cover;
}
```

### Transparan Arkaplan

```jsx
backgroundColor: 'rgba(52, 52, 52, 0.0)' // 0.0 opaklık değeridir
backgroundColor: 'transparent'
backgroundColor: '#00000000' // ##rrggbbaa hex codes
```

> [Transparan arkaplan](https://stackoverflow.com/a/31404170/9770490)

## Faydalı Bağlantılar

* [Dökümantasyon](https://reactjs.org/docs/getting-started.html)
* [Ana Kavramlar](https://reactjs.org/docs/hello-world.html)
* [Hosting](https://www.roast.io/for/react)
* [Online IDE](https://codesandbox.io/s/new)
* [React Instagram Klonu](https://github.com/yedehrab/React-Instagram-Clone-2.0)
* [React Instagram Klonu 2](https://github.com/hibiken/hackafy)
* [Frontend'de React Backend'de Nodejs Kullanma](https://www.freecodecamp.org/news/how-to-make-create-react-app-work-with-a-node-backend-api-7c5c48acb1b0/)
* [Nodejs React ve Redux ile Medium Klonu](https://github.com/krissnawat/medium-clone-on-node)
* [React ile yapılan uygulama örnekleri](https://madewithreact.com/)
* [React Hotket Hook](https://github.com/JohannesKlauss/react-hotkeys-hook)

