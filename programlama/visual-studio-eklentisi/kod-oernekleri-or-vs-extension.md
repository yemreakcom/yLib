# 👨‍💻 Kod Örnekleri \| VS Extension

## 📃 VSIX Aktif Dokümanın İçeriğini Alma

```csharp
protected DTE2 dte;
dte2 = (EnvDTE80.DTE2)GetService(typeof(EnvDTE.DTE));

public string GetCurrentTextFile(){

  TextDocument doc = (TextDocument)(dte.ActiveDocument.Object("TextDocument"));
  var p = doc.StartPoint.CreateEditPoint();
  string s = p.GetText(doc.EndPoint);

  return s;            
}
```

## 🚄 Editör Üzerindeki Seçili Metni Sıralama

```csharp
using EnvDTE80;

var dte = await ServiceProvider.GetServiceAsync(typeof(DTE)).ConfigureAwait(false) as DTE2 ?? throw new NullReferenceException("DTE alınamadı");
EnvDTE.TextSelection ts = dte.ActiveWindow.Selection as EnvDTE.TextSelection;
if (ts == null)
    return;

string[] selectedLines = ts.Text.Split('\n');
selectedLines = selectedLines.OrderBy(p => p).ToArray();
ts.Text = string.Join("\n", selectedLines);
```

