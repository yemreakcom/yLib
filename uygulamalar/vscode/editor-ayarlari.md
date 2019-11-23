---
description: VsCode editörünü özelleştirme
---

# 🔆 VsCode Editör Ayarları

## 👮‍♂️ Editör Ayarlarına Erişim

Sol alt köşedeki **ayarlar simgesi**'ne tıklayarak ayarlara erişebilirsin

* Sağ üst köşedeki `{}` simgesine tıklayıp JSON formatında ayarları görüntüleyebilirsin
* Kod formatlama \(intellisense\) ayarlarına [buradan](https://code.visualstudio.com/docs/editor/intellisense) erişebilirsin

**Ayar dosyaları:**

* Windows: `%APPDATA%\Code\User\settings.json`
* macOS: `$HOME/Library/Application Support/Code/User/settings.json`
* Linux: `$HOME/.config/Code/User/settings.json`

## 💎 Editör Değişkenleri

Değişkenlerin kullanım şekilleri:

* `${<değişken>}`
  * Eğer özel karakter içeriyorsa bu yöntem daha sağlıklıdır
* `$<değişken>`

| Değişken | Açıklama |
| :--- | :--- |
| `workspaceFolder` | Çalışma dizini yolu |
| `file` | Açık olan dosya yolu |
| `fullFileName` | Tam açık olan dosya yolu |
| `pythonPath` | Python yolu |

> Tüm değişkenlere [buradan](https://code.visualstudio.com/docs/editor/variables-reference) erişebilirsin.

## ✨ Faydalı Yazılar

{% page-ref page="ozellestirmelerim.md" %}

