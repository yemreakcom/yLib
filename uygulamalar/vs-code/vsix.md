---
description: Visual Studio Code eklentileri olan VSIX yazılımlarını programlama
---

# 🧩 VSIX Programlama \| VS Code

## 🧱 Temel Gereksinimler

Eklenti programlanması için gerekenler

* [NodeJS](https://nodejs.org/en/download/) uygulaması
* JavaScript bilgisi

## 🏗️ Giriş Kalıbını Oluşturma

* Nodejs uygulamasını yükleyin
* Terminal veya komut istemini açın
* `npm i -g yo generator-code` ile kalıp oluşturucuyu indirin
* Eklenti kalıbının oluşmasını istediğiniz dizine `cd` komutu ile gidin
* `yo code` ile yapılandırma ayarlarını yaparak kalıbı oluşturun

> 💁‍♂️ Debug, `package.json` ve ek açıklamalar kalıp ile oluşturulacaktır

## 🔀 Eklenti Oluşturma ve Paylaşma

* Öncelikle [Nodejs](https://nodejs.org/en/download/) uygulamasının yüklü olduğundan emin olun
* `npm install -g vsce` ile `vsix` oluşturucuyu indirin
* `vsce package` ile `.vsix` uzantılı eklentiyi oluşturun

## 🛰️ Eklentiyi Manuel Paylaşma

Manuel veya komut istemi üzerinden [VS Code Marketplace](https://marketplace.visualstudio.com/vscode) üzerine eklentinizi  yükleyebilirsiniz

### 💁‍♂️ Manuel Yükleme

* [VS Code Marketplace](https://marketplace.visualstudio.com/manage/publishers/) üzerinden `vsix` uzantılı dosyanızı sunucuya el ile yükleyebilirsiniz

### 🤖 Otomatik Yükleme

* Otomatik olarak yüklemek için ID değeriniz yoksa, [🔑 Token Oluşturma](notion://www.notion.so/@yemreak/s/lib/~/drafts/-M9F1K1mY5em5FBTPTjC/uygulamalar/vs-code/vsix#token-olusturma) adımından token oluşturun
* `vsce login <id>` komutu ve token ID değeriniz ile giriş yapın
* Package json'u [📜 Package JSON Örneği](https://www.notion.so/VSIX-Programlama-4602a3468a8a4478a7addb6b74e91a1f#1ba0ff2ce7f240199dad8bcdb41eb3fa) gibi ayarların
* `vsce publish` ile eklentiyi [VsCode Marketplace](https://marketplace.visualstudio.com/manage/publishers/)'e gönderebilirsiniz
  * `vscode publish minor` ile versiyonu arttırarak gönderirsiniz

{% hint style="info" %}
‍VS Code'un resmi sitesindeki [Publishing Extension](https://code.visualstudio.com/api/working-with-extensions/publishing-extension) açıklamasına bakmanızda fayda var.
{% endhint %}

## 🔑 Token Oluşturma

* Öncelikle [buradan](https://dev.azure.com/yedhrab/_usersSettings/tokens) token oluşturmanız gerekmekte
* `New Token` -&gt; `Organization` -&gt; `All accessiable organization` ****kısmını seçin
* `Scopes` altında `Marketplace` kısmından `Acquire` ve `Manage` kutucuklarını seçin
* Token oluşturup, verilen **ID** değerini kopyalayın

## 📜 Package JSON Örneği

```text
{
  "publisher": "Buraya vsce ile girdiğiniz hesabı yazın",
  "icon": "resim yolu",
  "license": "SEE LICENSE IN LICENSE.txt",
  "keywords": ["anahtar", "helimeler"],
  "repository": {
    "type": "git",
    "url": "github_proje urli"
  }
}
```

## 🔗 Harici Bağlantılar

* [VS Code Publishing Extension](https://code.visualstudio.com/api/working-with-extensions/publishing-extension)
* [VS Code Eklentileri Sık Sorulan Sorular](https://code.visualstudio.com/api/%3Eworking-with-extensions/publishing-extension#common-questions)

