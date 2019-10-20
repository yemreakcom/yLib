---
description: Microsoft'un sunduğu online git yönetim sitesi
---

# 🐙 Github

## 🗽 GitHub Nedir, Ne için Kullanılır

Kod camiasının sosyal medyası olarak da geçen github, 👩‍💻 kod 👨‍💻 paylaşım ve yönetim platformudur.

* Proje yönetimi kolaylaştırır
* ToDo yapılarıyla ekip işini destekler
* Eklentileri ile verimlilik sağlar
* Markdown, PDF ve `.ipynb` formatına ön izleme sağlar
  * Markdown videolarını desteklemez
  * Video eklemek için **gif** kullanın
  * **Gif**'e tıklandığında video linki verin
  * `[![app](res/app.gif)](res/app.mp4)`
* Alternatifleri: Gitlab, Bitbucket, Sourceforge ...

> Bu konuyla **birebir alakalı** olan [git notlarıma](https://github.com/yedhrab/YWiki/tree/169abadfd1b8862c004399268f6ca1f9f9359d61/Git%20Notları.md) bakmanda fayda var.

## 🌟 GitHub Pro

[Github](https://github.com) öğrenciler için ücretsiz **pro** faydaları sağlamaktadır.

* Faydalar için [buraya](https://education.github.com/benefits/offers) bakabilirsin.
* Kayıt ve detaylı işlemler için [buraya](https://education.github.com/students) bakabilirsin.
* Sunduğu faydalar için [buraya](https://education.github.com/pack/offers) bakabilirsin
* Eğitim topluluğu için [buraya](https://education.github.community/c/students) bakabilirsin
* Eğitim okulları için [buraya](https://education.github.com/partners/schools) bakabilirsin.
* [Octodex](https://octodex.github.com/)
* Detaylı bilgiler ve sık sorulan sorular için de [buraya](https://help.github.com/en/categories/teaching-and-learning-with-github-education) bakabilirsin.

> Diğer avantajlar için [github student pack](https://education.github.com/pack) sayfasına bakabilirsin.

## 💻 GitHub Desktop

Kodlarla uğraşmak yerine arayüzden işini halletmek isteyenler için.

* ✲ Ctrl ↩ Enter ile **commit** yapılır
* ✲ Ctrl P ile **push** edilir
* `History` alnından **commit**'lere sağ tıklayıp `Rever Commit` ile geri alabilrisiniz
  * 5 **commit** geri gidecekseniz, en tepeden aşağıya doğru 5 kere **revert** etmeniz lazım
  * Aksi takdirde 🐞 **merge conflict**'ler ile  uğraşırsınız

## 👨‍💼 Proje Yönetimi

### 🚙 Repository'nin Oluşturulması ve Dosyaların Aktarılması

* [Github](https://github.com) üzerinden sağ üst köşedeki `+` butonundan `New Repository` diyerek ya da direkt olarak [buradan](https://github.com/new) repository'i oluşturun
* `git clone` ile veya var olan projeniz üzerinden `git remote add origin <url>` ile bağlantıyı kurun
  * Uğraşmak istemez iseniz; projenizi `git clone` ile kopyalayın ve yüklemek istediklerinizi klonlanan projenin için atın
* Reponuzu güncellemek için sırasıyla;
  * `git add .`
  * `git commit -m "Açıklama"`
    * Açıklamlara `#` karakteri ile **Issue**'yi hedef gösterebilirsin
    * Genel yorum formatı: `<Açıklama> (#<IssueID>)` ve isteğe bağlı ek açıklamalar
  * `git push origin master`

### 💫 Repo Üzerinde Proje Yönetimi

Repository üzerinde proje yönetimi için scrum veya canvan \(yapılacaklar, yapılanlar, yapıldı vs..\) yapısı kullanılmaktadır.

* Repo sayfasında `Project` sekmesine girin ve `New Project` butonuna tıklayın
* Proje ismini ve açıklamasını yazdıktan sonra `Project Template` alanından `Automated Kanban` seçeniğini işaretleyin
* `Automated Kanban` yapısı oluşturulan sorunları, yapılacak planları ve yapılanları otomatik olarak ekler
* Repo sayfasında `Issue` alanında sorunları, yapılacak planları ve yapılanları oluşturun
* Oluşturduğun her `Issue` için `label`, `proje` ve kim ile alakalı ise onu `assign` alanında belirtin
  * `Issue`'lerde markdown formatı geçerlidir
  * `[ ]` yapısı ile ypaılacakları eklerseniz süreç analizi özelliği gelir
* Oluşturulan `Issue`'ler, `Automated Kanban` yapısı ve sayesinde belirttiğiniz projeye otomatik akatarılacaktır.
* `Milestones` ile yapılacak işlere süre sınırı \(deadline\) tanımlayabilirsin

## 📂 GitHub Üzerindeki Açılmayan Dosyalar

> [Stackoverflow açıklaması](https://stackoverflow.com/questions/19584255/what-does-a-grey-icon-in-remote-github-mean)

## 🔌 GitHub Eklentileri

Eklentilerin sayfasına [buradan](https://github.com/marketplace) erişebilirsin.

> Bilmiyorsan elleşme derim 🙄

| Eklenti | Açıklama |
| :--- | :--- |
| [todo](https://github.com/marketplace/todo) | Kod içerisindeki `@todo` ve `TODO` alanlarını _Github_'a entegre eder. |
| [Gitpod](https://github.com/marketplace/gitpod-io) | Online **vscode** temalı editör. \(💡 chrome [eklentisini](https://chrome.google.com/webstore/detail/gitpod-online-ide/dodmmooeoklaejobgleioelladacbeki) indirmeyi unutma\) |
| [Semaphor](https://github.com/marketplace/semaphore) | Bir bak 🙋‍♀️ |
| [GitLocalize](https://github.com/marketplace/gitlocalize) | Bir bak 🙋‍♀️ |
| [Codetree](https://github.com/marketplace/codetree) | Çevik \(agile\) takımların için proje yönetim eklentisi \(paralı 🧐\) |

## 🆘 GitHub Yardımcıları

| Yardımcı | Açıklama |
| :--- | :--- |
| [GitGuardian](https://www.gitguardian.com/) | Kimlik bilgilerinin paylaşılması durumunu kontrol eder, uyarır |

## 🔐 GitHub Credential Değiştirme

Kaynak için [buraya](https://www.youtube.com/watch?v=otBNYXz5Ie0) bakabilirsin

## 🔗 Harici Bağlantılar

* [GitHub page'e domain bağlama](https://medium.com/@tivikter/github-pagesi-%C3%B6zel-domain-ile-kullanmak-ce57d229dae9)

> Başka yok 😒

