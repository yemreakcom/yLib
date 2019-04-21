# Xiaomi Mi A2 Lite

## Stock Rom Yükleme

### ADB & Flashboot Kurulumu

Linux için kurulumuna [buradan](../%C4%B0%C5%9Fletim%20Sistemi%20Notlar%C4%B1%2FLinux%20Notlar%C4%B1.md#adb--fastboot-android-tools-kurulumu) erişebilirsin.

> Windows için kurulumu el ile yapmalı ve dosyaların olduğu dizini **ortam değişkenlerine** (*PATH* adı altına) eklemeniz gerekmektedir.

### Stock Rom Kurulumu

Buradaki [linke](https://en.miui.com/download-354.html) tıklayarak *stock rom*'u indirme sayfasına yönelebilirsin.

### Stock Rom'un Aktarılması

- Telefonunuzu kapatın
- Telefon kapandıktan sonra, `Volume Down (Ses Kısma)` butonuna basılır tutarak PC'ye bağlayın
- PC'de adb dosyalarının olduğu dizini PATH'e eklemeyi unutmayın
  - Linux için gerekli değildir
- İndirdiğiniz dosyayı çıkartın ve dizine gelip, windows için `flash_all_lock.bat` linux için `flash_all_lock.sh` scriptlerini çalıştırın