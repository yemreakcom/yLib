# Git Notları <!-- omit in toc -->

Programlama işlerindeki projelerin yönetimi için kaçınılmaz bir teknolojidir. Senkronize çalışmayı ve versiyon yönetimi sağlar.

## İçerik <!-- omit in toc -->

> `HOME` tuşu ile yukarı yönlenebilrsiniz.

- [Git İşleme Yapısı](#git-i%CC%87%C5%9Fleme-yap%C4%B1s%C4%B1)
- [Git'in Kullanıldığı Siteler](#gitin-kullan%C4%B1ld%C4%B1%C4%9F%C4%B1-siteler)
- [Git Kimlik Bilgileri](#git-kimlik-bilgileri)
  - [Git Kimlik Bilgilerini Ayarlama](#git-kimlik-bilgilerini-ayarlama)
  - [Git Kimlik Bilgilerini Kaydetme](#git-kimlik-bilgilerini-kaydetme)
  - [Git Kimlik Bilgilerini Sıfırlama](#git-kimlik-bilgilerini-s%C4%B1f%C4%B1rlama)
- [Git Deposunu Oluşturma & Güncelleme](#git-deposunu-olu%C5%9Fturma--g%C3%BCncelleme)
  - [Git Deposunu Güncelleme](#git-deposunu-g%C3%BCncelleme)
  - [Yeni repository oluşturma](#yeni-repository-olu%C5%9Fturma)
  - [Yerel repo klonlama](#yerel-repo-klonlama)
  - [Belli branch'i klonlama](#belli-branchi-klonlama)
  - [Uzak repo klonlama](#uzak-repo-klonlama)
  - [Proje dosyalarımızın depoya eklenmesi](#proje-dosyalar%C4%B1m%C4%B1z%C4%B1n-depoya-eklenmesi)
  - [Teslim etme hazırlığı ve yorum ekleme](#teslim-etme-haz%C4%B1rl%C4%B1%C4%9F%C4%B1-ve-yorum-ekleme)
  - [Teslim edilecek URL'i belirleme](#teslim-edilecek-urli-belirleme)
  - [Birden fazla teslim URL'i belirleme](#birden-fazla-teslim-urli-belirleme)
    - [Teslim URL'i ekleme](#teslim-urli-ekleme)
    - [Teslim URL'i kaldırma](#teslim-urli-kald%C4%B1rma)
    - [Teslim URL'lerini kontrol etme](#teslim-urllerini-kontrol-etme)
    - [Örnek Çıktı](#%C3%B6rnek-%C3%A7%C4%B1kt%C4%B1)
  - [Teslim Etme](#teslim-etme)
- [Branch İşlemleri](#branch-i%CC%87%C5%9Flemleri)
- [Branch (Dal) Oluşturma](#branch-dal-olu%C5%9Fturma)
  - [Branch (Dal) Değiştirme](#branch-dal-de%C4%9Fi%C5%9Ftirme)
  - [Branch (Dal) Kaldırma](#branch-dal-kald%C4%B1rma)
    - [Yerel branch silme](#yerel-branch-silme)
    - [Uzaktaki (remote) branch'ı silme](#uzaktaki-remote-branch%C4%B1-silme)
- [Faydalı git komutları](#faydal%C4%B1-git-komutlar%C4%B1)
  - [Git Üzerinde Kullanıcı Bilgilerini Saklama](#git-%C3%BCzerinde-kullan%C4%B1c%C4%B1-bilgilerini-saklama)
  - [Remote Kaldırma & Gösterme](#remote-kald%C4%B1rma--g%C3%B6sterme)
  - [Son hatalı yüklemeyi kaldırma](#son-hatal%C4%B1-y%C3%BCklemeyi-kald%C4%B1rma)
- [Uygulamalar Üzerinde Git](#uygulamalar-%C3%BCzerinde-git)
  - [JetBrains IDEs](#jetbrains-ides)
- [Git Cheat Sheet](#git-cheat-sheet)
- [Kitaplar](#kitaplar)
- [Harici Linkler](#harici-linkler)

## Git İşleme Yapısı

> Terimlerin üzerine tıklayarak, açıklamalarının yapıldığı yazıya yönelebilirsin.

- İşleme başlamadan önce üzerinde çalışılacak projenin aslı [pull](#git-deposunu-g%C3%BCncelleme) edilir.
- Her yenilik için **değişikliği açıklayan yorumla birlikte**  ayrı ayrı [commit](#Teslim%20etme%20haz%C4%B1rl%C4%B1%C4%9F%C4%B1%20ve%20yorum%20ekleme) yapılır.
- Eğer farklı alanda değişiklikler yapılıyor ise yeni bir [branch](#Branch%20İşlemleri) oluşturulur.
  - Yeni branch kontrol edildikten sonra orjinal (master) branch'ine dahil edilir. ( *Alakalı: [merge request](https://docs.gitlab.com/ee/gitlab-basics/add-merge-request.html)* )
  - Bu sistemle hataların orjinal projeyi bozması engellenmeye çalışılır.

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

*Windows:*

```bash
git config --system --unset credential.helper
```

*Diğerleri:*

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
git commit -m "Yorum" -m "Açıklama"
```

- -`m` message anlamına gelmektedir.

> Mesaj ve açıklama ile ile depoya teslim için hazırlama

### Teslim edilecek URL'i belirleme

```bash
git remote add [remote_name] [url]
```

- `remote_name` Kontrol ismi. *Örn: origin*
- `url` Yüklemek istediğimiz yerin adresi

> Github için, projenizin konumuna gelip, *download kısmındaki kopyalama resmine- basarak, projenizin url'ini kopyalabilirsiniz.

### Birden fazla teslim URL'i belirleme

Detaylı bilgi için [buraya](https://stackoverflow.com/a/14290145) bakabilirsin.

#### Teslim URL'i ekleme

```bash
git remote set-url --add --push [remote_name] [url1]
git remote set-url --add --push [remote_name] [url2]
```

- `--push` yerine diğer git işlemlerini de kullanabilirsiniz. *Örn: fetch*

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

## Branch (Dal) Oluşturma

```bash
git branch [branch_ismi]
```

> Yeni bir branch (imleç) oluştulur. Test işlemleri için sık kullanılırlar.

### Branch (Dal) Değiştirme

```bash
git checkout [branch]
```

- `branch` Seçilecek dal (HEAD (ana dal) için 'master' kullanılır)
  - git checkout master

> Seçili branch'i değiştiri. (Master iken test'e geçmek gibi)

### Branch (Dal) Kaldırma

Eklenen branch'i kaldırmak için uygulanır. Detaylara [buraya](https://koukia.ca/delete-a-local-and-a-remote-git-branch-61df0b10d323) tıklayarak erişebilirsin.

#### Yerel branch silme

```bash
git branch [param] [branch]
```

**Parametreler:**

- `-d` Silme parametresi
- `-D` Zorla silme parametresi

#### Uzaktaki (remote) branch'ı silme

```bash
git push [url] --delete [branch]
```

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

### Son hatalı yüklemeyi kaldırma

```bash
git reset HEAD~
```

> Son yüklemeyi kaldırır. Bu işlemden sonra tekrar commit etmeniz gerekmekte. Detay için [link](https://stackoverflow.com/questions/927358/how-do-i-undo-the-most-recent-commits-in-git)

## Uygulamalar Üzerinde Git

### JetBrains IDEs

- Branch kontrollerini sağ alt köşedeki git alanından yapabilirsin.
  - Bu alan açık iken klavyen ile *arama- yapabilirsin.
  - `New Branch` kısmından yeni *yerel branch* oluşturabilirsin.
  - `Remote branch` kısmındaki herhangi bir branch üzerine tıklayarak `Merge Into Current` ile kendi projene dahil edebilirsin.

## Git Cheat Sheet

![git](../images/git-cheet-sheet.jpeg)

## Kitaplar

- [Pro Git](https://drive.google.com/open?id=12bYrrbB2ESt531bYWnddf5NpEg2_fGzl)

## Harici Linkler

- [Sık kullanılan git komutları](https://github.com/joshnh/Git-Commands)
- [Start Using Git | Gitlab](https://docs.gitlab.com/ee/gitlab-basics/start-using-git.html)
- [Github ile Fork ve Pull Request](https://medium.com/@noteCe/github-ile-fork-ve-pull-request-be6077342834)
- [git: 'credential-cache' is not a git command](https://stackoverflow.com/a/11889392/9770490)