# Github Notları <!-- omit in toc -->

## İçerikler <!-- omit in toc -->

- [Github Nedir, Ne için Kullanılır](#Github-Nedir-Ne-i%C3%A7in-Kullan%C4%B1l%C4%B1r)
- [Github Pro](#Github-Pro)
- [Proje Yönetimi](#Proje-Y%C3%B6netimi)
  - [Repository'nin Oluşturulması ve Dosyaların Aktarılması](#Repositorynin-Olu%C5%9Fturulmas%C4%B1-ve-Dosyalar%C4%B1n-Aktar%C4%B1lmas%C4%B1)
  - [Repo Üzerinde Proje Yönetimi](#Repo-%C3%9Czerinde-Proje-Y%C3%B6netimi)
- [Github Üzerindeki Açılmayan Dosyalar](#Github-%C3%9Czerindeki-A%C3%A7%C4%B1lmayan-Dosyalar)
- [Github Eklentileri](#Github-Eklentileri)
- [Github Yardımcıları](#Github-Yard%C4%B1mc%C4%B1lar%C4%B1)
- [Github Credential Değiştirme](#Github-Credential-De%C4%9Fi%C5%9Ftirme)
- [Harici Bağlantılar](#Harici-Ba%C4%9Flant%C4%B1lar)

## Github Nedir, Ne için Kullanılır

Kod camiasının sosyal medyası olarak da geçen github, 👩‍💻 kod 👨‍💻 paylaşım ve yönetim platformudur.

- Proje yönetimi kolaylaştırır
- ToDo yapılarıyla ekip işini destekler
- Eklentileri ile verimlilik sağlar
- Markdown, PDF ve `.ipynb` formatına ön izleme sağlar
  - Markdown videolarını desteklemez
  - Video eklemek için **gif** kullanın
  - **Gif**'e tıklandığında video linki verin
  - `[![app](res/app.gif)](res/app.mp4)`
- Alternatifleri: Gitlab, Bitbucket, Sourceforge ...

> Bu konuyla **birebir alakalı** olan [git notlarıma][git notlarım] bakmanda fayda var.

## Github Pro

[Github] öğrenciler için ücretsiz **pro** faydaları sağlamaktadır.

- Faydalar için [buraya][benefits] bakabilirsin.
- Kayıt ve detaylı işlemler için [buraya][github student] bakabilirsin.
- Sunduğu faydalar için [buraya][github dev pack] bakabilirsin
- Eğitim topluluğu için [buraya](https://education.github.community/c/students) bakabilirsin
- Eğitim okulları için [buraya][github education school] bakabilirsin.
- [Octodex][github octodex]
- Detaylı bilgiler ve sık sorulan sorular için de [buraya][details] bakabilirsin.

## Proje Yönetimi

### Repository'nin Oluşturulması ve Dosyaların Aktarılması

- [Github] üzerinden sağ üst köşedeki `+` butonundan `New Repository` diyerek ya da direkt olarak [buradan][github repo oluşturma] repository'i oluşturun
- `git clone` ile veya var olan projeniz üzerinden `git remote add origin <url>` ile bağlantıyı kurun
  - Uğraşmak istemez iseniz; projenizi `git clone` ile kopyalayın ve yüklemek istediklerinizi klonlanan projenin için atın
- Reponuzu güncellemek için sırasıyla;
  - `git add .`
  - `git commit -m "Açıklama"`
    - Açıklamlara `#` karakteri ile **Issue**'yi hedef gösterebilirsin
    - Genel yorum formatı: `<Açıklama> (#<IssueID>)` ve isteğe bağlı ek açıklamalar
  - `git push origin master`

### Repo Üzerinde Proje Yönetimi

Repository üzerinde proje yönetimi için scrum veya canvan (yapılacaklar, yapılanlar, yapıldı vs..) yapısı kullanılmaktadır.

- Repo sayfasında `Project` sekmesine girin ve `New Project` butonuna tıklayın
- Proje ismini ve açıklamasını yazdıktan sonra `Project Template` alanından `Automated Kanban` seçeniğini işaretleyin
- `Automated Kanban` yapısı oluşturulan sorunları, yapılacak planları ve yapılanları otomatik olarak ekler
- Repo sayfasında `Issue` alanında sorunları, yapılacak planları ve yapılanları oluşturun
- Oluşturduğun her `Issue` için `label`, `proje` ve kim ile alakalı ise onu `assign` alanında belirtin
  - `Issue`'lerde markdown formatı geçerlidir
  - `[ ]` yapısı ile ypaılacakları eklerseniz süreç analizi özelliği gelir
- Oluşturulan `Issue`'ler, `Automated Kanban` yapısı ve sayesinde belirttiğiniz projeye otomatik akatarılacaktır.
- `Milestones` ile yapılacak işlere süre sınırı (deadline) tanımlayabilirsin

## Github Üzerindeki Açılmayan Dosyalar

> [Stackoverflow açıklaması](https://stackoverflow.com/questions/19584255/what-does-a-grey-icon-in-remote-github-mean)

## Github Eklentileri

Eklentilerin sayfasına [buradan][marketplace] erişebilirsin.

> Bilmiyorsan elleşme derim 🙄

| Eklenti                             | Açıklama                                                                                     |
| ----------------------------------- | -------------------------------------------------------------------------------------------- |
| [todo][todo - github]               | Kod içerisindeki `@todo` ve `TODO` alanlarını _Github_'a entegre eder.                       |
| [Gitpod][gitpod - github]           | Online **vscode** temalı editör. (💡 chrome [eklentisini][gitpod - chrome] indirmeyi unutma) |
| [Semaphor][semaphor - github]       | Bir bak 🙋‍♀️                                                                                   |
| [GitLocalize][gitlocalize - github] | Bir bak 🙋‍♀️                                                                                   |
| [Codetree][codetree - github]       | Çevik (agile) takımların için proje yönetim eklentisi (paralı 🧐)                            |

## Github Yardımcıları

| Yardımcı                   | Açıklama                                                       |
| -------------------------- | -------------------------------------------------------------- |
| [GitGuardian][gitguardian] | Kimlik bilgilerinin paylaşılması durumunu kontrol eder, uyarır |

## Github Credential Değiştirme

Kaynak için [buraya][credential settings - video] bakabilirsin

## Harici Bağlantılar

- [Github page'e domain bağlama]

> Başka yok 😒

[git notlarım]: ../Git%20Notlar%C4%B1.md
[benefits]: https://education.github.com/benefits/offers
[github student]: https://education.github.com/students
[github dev pack]: https://education.github.com/pack/offers
[github comminity]: https://education.github.community/c/students
[github octodex]: https://octodex.github.com/
[github education school]: https://education.github.com/partners/schools
[details]: https://help.github.com/en/categories/teaching-and-learning-with-github-education

<!-- Proje Yönetimi -->

[github]: https://github.com
[github repo oluşturma]: https://github.com/new

<!-- Eklentiler -->

[marketplace]: https://github.com/marketplace
[todo - github]: https://github.com/marketplace/todo
[gitpod - github]: https://github.com/marketplace/gitpod-io
[gitpod - chrome]: https://chrome.google.com/webstore/detail/gitpod-online-ide/dodmmooeoklaejobgleioelladacbeki
[semaphor - github]: https://github.com/marketplace/semaphore
[gitlocalize - github]: https://github.com/marketplace/gitlocalize
[codetree - github]: https://github.com/marketplace/codetree
[gitguardian]: https://www.gitguardian.com/
[github page'e domain bağlama]: https://medium.com/@tivikter/github-pagesi-%C3%B6zel-domain-ile-kullanmak-ce57d229dae9
[credential settings - video]: https://www.youtube.com/watch?v=otBNYXz5Ie0
