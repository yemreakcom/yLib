# Xiaomi Mi A2 Lite <!-- omit in toc -->

## İçerikler <!-- omit in toc -->

- [Güvenli Modda Açma](#g%c3%bcvenli-modda-a%c3%a7ma)
- [Telefonun Ekranının Kendiliğinden Kapanması](#telefonun-ekran%c4%b1n%c4%b1n-kendili%c4%9finden-kapanmas%c4%b1)
- [Stock Rom Yükleme](#stock-rom-y%c3%bckleme)
  - [ADB & Flashboot Kurulumu](#adb--flashboot-kurulumu)
  - [Bootloader Klidini Açma](#bootloader-klidini-a%c3%a7ma)
  - [Stock Rom Kurulumu](#stock-rom-kurulumu)
  - [Stock Rom'un Aktarılması](#stock-romun-aktar%c4%b1lmas%c4%b1)
- [Harici Bağlantılar](#harici-ba%c4%9flant%c4%b1lar)

## Güvenli Modda Açma

- Güç tuşuna basın
- Kapat butonuna basılı tutun
- Güvenli modda başlat seçeneği belirecektir

## Telefonun Ekranının Kendiliğinden Kapanması

Görüntü boyutunu değiştirip eski haline getirin 😅

> Kaynak için [buraya](https://www.reddit.com/r/Xiaomi/comments/apkwo9/mi_a2_lite_autoclosing_apps/) bakabilirsin

## Stock Rom Yükleme

### ADB & Flashboot Kurulumu

Linux için kurulumuna [buradan](../%C4%B0%C5%9Fletim%20Sistemi%20Notlar%C4%B1%2FLinux%20Notlar%C4%B1.md#adb--fastboot-android-tools-kurulumu) erişebilirsin.

> Windows için kurulumu el ile yapmalı ve dosyaların olduğu dizini **ortam değişkenlerine** (_PATH_ adı altına) eklemeniz gerekmektedir.

### Bootloader Klidini Açma

- Cihazı PC'ye USB ile bağlayın
- Ses kısma ve güç tuşlarına basılı tutup **fastboot** alanına girin
- `fastboot oem unlock` komutu ile kilidi açın

### Stock Rom Kurulumu

Buradaki [linke](https://en.miui.com/download-354.html) tıklayarak _stock rom_'u indirme sayfasına yönelebilirsin.

- Link çalışmazsa [buradan](https://drive.google.com/open?id=1_1wuJdhp8VJDl-Ho6ChG_YlU6pGWUaQv) yedeklememe erişebilirsin
- Gerekirse USB driverı da yedeklememden indirebilirsin

### Stock Rom'un Aktarılması

- Telefonunuzu kapatın
- Telefon kapandıktan sonra, `Volume Down (Ses Kısma)` butonuna basılır tutarak PC'ye bağlayın
- PC'de adb dosyalarının olduğu dizini PATH'e eklemeyi unutmayın
  - Linux için gerekli değildir
- İndirdiğiniz dosyayı çıkartın ve dizine gelip, windows için `flash_all_lock.bat` linux için `flash_all_lock.sh` scriptlerini çalıştırın

## Harici Bağlantılar

- [Xiaomi Mi A2 Lite Bilinen Hatalar ve Çözümleri](https://mobileinternist.com/xiaomi-mi-a2-issues-solved)
