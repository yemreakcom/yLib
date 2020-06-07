---
description: 'Markdown tablo veya menü oluşturma, matematik işlemleri (latex) kullanımı'
---

# �� Markdown'da İstatistik

## 📊 Tablo Oluşturma

```text
| Tables   |      Are      |   Cool |
| -------- | :-----------: | -----: |
| col 1 is | left-aligned  | \$1600 |
| col 2 is |   centered    |   \$12 |
| col 3 is | right-aligned |    \$1 |
```

| Tables | Are | Cool |
| :--- | :---: | ---: |
| col 1 is | left-aligned | $1600 |
| col 2 is | centered | $12 |
| col 3 is | right-aligned | $1 |

## 📋 Açılır Menü Oluşturma

* `details` etiketi ile açılır menü oluşturulur
* `summary` kısmı görünen metindir

> `summary` alanında sonra boş satır olmazsa içerisindeki markdown işlenmez, olduğu gibi gözükür

```text
<details>
<summary>Görünen metin</summary>

- Detaylar

</details>
```

Görünen metin - Detaylar

## 🔢 Matematik Denklemleri

Detaylı bilgi için [buraya](https://csrgxtu.github.io/2015/03/20/Writing-Mathematic-Fomulars-in-Markdown/) bakabilirsin.

* Latex listesi için [buraya](https://oeis.org/wiki/List_of_LaTeX_mathematical_symbols) bakabilirsin
* Latex sembolleri için [buraya](https://artofproblemsolving.com/wiki/index.php/LaTeX:Symbols) bakabilirsin

> Online editör için [buraya](https://www.codecogs.com/latex/eqneditor.php) bakabilirsin.

### 🧬 Formül Yapısı

$$z^{[1] (i)} = W^{[1]} x^{(i)} + b^{[1]}\tag{1}$$ $$a^{[1] (i)} = \tanh(z^{[1] (i)})\tag{2}$$ $$z^{[2] (i)} = W^{[2]} a^{[1] (i)} + b^{[2]}\tag{3}$$ $$\hat{y}^{(i)} = a^{[2] (i)} = \sigma(z^{ [2] (i)})\tag{4}$$ $$y^{(i)}_{prediction} = \begin{cases} 1 & \mbox{if } a^{[2](i)} > 0.5 \\ 0 & \mbox{otherwise } \end{cases}\tag{5}$$ $$J = - \frac{1}{m} \sum\limits_{i = 0}^{m} \large\left(\small y^{(i)}\log\left(a^{[2] (i)}\right) + (1-y^{(i)})\log\left(1- a^{[2] (i)}\right) \large \right) \small \tag{6}$$

```text
$$z^{[1] (i)} =  W^{[1]} x^{(i)} + b^{[1]}\tag{1}$$
$$a^{[1] (i)} = \tanh(z^{[1] (i)})\tag{2}$$
$$z^{[2] (i)} = W^{[2]} a^{[1] (i)} + b^{[2]}\tag{3}$$
$$\hat{y}^{(i)} = a^{[2] (i)} = \sigma(z^{ [2] (i)})\tag{4}$$
$$y^{(i)}_{prediction} = \begin{cases} 1 & \mbox{if } a^{[2](i)} > 0.5 \\ 0 & \mbox{otherwise } \end{cases}\tag{5}$$
$$J = - \frac{1}{m} \sum\limits_{i = 0}^{m} \large\left(\small y^{(i)}\log\left(a^{[2] (i)}\right) + (1-y^{(i)})\log\left(1- a^{[2] (i)}\right)  \large  \right) \small \tag{6}$$
```

## 

