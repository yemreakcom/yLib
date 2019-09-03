# 2 - Linux Terminali <!-- omit in toc -->

Linux işletim sistemindeki komutlardır. Terminal üzerinden kernel'a bildirilir.

## Terminal Numaları

Çok sık kullanılan ve faydalı olacak olan bir kaç terminal yöntemleri:

- Terminal üzerinden hızlıca dosya düzenlemek isterseniz `nano` komutunu kullanın
- Tüm terminal ön işlemleri `~/.bashrc` dosyasındadır.
- `alias` ile kendinize özgü komutlar oluşturabilirsiniz
  - sudo ile kullanılması için `alias sudo='sudo '` satırını `.bashrc` dosyanıza eklemeniz gerekmektedir
  - `echo "alias sudo='sudo '" >> ~/.bashrc`
  - Kaynak için [buraya](https://askubuntu.com/a/22043/898692) bakabilirsin
- `grep` komutu ile dosya araması yapabilirsiniz.
  - Kaynak için [buraya](https://stackoverflow.com/a/16957078/9770490) bakabilirsin.

| Yöntem                                                | Açıklama                                               |
| ----------------------------------------------------- | ------------------------------------------------------ |
| `<komut> --help`                                      | Komutlar için yardım metni                             |
| <kbd>⭾ Tab</kbd>                                      | Kod tamamlama                                          |
| `cwd`                                                 | Çalışma dizini yolu                                    |
| `-`                                                   | Son çalışan dizine gitme                               |
| `~`                                                   | Home dizini                                            |
| `<komut>; <komut>;`                                   | Birden fazla komut işleme (birbirlerini beklemez)      |
| `<komut> && <komut>`                                  | 1. komut çalışırsa 2.'yi işleme                        |
| `<komut> || <komut>`                                  | 1. olmazsa 2. komutu işleme                            |
| `<komut> | <komut>`                                   | İlk komutun sonucunu 2'ye aktarma (pipeline)           |
| <kbd>✲ Ctrl</kbd> + <kbd>W</kbd>                      | Kelime silme                                           |
| <kbd>✲ Ctrl</kbd> + <kbd>R</kbd> `<aranan_terim>`     | Önceki komutlarda arama yapma                          |
| <kbd>✲ Ctrl</kbd> + <kbd>Q</kbd>                      | Kitlenmiş terminali kurtarma                           |
| <kbd>✲ Ctrl</kbd> + <kbd>A</kbd>                      | Komutların satırının başına gelme                      |
| <kbd>✲ Ctrl</kbd> +<kbd>E</kbd>                       | Komut satırının sonuna gelme                           |
| `tail -f <dosya>`                                     | Dosyayı anlık olarak okuma                             |
| `cat` ve `less`                                       | Ufak ve büyük dosyaları okuma                          |
| `!$`                                                  | Bir önce kullanılan değişkeni kullanma                 |
| `!!`                                                  | Bir önceki komutu kullanma                             |
| `alias`                                               | Komut yönlendirme, yeni komut oluşturma                |
| <kbd>✲ Ctrl</kbd> + <kbd>⎇ Alt</kbd> + <kbd>E</kbd>   | Oluşturulan komutların (alias) karşılıklarını gösterme |
| <kbd>✲ Ctrl</kbd> + <kbd>⇧ Shift</kbd> + <kbd>C</kbd> | Kopyalama işlemi                                       |
| <kbd>✲ Ctrl</kbd> + <kbd>⇧ Shift</kbd> + <kbd>V</kbd> | Yapıştırma işlemi                                      |
| `yes | <komut_ya_da_script>`                          | İnteraktif veri isteyen işleme 'yes' verisi gönderme   |
| `grep <aranan_kelime>`                                | Kelime arama                                           |
| `<komut> | grep <aranan_kelime>`                      | Komut sonucunda kelime arama                           |

## Temel Terminal Komutları

Detalar için [buraya](https://gist.github.com/sayz/1130312/a45b548b82ee459e05a9159ec532224757a2ca56) tıklayarak, açıklamalara ulaşabilirsin.

- `clear` Terminali temizleme
- `sudo -s` Terminali root yapma `exit` rootlu terminali kapatma
- `sudo apt-get install <paket_adi>` Paket kurulumu
- `sudo apt-get install --fix-broken` Hatalı kurulumları veya gerekli bağımlılıkları kurma
- `sudo apt-get purge <paket_adi>` paketadi paketini kaldirma
- `sudo apt-get purge <paket_adi>*` Bulunan dizinde paket ile başlayan tüm paketleri kaldırma
- `sudo apt-get purge '<paket_adi>*'` paket ile başlayan tüm paketleri ve alt bileşenlerini kaldırma
- `sudo apt-cache search <paket_adi>` Depoda paketadi arama işlemi

### Sudo Komutları

| Komut          | Açıklama                                                     |
| -------------- | ------------------------------------------------------------ |
| `search`       | search in package descriptions                               |
| `show`         | show package details                                         |
| `install`      | install packages                                             |
| `reinstall`    | reinstall packages                                           |
| `remove`       | remove packages                                              |
| `autoremove`   | Remove automatically all unused packages                     |
| `update`       | update list of available packages                            |
| `upgrade`      | upgrade the system by installing/upgrading packages          |
| `full-upgrade` | upgrade the system by removing/installing/upgrading packages |
| `edit-sources` | edit the source information file                             |

## Kurulum Notları

Linux ile kurulumlar terminal üzerinden bir kaç komut gerektirir.

> Yeni linux kurulum yöntemi olan **snapd** ilk açılmada gecikmeye sebebiyet vermekte

### Snapd Kurulum

Ubuntu yerel mağazasından yapılan indirmelerdir

- Snapd kurulum önceden derlenmiş ve hazırlanmış uygulamalardır.
- Hız açısından **dpkg** daha iyidir, lakin ek paketler ve bağımlılıklar gerektirir
- Hızlı ve çalışabilirlik açısından **snapd** daha verimlidir, her platformda çalışır

### Dpkg - Debian Paket Kurma

#### Apt ile kurulum

```sh
sudo apt install -f ./dosya.deb # Hatalı paketleri yenileyerek kurma (-f: --fix-broken)
sudo apt autoremove # Artıkları temizleme
```

#### Dpkg ile Kurulum

- `sudo dpkq -i deb_uzantılı.deb` (kurulumu başlatma)
- `sudo apt-get install --fix-broken` (kurulum için gerekli paketleri kurma)
- `sudo dpkq -i deb_uzantılı.deb` (kurulumu yeniden deneme)
- `sudo apt-get autoremove` (gereksizleri kaldırma)

> Kaynak için [buraya][dpkg kurulumu] bakabilrisin.

### Tar dosyalarının kurulumları

Tar.gz uzantılı dosyayı bulup, sağ tıklayıp, buraya çıkar diyoruz. Ya da terminal yardımıyla arşivi çıkarın

| Parametre | Açıklama                                 |
| --------- | ---------------------------------------- |
| `x`       | Çıkarmak (e**x**tract)                   |
| `c`       | Arşivelemek (**c**ompress)               |
| `z`       | G**z**ip ile işleme sokma                |
| `v`       | Yapılan işlemleri gösterme (**v**erbose) |
| `f`       | Dosya ismi belirtme (**f**ilename)       |
| `C`       | Çıkartılacak dizin                       |

```sh
tar xzvf "dosya.tar.gz" -C "./dizin"
```

> Terminat komutlarını kullandıysanız, direk alttaki komutları uygulayabilirisiniz.

Ardından çıkarılan dosyaların olduğu dizine girip, alttaki komutları yazıyoruz.

```sh
./configure
make -j $(nproc --all)
sudo make install
```

### AppImage Uzantılı Dosyaların Kurulumu

AppImage özelliği uygulamaları kurmadan çalıştırabilmemizi sağlar.

```sh
chmod a+x <appimage_dosyası>
./<appimage_dosyası>
```

### Run Uzantılı Dosyaların Kurulumu

Run dosyaları kurulum dosyalarıdır bu sebeple yetkileri olmadan çalıştırılamaz.

```sh
chmod +x <run_dosyası>
./<run_dosyası>
```

### Seçmeli veya Koşul Kabul Etmeli Kurulumlar (<OK> Butonu)

`<OK>` butonunu veya başka butonları seçmek için:

- <kbd>⭾ Tab</kbd> tuşuna basıp <kbd>ENTER</kbd>'a basın

## Kaldırma Notları

- `sudo apt remove` veya `sudo dpkg -r` komutu ile kaldırabilrsiniz
- `sudo apt remove --purge` veya `sudo dpkg -P` komutu ile yapılandırma ayarları ile kaldırabilirsiniz

## Terminal Üzerinde Çalışan Faydalı Paketler

### Terminal Üzerinden PDF işlemleri

- PDF'e dönüştürme işlemlerini [unoconv](https://github.com/unoconv/unoconv) paketi ile yapabilirsin
  - Çok fazla dosya formatını PDF'e dönüştürebilir
  - `sudo apt install unoconv` ile kurulur
- PDF işlemlerini [pdfkit](https://linuxhint.com/install_pdftk_ubuntu/) ile yapabilirsin

```sh
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

- `ln` İki dosya arasında link oluşturma
- `-s` Statik link yerine sembolik link oluşturma
- `/dosya/yolu` Örneğin /home/\$USER
- `dosyaAdi` Oluşturulacak kısayolun ismi

## Shell (Bash) Scripting

Shell script hakkında detaylı bilgi için [buraya][shell script] bakabilrisin.

### 100MB ve Üzeri Dosyaları Bulma

```sh
find /User/mkyong -type f -size +100000k -exec ls -lh {} \; | awk '{ print $9 ": " $5 }'
Copy
```

## Harici Bağlantılar

- [Batch Script ile 'Yes/No' yapısı oluşturma]

[shell script]: ../../Programlama%20Notlar%C4%B1%2FShell%20Script.md
[batch script ile 'yes/no' yapısı oluşturma]: https://stackoverflow.com/a/226724/9770490
[dpkg kurulumu]: https://unix.stackexchange.com/a/159114/344875
