---
description: VsCode üzerinde tanımlı olan değişkenler
---

# 💎 Değişkenler \| VS Code

## 💎 Predefined variables

The following predefined variables are supported:

* **${workspaceFolder}** - the path of the folder opened in VS Code
* **${workspaceFolderBasename}** - the name of the folder opened in VS Code without any slashes \(/\)
* **${file}** - the current opened file
* **${relativeFile}** - the current opened file relative to `workspaceFolder`
* **${relativeFileDirname}** - the current opened file's dirname relative to `workspaceFolder`
* **${fileBasename}** - the current opened file's basename
* **${fileBasenameNoExtension}** - the current opened file's basename with no file extension
* **${fileDirname}** - the current opened file's dirname
* **${fileExtname}** - the current opened file's extension
* **${cwd}** - the task runner's current working directory on startup
* **${lineNumber}** - the current selected line number in the active file
* **${selectedText}** - the current selected text in the active file
* **${execPath}** - the path to the running VS Code executable
* **${defaultBuildTask}** - the name of the default build task

## ⭐ Predefined variables examples

Supposing that you have the following requirements:

1. A file located at `/home/your-username/your-project/folder/file.ext` opened in your editor;
2. The directory `/home/your-username/your-project` opened as your root workspace.

So you will have the following values for each variable:

* **${workspaceFolder}** - `/home/your-username/your-project`
* **${workspaceFolderBasename}** - `your-project`
* **${file}** - `/home/your-username/your-project/folder/file.ext`
* **${relativeFile}** - `folder/file.ext`
* **${relativeFileDirname}** - `folder`
* **${fileBasename}** - `file.ext`
* **${fileBasenameNoExtension}** - `file`
* **${fileDirname}** - `/home/your-username/your-project/folder`
* **${fileExtname}** - `.ext`
* **${lineNumber}** - line number of the cursor
* **${selectedText}** - text selected in your code editor
* **${execPath}** - location of Code.exe

> **Tip**: Use IntelliSense inside string values for `tasks.json` and `launch.json` to get a full list of predefined variables.

## 🔗 Faydalı Bağlantılar

{% embed url="https://code.visualstudio.com/docs/editor/variables-reference" %}

