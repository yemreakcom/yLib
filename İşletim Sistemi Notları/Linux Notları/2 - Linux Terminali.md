# 2 - Linux Terminali <!-- omit in toc -->

Linux işletim sistemindeki komutlardır. Terminal üzerinden kernel'a bildirilir.

## İçerikler <!-- omit in toc -->

- [Terminal Numaları](#terminal-numalar%C4%B1)
- [Temel Terminal Komutları](#temel-terminal-komutlar%C4%B1)
- [Kurulum Notları](#kurulum-notlar%C4%B1)
  - [Snapd Kurulum](#snapd-kurulum)
  - [Dpkg - Debian Paket Kurma](#dpkg---debian-paket-kurma)
  - [Tar dosyalarının kurulumları](#tar-dosyalar%C4%B1n%C4%B1n-kurulumlar%C4%B1)
  - [AppImage Uzantılı Dosyaların Kurulumu](#appimage-uzant%C4%B1l%C4%B1-dosyalar%C4%B1n-kurulumu)
  - [Run Uzantılı Dosyaların Kurulumu](#run-uzant%C4%B1l%C4%B1-dosyalar%C4%B1n-kurulumu)
- [Kısayol oluşturma](#k%C4%B1sayol-olu%C5%9Fturma)
- [Shell (Bash) Scripting](#shell-bash-scripting)
  - [100MB ve Üzeri Dosyaları Bulma](#100mb-ve-%C3%BCzeri-dosyalar%C4%B1-bulma)
- [Harici Bağlantılar](#harici-ba%C4%9Flant%C4%B1lar)

## Terminal Numaları

Çok sık kullanılan ve faydalı olacak olan bir kaç terminal yöntemleri:

- Tüm terminal ön işlemleri `~/.bashrc` dosyasındadır.
- `alias` ile kendinize özgü komutlar oluşturabilirsiniz
  - sudo ile kullanılması için `alias sudo='sudo '` satırını `.bashrc` dosyanıza eklemeniz gerekmektedir
  - `echo "alias sudo='sudo '" >> ~/.bashrc`
  - Kaynak için [buraya](https://askubuntu.com/a/22043/898692) bakabilirsin
- `grep` komutu ile dosya araması yapabilirsiniz.
  - Kaynak için [buraya](https://stackoverflow.com/a/16957078/9770490) bakabilirsin.

| Yöntem                                            | Açıklama                                               |
| ------------------------------------------------- | ------------------------------------------------------ |
| `<komut> --help`                                  | Komutlar için yardım metni                             |
| <kbd>TAB</kbd>                                    | Kod tamamlama                                          |
| `cwd`                                             | Çalışma dizini yolu                                    |
| `-`                                               | Son çalışan dizine gitme                               |
| `~`                                               | Home dizini                                            |
| `<komut>; <komut>;`                               | Birden fazla komut işleme (birbirlerini beklemez)      |
| `<komut> && <komut>`                              | 1. komut çalışırsa 2.'yi işleme                        |
| `<komut> || <komut>`                              | 1. olmazsa 2. komutu işleme                            |
| `<komut> | <komut>`                               | İlk komutun sonucunu 2'ye aktarma (pipeline)           |
| <kbd>CTRL</kbd> + <kbd>W</kbd>                    | Kelime silme                                           |
| <kbd>CTRL</kbd> + <kbd>R</kbd> `<aranan_terim>`   | Önceki komutlarda arama yapma                          |
| <kbd>CTRL</kbd> + <kbd>Q</kbd>                    | Kitlenmiş terminali kurtarma                           |
| <kbd>CTRL</kbd> + <kbd>A</kbd>                    | Komutların satırının başına gelme                      |
| <kbd>CTRL</kbd> +<kbd>E</kbd>                     | Komut satırının sonuna gelme                           |
| `tail -f <dosya>`                                 | Dosyayı anlık olarak okuma                             |
| `cat` ve `less`                                   | Ufak ve büyük dosyaları okuma                          |
| `!$`                                              | Bir önce kullanılan değişkeni kullanma                 |
| `!!`                                              | Bir önceki komutu kullanma                             |
| `alias`                                           | Komut yönlendirme, yeni komut oluşturma                |
| <kbd>CTRL</kbd> + <kbd>ALT</kbd> + <kbd>E</kbd>   | Oluşturulan komutların (alias) karşılıklarını gösterme |
| <kbd>CTRL</kbd> + <kbd>SHIFT</kbd> + <kbd>C</kbd> | Kopyalama işlemi                                       |
| <kbd>CTRL</kbd> + <kbd>SHIFT</kbd> + <kbd>V</kbd> | Yapıştırma işlemi                                      |
| `yes | <komut_ya_da_script>`                      | İnteraktif veri isteyen işleme 'yes' verisi gönderme   |
| `grep <aranan_kelime>`                            | Kelime arama                                           |
| `<komut> | grep <aranan_kelime>`                  | Komut sonucunda kelime arama                           |

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

## Kurulum Notları

Linux ile kurulumlar terminal üzerinden bir kaç komut gerektirir.

> Yeni linux kurulum yöntemi olan **snapd** ilk açılmada gecikmeye sebebiyet vermekte

### Snapd Kurulum

Ubuntu yerel mağazasından yapılan indirmelerdir

- Snapd kurulum önceden derlenmiş ve hazırlanmış uygulamalardır.
- Hız açısından **dpkg** daha iyidir, lakin ek paketler ve bağımlılıklar gerektirir
- Hızlı ve çalışabilirlik açısından **snapd** daha verimlidir, her platformda çalışır

### Dpkg - Debian Paket Kurma

- `sudo dpkq -i deb_uzantılı.deb` (kurulumu başlatma)
- `sudo apt-get install --fix-broken` (kurulum için gerekli paketleri kurma)
- `sudo dpkq -i deb_uzantılı.deb` (kurulumu yeniden deneme)
- `sudo apt-get autoremove` (gereksizleri kaldırma)

### Tar dosyalarının kurulumları

Tar.gz uzantılı dosyayı bulup, sağ tıklayıp, buraya çıkar diyoruz. Ya da terminal yardımıyla arşivi çıkarın

```bash
tar xzf dosya.tar.gz -C ./dizin
cd dizin
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

## Kısayol oluşturma

Detaylar için [buraya](https://manpages.debian.org/stretch/coreutils/ln.1.en.html) tıklayabilirsin.

```bash
sudo ln -s /dosya/yolu/ dosyaAdi
```

- `ln` İki dosya arasında link oluşturma
- `-s` Statik link yerine sembolik link oluşturma
- `/dosya/yolu` Örneğin /home/$USER
- `dosyaAdi` Oluşturulacak kısayolun ismi

## Shell (Bash) Scripting

Shell script hakkında detaylı bilgi için [buraya][Shell Script] bakabilrisin.

### 100MB ve Üzeri Dosyaları Bulma

```sh
find /User/mkyong -type f -size +100000k -exec ls -lh {} \; | awk '{ print $9 ": " $5 }'
Copy
```

## Harici Bağlantılar

- [Batch Script ile 'Yes/No' yapısı oluşturma]

[Shell Script]: ../../Programlama%20Notlar%C4%B1%2FShell%20Script.md
[Batch Script ile 'Yes/No' yapısı oluşturma]: https://stackoverflow.com/a/226724/9770490
