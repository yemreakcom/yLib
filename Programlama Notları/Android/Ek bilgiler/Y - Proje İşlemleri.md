# Proje İşlemleri

## Projeyi Oluşturduktan Sonra Package İsmi Değiştirme

- Project sekmesinden "Ayarlar" ikonundan "Hide Empty Middle Package"a tıklıyoruz.
- Değiştirmek istediğimiz klasöre sağ tıklayıp, "Refactor" -> "Rename" diyoruz ve adlandırıyoruz. (3. klasöre de aynısı yapıyoruz)
- Eğer klasörü kaldırmak istiyorsak; Kalkacak olan klasörün içindekileri, onun üstündeki klasöre (yani onun yanına) yapıştırıyoruz.
  - Örn; "moddedsnake"i kesip, "com" adlı klasöre yapıştırıyoruz ve "yemreak" ı siliyoruz.
- Gradle'imizdaki build.gradle (Module: app) 'a giriyoruz ve applicationId'yi güncelliyoruz. Bizim örneğimizde oraya "com.yemreak.moddedsnake" yazıyoruz.
- Son olarak; Manifestimize girip "package name"i güncelliyoruz.
- Artık başarıyla "package name"i güncellemiş olduk. Emin olmak için projenizi Build etmeyi unutmayın :)

![Change Package Name1](../res/android_change_packagename1.png)

![Change Package Name2](../res/android_change_packagename2.png)

![Change Package Name3](../res/android_change_packagename3.png)

![Change Package Name4](../res/android_change_packagename4.png)
