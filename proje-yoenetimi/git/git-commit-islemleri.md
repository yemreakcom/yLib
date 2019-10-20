---
description: Her değişikliği belirten commitler hakkında detaylar
---

# ✨ Git Commit İşlemleri

## Son Commit'i Kaldırma

```bash
git reset HEAD^ # remove commit locally
git push origin +HEAD # force-push the new HEAD commit
# git push origin +HEAD^:<name of your branch, most likely 'master'> sadece uzaktakini kaldırır
```

> Son yüklemeyi kaldırır. Bu işlemden sonra tekrar commit etmeniz gerekmekte. Detay için [link](https://stackoverflow.com/a/8225166)

## Son Değişiklikleri Geri Alma

```bash
git revert --strategy resolve <commit>
```

> [https://stackoverflow.com/a/3207170](https://stackoverflow.com/a/3207170)

## Pull From işlemini Geri Alma

Bunun için başka bir branch'a geçip, geri almak istediğimiz branch'ı siliyoruz.

```bash
git checkout <branch2>
git branch -D <branch1>
git checkout <branch1>
```

* `<branch1>` Düzeltilmek istenen branch
* `<branch2>` Farkı herhangi bir branch

## Tüm Commitlerden Dizini Kaldırma

Alttaki script'te `<dizin>` yazan kısmı kaldırmak istediğiniz dizinin ismi ile değiştirin.

```bash
git filter-branch --tree-filter "rm -rf <dizin>" --prune-empty -f HEAD
git for-each-ref --format="%(refname)" refs/original/ | xargs -n 1 git update-ref -d
echo <dizin>/ >> .gitignore
git add .gitignore
git commit -m 'Removing sessions from git history'
git gc
git push origin master --force
```

## Git Tag'ları Kaldırma \(Release Aşamasındakiler\)

```bash
# Localde kaldırma
git tag -d `git tag | grep -E '.'`

# Remote'da kaldırma
git ls-remote --tags origin | awk '/^(.*)(s+)(.*[a-zA-Z0-9])$/ {print ":" $2}' | xargs git push origin
```

> [Deleting Git Tags Locally and on Github](https://www.alwaystwisted.com/articles/deleting-git-tags-locally-and-on-github)

