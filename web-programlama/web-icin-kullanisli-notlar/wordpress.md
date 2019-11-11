---
description: Açık kaynaklı php dilinde yazılmış web içerik yöneticisi yazılımıdır.
---

# 🧇 Wordpress

## 🏠 Localhost Üzerinde Wordpress

### ⏬ XAMPP Kurulumu

XAMPP kurulum yönergeleri için alttaki işletim sistemlerine tıklayabilirsin:

* [Linux](https://github.com/yedhrab/YWiki/tree/169abadfd1b8862c004399268f6ca1f9f9359d61/1%20-%20Programlama%20Notları/5%20-%20Web%20Programlama/İşletim%20Sistemi%20Notları/Linux%20Notları.md#xampp-kurulumu)
* [Windows & MacOS](https://www.apachefriends.org/download.html)

### ✨ PHPMyAdmin Database Oluşturma

Wordpress kurulumu için veritabanı gerekmektedir.

* XAMPP üzerinden _MySQL_, _Apache_ sunucuları çalıştırın
* [Yerel sunucu sayfası](http://localhost/phpmyadmin/) olan `localhost/phpmyadmin` sayfasına girin
* Sol üst kısımdan `New` bağlantısına ya da [buraya](http://localhost/phpmyadmin/server_databases.php?server=1) tıklayın
* Database ismi ve karakter formatı belirleyin
  * Örn: `yemreak` `utf8_general_ci`
* İstediğiniz şekilde tablo ve sütunlar ekleyebilirsiniz

### 🚧 Wordpress Dosyalarının İndirilmesi ve Hazırlanması

_Wordpress_ dosyalarını indirmek için [buraya](https://wordpress.org/download/) tıklayabilirsiniz.

* İndirilen dosyaları çıkartıp XAMPP'ın `htdocs` dizinine taşıyın
  * Taşıdığınız `wordpress` adlı dosyasına ve alt dosyalarına **okuma ve yazma** erişimimizin olmasını sağlayın.
  * Linux için `sudo nautilus /opt/lampp/htdocs` ile dosya gezginini açıp, alttaki dosyalara sağ tıklayıp `Özellikler > İzinler` alanından her kullanıcıya \(_other_ en alttaki\) **okuma ve yazma** izinlerini verin.
    * Terminal ile bu komut yardımıyla `sudo chmod -R 757 /opt/lampp/htdocs/wordpress/` ya da el ile yetki verin.
    * `wordpress`
    * `wordpress/wp-content`
    * `wordpress/wp-admin`
    * `wordpress/wp-includes`
  * _Wordpress_'in oluşturduğu dosyalardaki kullanıcı adı `deamon`'dur. \(Dosya izinleri için gerekebilir\)
* İster [buraya](http://localhost/wordpress) tıklayarak, isterseniz `localhost/wordpress` yolu ile kopyaladığınız dizine tarayıcıdan erişin.
* İstenen bilgileri girin
  * Kullanıcı adı ve şifre işlemleri için [buraya](https://www.coderhold.com/how-to-change-or-set-phpmyadmin-password-on-xampp.html) bakabilirsiniz
* Yapılandırma dosyalarının oluşumunda hata meydana gelirse, XAMPP içerisindeki `htdocs/wordpress` dizinine `wp-config.php` dosyası oluşturup, içerisine yapılandırma bilgilerinizi yapıştırın.
* FTP kullanmak için `wp-config.php` dosyanıza `define('FS_METHOD', 'direct');` satırını ekleyin.
  * FTP için kullanıcı adı ve şifreniz **PC**'nizin bilgileridir, wordpress hesabınızın değil.
  * FTP ile yerel dosya işlemleri yapabilirsiniz
  * İnternet'ten tema indirme, deneme vs.

### 🏹 Wordpress'in Aktarılması

_Wordpress_'in aktarılması için:

* Tüm dosyaların aktarılması
* Veriler _database_'de tutulduğu için, _database_'in aktarılması
* Yapılandırma dosyasının aktarılması ya da yeniden oluşturulması

gerekmektedir.

## 🌍 Online Wordpress Sunucusu \(Hosting\)

* [Natro](https://www.natro.com/hosting/wordpress-hosting)

## 🐞 Wordpress Hata Çözümleri

### Unable to create directory wp-content/uploads/2019/04. Is its parent directory writable by the server

Bu hata dizin ve dosya yetki sorunlarından kaynaklanır. [Wordpress Dosyalarının İndirilmesi ve Hazırlanması]() aşamasındaki izinleri düzgün tamamladığınızdan emin olun.

* Wordpress'in kullanıcı adı `deamon` olarak geçer
* Her dizinin 755 yetkisine \(Create & Delete\)
* Her dosyanın 644 yetkisine \(Read & Write\)

sahip olması gerekir

> Linux için `chmod 755 <dizin_yolu>` \| `chmod 644 <dosya_yolu>` komutunu kullanabilirsin

### You won’t be able to install new themes from here yet since your install requires SFTP credentials

Çözüm için `wp-config.php` dosyanıza `define('FS_METHOD', 'direct');` satırını ekleyin.

> `wp-config.php` dosyası XAMPP'ın kurulu olduğu dizindeki `htdocs/wordpress/` yolundadır.

## 📑 Markdown Wordpress

* [Markdown Editörü](https://terryl.in/en/repository/wordpress-markdown-plugin-githuber-md/)
* [Markdown yanlısı tema](https://terryl.in/en/repository/mynote/)

## 🔗 Harici Bağlantılar

* [10 Markdowns for Wordpress](https://blogging.org/blog/10-best-markdown-plugins-for-wordpress-websites/)
* [Twentyfifteen Theme](https://wordpress.org/themes/twentyfifteen/)
* [Natro Hosting](https://www.natro.com/hosting/wordpress-hosting)
* [Markdown Wordpress Editor](https://en.support.wordpress.com/wordpress-editor/blocks/markdown-block/)y
* [Markdown Plugins](https://wordpress.org/plugins/tags/markdown/)
* [How to change or set username or password](https://www.coderhold.com/how-to-change-or-set-phpmyadmin-password-on-xampp.html)
* [5 quick fixes for ‘failed to write file to disk WordPress error](https://bobcares.com/blog/failed-to-write-file-to-disk-wordpress-error/)
* [Blogger'ı Wordpress'e Aktarma](https://firstsiteguide.com/move-blogger-to-wordpress/)

