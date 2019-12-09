---
description: GitHub API ile repoların bilgilerine erişme
---

# 💫 GitHub API

## 🔰 GitHub API Hakkında

* 💰 Ücretsizdir ve API key gerektirmez
* 👮‍♂️ Aynı IP üzerindeki isteklerin belirli limitleri vardır

## ⭐ Release Bilgilerine Erişme

* 🏗️ `https://api.github.com/repos/username/projectName/releases/latest` URL yapısı ile erişilir
* 🔗 [`https://api.github.com/repos/yedhrab/YHotkeys/releases/latest`](https://api.github.com/repos/yedhrab/YHotkeys/releases/latest)
* 📜 JSON içerisindeki `assets_url` release dosyalarının URL'lerinin bilgisini verir
* 📂 Proje **assets** dosyalarına direkt erişmek için `/owner/name/releases/latest/download/asset-name.zip` yapısı kullanılır
  * 👀 Detaylar için [Linking to Releases](https://help.github.com/en/github/administering-a-repository/linking-to-releases) alanına bakabilirsin
  * 👁️ [Is there a link to GitHub for downloading a file in the latest release of a repository?](https://stackoverflow.com/questions/24987542/is-there-a-link-to-github-for-downloading-a-file-in-the-latest-release-of-a-repo)



