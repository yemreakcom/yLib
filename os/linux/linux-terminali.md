---
description: 'Linux işletim sistemi komutlarıdır, terminal üzerinden kernel''a bildirilir.'
---

# 🖤 Linux Terminali

## Terminal Numaları

Çok sık kullanılan ve faydalı olacak olan bir kaç terminal yöntemleri:

* Terminal üzerinden hızlıca dosya düzenlemek isterseniz `nano` komutunu kullanın
* Tüm terminal ön işlemleri `~/.bashrc` dosyasındadır.
* `alias` ile kendinize özgü komutlar oluşturabilirsiniz
  * sudo ile kullanılması için `alias sudo='sudo '` satırını `.bashrc` dosyanıza eklemeniz gerekmektedir
  * `echo "alias sudo='sudo '" >> ~/.bashrc`
  * Kaynak için [buraya](https://askubuntu.com/a/22043/898692) bakabilirsin
* `grep` komutu ile dosya araması yapabilirsiniz.
  * Kaynak için [buraya](https://stackoverflow.com/a/16957078/9770490) bakabilirsin.

| Yöntem | Açıklama |  |  |
| :--- | :--- | :--- | :--- |
| `<komut> --help` | Komutlar için yardım metni |  |  |
| ⭾ Tab | Kod tamamlama |  |  |
| `cwd` | Çalışma dizini yolu |  |  |
| `-` | Son çalışan dizine gitme |  |  |
| `~` | Home dizini |  |  |
| `<komut>; <komut>;` | Birden fazla komut işleme \(birbirlerini beklemez\) |  |  |
| `<komut> && <komut>` | 1. komut çalışırsa 2.'yi işleme |  |  |
| \` |  | \` | 1. olmazsa 2. komutu işleme |
| \` | \` | İlk komutun sonucunu 2'ye aktarma \(pipeline\) |  |
| ✲ Ctrl + W | Kelime silme |  |  |
| ✲ Ctrl + R `<aranan_terim>` | Önceki komutlarda arama yapma |  |  |
| ✲ Ctrl + Q | Kitlenmiş terminali kurtarma |  |  |
| ✲ Ctrl + A | Komutların satırının başına gelme |  |  |
| ✲ Ctrl +E | Komut satırının sonuna gelme |  |  |
| `tail -f <dosya>` | Dosyayı anlık olarak okuma |  |  |
| `cat` ve `less` | Ufak ve büyük dosyaları okuma |  |  |
| `!$` | Bir önce kullanılan değişkeni kullanma |  |  |
| `!!` | Bir önceki komutu kullanma |  |  |
| `alias` | Komut yönlendirme, yeni komut oluşturma |  |  |
| ✲ Ctrl + ⎇ Alt + E | Oluşturulan komutların \(alias\) karşılıklarını gösterme |  |  |
| ✲ Ctrl + ⇧ Shift + C | Kopyalama işlemi |  |  |
| ✲ Ctrl + ⇧ Shift + V | Yapıştırma işlemi |  |  |
| \`yes | \` | İnteraktif veri isteyen işleme 'yes' verisi gönderme |  |
| `grep <aranan_kelime>` | Kelime arama |  |  |
| \` | grep \` | Komut sonucunda kelime arama |  |

## Temel Terminal Komutları

Detalar için [buraya](https://gist.github.com/sayz/1130312/a45b548b82ee459e05a9159ec532224757a2ca56) tıklayarak, açıklamalara ulaşabilirsin.

* `clear` Terminali temizleme
* `sudo -s` Terminali root yapma `exit` rootlu terminali kapatma
* `sudo apt-get install <paket_adi>` Paket kurulumu
* `sudo apt-get install --fix-broken` Hatalı kurulumları veya gerekli bağımlılıkları kurma
* `sudo apt-get purge <paket_adi>` paketadi paketini kaldirma
* `sudo apt-get purge <paket_adi>*` Bulunan dizinde paket ile başlayan tüm paketleri kaldırma
* `sudo apt-get purge '<paket_adi>*'` paket ile başlayan tüm paketleri ve alt bileşenlerini kaldırma
* `sudo apt-cache search <paket_adi>` Depoda paketadi arama işlemi

### Sudo Komutları

| Komut | Açıklama |
| :--- | :--- |
| `search` | search in package descriptions |
| `show` | show package details |
| `install` | install packages |
| `reinstall` | reinstall packages |
| `remove` | remove packages |
| `autoremove` | Remove automatically all unused packages |
| `update` | update list of available packages |
| `upgrade` | upgrade the system by installing/upgrading packages |
| `full-upgrade` | upgrade the system by removing/installing/upgrading packages |
| `edit-sources` | edit the source information file |

## Kurulum Notları

Linux ile kurulumlar terminal üzerinden bir kaç komut gerektirir.

> Yeni linux kurulum yöntemi olan **snapd** ilk açılmada gecikmeye sebebiyet vermekte

### Snapd Kurulum

Ubuntu yerel mağazasından yapılan indirmelerdir

* Snapd kurulum önceden derlenmiş ve hazırlanmış uygulamalardır.
* Hız açısından **dpkg** daha iyidir, lakin ek paketler ve bağımlılıklar gerektirir
* Hızlı ve çalışabilirlik açısından **snapd** daha verimlidir, her platformda çalışır

### Dpkg - Debian Paket Kurma

#### Apt ile kurulum

```bash
sudo apt install -f ./dosya.deb # Hatalı paketleri yenileyerek kurma (-f: --fix-broken)
sudo apt autoremove # Artıkları temizleme
```

#### Dpkg ile Kurulum

* `sudo dpkq -i deb_uzantılı.deb` \(kurulumu başlatma\)
* `sudo apt-get install --fix-broken` \(kurulum için gerekli paketleri kurma\)
* `sudo dpkq -i deb_uzantılı.deb` \(kurulumu yeniden deneme\)
* `sudo apt-get autoremove` \(gereksizleri kaldırma\)

> Kaynak için [buraya](https://unix.stackexchange.com/a/159114/344875) bakabilrisin.

### Tar dosyalarının kurulumları

Tar.gz uzantılı dosyayı bulup, sağ tıklayıp, buraya çıkar diyoruz. Ya da terminal yardımıyla arşivi çıkarın

| Parametre | Açıklama |
| :--- | :--- |
| `x` | Çıkarmak \(e**x**tract\) |
| `c` | Arşivelemek \(**c**ompress\) |
| `z` | G**z**ip ile işleme sokma |
| `v` | Yapılan işlemleri gösterme \(**v**erbose\) |
| `f` | Dosya ismi belirtme \(**f**ilename\) |
| `C` | Çıkartılacak dizin |

```bash
tar xzvf "dosya.tar.gz" -C "./dizin"
```

> Terminat komutlarını kullandıysanız, direk alttaki komutları uygulayabilirisiniz.

Ardından çıkarılan dosyaların olduğu dizine girip, alttaki komutları yazıyoruz.

```bash
./configure
make -j $(nproc --all)
sudo make install
```

### AppImage Uzantılı Dosyaların Kurulumu

AppImage özelliği uygulamaları kurmadan çalıştırabilmemizi sağlar.

```bash
chmod a+x <appimage_dosyası>
./<appimage_dosyası>
```

### Run Uzantılı Dosyaların Kurulumu

Run dosyaları kurulum dosyalarıdır bu sebeple yetkileri olmadan çalıştırılamaz.

```bash
chmod +x <run_dosyası>
./<run_dosyası>
```

### Seçmeli veya Koşul Kabul Etmeli Kurulumlar \( Butonu\)

`<OK>` butonunu veya başka butonları seçmek için:

* ⭾ Tab tuşuna basıp ENTER'a basın

## Kaldırma Notları

* `sudo apt remove` veya `sudo dpkg -r` komutu ile kaldırabilrsiniz
* `sudo apt remove --purge` veya `sudo dpkg -P` komutu ile yapılandırma ayarları ile kaldırabilirsiniz

## Terminal Üzerinde Çalışan Faydalı Paketler

### Terminal Üzerinden PDF işlemleri

* PDF'e dönüştürme işlemlerini [unoconv](https://github.com/unoconv/unoconv) paketi ile yapabilirsin
  * Çok fazla dosya formatını PDF'e dönüştürebilir
  * `sudo apt install unoconv` ile kurulur
* PDF işlemlerini [pdfkit](https://linuxhint.com/install_pdftk_ubuntu/) ile yapabilirsin

```bash
# convert to pdf
unoconv -f pdf myfile1.odt myfile2.odt ...
# merge pdfs
pdftk myfile1.pdf myfile2.pdf ...
# remove individual pdf documents
rm myfile1.pdf myfile2.pdf ...
```

## Kısayol oluşturma

Detaylar için [buraya](https://manpages.debian.org/stretch/coreutils/ln.1.en.html) tıklayabilirsin.

```bash
sudo ln -s /dosya/yolu/ dosyaAdi
```

* `ln` İki dosya arasında link oluşturma
* `-s` Statik link yerine sembolik link oluşturma
* `/dosya/yolu` Örneğin /home/$USER
* `dosyaAdi` Oluşturulacak kısayolun ismi

## Shell \(Bash\) Scripting

Shell script hakkında detaylı bilgi için [buraya](https://github.com/yedhrab/YWiki/tree/169abadfd1b8862c004399268f6ca1f9f9359d61/Programlama%20Notları/Shell%20Script.md) bakabilrisin.

### 100MB ve Üzeri Dosyaları Bulma

```bash
find /User/mkyong -type f -size +100000k -exec ls -lh {} \; | awk '{ print $9 ": " $5 }'
Copy
```

## Harici Bağlantılar

* [Batch Script ile 'Yes/No' yapısı oluşturma](https://stackoverflow.com/a/226724/9770490)

