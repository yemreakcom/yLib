---
description: Submodule'ler repo içinde repo yapısıdır.
---

# 📂 Git Submodules

## ❔ Nedir

* Bu sistem sayesinden parçalı olarak geliştirme mümkün kılınır
* Komutlarla tüm projenin her modülü güncellenir

### ✨ SubModule Oluşturma

```bash
git submodule add <url> <path>
git submodule --name <isim> add <url> <path> # İsim ile ekleme
```

> [Git: symlink/reference to a file in an external repository](https://stackoverflow.com/a/27770463/9770490)

### 💫 SubModuleleri Güncelleme

```bash
git submodule init
git submodule update --remote
```

> [Easy way to pull latest of all git submodules](https://stackoverflow.com/a/1032653)

