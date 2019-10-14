---
description: MSStore üzerinden indirilen uygulumalara direkt olarak erişimin nasıl olacağını anlatır.
---

## 👜 Windows Mağazasından İndirilen Uygulamaları Komut ile Çalıştırma

### 🤓 Komutu Oluşturmak için Gerekli Bilgileri Alma

- PowerShell üzerinden `Get-AppxPackage > appxpackages.txt` komutu ile dosyaya appx paketlerinin bilgilerini kaydedin
- `.\appxpackages.txt` komutu ile dosyayı açın
- <kbd>✲ Ctrl</kbd> <kbd>F</kbd> ile dosya içerisinde kısayol oluşturmak istediğiniz uygulamanın adını aratın
  - Örn: `OneNote`
- Bulduğunuz uygulama bilgilerindeki alttaki kısımlar ileride kullanılacaktır:
  -  `PackageFamilyName`
  -  `InstallLocation`
-  ` cat "InstallLocation\AppxManifest.xml" | grep Executable=` komutunu yazın ve çıkan sonuçtaki `Application Id=` değerini kaydedin

### 👨‍💻 Komutu Tanımlama

Çalıştırma komutu aşağıdaki gibi olacaktır:

-  `shell:appsFolder\PackageFamilyName!Application Id`
   -  `PackageFamilyName` ve `Application Id` kısmına yukarıdaki işlemlerde bulduğumuz değerleri yazacağız
-  OneNote için: `shell:appsFolder\Microsoft.Office.OneNote_8wekyb3d8bbwe!microsoft.onenoteim`

## 🔗 Harici Bağlantılar

- [Method to open any Windows 10 Apps from command line](https://www.tenforums.com/software-apps/57000-method-open-any-windows-10-apps-command-line.html) yazısından derlenmiştir.
