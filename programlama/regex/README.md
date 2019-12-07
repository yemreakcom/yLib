---
description: >-
  Fazla miktardaki veya büyük boyutlardaki metinlerini ayrıştırma için
  kullanılan dil formatı
---

# 💎 Regex

## 🧱 Temel İşlemler <a id="temel-islemler"></a>

Kullanım formatı `r""` \(python\) veya `/ /` \(javascript\) şeklindedir.![](https://github.com/yedhrab/YWiki/tree/169abadfd1b8862c004399268f6ca1f9f9359d61/1%20-%20Programlama%20Notlar%C4%B1/res/regex_cheat_sheets.png)

| 💎 RegEx | 📑 Açıklama |
| :--- | :--- |
| `|` | Or işlemi veya anlamına gelir |
| `[ab]` | `a` veya `b` demektir |
| `(ab)` | `ab` demektir |
| `(ab )` | `ab` anlamına gelir \(⚠ boşluğa dikkat\) |
| `[ab] | (ab)` | `a` veya `ab`, `b` veya `ab` demektir |
| `[aA]nkara` | `Ankara` veya `ankara` metinlerini bulur |
| `\w` | Herhangi bir harfi temsil eder |
| `\b` | `\bword` için sadece `word`'leri bulur, \([örnek](https://regexr.com/4ps8a)\) |

## 🧮 Miktar İşlemleri

| 💎 RegEx | 📑 Açıklama |
| :--- | :--- |
| `?` | 0 veya 1 kere |
| `*` | 0 veya daha fazla |
| `+` | 1 veya daha fazla |
| `{n}` | `n` tane |
| `{n,}` | En az `n` tane |
| `{n, m}` | En az `n` en fazla `m` tane |

## 🔍 Kelime Arama <a id="kelime-arama"></a>

| Regex | Açıklama | Link |
| :--- | :--- | :--- |
| `\wab\w` | `ab` geçen **4 harfli** kelimeleri bulur \(özel karakterleri desteklemez\) | ​[🔗](https://regex101.com/r/TxuXuH/2)​ |
| `\w*ab\w` | Sonda 1 farklı karakter olan `ab` içeren kelimeleri bulur |  |
| `\w*ab\w*` | İçerisinde herhangi bir yerde olan `ab` içeren kelimeleri bulur |  |
| `\baş` | Metin içerisinde `aş` olanları bulur \(özel karakterleri \(`ş`\) destekler \) | ​[🔗](https://regex101.com/r/TxuXuH/3)​ |
| `(\baş )` | İçerisinde `aş` geçen cümleleri bulur | ​[🔗](https://regex101.com/r/TxuXuH/5)​ |
| `\byunus | \bemre` | `yunus` veya `emre` olan kelimeleri bulur | ​[🔗](https://regex101.com/r/TxuXuH/6)​ |

## 💫 Karışık İşlemler <a id="karisik-islemler"></a>

| 💎 RegEx | 📑 Açıklama |
| :--- | :--- |
| `": \\s+"` | `": "` göre ayırma |
| `\\.` | `.` ya göre ayırma \(`"."` çalışmaz |

## 🔗 Faydalı Bağlantılar

{% embed url="https://regex101.com/" %}

