---
description: >-
  GitHub üzerinden projeleri, versiyonları ve ilerleyişi artırımlı olarak
  kontrol etme ve yönetme
---

# 👨‍💼 Versiyon Yönetimi \| GitHub

## 🚙 Repository'nin Oluşturulması ve Dosyaların Aktarılması

* [Github](https://github.com) üzerinden sağ üst köşedeki `+` butonundan `New Repository` diyerek ya da direkt olarak [buradan](https://github.com/new) repository'i oluşturun
* `git clone` ile veya var olan projeniz üzerinden `git remote add origin <url>` ile bağlantıyı kurun
  * Uğraşmak istemez iseniz; projenizi `git clone` ile kopyalayın ve yüklemek istediklerinizi klonlanan projenin için atın
* Reponuzu güncellemek için sırasıyla;
  * `git add .`
  * `git commit -m "Açıklama"`
    * Açıklamlara `#` karakteri ile **Issue**'yi hedef gösterebilirsin
    * Genel yorum formatı: `<Açıklama> (#<IssueID>)` ve isteğe bağlı ek açıklamalar
  * `git push origin master`

## 💫 Repo Üzerinde Proje Yönetimi

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

