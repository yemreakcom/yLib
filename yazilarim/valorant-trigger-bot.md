---
description: >-
  Valorant için çalışan ve sarı rengi gördüğü anda mouse sol tıklaması yapan
  AutoHotkey Scripti
---

# 🤖 Valorant Trigger Bot

## 📒 Temel Bilgiler

* Trigger bot; imleç rakibin üstüne geldiğinde otomatik olarak sol mouse tıklaması eylemini yaptıran scirpt demektir
* HWID Ban; Hardware ID ile ceza yemektir ve donanım ID'niz oyun sunucusu tarafından kaydedilir, aynı ID ile giriş yapıldığında sizin giriş yapmanıza izin vermez
* Spoofer; Donanım ID değerlerini değiştiren yazılımlara verilen isimdir ve bununla HWID ban kısıtlamasından kurtulunabilir

> 💁‍♂️ Bunları neden anlattım? Nelerle karşılaşabileceğini bilmen için

{% embed url="https://www.youtube.com/watch?v=1xSk90CbrhQ" %}
Valorant Trigger Bot
{% endembed %}

## 👨‍💼 Nasıl Kullanılır?

* Valorant Trigger Bot'u AHK scripti olduğunda öncelikle [AutoHotkey](https://www.autohotkey.com/download/?) indirmeniz gerekir
  * İlgilenenler için AutoHotkey, windows için scripting yazılımıdır
* Scriptin düzgün çalışması için, Valorant ayalarınnda **düşman rengini Sarı (Yeşil)** olarak ayarlamalısın
* **F2** tuşuna basıldığında aktif edilir, **F3** ile NoRecoil aktif edebilirsiniz **F4** ile NoRecoil'i kapatabilirsin

{% hint style="warning" %}
Script kullanırken herhangi bir şikayet ile HWID ban yeme durumunda sorumluluk sana aittir
{% endhint %}



## ⤵️ İndirme Bağlantısı

* Scripti  [buradan](https://cdn.discordapp.com/attachments/984172852133650472/988746276143267840/OvnitovenkHEK.ahk) indirebilirsiniz
* Direkt olarak alttaki kodları txt dosyasına kaydedip, uzantısını `ahk` olarak güncelleyebilirsiniz. (örn OvnitovenkHEK.ahk)

{% hint style="warning" %}
🕵️ Script kendi kodlamış olduğum bir içerik değildir, alıntıdır!
{% endhint %}

```
init:
#NoEnv
#SingleInstance, Force
#Persistent
#InstallKeybdHook
#UseHook
#KeyHistory, 0
#HotKeyInterval 1
#MaxHotkeysPerInterval 127
MsgBox, ,, Ornitorenk discord.gg/7C3y9zS
if (FileExist("config.ini")) 
{
}
Else
{
IniWrite, 0xA5A528, config.ini, main, EMCol
IniWrite, 20, config.ini, main, ColVn
}

IniRead, EMCol, config.ini, main, EMCol
IniRead, ColVn, config.ini, main, ColVn


toggle = 1
toggle2 = 1


AntiShakeX := (A_ScreenHeight // 160)
AntiShakeY := (A_ScreenHeight // 128)
ZeroX := (A_ScreenWidth // 2) ;dont touch?
ZeroY := (A_ScreenHeight // 2) 
CFovX := (A_ScreenWidth // 40)  ;configure for FOV up = smaller lower= bigger current boxes right fov
CFovY := (A_ScreenHeight // 64)
ScanL := ZeroX - CFovX
ScanT := ZeroY
ScanR := ZeroX + CFovX
ScanB := ZeroY + CFovY
NearAimScanL := ZeroX - AntiShakeX
NearAimScanT := ZeroY - AntiShakeY
NearAimScanR := ZeroX + AntiShakeX
NearAimScanB := ZeroY + AntiShakeY



~F2::

SetKeyDelay,-1, 1
SetControlDelay, -1
SetMouseDelay, -1
SetWinDelay,-1
SendMode, InputThenPlay
SetBatchLines,-1
ListLines, Off
CoordMode, Pixel, Screen, RGB
CoordMode, Mouse, Screen
PID := DllCall("GetCurrentProcessId")
Process, Priority, %PID%, High


Loop{
 
PixelSearch, AimPixelX, AimPixelY, NearAimScanL, NearAimScanT, NearAimScanR, NearAimScanB, EMCol, ColVn, Fast RGB	
 
		if GetKeyState("Shift"){
		if (ErrorLevel=0) {
		PixelSearch, AimPixelX, AimPixelY, NearAimScanL, NearAimScanT, NearAimScanR, NearAimScanB, EMCol, ColVn, Fast RGB
		loop , 1{
		send {Lbutton down}
		sleep, 10
		send {lbutton up}
						}
					}
				}
						
 
		if GetKeyState("LButton") {
		if (ErrorLevel=0) {
		if _recoil
			{
			mouseXY(0, 1) ;change the norecoil amount while aiming at target
			DllCall("mouse_event", uint, 2, int, x, int, y, uint, 0, int, 0)
			}
			}
		}
						
						
		if GetKeyState("LButton") {
		if (!ErrorLevel=0) {
		loop, 10 {
			PixelSearch, AimPixelX, AimPixelY, ScanL, ScanT, ScanR, ScanB, EMCol, ColVn, Fast RGB
			AimX := AimPixelX - ZeroX
			AimY := AimPixelY - ZeroY
			DirX := -1
			DirY := -1
			If ( AimX > 0 ) {
				DirX := 1
			}
			If ( AimY > 0 ) {
				DirY := 1
			}
			AimOffsetX := AimX * DirX
			AimOffsetY := AimY * DirY
			MoveX := Floor(( AimOffsetX ** ( 1 / 2 ))) * DirX
			MoveY := Floor(( AimOffsetY ** ( 1 / 2 ))) * DirY
			DllCall("mouse_event", uint, 1, int, MoveX * 0.7, int, MoveY, uint, 0, int, 0) ;turing mouse to color were it says * is the speed of the aimbot turn up for unhuman reactions lower for human
			if _recoil
			{
			mouseXY(0, 1) ;change the nocrecoil amount while not aiming at target
			DllCall("mouse_event", uint, 1, int, x, int, y, uint, 0, int, 0)
			}
			}
			}
			}
		}~F3::_recoil = true	
 
 
~F4::_recoil = false
	
	
~F5::
_auto := true
 
~LButton::autofire()
Numlock::_auto := ! _auto
F1::ExitApp
 
autofire()
{
global _auto
if _auto
{
Loop
{
if GetKeyState("LButton", "P")
{
SendInput {LButton DownTemp}
Sleep 30
mouseXY(0, 1)
SendInput {LButton Up}
Sleep 25
}
else
break
} ;; loop
} ;; if
} ;; autofire()
 
mouseXY(x,y)
{
    DllCall("mouse_event",uint,1,int,x,int,y,uint,0,int,0)
}
 
~F6::
_auto := false
Shift::Suspend, Toggle

*~$Space::
Sleep 5
Loop
{
GetKeyState, SpaceState, Space, P
If SpaceState = U
break
Sleep 20
Send, {Blind}{Space}
}
Return
         
```

