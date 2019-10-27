---
description: Versiyon yönetim dünyasına giriş
---

# 🚶‍ Git Giriş

## ❔ Git Nedir

Programlama işlerindeki projelerin yönetimi için kaçınılmaz bir teknolojidir.

* Senkronize çalışmayı ve versiyon yönetimi sağlar
* Branch yapısı ile geliştirmelerin birbirinden bağımsız ilerlemesine olanak sağlar

> 📢 Git'i detaylıca anlatan [Git ile Versiyon Kontrolü](https://book.git.yemreak.com) kitabını baz alan sayfama bakmanda fayda var

## 🌆 Git Kullanım Senaryosu

* İşleme başlamadan önce üzerinde çalışılacak projenin aslı [pull]() edilir.
* Her yenilik için **değişikliği açıklayan yorumla birlikte** ayrı ayrı [commit]() yapılır.
* Eğer farklı alanda değişiklikler yapılıyor ise yeni bir [branch]() oluşturulur.
  * Yeni branch kontrol edildikten sonra orjinal \(master\) branch'ine dahil edilir. \( _Alakalı:_ [_merge request_](https://docs.gitlab.com/ee/gitlab-basics/add-merge-request.html) \)
  * Bu sistemle hataların orjinal projeyi bozması engellenmeye çalışılır.
* Eğer 2 farklı alanda çalışılacakca yeni branch üzerinden dosyalar oluşturulmalı
  * Bu sayede master pull edildiğinde dosya kaybı söz konusu olmayacaktır
  * Bu yeni branch'lar master'a pull edilmez \(edilirse branch'a özgü dosyalar da aktarılır\)

> Github'ın oluşturduğu "[hello world](https://guides.github.com/activities/hello-world/)" sayfasına da bakabilirsin 👶

## 🔗 Git'in Kullanımına Olanak Sağlayan Siteler

* [Github](https://www.github.com)
* [GitLab](https://gitlab.com/)
* [Bitbucket](https://bitbucket.org/)

## 🆔 Git Kimlik Bilgileri

Kimlik bilgileri ayarı ile git işlemlerinin her birinde giriş yapmanız gerekmez.

### 🔩 Kimlik Bilgilerini Ayarlama

```bash
git config --global user.email "you@example.com"
git config --global user.name "Your Name"
```

### 💾 Kimlik Bilgilerini Kaydetme

```bash
git config --global credential.helper store
```

### 💽 Kullanıcı Bilgilerini Geçici Olarak Saklama

```bash
git config --global credential.helper cache
git config --global credential.helper 'cache --timeout=3600'
```

> Detaylar için [buraya](https://help.github.com/articles/caching-your-github-password-in-git/) tıklayabilirsin.

### 🧹 Kimlik Bilgilerini Sıfırlama

Detaylar için [buraya](https://stackoverflow.com/a/15382950) tıklayabilirsin.

_Windows:_

```bash
git config --system --unset credential.helper
```

_Diğerleri:_

```bash
git config --global --unset credential.helper
```

## 🔗 Harici Linkler

* [Start Using Git \| Gitlab](https://docs.gitlab.com/ee/gitlab-basics/start-using-git.html)
* [git: 'credential-cache' is not a git command](https://stackoverflow.com/a/11889392/9770490)
* [Most known command](https://dev.to/juni/git-and-github---must-know-commands-to-make-your-first-commit-333c)

