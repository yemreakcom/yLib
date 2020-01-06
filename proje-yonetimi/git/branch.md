---
description: Projedeki her geliştirme dallarının yönetimi
---

# 🌳 Git ile Branch İşlemleri

## 🚧 Branch İşlemleri

Branch \(dal\) git yığıtlarında imleç görevi gören araçlardır. Ek bilgi için [buraya](https://git-scm.com/book/tr/v1/Git-te-Dallanma-Dal-Nedir%3F) tıklayabilirsin.

* **Önemli:** Dallandırmaları orjinal proje üzerinden yapmazsanız diğer dallar ile karışabilir.

> Genelde master işlemi \(projenin aslı\) ile test işlemlerini birbirinden ayrı yerlerde saklamak amaçlı kullanılırlar

![branch-pic](https://git-scm.com/figures/18333fig0305-tn.png)

> `HEAD` üzerinde bulunduğumuz branch'i \(imleci \| dalı\) gösterir. `Yeşil renkli kareler` Commit işlemlerini gösterir.

![detailed-branch-pic](https://git-scm.com/figures/18333fig0309-tn.png)

## 🌟 Sık Kullanılan Branch İşlemleri

Yeni bir branch, test işlemleri için sıklıkla kullanılır.

| İşlem | Açıklama |
| :--- | :--- |
| `git branch <branch_ismi>` | Branch oluşturma |
| `git checkout <branch>` | Branch değiştirme |
| `git branch -d <branch>` | Local branch kaldırma silme |
| `git branch -D <branch>` | Local branch zorla kaldırma silme |
| `git push <url veya remote> -d <branch>` | Remote branch kaldırma |

* `<branch>` Seçilecek dal \(HEAD \(ana dal\) için 'master' kullanılır\)
  * Örn: `master`
* `-d` Silme parametresi yani `--delete`
* `-D` Zorla silme parametresi yani `--delete --force`
* `<url | remote>` Uzaktaki git adresi veya ismi
  * **Örn**: `origin` veya `https://github.com/yedhrab/YBilgiler.git`

> Branch kaldırma hakkında ek bilgi için \[buraya\]\[git branch silme işlemleri\] bakabilirsin

## 🌍 Remote Kaldırma & Gösterme

```bash
git remote -v
```

* `-v` Verbose, kontrol edilenleri gösterir.

```bash
git remote rm [branch]
```

* `branch` Kontrol türü. Mesela origin

> Detaylı açıklama için [buraya](https://help.github.com/articles/removing-a-remote/) tıklayabilirsin.

## 🔗 Harici Bağlantılar

* [Git branch silme işlemleri](https://stackoverflow.com/a/2003515)
* [Git Rebase Kavramı](https://git-scm.com/book/tr/v1/Git-te-Dallanma-Rebasing-Tekrar-Adresleme)

