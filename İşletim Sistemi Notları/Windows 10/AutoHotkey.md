---
description: Windows üzerinde kişisel kısayolları ve scriptleri oluşturmaya olanak sağlar.
---

# 💫 AutoHotkey

## 🗽 Açıklama

- Çok stabil çalışmaktadır, windows'un kendi içindeki kısayol sisteminden daha verimlidir
- VsCode üzerinden script yazacaksanız [AutoHotkey](https://marketplace.visualstudio.com/items?itemName=slevesque.vscode-autohotkey) eklentisini indirmeniz tavsiye edilir

> Windows 10'da denenmiştir.

## Pencere Açma, Açıksa Gizleme

- `WinName` alanına kendi pencere isminizi yazmayı unutmayın.
- Bu örnek mesajlaşma uygulamarını tek platformda sunan [Rambox](https://rambox.pro/) için kısayoldur

```ahk
#SingleInstance Force

SetTitleMatchMode, 2

ShowWin(windowName, url) {
    IfWinExist, %windowName%
    {
        WinGet, WinState, MinMax 
        if (WinState = -1)
            WinRestore
        else 
            WinMinimize
    }
    else
        Run, %url%
    return
}

;windowName=%A_ScriptName%
return

!w::
    ShowWin("Rambox", "C:\Program Files\Rambox\Rambox.exe")
    return
```

> [Minimize and Restore Window with one command](https://autohotkey.com/board/topic/49207-minimize-and-restore-window-with-one-command/?p=306623)
