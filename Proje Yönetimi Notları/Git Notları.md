# Git Notları <!-- omit in toc -->

Programlama işlerindeki projelerin yönetimi için kaçınılmaz bir teknolojidir. Senkronize çalışmayı ve versiyon yönetimi sağlar.

<!-- TODO: Yapıyı temizle -->

## Git İşleme Yapısı

- İşleme başlamadan önce üzerinde çalışılacak projenin aslı [pull](#git-deposunu-g%C3%BCncelleme) edilir.
- Her yenilik için **değişikliği açıklayan yorumla birlikte** ayrı ayrı [commit](#Teslim%20etme%20haz%C4%B1rl%C4%B1%C4%9F%C4%B1%20ve%20yorum%20ekleme) yapılır.
- Eğer farklı alanda değişiklikler yapılıyor ise yeni bir [branch](#Branch%20İşlemleri) oluşturulur.
  - Yeni branch kontrol edildikten sonra orjinal (master) branch'ine dahil edilir. ( _Alakalı: [merge request](https://docs.gitlab.com/ee/gitlab-basics/add-merge-request.html)_ )
  - Bu sistemle hataların orjinal projeyi bozması engellenmeye çalışılır.
- Eğer 2 farklı alanda çalışılacakca yeni branch üzerinden dosyalar oluşturulmalı
  - Bu sayede master pull edildiğinde dosya kaybı söz konusu olmayacaktır
  - Bu yeni branch'lar master'a pull edilmez (edilirse branch'a özgü dosyalar da aktarılır)

> Github'ın oluşturduğu "[hello world](https://guides.github.com/activities/hello-world/)" sayfasına da bakabilirsin 👶

## Git'in Kullanıldığı Siteler

- [Github](https://www.github.com)
- [GitLab](https://gitlab.com/)
- [Bitbucket](https://bitbucket.org/)

## Git Kimlik Bilgileri

Kimlik bilgileri ayarı ile git işlemlerinin her birinde giriş yapmanız gerekmez.

### Git Kimlik Bilgilerini Ayarlama

```bash
git config --global user.email "you@example.com"
git config --global user.name "Your Name"
```

### Git Kimlik Bilgilerini Kaydetme

```sh
git config --global credential.helper store
```

### Git Kimlik Bilgilerini Sıfırlama

Detaylar için [buraya](https://stackoverflow.com/a/15382950) tıklayabilirsin.

_Windows:_

```bash
git config --system --unset credential.helper
```

_Diğerleri:_

```bash
git config --global --unset credential.helper
```

## Git Deposunu Oluşturma & Güncelleme

### Git Deposunu Güncelleme

```bash
git fetch --all
git pull
```

Detaylı bilgi için [buraya](https://www.atlassian.com/git/tutorials/setting-up-a-repository/git-clone) bakabilirisin.

### Yeni repository oluşturma

```bash
git init
```

> Git için gerkeli olan dosyaları oluşturur.

### Yerel repo klonlama

```bash
git clone [url] [kopyalanacağı yol]
```

- `url` Github'daki projenin adresi <https://...>
- `kopyalanacağı yol` Bilgisayardaki özel bir yol (C:\Desktop\Temp)

> Var olan git'i istenen dizine kopyalar

### Belli branch'i klonlama

Çoklu değişimin olduğu projelerde sadece kendi branch'imiz üzerinden işlem yapmak isteyebilir ve diğer değişikliklerle uğraşmaya biliriz.

```bash
git clone -branch [branch_name] [url]
```

### Uzak repo klonlama

```bash
git clone [username]@[host]:[url]
```

### Proje dosyalarımızın depoya eklenmesi

```bash
git add .
```

> Bütün dosyalar (. dizindeki tüm dosyalar demektir.) eklenir.

### Teslim etme hazırlığı ve yorum ekleme

```bash
git commit -m "Yorun" # Kısa Açıklama
git commit -m "Yorum" -m "Açıklama" # Başlıklı uzun açıklama
```

- -`m` message anlamına gelmektedir.

> Mesaj ve açıklama ile ile depoya teslim için hazırlama

### Teslim edilecek URL'i belirleme

```bash
git remote add [remote_name] [url]
```

- `remote_name` Kontrol ismi. _Örn: origin_
- `url` Yüklemek istediğimiz yerin adresi

> Github için, projenizin konumuna gelip, \*download kısmındaki kopyalama resmine- basarak, projenizin url'ini kopyalabilirsiniz.

### Birden fazla teslim URL'i belirleme

Detaylı bilgi için [buraya](https://stackoverflow.com/a/14290145) bakabilirsin.

#### Teslim URL'i ekleme

```bash
git remote set-url --add --push [remote_name] [url1]
git remote set-url --add --push [remote_name] [url2]
```

- `--push` yerine diğer git işlemlerini de kullanabilirsiniz. _Örn: fetch_

> Uzaktan kontrol (remote) eklemek için `git remote add [remote_name] [url]` ile oluşturulması gerekir. Aksi halde hata verir.

#### Teslim URL'i kaldırma

```bash
git remote set-url --delete --push [remote_name] [url]
```

#### Teslim URL'lerini kontrol etme

```bash
git remote -v
```

#### Örnek Çıktı

```bash
> git remote -v
origin  https://gitlab.com/yedehrab/bilgiler.git (fetch)
origin  https://github.com/yedehrab/Bilgiler.git (push)
origin  https://gitlab.com/yedehrab/bilgiler.git (push)
```

### Teslim Etme

```bash
git push -u origin [branch]
```

- `branch` Varsa dal ismi (bilginiz yoksa 'master' kullanın)
  - git push -u origin master

> Master olarak url'e yükleme işlemi

## Branch İşlemleri

Branch (dal) git yığıtlarında imleç görevi gören araçlardır. Ek bilgi için [buraya](https://git-scm.com/book/tr/v1/Git-te-Dallanma-Dal-Nedir%3F) tıklayabilirsin.

- **Önemli:** Dallandırmaları orjinal proje üzerinden yapmazsanız diğer dallar ile karışabilir.

> Genelde master işlemi (projenin aslı) ile test işlemlerini birbirinden ayrı yerlerde saklamak amaçlı kullanılırlar

![branch-pic](https://git-scm.com/figures/18333fig0305-tn.png)

> `HEAD` üzerinde bulunduğumuz branch'i (imleci | dalı) gösterir.
> `Yeşil renkli kareler` Commit işlemlerini gösterir.

![detailed-branch-pic](https://git-scm.com/figures/18333fig0309-tn.png)

### Sık Kullanılan Branch İşlemleri

Yeni bir branch, test işlemleri için sıklıkla kullanılır.

| İşlem                                 | Açıklama                    |
| ------------------------------------- | --------------------------- |
| `git branch <branch_ismi>`            | Branch oluşturma            |
| `git checkout <branch>`               | Branch değiştirme           |
| `git branch -d <branch>`              | Local branch kaldırma       |
| `git branch -D <branch>`              | Local branch zorla kaldırma |
| `git push <url | remote> -d <branch>` | Remote branch kaldırma      |

- `<branch>` Seçilecek dal (HEAD (ana dal) için 'master' kullanılır)
  - Örn: `master`
- `-d` Silme parametresi yani `--delete`
- `-D` Zorla silme parametresi yani `--delete --force`
- `<url | remote>` Uzaktaki git adresi veya ismi
  - **Örn**: `origin` veya `https://github.com/yedhrab/YBilgiler.git`

> Branch kaldırma hakkında ek bilgi için [buraya][git branch silme işlemleri] bakabilirsin

## Faydalı git komutları

Zaman zaman gerekebilecek git komutları

### Git Üzerinde Kullanıcı Bilgilerini Saklama

```bash
git config --global credential.helper cache
git config --global credential.helper 'cache --timeout=3600'
```

> Detaylar için [buraya](https://help.github.com/articles/caching-your-github-password-in-git/) tıklayabilirsin.

### Remote Kaldırma & Gösterme

```bash
git remote -v
```

- `-v` Verbose, kontrol edilenleri gösterir.

```bash
git remote rm [branch]
```

- `branch` Kontrol türü. Mesela origin

> Detaylı açıklama için [buraya](https://help.github.com/articles/removing-a-remote/) tıklayabilirsin.

### Son Commiti Kaldırma

```bash
git reset HEAD^ # remove commit locally
git push origin +HEAD # force-push the new HEAD commit
# git push origin +HEAD^:<name of your branch, most likely 'master'> sadece uzaktakini kaldırır
```
> Son yüklemeyi kaldırır. Bu işlemden sonra tekrar commit etmeniz gerekmekte. Detay için [link](https://stackoverflow.com/a/8225166)

### Son Değişiklikleri Geri Alma

```sh
git revert --strategy resolve <commit>
```

> https://stackoverflow.com/a/3207170

### Pull From işlemini Geri Alma

Bunun için başka bir branch'a geçip, geri almak istediğimiz branch'ı siliyoruz.

```sh
git checkout <branch2>
git branch -D <branch1>
git checkout <branch1>
```

- `<branch1>` Düzeltilmek istenen branch
- `<branch2>` Farkı herhangi bir branch

## Uygulamalar Üzerinde Git

### JetBrains IDEs

- Branch kontrollerini sağ alt köşedeki git alanından yapabilirsin.
  - Bu alan açık iken klavyen ile \*arama- yapabilirsin.
  - `New Branch` kısmından yeni _yerel branch_ oluşturabilirsin.
  - `Remote branch` kısmındaki herhangi bir branch üzerine tıklayarak `Merge Into Current` ile kendi projene dahil edebilirsin.

## Git Cheat Sheet

![git](../res/git-cheet-sheet.jpeg)

## Kitaplar

- [Pro Git](https://drive.google.com/open?id=12bYrrbB2ESt531bYWnddf5NpEg2_fGzl)

## Harici Linkler

- [Sık kullanılan git komutları](https://github.com/joshnh/Git-Commands)
- [Start Using Git | Gitlab](https://docs.gitlab.com/ee/gitlab-basics/start-using-git.html)
- [Github ile Fork ve Pull Request](https://medium.com/@noteCe/github-ile-fork-ve-pull-request-be6077342834)
- [git: 'credential-cache' is not a git command](https://stackoverflow.com/a/11889392/9770490)
- [Git Rebase Kavramı](https://git-scm.com/book/tr/v1/Git-te-Dallanma-Rebasing-Tekrar-Adresleme)
- [Git branch silme işlemleri]

[git branch silme işlemleri]: https://stackoverflow.com/a/2003515
