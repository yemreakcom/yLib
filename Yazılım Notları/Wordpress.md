# Wordpress <!-- omit in toc -->

Açık kaynaklı php dilinde yazılmış web içerik yöneticisi yazılımıdır.

## İçerikler <!-- omit in toc -->

- [Localhost Üzerinde Wordpress](#localhost-%C3%BCzerinde-wordpress)
  - [XAMPP Kurulumu](#xampp-kurulumu)
  - [PHPMyAdmin Database Oluşturma](#phpmyadmin-database-olu%C5%9Fturma)
  - [Wordpress Dosyalarının İndirilmesi ve Hazırlanması](#wordpress-dosyalar%C4%B1n%C4%B1n-i%CC%87ndirilmesi-ve-haz%C4%B1rlanmas%C4%B1)
  - [Wordpress'in Aktarılması](#wordpressin-aktar%C4%B1lmas%C4%B1)
- [Online Wordpress Sunucusu (Hosting)](#online-wordpress-sunucusu-hosting)
- [Wordpress Hata Çözümleri](#wordpress-hata-%C3%A7%C3%B6z%C3%BCmleri)
  - [Unable to create directory wp-content/uploads/2019/04. Is its parent directory writable by the server](#unable-to-create-directory-wp-contentuploads201904-is-its-parent-directory-writable-by-the-server)
  - [You won’t be able to install new themes from here yet since your install requires SFTP credentials](#you-wont-be-able-to-install-new-themes-from-here-yet-since-your-install-requires-sftp-credentials)
- [Markdown Wordpress](#markdown-wordpress)
- [Harici Bağlantılar](#harici-ba%C4%9Flant%C4%B1lar)

## Localhost Üzerinde Wordpress

### XAMPP Kurulumu

XAMPP kurulum yönergeleri için alttak
 işletim sistemlerine tıklayabilirsin:

- [Linux](../%C4%B0%C5%9Fletim%20Sistemi%20Notlar%C4%B1%2FLinux%20Notlar%C4%B1.md#xampp-kurulumu)
- [Windows & MacOS](https://www.apachefriends.org/download.html)

### PHPMyAdmin Database Oluşturma

Wordpress kurulumu için veritabanı gerekmektedir.

- XAMPP üzerinden *MySql*, *Apache* sunucuları çalıştırın
- [Yerel sunucu sayfası](http://localhost/phpmyadmin/) olan `localhost/phpmyadmin` sayfasına girin
- Sol üst kısımdan `New` bağlantısına ya da [buraya](http://localhost/phpmyadmin/server_databases.php?server=1) tıklayın
- Database ismi ve karakter formatı belirleyin
  - Örn: `yemreak` `utf8_general_ci`
- İstediğiniz şekilde tablo ve sütunlar ekleyebilirsiniz

### Wordpress Dosyalarının İndirilmesi ve Hazırlanması

*Wordpress* dosyalarını indirmek için [buraya](https://wordpress.org/download/) tıklayabilirsiniz.

- Indirelen dosyaları çıkartıp XAMPP'ın `htdocs` dizinine taşıyın
  - Taşıdığınız `wordpress` adlı dosyasına ve alt dosyalarına **okuma ve yazma** erişiminizin olmasını sağlayın.
  - Linux için `sudo nautilus /opt/lampp/htdocs` ile dosya gezgininni açıp, alddaki dosyalara sağ tıklayıp `Özellikler > İzinler` alanından her kullanıcıya (*other* en alttaki) **okuma ve yazma** izinlerini verin.
    - `wordpress`
    - `wordpress/wp-content`
    - `wordpress/wp-admin`
    - `wordpress/wp-includes`
  - *Wordpress*'in oluşturduğu dosyalardaki kullanıcı adı `deamon`'dur. (Dosya izinleri için gerekebilir)
- İster [buraya](http://localhost/wordpress) tıklayarak, isterseniz `localhost/wordpress` yolu ile kopyaladığınız dizine tarayıcıdan erişin.
- İstenen bilgileri girin
  - Kullanıcı adı ve şifre işlemleri için [buraya][Username & Password] bakabilirsiniz
- Yapılandırma dosyalarının oluşumunda hata meydana gelirse, XAMPP içerisindeki `htdocs/wordpress` dizinine `wp-config.php` dosyası oluşturup, içerisine yapılandırma bilgilerinizi yapıştırın.
- FTP kullanmak için `wp-config.php` dosyanıza `define('FS_METHOD', 'direct');` satırını ekleyin.
  - FTP ile yerel dosya işlemleri yapabilrisiniz
  - İnternetten tema indirme, deneme vs.

### Wordpress'in Aktarılması

*Wordpress*'in aktarılması için:

- Tüm dosyaların aktarılması
- Veriler *database*'de tutulduğu için, *database*'in aktarılması
- Yapılandırma dosyasının aktarılması ya da yeniden oluşturulması

gerekmektedir.

## Online Wordpress Sunucusu (Hosting)

- [Natro](https://www.natro.com/hosting/wordpress-hosting)

## Wordpress Hata Çözümleri

### Unable to create directory wp-content/uploads/2019/04. Is its parent directory writable by the server

Bu hata dizin ve dosya yetki sorunlarından kaynaklanır.  [Wordpress Dosyalarının İndirilmesi ve Hazırlanması](#wordpress-dosyalar%C4%B1n%C4%B1n-i%CC%87ndirilmesi-ve-haz%C4%B1rlanmas%C4%B1) aşamasındaki izinleri düzgün tamamladığınızdan emin olun.

- Wordpress'in kullanıcı adı `deamon` olarak geçer
- Her dizinin 755 yetkisine (Create & Delete)
- Her dosyanın 644 yetkisine (Read & Write)

sahip olması gerekir

> Linux için `chmod 755 <dizin_yolu>` | `chmod 644 <dosya_yolu>` komutunu kullanabilirsin

### You won’t be able to install new themes from here yet since your install requires SFTP credentials

Çözüm için `wp-config.php` dosyanıza `define('FS_METHOD', 'direct');` satırını ekleyin.

> `wp-config.php` dosyası XAMPP'ın kurulu olduğu dizindeki `htdocs/wordpress/` yolundadır.

## Markdown Wordpress

- [Markdown Editörü][WP Githuber MD]
- [Markdown yanlısı tema][Mynote WordPress Theme]

## Harici Bağlantılar

- [10 Markdowns for Wordpress]
- [Twentyfifteen Theme]
- [Natro Hosting]
- [Markdown Wordpress Editor]
- [Markdown Plugins]
- [How to change or set username or password][Username & Password]
- [5 quick fixes for ‘failed to write file to disk WordPress error]

[10 Markdowns for Wordpress]: https://blogging.org/blog/10-best-markdown-plugins-for-wordpress-websites/
[Twentyfifteen Theme]: https://wordpress.org/themes/twentyfifteen/
[Natro Hosting]: https://www.natro.com/hosting/wordpress-hosting
[Markdown Wordpress Editor]: https://en.support.wordpress.com/wordpress-editor/blocks/markdown-block/
[Markdown Plugins]: https://wordpress.org/plugins/tags/markdown/
[Username & Password]: https://www.coderhold.com/how-to-change-or-set-phpmyadmin-password-on-xampp.html
[5 quick fixes for ‘failed to write file to disk WordPress error]: https://bobcares.com/blog/failed-to-write-file-to-disk-wordpress-error/
[WP Githuber MD]: https://terryl.in/en/repository/wordpress-markdown-plugin-githuber-md/
[Mynote WordPress Theme]: https://terryl.in/en/repository/mynote/