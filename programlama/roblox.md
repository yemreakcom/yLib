# ⏹ Roblox

## 🌃 Roblox Studio

![](../.gitbook/assets/robloxstudio_usage%20%283%29.png)

## 📜 Script Ekleme

![](../.gitbook/assets/robloxstudio_addscript.png)

## ☠️ Ölüm Script'i

* 🤵 Kullanıcı objeye değdiğinde anda ölür
* 🤵 `Humanoid` insan anlamına gelmektedir
* 🦄 `FindFirstChild` ile ilk değen obje bulunur
* 🩸 `BreakJoints` ile değen kişi öldürülür

```lua
script.Parent.Touched:Connect(function(hit)
	if hit.Parent:FindFirstChild("Humanoid") then 
		hit.Parent:BreakJoints()
	end
end)
```

## ⤵ Bloklarda Çarpışmayı Kapatma

* ✖️ Ayarlar kısmından `canCollide` özelliği kapatın

## 🔗 Faydalı Bağlantılar

{% embed url="https://www.youtube.com/watch?v=rWUbmR9EmLU" %}



