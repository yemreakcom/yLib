# React Hızlı Notlar

- [React IDE](https://github.com/reactide/reactide)

> Burası ileride kaldırılacak

## CSS Oluşturma

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
