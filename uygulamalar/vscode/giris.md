---
description: VsCode hakkında temel bilgiler ve genel kullanım notlarım
---

# 🔰 VsCode'a Giriş

## 💙 Önemli Notlar

VsCode dünyanın en çok kullanılan text editörü olarak geçmektedir.

* İlk defa VsCode kullanıyor isen [Introductory Videos](https://code.visualstudio.com/docs/getstarted/introvideos) videoları izlemen ve açıklamaları okuman oldukça önemli \(okumadan öğrenemezsin 😔\)
* VsCode'a başlamadan önce [Tips & Trick](https://code.visualstudio.com/docs/getstarted/tips-and-tricks) alanından, hangi dile odaklı çalışacaksanız onun dökümasyanunu okuyun
* Ardından gerekli olan eklentileri, eklenti mağazasından indirin \(✲ Ctrl + ⇧ Shift + X\)
* Sağ taraftaki kodların önizlemesinin olduğu alanı \(minimap\) kaldırmak için `"editor.minimap.enabled": false`

## 📑 Encoding Düzenleme <a id="encoding-duzenleme"></a>

VsCode'un emojileri ve özel karakterleri destekleyen türde dosya kaydetmesini sağlamak için:

* 👀 VsCode arayüzünde altta bulunan **Status Bar** alanına bakın
* 👉 **UTF-8** Yazısında tıklayın
* 💾 Çıkan ekranda **Save with Encoding** seçeneğine tıklayın
* 👨‍💻 **UTF-8 with BOM** seçeneğini seçin

![](../../.gitbook/assets/image%20%2828%29.png)

{% hint style="info" %}
🧙‍♂️ İsterseniz direkt olarak `CTRL + SHIFT + P` ile açılan komut penceresine **Save with Encoding** yazabilirsiniz
{% endhint %}

## 🐛 Debug Ayarları

Debug ayarlarına erişmek için:

* ✲ Ctrl + ⇧ Shift + `D` ile debug sekmesini açın
  * İsterseniz soldaki **activity bar** üzerinden erişebilirsiniz
* Sağ üstteki `ayarlar ikonuna` tıklayın
* `Launch.json` dosyası açılacaktır

## 🔍 Arama Özelliği

* 🕵️‍♂️ ✲ Ctrl F ile dosya, ✲ Ctrl ⇧ Shift F ile tüm proje içerisinde arayabilirsiniz
* 🕵️‍♂️ ✲ Ctrl H ile dosya, ✲ Ctrl ⇧ Shift H ile tüm proje içerisinde değiştirme yapabilirsiniz
* 🤝 Regex destekler
* 🐣 Regex gruplarına `$` işareti ile erişebilirsiniz
  * 🔸 `$0` ile tüm regex grubuna
  * 🔸 `$1`, `$2` ile  gruplara

![](../../.gitbook/assets/image%20%2890%29.png)

{% hint style="info" %}
‍🧙‍♂ Detaylı bilgi için [VSCode regex find & replace submatch math?](https://stackoverflow.com/questions/34618383/vscode-regex-find-replace-submatch-math) alanına bakabilirsin.
{% endhint %}

## 🚀 GitHub projelerini Açma

Online ortamda projelerini VsCode altyapısını kullanan Gitpod ile çalıştırmak için [buraya](../../proje-yonetimi/github/web.md#repoyu-vscode-ile-acma) bakabilirsin

## 🔗 Harici Bağlantılar

* [VsCode ile Yapılabilecekler](https://vscodecandothat.com/)
* [Debugging ES6 in Visual Studio Code](https://medium.com/@drcallaway/debugging-es6-in-visual-studio-code-4444db797954)



