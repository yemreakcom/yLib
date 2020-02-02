---
description: Kendi cep telefonum hakkında bildiklerimi derlediğim proje.
---

# 📱 Xiaomi Mi A2 Lite Notlarım

## 🔏 Güvenli Mod ile Açma

* Güç tuşuna basın
* Kapat butonuna basılı tutun
* Güvenli mod ile başlat seçeneği belirecektir

## 🧰 Stock Rom Yükleme

### ‍👷‍♂️ ADB Kurulumu

* 🐧 Linux için kurulumuna [buradan](https://github.com/yedhrab/YWiki/tree/169abadfd1b8862c004399268f6ca1f9f9359d61/İşletim%20Sistemi%20Notları/Linux%20Notları.md#adb--fastboot-android-tools-kurulumu) erişebilirsin.
* ✴️ Windows için kurulumu el ile yapmalı ve dosyaların olduğu dizini **ortam değişkenlerine** \(_PATH_ adı altına\) eklemeniz gerekmektedir.
  * 🍫 Choco için `choco install adb`
  * 👨‍💻 `%localappdata%\Android\Sdk\platform-tools` dizininde `adb` olabilir

### 🔌 Cihazı Geliştirici Moduna Alma ve Erişme

* Cihazdan ayarlar alanına girin
* En üstte **Telefon Hakkında** alınına tıklayın
* Açılan pencerede en altta bulunun **Derleme Numarası**'ya 7, 8 kere dokunun
* Geliştirici ayarlarından **USB hata ayıklamasını** aktif edin
* PC'ye telefonu bağlayın
* `adb devices` komutu ile `adb` servisini başlatıp, telefona gelen pop-up'tan izin verin

### 🔓 Bootloader Klidini Açma

* 💦 Öncelikle bu işlemin cihazın hafızasının **sıfırlayacağının** farkında olun
* 🔌 Cihazı PC'ye USB ile bağlayın
* 🔉 Ses kısma ve güç tuşlarına basılı tutup **fastboot** alanına girin 
* 👨‍💻`fastboot oem unlock` komutu ile kilidi açın \(cmd veya bash'e yazılmalı\)

> Kapatmak için `fastboot oem lock` veya yükleme esnasında `flash_all_lock.sh` scriptini kullanın

### 🧱 Stock Rom Kurulumu

Buradaki [linke](http://en.miui.com/download-354.html) tıklayarak _stock rom_'u indirme sayfasına yönelebilirsin.

* 📦 Kararlı son ROM'u [Mi Community - MIUI Global ROM &gt; Mi A2 Lite](http://c.mi.com//miuidownload/detail?device=1700354) üzerinden indirebilirsin
* ⏬ Link çalışmazsa[ buradan \(Şubat 2020\) ](http://bigota.d.miui.com/V10.0.13.0.PDLMIXM/daisy_global_images_V10.0.13.0.PDLMIXM_20190813.0000.00_9.0_5d0d486f04.tgz)direkt olarak indirebilirsin
  * 📢 Orjinal stock rom dosyasıdır. \(checksum'dan geçmiştir\)
* 🧰 [MIUI ROM Flashing Tool](http://download.appmifile.com/images/2019/07/01/09cdc3a7-5a11-42aa-81f4-be27fe12ce80.msi) uygulamasını indirin

### 🚙 Stock Rom'un Aktarılması

* 👮‍♂️ Telefonunuzun [🔓 Bootloader Klidini Açma](xiaomi-mi-a2-lite.md#bootloader-klidini-acma) alanındaki yönerge ile bootloader kilidini açtığınızdan emin olun
* 🌃 Telefonunuzu kapatın
* 🔉 Telefon kapandıktan sonra, `Volume Down (Ses Kısma)` butonuna basılır tutarak PC'ye bağlayın
* 📢 PC'de adb dosyalarının olduğu dizini PATH'e eklemeyi unutmayın
  * 🐧 Linux için gerekli değildir
  * ✴️ Windows için choco ile yükleme yapıldıysa gerekli değildir
  * [👷‍♂️ ADB Kurulumu](xiaomi-mi-a2-lite.md#adb-kurulumu) alanına bakınız
* 📂 İndirdiğiniz ROM'u dizine çıkartın ardından alttaki seçeneklerden **biri** ile kurulumu yapın
  * 🧰 [MIUI ROM Flashing Tool](http://download.appmifile.com/images/2019/07/01/09cdc3a7-5a11-42aa-81f4-be27fe12ce80.msi) uygulamasına ROM'un yolunu kopyalayın
  * 👨‍💻 İndirdiğiniz dosyayı çıkartın ve dizine gelip, windows için `flash_all_lock.bat` linux için `flash_all_lock.sh` scriptlerini çalıştırın

> `🐞 FAILED (remote: 'device is locked. Cannot erase')` sorunu gelirse [🔓 Bootloader Klidini Açma](xiaomi-mi-a2-lite.md#bootloader-klidini-acma) alanındaki talimatları uygulayın.

## 📃 Özel Scriptler

* `images` klasörünün içerisinde imajlar olmalıdır
* Klasörün yanında da alttaki script olmalıdır
* Script'in çalışması için `adb` gereklidir

### 👨‍💻 Windows için Flash All

```text
fastboot %* getvar product 2>&1 | findstr /r /c:"^product: *daisy" || @echo "error : Missmatching image and device" && exit /B 1
set CURRENT_ANTI_VER=1
for /f "tokens=2 delims=: " %%i in ('fastboot %* getvar rollback_ver 2^>^&1 ^| findstr /r /c:"rollback_ver:"') do (set version=%%i)
if [%version%] EQU [] set version=0
if %version% GTR %CURRENT_ANTI_VER% (
    @echo "error : current device antirollback version is greater than this package"
    exit /B 1
)
fastboot %* erase boot_a || @echo "Erase boot_a error" && exit /B 1
fastboot %* flash modem_a %~dp0\images\modem.img || @echo "Flash modem_a error" && exit /B 1
fastboot %* flash modem_b %~dp0\images\modem.img || @echo "Flash modem_b error" && exit /B 1
fastboot %* flash sbl1_a %~dp0\images\sbl1.img || @echo "Flash sbl1_a error" && exit /B 1
fastboot %* flash sbl1_b %~dp0\images\sbl1.img || @echo "Flash sbl1_b error" && exit /B 1
fastboot %* flash rpm_a %~dp0\images\rpm.img || @echo "Flash rpm_a error" && exit /B 1
fastboot %* flash rpm_b %~dp0\images\rpm.img || @echo "Flash rpm_b error" && exit /B 1
fastboot %* flash tz_a %~dp0\images\tz.img || @echo "Flash tz_a error" && exit /B 1
fastboot %* flash tz_b %~dp0\images\tz.img || @echo "Flash tz_b error" && exit /B 1
fastboot %* flash devcfg_a %~dp0\images\devcfg.img || @echo "Flash devcfg_a error" && exit /B 1
fastboot %* flash devcfg_b %~dp0\images\devcfg.img || @echo "Flash devcfg_b error" && exit /B 1
fastboot %* flash dsp_a %~dp0\images\dsp.img || @echo "Flash dsp_a error" && exit /B 1
fastboot %* flash dsp_b %~dp0\images\dsp.img || @echo "Flash dsp_b error" && exit /B 1
fastboot %* flash sec %~dp0\images\sec.dat || @echo "Flash sec error" && exit /B 1
fastboot %* flash splash %~dp0\images\splash.img || @echo "Flash splash error" && exit /B 1
fastboot %* flash aboot_a %~dp0\images\emmc_appsboot.mbn || @echo "Flash aboot_a error" && exit /B 1
fastboot %* flash aboot_b %~dp0\images\emmc_appsboot.mbn || @echo "Flash aboot_b error" && exit /B 1
fastboot %* flash boot_a %~dp0\images\boot.img || @echo "Flash boot_a error" && exit /B 1
fastboot %* flash boot_b %~dp0\images\boot.img || @echo "Flash boot_b error" && exit /B 1
fastboot %* flash system_a %~dp0\images\system.img || @echo "Flash system_a error" && exit /B 1
fastboot %* flash system_b %~dp0\images\system_other.img || @echo "Flash system_b error" && exit /B 1
fastboot %* flash vendor_a %~dp0\images\vendor.img || @echo "Flash vendor_a error" && exit /B 1
fastboot %* flash vendor_b %~dp0\images\vendor.img || @echo "Flash vendor_b error" && exit /B 1
fastboot %* flash lksecapp %~dp0\images\lksecapp.img || @echo "Flash lksecapp error" && exit /B 1
fastboot %* flash lksecappbak %~dp0\images\lksecapp.img || @echo "Flash lksecappbak error" && exit /B 1
fastboot %* flash cmnlib_a %~dp0\images\cmnlib.img || @echo "Flash cmnlib_a error" && exit /B 1
fastboot %* flash cmnlib_b %~dp0\images\cmnlib.img || @echo "Flash cmnlib_b error" && exit /B 1
fastboot %* flash cmnlib64_a %~dp0\images\cmnlib64.img || @echo "Flash cmnlib64_a error" && exit /B 1
fastboot %* flash cmnlib64_b %~dp0\images\cmnlib64.img || @echo "Flash cmnlib64_b error" && exit /B 1
fastboot %* flash keymaster_a %~dp0\images\keymaster.img || @echo "Flash keymaster_a error" && exit /B 1
fastboot %* flash keymaster_b %~dp0\images\keymaster.img || @echo "Flash keymaster_b error" && exit /B 1
fastboot %* flash userdata %~dp0\images\userdata.img || @echo "Flash userdata error" && exit /B 1
fastboot %* set_active a
fastboot %* reboot || @echo "Reboot error" && exit /B 1
```

### 🐧 Linux için Flash All

```bash
fastboot $* getvar product 2>&1 | grep -E "^product: *daisy$"
if [ $? -ne 0 ] ; then echo "error : Missmatching image and device"; exit 1; fi
CURRENT_ANTI_VER=1
version=`fastboot getvar rollback_ver 2>&1 | grep "rollback_ver:" | awk -F ": " '{print $2}'`
if [  "${version}"x == ""x ] ; then version=0 ; fi
if [ ${version} -gt ${CURRENT_ANTI_VER} ] ; then  echo "error : current device antirollback version is greater than this package" ; exit 1 ; fi
fastboot $* erase boot_a
if [ $? -ne 0 ] ; then echo "Erase boot_a error"; exit 1; fi
fastboot $* flash modem_a `dirname $0`/images/modem.img
if [ $? -ne 0 ] ; then echo "Flash modem_a error"; exit 1; fi
fastboot $* flash modem_b `dirname $0`/images/modem.img
if [ $? -ne 0 ] ; then echo "Flash modem_b error"; exit 1; fi
fastboot $* flash sbl1_a `dirname $0`/images/sbl1.img
if [ $? -ne 0 ] ; then echo "Flash sbl1_a error"; exit 1; fi
fastboot $* flash sbl1_b `dirname $0`/images/sbl1.img
if [ $? -ne 0 ] ; then echo "Flash sbl1_b error"; exit 1; fi
fastboot $* flash rpm_a `dirname $0`/images/rpm.img
if [ $? -ne 0 ] ; then echo "Flash rpm_a error"; exit 1; fi
fastboot $* flash rpm_b `dirname $0`/images/rpm.img
if [ $? -ne 0 ] ; then echo "Flash rpm_b error"; exit 1; fi
fastboot $* flash tz_a `dirname $0`/images/tz.img
if [ $? -ne 0 ] ; then echo "Flash tz_a error"; exit 1; fi
fastboot $* flash tz_b `dirname $0`/images/tz.img
if [ $? -ne 0 ] ; then echo "Flash tz_b error"; exit 1; fi
fastboot $* flash devcfg_a `dirname $0`/images/devcfg.img
if [ $? -ne 0 ] ; then echo "Flash devcfg_a error"; exit 1; fi
fastboot $* flash devcfg_b `dirname $0`/images/devcfg.img
if [ $? -ne 0 ] ; then echo "Flash devcfg_b error"; exit 1; fi
fastboot $* flash dsp_a `dirname $0`/images/dsp.img
if [ $? -ne 0 ] ; then echo "Flash dsp_a error"; exit 1; fi
fastboot $* flash dsp_b `dirname $0`/images/dsp.img
if [ $? -ne 0 ] ; then echo "Flash dsp_b error"; exit 1; fi
fastboot $* flash sec `dirname $0`/images/sec.dat
if [ $? -ne 0 ] ; then echo "Flash sec error"; exit 1; fi
fastboot $* flash splash `dirname $0`/images/splash.img
if [ $? -ne 0 ] ; then echo "Flash splash error"; exit 1; fi
fastboot $* flash aboot_a `dirname $0`/images/emmc_appsboot.mbn
if [ $? -ne 0 ] ; then echo "Flash aboot_a error"; exit 1; fi
fastboot $* flash aboot_b `dirname $0`/images/emmc_appsboot.mbn
if [ $? -ne 0 ] ; then echo "Flash aboot_b error"; exit 1; fi
fastboot $* flash boot_a `dirname $0`/images/boot.img
if [ $? -ne 0 ] ; then echo "Flash boot_a error"; exit 1; fi
fastboot $* flash boot_b `dirname $0`/images/boot.img
if [ $? -ne 0 ] ; then echo "Flash boot_b error"; exit 1; fi
fastboot $* flash system_a `dirname $0`/images/system.img
if [ $? -ne 0 ] ; then echo "Flash system_a error"; exit 1; fi
fastboot $* flash system_b `dirname $0`/images/system_other.img
if [ $? -ne 0 ] ; then echo "Flash system_b error"; exit 1; fi
fastboot $* flash vendor_a `dirname $0`/images/vendor.img
if [ $? -ne 0 ] ; then echo "Flash vendor_a error"; exit 1; fi
fastboot $* flash vendor_b `dirname $0`/images/vendor.img
if [ $? -ne 0 ] ; then echo "Flash vendor_b error"; exit 1; fi
fastboot $* flash lksecapp `dirname $0`/images/lksecapp.img
if [ $? -ne 0 ] ; then echo "Flash lksecapp error"; exit 1; fi
fastboot $* flash lksecappbak `dirname $0`/images/lksecapp.img
if [ $? -ne 0 ] ; then echo "Flash lksecappbak error"; exit 1; fi
fastboot $* flash cmnlib_a `dirname $0`/images/cmnlib.img
if [ $? -ne 0 ] ; then echo "Flash cmnlib_a error"; exit 1; fi
fastboot $* flash cmnlib_b `dirname $0`/images/cmnlib.img
if [ $? -ne 0 ] ; then echo "Flash cmnlib_b error"; exit 1; fi
fastboot $* flash cmnlib64_a `dirname $0`/images/cmnlib64.img
if [ $? -ne 0 ] ; then echo "Flash cmnlib64_a error"; exit 1; fi
fastboot $* flash cmnlib64_b `dirname $0`/images/cmnlib64.img
if [ $? -ne 0 ] ; then echo "Flash cmnlib64_b error"; exit 1; fi
fastboot $* flash keymaster_a `dirname $0`/images/keymaster.img
if [ $? -ne 0 ] ; then echo "Flash keymaster_a error"; exit 1; fi
fastboot $* flash keymaster_b `dirname $0`/images/keymaster.img
if [ $? -ne 0 ] ; then echo "Flash keymaster_b error"; exit 1; fi
fastboot $* flash userdata `dirname $0`/images/userdata.img
if [ $? -ne 0 ] ; then echo "Flash userdata error"; exit 1; fi
fastboot $* set_active a
fastboot $* reboot
if [ $? -ne 0 ] ; then echo "Reboot error"; exit 1; fi
```

## 🐞 Hata Notları

### 👇 Dokunmatikte Sorunlu Algılama

Maalesef cihazın donanımsal kusurudur 😥

### 🔲 Telefonun Ekranının Kendiliğinden Kapanması

Görüntü boyutunu değiştirip eski haline getirin 😅

> Kaynak için [buraya](https://www.reddit.com/r/Xiaomi/comments/apkwo9/mi_a2_lite_autoclosing_apps/) bakabilirsin

## 🔗 Harici Bağlantılar

* [⏬ Mi A2 Lite Kararlı ROM](http://c.mi.com//miuidownload/detail?device=1700354)
* [📖 Fastboot Güncellemesi](http://c.mi.com/tr/miuidownload/detail?guide=2)
* [Xiaomi Mi A2 Lite Bilinen Hatalar ve Çözümleri](https://mobileinternist.com/xiaomi-mi-a2-issues-solved)
* [Unbrick All Qualcomm Snapdragon’s from Qualcomm HS-USB QDLoader 9008 \(if you have the right kind of rom\)](https://www.androidbrick.com/unbrick-all-qualcomm-snapdragons-from-qualcomm-hs-usb-qdloader-9008-if-you-have-the-right-kind-of-rom-qhsusb_dload_edl/)

