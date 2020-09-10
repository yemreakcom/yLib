---
description: Git ile proje yönetimini ele alır
---

# 📦 Git ile Repository İşlemleri

## 🔄 Git Deposunu Güncelleme

```bash
git fetch --all
git pull
```

Detaylı bilgi için [buraya](https://www.atlassian.com/git/tutorials/setting-up-a-repository/git-clone) bakabilirisin.

## ✨ Yeni repository oluşturma

```bash
git init
```

> Git için gerkeli olan dosyaları oluşturur.

## ⏬ Yerel repo klonlama

```bash
git clone [url] [kopyalanacağı yol]
```

* `url` Github'daki projenin adresi [https://...](https://...)
* `kopyalanacağı yol` Bilgisayardaki özel bir yol \(C:\Desktop\Temp\)

> Var olan git'i istenen dizine kopyalar

## 💡 Git Bilgilerini Alma

```bash
git config --get remote.origin.url # Url'i alma
```

{% hint style="info" %}
‍🧙‍♂ Detaylı bilgi için [How can I determine the URL that a local Git repository was originally cloned from?](https://stackoverflow.com/questions/4089430/how-can-i-determine-the-url-that-a-local-git-repository-was-originally-cloned-fr) alanına bakabilirsin.
{% endhint %}

## ⏬ Belli branch'i klonlama

Çoklu değişimin olduğu projelerde sadece kendi branch'imiz üzerinden işlem yapmak isteyebilir ve diğer değişikliklerle uğraşmaya biliriz.

```bash
git clone -branch [branch_name] [url]
```

## ⏬ Uzak repo klonlama

```bash
git clone [username]@[host]:[url]
```

## ➕ Proje dosyalarımızın depoya eklenmesi

```bash
git add .
```

> Bütün dosyalar \(. dizindeki tüm dosyalar demektir.\) eklenir.

## 💬 Teslim etme hazırlığı ve yorum ekleme

```bash
git commit -m "Yorun" # Kısa Açıklama
git commit -m "Yorum" -m "Açıklama" # Başlıklı uzun açıklama
```

* -`m` message anlamına gelmektedir.

> Mesaj ve açıklama ile ile depoya teslim için hazırlama

## 🔗 Teslim edilecek URL'i belirleme

```bash
git remote add [remote_name] [url]
```

* `remote_name` Kontrol ismi. _Örn: origin_
* `url` Yüklemek istediğimiz yerin adresi

> Github için, projenizin konumuna gelip, \*download kısmındaki kopyalama resmine- basarak, projenizin url'ini kopyalabilirsiniz.

## 🛰️ Birden fazla teslim URL'i belirleme

Detaylı bilgi için [buraya](https://stackoverflow.com/a/14290145) bakabilirsin.

### ➕ Teslim URL'i ekleme

```bash
git remote set-url --add --push [remote_name] [url1]
git remote set-url --add --push [remote_name] [url2]
```

* `--push` yerine diğer git işlemlerini de kullanabilirsiniz. _Örn: fetch_

> Uzaktan kontrol \(remote\) eklemek için `git remote add [remote_name] [url]` ile oluşturulması gerekir. Aksi halde hata verir.

### ➖ Teslim URL'i kaldırma

```bash
git remote set-url --delete --push [remote_name] [url]
```

### 👁️ Teslim URL'lerini kontrol etme

```bash
git remote -v
```

### ⭐ Örnek Çıktı

```bash
> git remote -v
origin  https://gitlab.com/yedehrab/bilgiler.git (fetch)
origin  https://github.com/yedehrab/Bilgiler.git (push)
origin  https://gitlab.com/yedehrab/bilgiler.git (push)
```

## ⏫ Teslim Etme

```bash
git push -u origin [branch]
```

* `branch` Varsa dal ismi \(bilginiz yoksa 'master' kullanın\)
  * git push -u origin master

> Master olarak url'e yükleme işlemi

## 💦 Dosya Silme

* Git önbelleğindeki dosyayı siler
* Gİt geçmişinde gözükmez

```bash
git rm --cached <dosya_yolu>
```

{% hint style="info" %}
‍🧙‍♂ Detaylı bilgi için [👪 Clear git local cache](https://stackoverflow.com/a/41863575/9770490) alanına bakabilirsin.
{% endhint %}

## 🚚 Dosyayı Taşıma veya Yeniden Adlandırma

* Git içerisinde büyük küçük harflerden kaynaklı oluşan sıkıntılar için önerilir
* Dosyanın git içerisindeki konumu günceller

```bash
git mv <old_name> <new_name>
```

## 🔗 Harici Linkler

* [📕 Pro Git](https://drive.google.com/open?id=12bYrrbB2ESt531bYWnddf5NpEg2_fGzl)
* [Sık kullanılan git komutları](https://github.com/joshnh/Git-Commands)
* [Github ile Fork ve Pull Request](https://medium.com/@noteCe/github-ile-fork-ve-pull-request-be6077342834)

