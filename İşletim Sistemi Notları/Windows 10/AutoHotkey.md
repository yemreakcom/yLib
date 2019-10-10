---
description: Windows üzerinde kişisel kısayolları ve scriptleri oluşturmaya olanak sağlar.
---

# 💫 AutoHotkey

## 🗽 Açıklama

- Çok stabil çalışmaktadır, windows'un kendi içindeki kısayol sisteminden daha verimlidir
- VsCode üzerinden script yazacaksanız [AutoHotkey](https://marketplace.visualstudio.com/items?itemName=slevesque.vscode-autohotkey) eklentisini indirmeniz tavsiye edilir

> Windows 10'da denenmiştir.


## Kısayol Tanımlamaları

| Symbol | Description                                                                                          |
| ------ | ---------------------------------------------------------------------------------------------------- |
| `#`    | Win (Windows logo key)                                                                               |
| `!`    | Alt                                                                                                  |
| `^`    | Control                                                                                              |
| `+`    | Shift                                                                                                |
| `&`    | An ampersand may be used between any two keys or mouse buttons to combine them into a custom hotkey. |

> [Kısayol Tanımlamaları](https://www.autohotkey.com/docs/Tutorial.htm#s21)
## Hızlı Notlar

| Komut                                                                               | Açıklama                               |
| ----------------------------------------------------------------------------------- | -------------------------------------- |
| [SetTitleMatchMode](https://www.autohotkey.com/docs/commands/SetTitleMatchMode.htm) | Pencere başlığındaki isimlerin alınışı |

## Pencere Açma, Açıksa Gizleme

- `WinName` alanına kendi pencere isminizi yazmayı unutmayın.

> Bu örnek mesajlaşma uygulamarını tek platformda sunan [Rambox](https://rambox.pro/) için kısayolunu da içerir

```ahk
#SingleInstance Force

SetTitleMatchMode, 2

ToggleWindow(windowName)
{   
    WinGet, WinState, MinMax, %windowName%
    if (WinState == -1)
    {
        WinRestore, %windowName%
        WinActivate, %windowName%
    }
    else
    {
        WinMinimize, %windowName%
    }
}

ShowWin(windowName, url) 
{   
    IfWinExist, %windowName%
    {
        ToggleWindow(windowName)
    }
    else
        Run, %url%
    return
}

;windowName=%A_ScriptName%
return

#w::
    ShowWin("Rambox", "C:\ProgramData\chocolatey\lib\rambox\tools\Rambox.exe")
    return
#q::
    ShowWin("- OneNote", "shell:appsFolder\Microsoft.Office.OneNote_8wekyb3d8bbwe!microsoft.onenoteim")
    return
#t::
    ShowWin("Tureng", "shell:appsFolder\24232AlperOzcetin.Tureng_9n2ce2f97t3e6!App")
    return
#+t::
    ShowWin("Trello", "shell:appsFolder\45273LiamForsyth.PawsforTrello_7pb5ddty8z1pa!trello")
    return

```

> [Minimize and Restore Window with one command](https://autohotkey.com/board/topic/49207-minimize-and-restore-window-with-one-command/?p=306623)
