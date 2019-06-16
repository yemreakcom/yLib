# Windows10 Gelişmiş <!-- omit in toc -->

## İçerikler <!-- omit in toc -->

- [Otomatik Giriş Yapma](#otomatik-giri%C5%9F-yapma)
- [Windows10 Karanlık Tema Kurulumu](#windows10-karanl%C4%B1k-tema-kurulumu)
- [Windows Saat Sorunu](#windows-saat-sorunu)
  - [Yerel Saati Kullanma](#yerel-saati-kullanma)
  - [Evrensel (UTC) Saati Kullanma](#evrensel-utc-saati-kullanma)
  - [Windows Boot Kurtarma](#windows-boot-kurtarma)
- [Harici Bağlantılar](#harici-ba%C4%9Flant%C4%B1lar)

## Otomatik Giriş Yapma

Her defasında şifre girişi yapmaz istemezseniz, otomatik şifre girmek sizin için faydalı olacaktır.

- Arama yerine `netplwiz` yazın ve <kbd>ENTER</kbd>'a basın
- Çıkan alandaki kutucuğun işaretini kaldırın
- Şifrenizi girin ve onlayın

## Windows10 Karanlık Tema Kurulumu

En çok sevilen karanlık tema olan [Nocturnal] temasını kurmak için:

- Kurulum dosyasını [buradan][Nocturnal - Download] indirin ve `zip` halinden çıkarın , eğer bu link çalışmaz ise sitesinden erişebilirsiniz
- Güvenlik amaçlı *System Geri Dönüşüm Noktası* oluşturun
- İndirdiğiniz dosyada `Blank Caption Text` dizine girin ve içerisinde bulunan `Blank.ttf` dosyasına sağ tıklayın ve `Yükle` deyin
- Ardından `Blank.reg` dosyasını çalıştırın
  - Bu değişikliği geri almak isterseniz `Default.reg` dosyasınını kullanabilirsiniz
- `Visual Style` dizinindeki seçtiğiniz bir version ismine sahip olan klasörün **içindekileri** kopyalayın ve `C:\Windows\Resources\Themes` dizinine yapıştırın
- [UltraUXThemePatcher] ile bilgisayarınıza tema yamasını kurun
- *Settings > Personalization > Themes > Select the theme*
- Dosya gezginindeki en üstteki çubuğu kaldırmak (*ribbon*) için:
  - [OldNewExplorer] programını indirin ve çıkartarak `.exe` uzantılı dosyayı **yönetici olarak** çalıştırın
  - `Use commond bar instead of ribbon` kutucuğunu seçin
    - Altındaki kutucuklardan sadece `Use alternate navigation button style` olanı seçin
  - `Show status bar` kutucuğunun seçimini kaldırın
  - `Install` butonuna tıklayın
- Tüm işlemler bittiğine göre artık, Ayarlar > Kişiselleştirme > Tema kısmından `Nocturnal` temasını seçebilirsiniz

## Windows Saat Sorunu

Windows yanına linux kurulmasında gerçekleşen bu sorunun çözümü **yerel saati** kullanmaktır.

> Alttaki metinleri dosya açıp içine kopyaladıktan sonra, dosya uzantısını `reg` yapın ve çalıştırın.

### Yerel Saati Kullanma

```reg
Windows Registry Editor Version 5.00

[HKEY_LOCAL_MACHINE\System\CurrentControlSet\Control\TimeZoneInformation]
"RealTimeIsUniversal"=-
```

### Evrensel (UTC) Saati Kullanma

```reg
Windows Registry Editor Version 5.00

[HKEY_LOCAL_MACHINE\System\CurrentControlSet\Control\TimeZoneInformation]
"RealTimeIsUniversal"=dword:00000001
```

### Windows Boot Kurtarma

```bat
diskpart
list disk
sel disk 0

list vol
sel vol 2
assign letter=G:

cd /d G:\EFI\Microsoft\Boot\
bootrec /fixboot

ren BCD BCD.old
bcdboot C:\Windows /l tr-tr /s G: /f ALL

exit
```

> [Kaynak](https://www.easeus.com/partition-manager-software/fix-uefi-boot-in-windows-10-8-7.html)

## Harici Bağlantılar

- [Windows yanına linux kurulduğunda windows saatinin bozulması]

[Nocturnal]: https://www.deviantart.com/chloechantelle/art/Nocturnal-W10-582106490
[Nocturnal - Download]: https://www.deviantart.com/download/582106490/d9mkk8q-d0678559-518e-48f3-bf36-30bd91f73496?token=53c9fe62794d3574b12d5aad67c1998665b93c20&ts=1558436081
[UltraUXThemePatcher]: https://www.deviantart.com/users/outgoing?https://www.syssel.net/hoefs/software_uxtheme.php?lang=en
[OldNewExplorer]: https://tihiy.net/files/OldNewExplorer.rar

[Windows yanına linux kurulduğunda windows saatinin bozulması]: https://www.howtogeek.com/323390/how-to-fix-windows-and-linux-showing-different-times-when-dual-booting/
