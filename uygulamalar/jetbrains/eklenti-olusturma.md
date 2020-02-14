---
description: >-
  JetBrains, IntelliJ, WebStorm, Android Studio gibi JetBrains IDE'leri için
  eklenti oluşturma
---

# 🔌 Eklenti Oluşturma \| JetBrains IDE

## 🏗️ Eklenti Projesi Oluşturma

* 📢 `Gradle-Java` eklentisinin yüklü olduğundan emin olun
* 👷‍♂️ `New Project` - `Gradle` - `IntelliJ Platform Plugin` - `Java` veya `Kotlin / JVM`

> 💁‍♂️ İsterseniz yeni Gradle olan `Kotlin DSL`'i de kullanabilirsiniz

![](../../.gitbook/assets/intellij_new_project.png)

{% hint style="info" %}
‍🧙‍♂ Detaylı bilgi için [Creating a Gradle-Based IntelliJ Platform Plugin with New Project Wizard](https://www.jetbrains.org/intellij/sdk/docs/tutorials/build_system/prerequisites.html#creating-a-gradle-based-intellij-platform-plugin-with-new-project-wizard) alanına bakabilirsin.
{% endhint %}

## 👨‍💼 Tema Yönetimi

![](../../.gitbook/assets/theme_edit_button.png)

## 🏗️ Eklentiyi Oluşturma

![](../../.gitbook/assets/jetbrain_build_plugin.png)

## 🎃 Kotlin DSL ile Yayınlama

*  👨‍🔧 Kotlin Gradle için `publishPlugin` yapısı `tasks.publishPlugin` kullanılır

{% code title="build.gradle.kts" %}
```groovy
tasks.publishPlugin {
    token("TOKEN BİLGİSİ")
}
```
{% endcode %}

{% hint style="info" %}
‍🧙‍♂ Detaylı bilgi için [Project Setup](https://www.jetbrains.org/intellij/sdk/docs/basics/plugin_structure/plugin_dependencies.html#project-setup) alanına bakabilirsin.
{% endhint %}

## 🔗​ Faydalı Bağlantılar

* [📖 Gradle ile Eklenti Oluşturma \(Tavsiye Edilir\)](https://www.jetbrains.org/intellij/sdk/docs/basics/getting_started.html#using-gradle)
* [📖 IntelliJ Platform based products of recent IDE version](https://www.jetbrains.org/intellij/sdk/docs/basics/getting_started/build_number_ranges.html#intellij-platform-based-products-of-recent-ide-versions)
* [📖​ Creating Custom UI Themes](https://www.jetbrains.org/intellij/sdk/docs/reference_guide/ui_themes/themes.html)
* [📖 Customizing UI Themes - Icons and UI Controls](https://www.jetbrains.org/intellij/sdk/docs/reference_guide/ui_themes/themes_customize.html)
* [📖​ UI Themes - Editor Schemes and Background Images](https://www.jetbrains.org/intellij/sdk/docs/reference_guide/ui_themes/themes_extras.html)\*\*\*\*
* [📖​ Enabling Internal Mode](https://www.jetbrains.org/intellij/sdk/docs/reference_guide/internal_actions/enabling_internal.html)
* [**📖** Internal Actions - LaF Defaults](https://www.jetbrains.org/intellij/sdk/docs/reference_guide/internal_actions/internal_ui_lafd.html) ****
* [📃 Gradle IntelliJ Plugin](https://github.com/JetBrains/gradle-intellij-plugin/)

