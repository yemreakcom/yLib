# VsCode Özelleştirmem <!-- omit in toc -->

Özelleştirmelerin artık [Github Gist ☁](https://gist.github.com/yedhrab/4b13743a36cece5c3c22a5042897a83d) üzerine taşındı.

> [Settings Sync 🔄](https://marketplace.visualstudio.com/items?itemName=Shan.code-settings-sync) eklentisi ile online olarak yönetilebilmekte.

## İçerikler <!-- omit in toc -->

- [Snippets](#Snippets)
- [Editör Ayarlarım](#Edit%C3%B6r-Ayarlar%C4%B1m)
- [Klavye Kısayolları Ayarım](#Klavye-K%C4%B1sayollar%C4%B1-Ayar%C4%B1m)
- [Eklentilerim](#Eklentilerim)
- [Harici Bağlantılar](#Harici-Ba%C4%9Flant%C4%B1lar)

## Snippets

Verimli çalışmak için kod parçaları

<details>
<summary>Markdown snippets</summary>

````json
{
  // Place your snippets for markdown here. Each snippet is defined under a snippet name and has a prefix, body and
  // description. The prefix is what is used to trigger the snippet and the body will be expanded and inserted. Possible variables are:
  // $1, $2 for tab stops, $0 for the final cursor position, and ${1:label}, ${2:another} for placeholders. Placeholders with the
  // same ids are connected.
  // Example:
  // "Print to console": {
  // 	"prefix": "log",
  // 	"body": [
  // 		"console.log('$1');",
  // 		"$2"
  // 	],
  // 	"description": "Log output to console"
  // }
  "Insert head": {
    "prefix": "head",
    "body": [
      "# $1 <!-- omit in toc -->",
      "",
      "$2",
      "## İçerikler <!-- omit in toc -->",
      "",
      "$0"
    ],
    "description": "Markdown üst bilgisi ekleme"
  },
  "Omit": {
    "prefix": "om",
    "body": ["<!-- omit in toc -->"],
    "description": "Omit from ToC"
  },
  "Insert win key button": {
    "prefix": "kWin",
    "body": ["<kbd>❖ Win</kbd>$0"]
  },
  "Insert tab key button": {
    "prefix": "kTab",
    "body": ["<kbd>⭾ Tab</kbd>$0"]
  },
  "Insert shift key button": {
    "prefix": "kShift",
    "body": ["<kbd>⇧ Shift</kbd>$0"]
  },
  "Insert enter key button": {
    "prefix": "kEnter",
    "body": ["<kbd>↩ Enter</kbd>$0"]
  },
  "Insert arrow key button": {
    "prefix": "kArrow",
    "body": ["<kbd>↑ ↓ ← → Arrow</kbd>$0"]
  },
  "Insert esc key button": {
    "prefix": "kEsc",
    "body": ["<kbd>⎋ Esc</kbd>$0"]
  },
  "Insert 1 button key": {
    "prefix": "k1",
    "body": ["<kbd>$1</kbd>$0"],
    "description": "1 Buton anahtarı oluşturur"
  },
  "Insert 2 button key": {
    "prefix": "k2",
    "body": ["<kbd>$1</kbd> <kbd>$2</kbd>$0"],
    "description": "2 Buton anahtarı oluşturur"
  },
  "Insert 3 button key": {
    "prefix": "k3",
    "body": ["<kbd>$1</kbd> <kbd>$2</kbd> <kbd>$3</kbd>$0"],
    "description": "3 Buton anahtarı oluşturur"
  },
  "Insert toggle menu": {
    "prefix": "menu",
    "body": [
      "<details>",
      "<summary>$1</summary>",
      "",
      "$2",
      "",
      "</details>",
      "",
      "$0"
    ],
    "description": "3 Buton anahtarı oluşturur"
  },
  "Insert code": {
    "prefix": "code",
    "body": ["```$1", "$2", "```", "$0"],
    "description": "Kod parçası ekler"
  },
  "Insert toggle code menu": {
    "prefix": "code-menu",
    "body": [
      "<details>",
      "<summary>$1</summary>",
      "",
      "```$2",
      "$3",
      "```",
      "",
      "</details>",
      "",
      "$0"
    ],
    "description": "Açılır kod menüsü ekler"
  },
  "Insert code block": {
    "prefix": "code-block",
    "body": [
      "##$1",
      "",
      "$2",
      "",
      "<details>",
      "<summary>$3</summary>",
      "",
      "```$4",
      "$5",
      "```",
      "",
      "</details>",
      "",
      "$0"
    ],
    "description": "Kod bloğu oluşturur"
  }
}
````

</details>

## Editör Ayarlarım

<details>
<summary>Ayaları göster</summary>

```json
{
  // Tasarım ve arayüz ayarları
  "workbench.iconTheme": "material-icon-theme",
  "workbench.colorTheme": "DarkCode Theme Adopted Python and Markdown",
  "window.menuBarVisibility": "toggle",
  // Terminal ayarları
  "terminal.integrated.cursorStyle": "line",
  // Gizlilik ayarları
  "telemetry.enableTelemetry": false,
  "telemetry.enableCrashReporter": false,
  // Editör ayarları
  "editor.formatOnSave": true,
  "editor.minimap.enabled": false,
  "editor.cursorBlinking": "phase", // İmleç yanıp sönmesi
  "files.insertFinalNewline": true, // Dosyaların sonuna boş satır koyar
  // Font Ayarları https://github.com/tonsky/FiraCode/releases/download/1.206/FiraCode_1.206.zip
  "editor.fontFamily": "Fira Code Retina, 'Droid Sans Mono', 'monospace', monospace, 'Droid Sans Fallback'", // Linux fontu: Droid Sans Mono
  "editor.fontLigatures": true,
  "editor.fontSize": 13.1,
  // Terminal ayarlarım
  "terminal.integrated.fontSize": 13,
  "terminal.integrated.fontFamily": "Consolas",
  "terminal.integrated.shell.windows": "C:\\Program Files\\Git\\usr\\bin\\bash.exe",
  // Satır uzunluğu ayarı
  "editor.wordWrap": "bounded",
  "editor.wordWrapColumn": 200,
  // Formatlama ayarları
  "[python]": {
    "editor.defaultFormatter": "ms-python.python"
  },
  "[javascript]": {
    "editor.defaultFormatter": "esbenp.prettier-vscode"
  },
  // Dosya işlemleri ayarları
  "explorer.confirmDragAndDrop": false,
  "explorer.confirmDelete": false,
  // Git ayarları
  "git.confirmSync": false,
  "git.autofetch": false,
  // Github ayarları
  "github.username": "yedhrab",
  // Python ayarları
  "python.jediEnabled": false,
  "python.formatting.provider": "autopep8",
  // Pano'dan resim kopyalam ayarı
  "pasteImage.path": "${projectRoot}/res",
  // Todo-Tree ayarları
  "todo-tree.tags": ["TODO:", "BUG:", "DEV:", "RES:", "OLD:", "WARN:", "TIP:"],
  "todo-tree.labelFormat": "${after}", // (${line})
  "todo-tree.grouped": true,
  "todo-tree.tagsOnly": true,
  "todo-tree.excludeGlobs": ["**/*.json"],
  "todo-tree.defaultHighlight": {
    "icon": "tasklist",
    "type": "text",
    "background": "#6FA5FF",
    "opacity": 17,
    "iconColour": "#6FA5FF"
  },
  "todo-tree.customHighlight": {
    // TIP: Bilgiler (tip)
    "TIP:": {
      "icon": "book",
      "type": "text",
      "foreground": "#f5f2a9",
      "background": "#f5f2a9",
      "opacity": 7,
      "iconColour": "#f5f2a9"
    },
    // TODO:: Yapılacak (todo)
    "TODO:": {
      "icon": "checklist",
      "type": "text",
      "fontStyle": "normal",
      "foreground": "#6FA5FF",
      "background": "#6FA5FF",
      "opacity": 7,
      "iconColour": "#6FA5FF"
    },
    // BUG: Hatalar (bug)
    "BUG:": {
      "icon": "bug",
      "type": "text",
      "foreground": "#FF2C2C",
      "background": "#FF2C2C",
      "opacity": 7,
      "iconColour": "#FF2C2C"
    },
    // DEV: İyileştirme, geliştirme (dev)
    "DEV:": {
      "icon": "telescope",
      "type": "text",
      "foreground": "#72CB6A",
      "background": "#72CB6A",
      "opacity": 7,
      "iconColour": "#72CB6A"
    },
    // RES: Gelecek planları, araştırmalar (res)
    "RES:": {
      "icon": "beaker",
      "type": "text",
      "foreground": "#9CF7FF",
      "background": "#9CF7FF",
      "opacity": 7,
      "iconColour": "#9CF7FF"
    },
    // WARN: Uyarılar (warn)
    "WARN:": {
      "icon": "megaphone",
      "type": "text",
      "foreground": "#CFCC35",
      "background": "#CFCC35",
      "opacity": 7,
      "iconColour": "#CFCC35"
    },
    // OLD: Eskimiş, kaldırılacak (deprecated)
    "OLD:": {
      "icon": "trashcan",
      "type": "text",
      "foreground": "#959595",
      "background": "#959595",
      "opacity": 7,
      "iconColour": "#959595"
    }
  },
  // Markdown PDF ayarları
  "markdown.extension.toc.downcaseLink": false,
  "markdown-pdf.outputDirectory": "Dökümanlar",
  "markdown-pdf.styles": ["http://tiny.cc/yek86y"],
  "markdown-pdf.headerTemplate": "<div style=\"width: 100%; font-size: 7px; margin: 0 auto; font: Segoe UI Light; text-align: center;\"><div style=\"float: left; width: 33.33%;\"><a style='text-decoration: none; font: Risque; color: red;' href='https://gogetfunding.com/yemreak/'>Destek ❤</a></div><div style=\"float: left; width: 33.33%;\"><a style='text-decoration: none; color: navy;' href='https://www.yemreak.com'>The MIT License Copyright &copy; Yunus Emre Ak</a></div><div style=\"float: left; font-size: 7px; width: 33.33%; color: gainsboro;\"><span class='date'></span></div></div>",
  "markdown-pdf.footerTemplate": "<div style=\"width: 100%; font-size: 7px; margin: 0 auto; font: Segoe UI Light\"> <div style=\"float: left; width: 20%; text-align: center\"><a style=\"text-decoration: none; display: inline-block; color: dodgerblue;\" href=\"https://yemreak.com\">Website</a></div><div style=\"float: left; width: 20%; text-align: center\"><a style=\"text-decoration: none; display: inline-block; color: dodgerblue;\" href=\"https://github.com/yedhrab \">Github</a></div><div style=\"float: left; width: 20%; text-align: center\"><span class=\"pageNumber \">3 </span> / <span class=\"totalPages \"> 5</span></div><div style=\"float: left; width: 20%; text-align: center\"><a style=\"text-decoration: none; display: inline-block; color: dodgerblue;\" href=\"https://www.linkedin.com/in/yemreak/\">LinkedIn</a></div><div style=\"float: left; width: 20%; text-align: center\"><a style=\"text-decoration: none; display: inline-block; color: dodgerblue;\" href=\"mailto::yedhrab@gmail.com?subject=YPDF%20%7C%20Github\">İletişim</a></div></div>"
}
```

</details>

## Klavye Kısayolları Ayarım

<details>
<summary>Windows 10</summary>

```json
// Place your key bindings in this file to override the defaults
[
  {
    "key": "ctrl+oem_7 ctrl+oem_7",
    "command": "git.sync"
  },
  {
    "key": "ctrl+j",
    "command": "workbench.action.terminal.toggleTerminal"
  },
  {
    "key": "ctrl+j",
    "command": "-workbench.action.togglePanel"
  },
  {
    "key": "alt+v",
    "command": "extension.pasteImage",
    "when": "editorTextFocus"
  },
  {
    "key": "ctrl+alt+v",
    "command": "-extension.pasteImage",
    "when": "editorTextFocus"
  },
  {
    "key": "ctrl+shift+oem_7",
    "command": "workbench.view.extension.todo-tree-container"
  }
]
```

</details>

<details>
<summary>Linux</summary>

```json
[
  {
    "key": "ctrl+[KeyI] ctrl+[KeyI]",
    "command": "git.sync"
  },
  {
    "key": "ctrl+[KeyI] ctrl+p",
    "command": "git.pull"
  },
  {
    "key": "ctrl+shift+[KeyI] ctrl+shift+p",
    "command": "git.pullFrom"
  },
  {
    "key": "ctrl+[KeyI] ctrl+o",
    "command": "git.checkout"
  },
  {
    "key": "ctrl+j",
    "command": "workbench.action.terminal.toggleTerminal"
  },
  {
    "key": "ctrl+j",
    "command": "-workbench.action.togglePanel"
  },
  {
    "key": "ctrl+meta+left",
    "command": "workbench.action.moveEditorToLeftGroup"
  },
  {
    "key": "ctrl+meta+right",
    "command": "workbench.action.moveEditorToRightGroup"
  },
  {
    "key": "ctrl+meta+up",
    "command": "workbench.action.moveEditorToAboveGroup"
  },
  {
    "key": "ctrl+meta+down",
    "command": "workbench.action.moveEditorToBelowGroup"
  }
]
```

</details>

## Eklentilerim

<details>
<summary>Eklenti indirme komutunu göster</summary>

```code
code \
  --install-extension yedhrab.darkcode-theme-adopted-python-and-markdown \
  --install-extension yzhang.markdown-all-in-one \
  --install-extension yzane.markdown-pdf \
  --install-extension bierner.markdown-preview-github-styles \
  --install-extension pkief.material-icon-theme \
  --install-extension mushan.vscode-paste-image \
  --install-extension esbenp.prettier-vscode \
  --install-extension wakatime.vscode-wakatime \
  --install-extension ms-vscode.github-issues-prs \
  --install-extension mikestead.dotenv \
  --install-extension Gruntfuggly.todo-tree \
  --install-extension foxundermoon.shell-format \
  --install-extension ms-python.python
```

![ex_output](../../res/ex_output.png)

</details>

## Harici Bağlantılar

- [Faydalı eklentiler](https://nickjanetakis.com/blog/my-favorite-vscode-extensions-and-settings)
