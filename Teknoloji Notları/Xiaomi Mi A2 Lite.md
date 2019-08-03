# Xiaomi Mi A2 Lite <!-- omit in toc -->

## İçerikler <!-- omit in toc -->

- [Güvenli Modda Açma](#G%C3%BCvenli-Modda-A%C3%A7ma)
- [Telefonun Ekranının Kendiliğinden Kapanması](#Telefonun-Ekran%C4%B1n%C4%B1n-Kendili%C4%9Finden-Kapanmas%C4%B1)
- [Stock Rom Yükleme](#Stock-Rom-Y%C3%BCkleme)
  - [ADB & Flashboot Kurulumu](#ADB--Flashboot-Kurulumu)
  - [Bootloader Klidini Açma](#Bootloader-Klidini-A%C3%A7ma)
  - [Stock Rom Kurulumu](#Stock-Rom-Kurulumu)
  - [Stock Rom'un Aktarılması](#Stock-Romun-Aktar%C4%B1lmas%C4%B1)
- [Harici Bağlantılar](#Harici-Ba%C4%9Flant%C4%B1lar)

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

Buradaki [linke](http://en.miui.com/download-354.html) tıklayarak _stock rom_'u indirme sayfasına yönelebilirsin.

- Link çalışmazsa [buradan (June 2019)](https://bigota.d.miui.com/V10.0.10.0.PDLMIXM/miui_DAISYGlobal_V10.0.10.0.PDLMIXM_e3710856b5_9.0.zip) direkt olarak indirebilirsin
- Gerekirse USB driverı da yedeklememden indirebilirsin

### Stock Rom'un Aktarılması

- Telefonunuzu kapatın
- Telefon kapandıktan sonra, `Volume Down (Ses Kısma)` butonuna basılır tutarak PC'ye bağlayın
- PC'de adb dosyalarının olduğu dizini PATH'e eklemeyi unutmayın
  - Linux için gerekli değildir
- İndirdiğiniz dosyayı çıkartın ve dizine gelip, windows için `flash_all_lock.bat` linux için `flash_all_lock.sh` scriptlerini çalıştırın

## Harici Bağlantılar

- [Xiaomi Mi A2 Lite Bilinen Hatalar ve Çözümleri](https://mobileinternist.com/xiaomi-mi-a2-issues-solved)
