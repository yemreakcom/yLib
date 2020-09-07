# 🚴‍♂️ Giriş \| VS Extension

## 💎 Ön Gereksinimler

Eklentiyi Visual Studio için C\# ile programlayacağımızdan dolayı:

* ⏬ `Visual Studio` ve `Visual Studio extension development` iş yükü indirilmelidir
* 💁‍♂️ Eklenti için derinden bir C\# bilgisi yerine hızlı bir öğrenmeye odaklanılması kafidir
* 🏃‍♂️ Hızlıca C\# öğrenmek için [CSharp Quick Guide](https://www.tutorialspoint.com/csharp/csharp_quick_guide.htm) sayfasına bakmalısın
* 👮‍♂️ Yazım standartları için [CSharp Coding Standarts](https://www.dofactory.com/reference/csharp-coding-standards) alanına da bakabilirsin

> 📃 C\# Hakkında bilgi için [C\# Quick Start](./assets/C#%20Quick%20Start.pdf) pdf notlarımı da inceleyebilirsin

![](../../.gitbook/assets/visual_studio_extension_development.png)

## 📹 Eği tici Video

Aşağıdaki video ile başlangıç seviyesi için hızlıca gerekli bilgileri öğrenebilirsin

{% embed url="https://channel9.msdn.com/Events/Build/2016/B886/player" %}

## 🏗️ VSIX Eklentisi Proje Yapısı

* `vcst` ve `vsixmanifest` dosyası `sync` edilmeli

![](../../.gitbook/assets/vsix_project_structure.png)

## 👨‍🔧 Proje İsmi Güncelleme

* `Solution Explorer` üzerinden `Properties` alanından güncellenir

![](../../.gitbook/assets/vsix_change_project_name.png)

## 🤖 VSIX Komutları için Guid Otomasyonu

* Aşağıdaki alanlar senkronize olan `vsct` c\# dosyasından çekilmelidir

```csharp
internal sealed class CompareHistoryCommand
{
    /// <summary>
    /// Command ID.
    /// </summary>
    public const int CommandId = PackageIds.CompareHistoryCommandId;

    /// <summary>
    /// Command menu group (command set GUID).
    /// </summary>
    public static readonly Guid CommandSet = PackageGuids.guidFile_VSPackageCmdSet;
// ...
}
```

## 🆔 VS SDK Menu ID'leri

* [GUIDs and IDs of Visual Studio menus](https://docs.microsoft.com/en-us/visualstudio/extensibility/internals/guids-and-ids-of-visual-studio-menus?view=vs-2019s)
* [IDE-Defined Commands for Extending Project Systems](https://docs.microsoft.com/en-us/visualstudio/extensibility/internals/ide-defined-commands-for-extending-project-systems?view=vs-2019s)

## 🖼️ VSIX için ikon ekleme

![](../../.gitbook/assets/vsix_known_monikers.png)

* 🌟 PNG dışındaki formatları da destekler ama PNG kullan
* 📦 VSIX'de 3000 icon vardır bunları kullanabilmek için [Extensibility Essentials 2019](https://marketplace.visualstudio.com/items?itemName=MadsKristensen.ExtensibilityEssentials2019) eklentisini indir
* ⚙️ View -&gt; Other Windows -&gt; KnownMoniker
* 📝 Çıkan panelde seçilen ikonu Resource içerisine alttak özelliklerle eklemeliyiz:
  * `16 width` ile  `*Command.png` icon dosyasını overwrite ederek
  * `175 width` ile `Preview` isimle
  * `90 width` ile `Icon` isimle
* 💦 `*.vsct` dosyası içerisinde **silmen gereken** kısımlar
  * `Bitmap` alanında `usedList` kısmındaki değerlerden ilki hariç diğerlerini
  * `GuidSymbol` alanındaki `IDSymbol` satırlarından ilki hariç diğerlerini
* ➕ Son eklenen resimleri projeye dahil etmek için `Solution Explorer` alanında  sağdan 3. ikon `Show all files` ile resimleri bulup, onları seçip `Include From Project` demeliyiz

![](../../.gitbook/assets/vsix_resources_example.png)



* 🔨 ```*.vsixmanifest`` dosyasına ikon ve ön izleme resmi eklenmeli

![](../../.gitbook/assets/vsix_manifest_res_icon.png)

## 

