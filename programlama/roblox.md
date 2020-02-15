# ⏹ Roblox

## 🌃 Roblox Studio

![](../.gitbook/assets/robloxstudio_usage%20%283%29.png)

## 📜 Script Ekleme

![](../.gitbook/assets/robloxstudio_addscript.png)

## 🐣 Spawn Point Ayarlama

* 🚄 Öldükten sonra en son değilen `spawnpoint` üzerinden doğmayı sağlar
* ➕ Eklemek için `🌍 Workspace` objesinin içindeki `scripts` dosyasına alttaki kodu kopyalayın

```lua
local Players = game:GetService("Players")
 
local function addSpawn(spawnLocation)
	-- listen for the spawn being touched
	spawnLocation.Touched:Connect(function(hit)
		local character = hit:FindFirstAncestorOfClass("Model")
		if character then
			local player = Players:GetPlayerFromCharacter(character)
			if player and player.RespawnLocation ~= spawnLocation then
				local humanoid = character:FindFirstChildOfClass("Humanoid")
				-- make sure the character isn't dead
				if humanoid and humanoid:GetState() ~= Enum.HumanoidStateType.Dead then
					print("spawn set")
					player.RespawnLocation = spawnLocation
				end
			end
		end
	end)
end
 
local firstSpawn
 
-- look through the workspace for spawns
for _, descendant in pairs(workspace:GetDescendants()) do
	if descendant:IsA("SpawnLocation") then
		if descendant.Name == "FirstSpawn" then
			firstSpawn = descendant
		end
		addSpawn(descendant)
	end
end
 
local function playerAdded(player)
	player.RespawnLocation = firstSpawn
end
 
-- listen for new players
Players.PlayerAdded:Connect(playerAdded)
```

{% hint style="info" %}
‍🧙‍♂ Detaylı bilgi için [Respawn Location](https://developer.roblox.com/en-us/api-reference/property/Player/RespawnLocation) alanına bakabilirsin.
{% endhint %}

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

## 🧩 Block Ayarları

| 💎 Özellik | 📝 Açıklama |
| :--- | :--- |
| `CanCollide` | ⤵ Blokların içinden geçilir |
| `Anchored` | 🕊️ Aşağı düşmesini engeller |

## 🔗 Faydalı Bağlantılar

{% embed url="https://www.youtube.com/watch?v=rWUbmR9EmLU" %}



