---
description: Visual Studio 2019 eklentisini yönetme ve geliştirme
---

# 👨‍💼 Eklenti Yönetimi \| VSIX

## ❔ `.vsct` Dosyası Nedir

* Proje içerisindeki komutlar, resimler ve benzeri her bilişen bilgisi burada saklanır
* Tüm bileşenler birbirlerine ve kaynak kodlara guid değerleri ile bağlanır
* Proje içerisinde tek bir vsct dosyası bulunur

## 🆔 GUID Değerlerini Tanımlama

* Bileşen arasındaki bağlantılar için değişkenleri tanımlayan guid değerleri kullanılır
* Her guid değeri eşsiz olmak zorundadır
* `Symbols` alanı içerisinde ilk başta paket guid değeri tanımlanır
* `GuidSymbol` ile paket içerisindeki belirli guidler için alt değerler `IDSymbol` ile tanımlanır
  * usedList="1" için `IDSymbol` değeri `1` olan \`usedList="bmpPic1" aynıdır
  * `*CmdSet` isimli `GuidSymbol` değerleri, komut gruplarını işaretlemek için kullanılır
  * `*Images` olarak tanımlananlar ise resimler işaretlerler
* IDSymbol değeri `CommandId` ile bitenler komutların guid değerlerini temsil eder

```markup
<Symbols>
<!-- Paket bilgisi tutan değişken. -->
<GuidSymbol name="guidDesignDifferPackage" value="{97999930-ccf3-4150-8507-52957afe824c}" />

<!-- Menü komutlarını bir arada tutmak için kullanılan değişkenler. -->
<GuidSymbol name="guidFile_VSPackageCmdSet" value="{020df2a1-db50-4da9-b02d-429321000270}">
    <IDSymbol name="FileContextMenuGroup" value="0x110" />
    <IDSymbol name="EditorContextMenuGroup" value="0x120" />
    <IDSymbol name="DiffFilesCommandId" value="0x0100" />
    <IDSymbol name="CompareHistoryCommandId" value="0x0101" />
    <IDSymbol name="DiffContentCommandId" value="0x0102" />
</GuidSymbol>

<!-- Resimleri bağlamak için kullanılan değişkenler. -->
<GuidSymbol name="guidImages" value="{2a122da1-1d9a-48b8-89ff-ee6527567153}">
    <!-- Birden fazla resim içeren bir dosyadan istenen sıradaki resmi almak için kullanılır -->
    <IDSymbol name="firstImage" value="1" />
    <IDSymbol name="bmpDiff" value="2" />
</GuidSymbol>

<!-- İsteğe bağlı sabit değerler de kullanılabildiğinden değişkensiz resim işaretçisi tanımlanabilir -->
<GuidSymbol name="guidImages1" value="{ed02defe-f3bf-4cf7-913b-9772fffe8e26}"></GuidSymbol>
<GuidSymbol name="guidImages2" value="{1dd321f2-63ba-4bff-aee8-6f6d3995c650}"></GuidSymbol>
</Symbols>
```

## 👨‍💻 Komut Ekleme

* Komutlar `Commands` içeriside `Groups` objeleri içindeki `Group` değerleri ile derlenir
* `Group` içerisindeki `Parent` objelerindaki `id` değeri ile komutun nasıl çalışacağını ifade ederiz
  * `IDM_VS_CTXT_ITEMNODE` ile `Solution Explorer` üzerine sağ tıklandığında çıkan menüye eklenen komutları
  * `IDM_VS_CTXT_CODEWIN` ile editöre sağ tıklandığında çıkan menüdeki komutları
  * [GUIDs and IDs of Visual Studio menus](https://docs.microsoft.com/en-us/visualstudio/extensibility/internals/guids-and-ids-of-visual-studio-menus?view=vs-2019s)
  * [IDE-Defined Commands for Extending Project Systems](https://docs.microsoft.com/en-us/visualstudio/extensibility/internals/ide-defined-commands-for-extending-project-systems?view=vs-2019s)
* `priority` değeri ile grubun bulunacağı konum belirlenir, düşük değerler daha yukarıya alır

```markup
<Groups>
    <Group guid="guidFile_VSPackageCmdSet" id="FileContextMenuGroup" priority="0x0400">
        <Parent guid="guidSHLMainMenu" id="IDM_VS_CTXT_ITEMNODE" />
    </Group>
    <Group guid="guidFile_VSPackageCmdSet" id="EditorContextMenuGroup" priority="0x0300">
        <Parent guid="guidSHLMainMenu" id="IDM_VS_CTXT_CODEWIN" />
    </Group>
