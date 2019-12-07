# 🤯 Regex Gelişmiş Notlar

## 👀 Hızlı Bakış‍

* `!` eki olumsuzluk iken `=` eşitlik anlamındadır

| 💎 Regex | 📑 Açıklama |
| :--- | :--- |
| `(?=exp)` | Sonrasında `exp` koşulu sağlanmalıdır |
| `(?<!exp)` | Arkasında `exp` koşulu olmamalıdır |
| `(?<=exp)` | Arkasında `exp` koşulunu sağlamalıdır |
| `(?<=^)` | Satır başında olmalıdır |
| `[exp]` | Verilen `exp` değerlerinden herhangi biri olmalıdır |
| `[^exp]` | Verilen `exp` değerleri olmamalıdır |

## 👨‍💻 Hızlı Örnekler

| 💎 Regex | 📑 Açıklama | ⭐ |
| :--- | :--- | :--- |
| `(?<!\w)\b[A-Z]+[\_]*[A-Z]*\b(?=\s)` | Büyük harf içeren değişkenleri bulma \(`Y_EMRE`\) | [🔗](https://regex101.com/r/fgHYX0/3) |
| `\b(?<!\n)(?!MsgBox)([\w]+)(?=\()` | Çağrılan fonksiyonların isimlerini bulma | [🌍](https://regex101.com/r/fgHYX0/2/) |
| `^(?!.bar).$` | İçerisinde `bar` geçmeyen satırları bulma |  |
| `(?<=\(\ |\,\ |\(|\,)\w+` |  |  |

{% hint style="success" %}
⭐ Örnekler için sağdaki emojilere tıklayabilirsin
{% endhint %}

