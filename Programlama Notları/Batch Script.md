# Batch Script <!-- omit in toc -->

Windows işletim sistemlerinin ortak programlama dilidir.

## İçerikler <!-- omit in toc -->

- [Başlatma İşlemleri (Start)](#ba%C5%9Flatma-i%CC%87%C5%9Flemleri-start)
- [Yazırma İşlemleri (Echo)](#yaz%C4%B1rma-i%CC%87%C5%9Flemleri-echo)
- [Koşullu İşlemleri (IF / Else)](#ko%C5%9Fullu-i%CC%87%C5%9Flemleri-if--else)
- [Sessiz Kurulumlar](#sessiz-kurulumlar)
  - [Koşullu İndirme Scripti](#ko%C5%9Fullu-i%CC%87ndirme-scripti)
  - [Java JRE Sessiz Kurulumu](#java-jre-sessiz-kurulumu)
  - [Python Sessiz Kurulumu](#python-sessiz-kurulumu)
- [Hata Notları](#hata-notlar%C4%B1)
  - [`\Common was unexpected at this time` Hatası](#common-was-unexpected-at-this-time-hatas%C4%B1)

## Başlatma İşlemleri (Start)

- `start .` Bulunduğumuz dizini açma
- `start /w <bat>` Bat dosyası bitene kadar bekleme
- `start "" <bat>` Bat dosyasını çalıştırıp cmd'yi kapatma
- `start /b <bat>` Dosyayı asenkron çalıştırma

> Ek bağlantılar
>
> - [CMD dosya çalıştırıp kapatma]
> - [CMD'yi arkaplanda sessiz çalıştırma]

## Yazırma İşlemleri (Echo)

- `@` karakteri çıktı verme anlamına gelmektedir
- `@echo off` tüm çıktıları gizler

> Ek bağlantılar
>
> - [Echo off]

## Koşullu İşlemleri (IF / Else)

```bat
IF EXIST "filename" (
  REM Do one thing
) ELSE (
  REM Do another thing
)
```

> Ek bağlantılar
>
> - [If else]

## Sessiz Kurulumlar

### Koşullu İndirme Scripti

```bat
(wget.exe -O "python-3.7.3.exe" "https://www.python.org/ftp/python/3.7.3/python-3.7.3-amd64.exe" && wget.exe -O "jre-8u211-windows-i586.exe" "https://javadl.oracle.com/webapps/download/AutoDL?BundleId=238727_478a62b7d4e34b78b671c754eaaf38ab") || echo "Error while installation" && pause && exit
```

> `wget.exe` gereklidir, [buradan][Wget] indirebilirsin.

### Java JRE Sessiz Kurulumu

```bat
 start /w jre-8u211-windows-i586.exe /s INSTALLDIR=%userprofile%\AppData\Local\Programs\java\jre1.8.2
```

### Python Sessiz Kurulumu

```bat
python-3.7.3.exe InstallAllUsers=0 Include_launcher=0 Include_test=0 SimpleInstall=1 SimpleInstallDescription="Just for YEmreAk 🤖"
```

## Hata Notları

### `\Common was unexpected at this time` Hatası

- Scriptten değişkenleri (`%..%`) kaldırman gerekmekte
- Örn: `set PATH=%PATH%;C:\Path\to\file` yerine `set PATH=C:\Path\to\file`  kullnılmalıdır

> Ek bağlantılar
>
> - [\Common was unexpected at this time]

[Echo off]: https://stackoverflow.com/a/8486061/9770490
[If else]: https://stackoverflow.com/a/3022193
[CMD dosya çalıştırıp kapatma]: https://stackoverflow.com/a/12848306/9770490
[CMD'yi arkaplanda sessiz çalıştırma]: https://stackoverflow.com/a/298636/9770490
[\Common was unexpected at this time]: https://splogadev.wordpress.com/2012/07/03/common-was-unexpected-at-this-time/
[Wget]: https://eternallybored.org/misc/wget/