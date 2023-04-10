---
description: >-
  JetBrains, IntelliJ, WebStorm, Android Studio gibi JetBrains IDE'leri için
  eklenti veya plugin oluşturma
---

# 🔌 Plugin Oluşturma | JetBrains IDE

## 🎈 Eklenti Projesi Açma

* 📢 `Gradle-Java` eklentisinin yüklü olduğundan emin olun
* 👷‍♂️ `New Project` - `Gradle` - `IntelliJ Platform Plugin` - `Java` veya `Kotlin / JVM`
* ⚙️ Eklentinin yönetimi `plugin.xml` dosyası ile yapılmaktadır

> 💁‍♂️ İsterseniz yeni Gradle olan `Kotlin DSL`'i de kullanabilirsiniz

![](../../.gitbook/assets/intellij\_new\_project.png)

{% hint style="info" %}
‍🧙‍♂ Detaylı bilgi için [Creating a Gradle-Based IntelliJ Platform Plugin with New Project Wizard](https://www.jetbrains.org/intellij/sdk/docs/tutorials/build\_system/prerequisites.html#creating-a-gradle-based-intellij-platform-plugin-with-new-project-wizard) alanına bakabilirsin.
{% endhint %}

## 👨‍💼 Tema Yönetimi

* 🔨 En son eklenen tema, eklenti indirildiği zaman varsayılan olarak seçilir
* ⭐ Varsayılan olmasını istediğiniz temanızı plugin.xml içerisindeki extensions bloğu içerisindeki en alta getirin

![](../../.gitbook/assets/theme\_edit\_button.png)

## ✨ Plugin Oluşturma

* 🏗️ Eklentiyi oluşturmadan önce [👨‍💻 Plugin Structure](https://www.jetbrains.org/intellij/sdk/docs/basics/plugin\_structure.html) alanına bakmanda fayda var
* 🔨 Plugin yapılandırma ayarları için [👨‍💻 Plugin Configuration File](https://www.jetbrains.org/intellij/sdk/docs/basics/plugin\_structure/plugin\_configuration\_file.html) alanına bakmalısın
* 🤝 Plugin tüm platformlarda olması için `plugin.xml` dosyana `since-build` eklemen gerekir
* 🖼️ Resim gösterme işlemleri için online URL'ler kullanmalısınız, yerel resimlere erişemez

{% tabs %}
{% tab title="📜 XML" %}
{% code title="plugin.xml" %}
```markup
<idea-version since-build="173.0"/>
```
{% endcode %}
{% endtab %}

{% tab title="☕ Gradle" %}
{% code title="build.gradle" %}
```groovy
patchPluginXml {
    sinceBuild '173.0'
    
    /*
    def changelogPath = "$projectDir/build/CHANGELOG.html"
    def readmePath = "$projectDir/build/README.html"

    if (file(changelogPath).exists()) {    
        changeNotes file(changelogPath).text
    }

    if (file(readmePath).exists()) {
        pluginDescription file(readmePath).text
    }
    */
}
```
{% endcode %}
{% endtab %}

{% tab title="🎃 Kotlin DSL" %}
{% code title="build.gradle.kts" %}
```groovy
tasks.getByName
    <org.jetbrains.intellij.tasks.PatchPluginXmlTask>("patchPluginXml") {
    
    val sinceBuild = "173.0" // Android compatibility

    /*
    val changelogPath = "$projectDir/.github/assets/CHANGELOG.html"
    val readmePath = "$projectDir/.github/assets/README.html"
    */

    sinceBuild(sinceBuild)
    
    /*
    if (file(changelogPath).exists()) {
        changeNotes(file(changelogPath).readText(Charsets.UTF_8))
    }

    if (file(readmePath).exists()) {
        pluginDescription(file(readmePath).readText(Charsets.UTF_8))
    }
    */
}
```
{% endcode %}
{% endtab %}
{% endtabs %}

![](../../.gitbook/assets/jetbrain\_build\_plugin.png)

## 🛰️ Plugin'i Yayınlama

* 🏳 Proje ilk kez yayınlanacaksa, elle [Upload Plugin](https://plugins.jetbrains.com/plugin/add) alanından upload edilmesi gerekir
* 👨‍🔧 Kotlin Gradle için `publishPlugin` yapısı `tasks.publishPlugin` kullanılır

{% tabs %}
{% tab title="🎃 Kotlin DSL" %}
{% code title="build.gradle.kts" %}
```groovy
tasks.publishPlugin {
    token("TOKEN BİLGİSİ")
}
```
{% endcode %}
{% endtab %}
{% endtabs %}

{% hint style="info" %}
‍🧙‍♂ Detaylı bilgi için [Project Setup](https://www.jetbrains.org/intellij/sdk/docs/basics/plugin\_structure/plugin\_dependencies.html#project-setup) alanına bakabilirsin.
{% endhint %}

## 🐞 Hata Notları

### 💾 Fail to load plugin descriptor from file \*.jar

* 📃 Description içeriğinizde `css` , `javascript` yada `html attributes` olması durumunda gelir
* 🦄 Sadece html `body` içeriğini yazmanız gerekmekte

### 👁️ Açıklama alanında resimlerin gözükmemesi

* 🙄 JetBrains html açıklamasını yüklerken diğer dosyaları yüklemez
* 🔗 Tüm resim bağlantılarının internet üzerindeki resimlere olması gerekmektedir

## 🔗​ Faydalı Bağlantılar

* [📖 Gradle ile Eklenti Oluşturma (Tavsiye Edilir)](https://www.jetbrains.org/intellij/sdk/docs/basics/getting\_started.html#using-gradle)
* [📖 IntelliJ Platform based products of recent IDE version](https://www.jetbrains.org/intellij/sdk/docs/basics/getting\_started/build\_number\_ranges.html#intellij-platform-based-products-of-recent-ide-versions)
* [📖​ Creating Custom UI Themes](https://www.jetbrains.org/intellij/sdk/docs/reference\_guide/ui\_themes/themes.html)
* [📖 Customizing UI Themes - Icons and UI Controls](https://www.jetbrains.org/intellij/sdk/docs/reference\_guide/ui\_themes/themes\_customize.html)
* [📖​ UI Themes - Editor Schemes and Background Images](https://www.jetbrains.org/intellij/sdk/docs/reference\_guide/ui\_themes/themes\_extras.html)\*\*\*\*
* [📖​ Enabling Internal Mode](https://www.jetbrains.org/intellij/sdk/docs/reference\_guide/internal\_actions/enabling\_internal.html)
* [**📖** Internal Actions - LaF Defaults](https://www.jetbrains.org/intellij/sdk/docs/reference\_guide/internal\_actions/internal\_ui\_lafd.html) \*\*\*\*
* [📃 Gradle IntelliJ Plugin](https://github.com/JetBrains/gradle-intellij-plugin/)

{% hint style="success" %}
🚀 Bu alandaki bağlantılar [YEmoji \~Bağlantılar](https://emoji.yemreak.com/kullanim/baglantilar) yapısına uygundur
{% endhint %}
