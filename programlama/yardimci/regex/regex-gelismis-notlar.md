# 🤯 Regex Gelişmiş Notlar

## 👀 Hızlı Bakış

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

```python
regex = r"(?<!\w)\b[A-Z]+[\_]*[A-Z]*\b(?=\s)" # CONSTANT_VARIABLE bulma
regex2 = r"\b(?<!\n)(?!MsgBox)([\w]+)(?=\()" # Çağırılan fonksiyonların isimlerini bulma
```

