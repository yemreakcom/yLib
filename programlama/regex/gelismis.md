---
description: Regex hakkında gelişmiş notlar ve örnekler
---

# 🤯 Gelişmiş Notlar \| Regex

## 👀 Hızlı Bakış‍

* 💡`!` eki olumsuzluk iken `=` eşitlik anlamındadır 
* 💁‍♂️ `exp` eki expression kısaltmasıdır

| 💎 Regex | 📑 Açıklama |
| :--- | :--- |
| `(?=exp)` | Sonrasında `exp` koşulu sağlanmalıdır |
| `(?<!exp)` | Arkasında `exp` koşulu olmamalıdır |
| `(?<=exp)` | Arkasında `exp` koşulunu sağlamalıdır |
| `(?<=^)` | Satır başında olmalıdır |
| `[exp]` | Verilen `exp` değerlerinden herhangi biri olmalıdır |
| `[^exp]` | Verilen `exp` değerlerinin hiçbiri olmamalıdır |

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

## 🔑 Şifre RegExleri

* 👀 Şifre kontroller için Look Behind yapısı kullanılır
* ➕ Alttaki alandan istediğiniz kurala uygun olanları **sırasıyla** yan yana ekleyiniz

| 💎 Regex | 📑 Açıklama |
| :--- | :--- |
| `^` | Satır başından arama  \(**zorunlu**\) |
| `(?!.*\ )`  | Boşluk karakteri olmayan |
| `(?=.*\d)` | Sayı içeren |
| `(?=.*[A-Z])` | Büyük harf içeren |
| `(?=.*[a-z])` | Küçük harf içeren |
| `(?=.*[!@#\$\%\^\&\*\(\)\_])` | Özel karakter içeren |
| `[\w\!\@\#\$\%\^\&\*\(\)\_]{6,}` | En az `6` karakterli \(**zorunlu**\) |
| `$` | Metnin sonunu temsil eder \(**zorunlu**\) |

{% hint style="warning" %}
📢 Yukarıdakilerden, **zorunlu** yazanlar hariç diğerleri isteğe bağlıdır
{% endhint %}

```python
import re
pattern = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[\!\@\#\$\%\^\&\*\(\)\_])(?!.*\ )[\w\!\@\#\$\%\^\&\*\(\)\_]{6,}$"
return bool(re.match(pattern, S))
```

## 📑 Markdown RegEx

| 💎 Regex | 📑 Açıklama |
| :--- | :--- |
| `\[([^\[\]]+)\]\(([^\(\)]+)\)` | Link regex değeri |
| `(#+) *(.*)` | Header |
| `<!--(.*?)-->` | Comment |