{% hint style="info" %}
‍🧙‍♂Detaylı bilgi için [YEmoji](https://emoji.yemreak.com/kullanim/baglantilar) yapısına uygun oluşturulmuş:

* [👪 How to get selected text of visual studio 2015 editor windows?](https://stackoverflow.com/a/40508224)
* [👨‍💻 Read a text file and sort in C\#](https://gist.github.com/Ellyll/7716439)

alanlarına bakabilirsin.
{% endhint %}

## 📂 Editör Üzerindeki Seçili Metnin içerisindeki Method İçeriğini Sıralama

```csharp
using EnvDTE80;

var dte = await ServiceProvider.GetServiceAsync(typeof(DTE)).ConfigureAwait(false) as DTE2 ?? throw new NullReferenceException("DTE alınamadı");

EnvDTE.TextSelection ts = dte.ActiveWindow.Selection as EnvDTE.TextSelection;
if (ts == null)
    return;
EnvDTE.CodeFunction func = ts.ActivePoint.CodeElement[vsCMElement.vsCMElementFunction] as EnvDTE.CodeFunction;
if (func == null)
    return;

// Func içerğini al -> sırala -> güncelle
string selectedCodeText = func.GetStartPoint(vsCMPart.vsCMPartBody).CreateEditPoint().GetText(func.EndPoint);
selectedCodeText = string.Join("\n", selectedCodeText.Split('\n').OrderBy(p => p));
func.GetStartPoint(vsCMPart.vsCMPartBody).CreateEditPoint().ReplaceText(func.EndPoint, selectedCodeText, (int) vsEPReplaceTextOptions.vsEPReplaceTextAutoformat);
```

{% hint style="info" %}
‍🧙‍♂Detaylı bilgi için [YEmoji](https://emoji.yemreak.com/kullanim/baglantilar) yapısına uygun oluşturulmuş:

* [👪 vs2010 automation : Get the text value of a EnvDTE.CodeElement](https://stackoverflow.com/a/21463351)
* [👪 Get function body programatically using Automation](https://social.msdn.microsoft.com/Forums/en-US/542a3756-6d6e-4744-a035-fc7238203857/get-function-body-programatically-using-automation?forum=vsxs)

alanlarına bakabilirsin.
{% endhint %}

## 📂 Aktif Dokümandaki Üretilen Kodları Sıralama

```csharp
using EnvDTE80;

private async void Execute(object sender, EventArgs e) {
    DTE2 dte = await Utility.GetDTE2Async(ServiceProvider);
    ProjectItem tempProjectItem = dte2.ItemOperations.AddExistingItem(tempFilePath);
    if (Utility.SortFunctionBodyIfExist(tempProjectItem.FileCodeModel, Utility.GeneratedFunctionName))
    {
        tempProjectItem.Save();
        string oldFilePath = filePath.Replace(selectedProjectItem.Name, tempProjectItem.Name);
        Utility.DiffFiles(dte2, oldFilePath, filePath);
    }
}

public static async Task<DTE2> GetDTE2Async(IAsyncServiceProvider asyncServiceProvider) => await asyncServiceProvider.GetServiceAsync(typeof(DTE)).ConfigureAwait(false) as DTE2 ?? throw new NullReferenceException("DTE alınamadı");

public static bool SortFunctionBodyIfExist(FileCodeModel fcm, string funcName)
{
    ThreadHelper.ThrowIfNotOnUIThread();
    if (IsFuncExistInFileCodeModel(fcm, funcName, out CodeFunction cf))
    {
        SortFunctionBody(cf);
        return true;
    }
    return false;
}

public static bool IsFuncExistInFileCodeModel(FileCodeModel fcm, string name, out CodeFunction cf)
{
    ThreadHelper.ThrowIfNotOnUIThread();
    return IsFuncExistInCodeElements(fcm.CodeElements, name, out cf);
}

public static void SortFunctionBody(CodeFunction cf)
{
    ThreadHelper.ThrowIfNotOnUIThread();
    string generatedCode = GetFunctionBodyText(cf);
    generatedCode = StripComments(generatedCode);
    generatedCode = SortContentBy(generatedCode, '\n');
    ReplaceFunctionBodyText(generatedCode, cf);
}

public static bool IsFuncExistInCodeElements(CodeElements codeElements, string name, out CodeFunction cf)
{
    ThreadHelper.ThrowIfNotOnUIThread();
    foreach (CodeElement element in codeElements)
    {
        if (element is CodeNamespace)
        {
            CodeNamespace nsp = element as CodeNamespace;

            foreach (CodeElement subElement in nsp.Children)
            {
                if (subElement is CodeClass)
                {
                    CodeClass c2 = subElement as CodeClass;
                    foreach (CodeElement item in c2.Children)
                    {
                        if (item is CodeFunction)
                        {
                            CodeFunction _cf = item as CodeFunction;
                            if (_cf.Name == name)
                            {
                                cf = _cf;
                                return true;
                            }
                        }
                    }
                }
            }
        }
    }
    cf = null;
    return false;
}
```

{% hint style="info" %}
‍🧙‍♂ Detaylı bilgi için  [👪 Get current source file methods in Visual Studio Text Editor Extension](https://stackoverflow.com/a/45181583) sayfasına bakabilirsin
{% endhint %}

## ♊ İki Dosya Arasındaki Farklılıkları Gösterme

* 💾 Dosyayı geçici dizine aynı uzantı ve ismle kayıt ediyoruz
* 🧰 Ardından `Tool.DiffFiles` komutu ile geçici dizindeki ile orjinal dosyayı karşılaştırıyoruz

```csharp
string[] splitFilepath = filepath.Split('\\');
string bareFilename = splitFilepath[splitFilepath.Length - 1];
string tempFilepath = System.IO.Path.GetTempPath() + bareFilename;
System.IO.File.WriteAllText(tempFilepath, fileContent, System.Text.Encoding.UTF8);
dte2.ExecuteCommand("Tools.DiffFiles", $"\"{tempFilepath}\" \"{filepath}\"");
```

## 🔀 Git Komutu Çalıştırma

### 🚩 Proje dizinini ve dosya yolunu alma

```csharp
string filepath = "...";
string solutionDir = System.IO.Path.GetDirectoryName(dte2.Solution.FullName);
filepath = filepath.Replace($"{solutionDir}\\", "").Replace("\\", "/");
```

{% hint style="info" %}
‍🧙‍♂ Detaylı bilgi için [👪 How do you get the current solution directory from a VSPackage?](https://stackoverflow.com/a/2338796s)alanına bakabilirsin.
{% endhint %}

### 🧵 Git process oluşturma

```csharp
static System.Diagnostics.Process GitProcess(string arguments, string workdir)
{
    return new System.Diagnostics.Process
    {
        StartInfo = {
            FileName = "git.exe",
            WorkingDirectory = workdir,
            Arguments = $"--no-pager {arguments}",
            RedirectStandardOutput = true,
            UseShellExecute = false,
            CreateNoWindow = true
        },
        EnableRaisingEvents = true
    };
}
```

### 👀 Git Çıktısını Okuma

```csharp
string fileContent = "";
gitProcess.Start();
while (!gitProcess.StandardOutput.EndOfStream)
{
    string line = gitProcess.StandardOutput.ReadLine();
    fileContent += line + "\n";
}
```

{% hint style="info" %}
‍🧙‍♂ Detaylı bilgi için [YEmoji](https://emoji.yemreak.com/kullanim/baglantilar) yapısına uygun oluşturulmuş:

* [👪 Process.start: how to get the output?](https://stackoverflow.com/a/4291965)
* [👪 Is there any async equivalent of Process.Start?](https://stackoverflow.com/a/10789196s)

alanlarına bakabilirsin.
{% endhint %}

## 👨‍💻 Dosyadan `FileCodeModel` Oluşturma

* 💡 Öncelikle stack overflow üzerindeki cevabım [buradadır](https://stackoverflow.com/a/63694341/9770490)
* 👮‍♂️ Visual Studio içerisinde açılan proje dosyalarının `FileCodeModel` objesine erişilebilir
* 🗃️ `dte.ItemOperations.OpenFile` ile açılan dosyalar, `Miscellaneous` olarak gözükür, `ProjectItem` değildir
* 📂 Dosyayı `ProjectItem` olarak açmak için `dte.ItemOperations.AddExistingItem(filePath);` kodu kullanılır
* 👨‍💻 Eklenen dosyanın `FileCodeModel` içeriğine `projectItem.FileCodeModel` şeklinde erişiriz
* İsteğe bağlı olarak`ProjectItem.Delete()` ile eklenen dosya kaldırılabilir

```csharp
using EnvDTE;

public static async Task<DTE2> GetDTE2Async(IAsyncServiceProvider asyncServiceProvider) => await asyncServiceProvider.GetServiceAsync(typeof(DTE)).ConfigureAwait(false) as DTE2 ?? throw new NullReferenceException("DTE alınamadı");

string filepath = "TODO";
DTE2 dte2 = await Utility.GetDTE2Async(asyncServiceProvider);
ProjectItem projectItem = dte2.ItemOperations.AddExistingItem(filepath);
FileCodeModel fcm = projectItem.FileCodeModel;
projectItem.Delete();
```

{% hint style="info" %}
‍🧙‍♂ Detaylı bilgi için [YEmoji](https://emoji.yemreak.com/kullanim/baglantilar) yapısına uygun oluşturulmuş:

* [👪 How do I programmatically add a file to a Solution?](https://stackoverflow.com/a/11934026/9770490s)
* [📃 FileCodeModel null for file in "Misc Files" project. ~ Windows Tech](http://www.windows-tech.info/4/004ffb867c3564c0.php)
* [👪 FileCodeModel null for file in "Misc Files" project. ~ Microsoft](https://social.msdn.microsoft.com/Forums/sqlserver/en-US/925a2ba3-728b-4bfd-8802-091ef258eace/filecodemodel-null-for-file-in-misc-files-project?forum=vsx)

alanlarına bakabilirsin.
{% endhint %}