</Groups>
```

## 🔘 Buton Ekleme

* Butonlar `Buttons` alanına `GUID` değer ile eklenir
* Buton guid değeri paket guid değeri ile aynı olur
* `priority` değeri ile butonun bulunacağı konum belirlenir, düşük değerler daha yukarıya alır
* Parent alanı ile bağlı olduğu komut butonu guid değeri verilir
  * Bu sayede grup üzerindeki komutların davranışlarına uygun konumlanır
  * `IDM_VS_CTXT_ITEMNODE` id değerine sahip komut grubu için `Solution Explorer` üzerine sağ tıklandığında çıkan menüye ekleinir
* Icon alanı ile butonun sağında olan ikon guid ile belirlenir
  * `guid` ile ikon dosyasına `id` ile kaçıncı resmi almak istediğimizi belirtiriz
  * Resim indeksleri `0`'dan değil `1`'den başlar
  * İkonları tutmak için `Bitmaps` alnında guid değerli `Bitmap` objeleri kullanılır
  * `href` alanı temsil ettiği resim objenin yolunu tutar
  * `usedList` ile birden fazla resim içeren objelerden, hangi resimlerin alınacağını söyleriz
  * `usedList="1"` ile ilk resmi, `usedList="1, 2, 3"` ile ilk 3 resmi projeye dahil ederiz
* `Strings` alanında `ButtonText` ise butondaki metni temsil eder

```markup
<Buttons>
    <Button guid="guidFile_VSPackageCmdSet" id="DiffFilesCommandId" priority="0x0100" type="Button">
        <Parent guid="guidFile_VSPackageCmdSet" id="FileContextMenuGroup" />
        <Icon guid="guidImages" id="1" />
        <Strings>
            <ButtonText>Compare with file...</ButtonText>
        </Strings>
    </Button>
    <Button guid="guidFile_VSPackageCmdSet" id="CompareHistoryCommandId" priority="0x0100" type="Button">
        <Parent guid="guidFile_VSPackageCmdSet" id="FileContextMenuGroup" />
        <Icon guid="guidImages1" id="1" />
        <Strings>
            <ButtonText>Compare designer file with history...</ButtonText>
        </Strings>
    </Button>
    <Button guid="guidFile_VSPackageCmdSet" id="DiffContentCommandId" priority="0x0100" type="Button">
        <Parent guid="guidFile_VSPackageCmdSet" id="EditorContextMenuGroup" />
        <Icon guid="guidImages2" id="1" />
        <Strings>
            <ButtonText>Sort Windows Form Designer Generated Code</ButtonText>
        </Strings>
    </Button>
</Buttons>

<!-- guidImages değişkeninin GuidSymbol olarak tanımlanmış olmaları gerekmektedir -->
<Bitmaps>
    <Bitmap guid="guidImages" href="Resources\DiffFilesCommand.png" usedList="1" />
    <Bitmap guid="guidImages1" href="Resources\CompareHistoryCommand.png" usedList="1" />
    <Bitmap guid="guidImages2" href="Resources\DiffContentCommand.png" usedList="1" />
</Bitmaps>
```

## 🔌 Kaynak Koda Bağlama

* Komutların tetiklenmesi durumunda yapılacak eylemler kaynak kod tarafında `Execute` metodu içerisinde belirlenir
* Kaynak koda komutu bağlamak için `CommandSet` ve o küme içerisindeki `CommandId` değeri gerekir
  * `CommandSet`, `vsct` dosyası içerisinde `*CmdSet` olarak adlandırılan guid değerini alır
  * `CommandId` yukarıdaki guid içerisindeki hedeflenen komutun `IDSymbol` değerlerini alır
* Bu işlemi senkronize etmek ve her guid değişikliğinde güncellemekten kurtulmak için
  * `vsct` dosyasına sağ tıklayın ve `Syncronize code file` butonuna tıklayın
  * `PackageGuids` ve `PackageIds` içeren C\# `class` objeleri otomatik olarak tanımlacaktır 

![](../../.gitbook/assets/vsix_sync_manifest.png)

```csharp
namespace DesignerDiffer
{
    /// <summary>
    /// Command handler
    /// </summary>
    internal sealed class DiffContentCommand
    {
        /// <summary>
        /// Command ID.
        /// </summary>
        public const int CommandId = PackageIds.DiffContentCommandId;

        /// <summary>
        /// Command menu group (command set GUID).
        /// </summary>
        public static readonly Guid CommandSet = PackageGuids.guidFile_VSPackageCmdSet;

        /// <summary>
        /// VS Package that provides this command, not null.
        /// </summary>
        private readonly AsyncPackage package;

        // ...
    }
}
```

