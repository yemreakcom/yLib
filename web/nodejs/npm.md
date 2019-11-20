---
description: Node package manager olarak adlandırılan nodejs paket yönetim aracıdır
---

# 🥬 NPM



## CLI Uygulaması Yapma

### CLI Args \(Komut Argümanları\)

Komut argümanları `node index.js arg1 arg2 ...` ile verilir.

* `process.argv` ile erişilir
* `process.argv[0]` Node'un yolu
* `process.argv[1]` Script'in yolu
* Geri kalanları kullanıcının yazıdığı parametrelerdir
* `process.argv.slice(2)` ile kullanıcı parametrelerine erişilir

#### Yargs ile Args Yönetme

Nodejs sitesindenki açıklamaya [buradan](https://nodejs.org/en/knowledge/command-line/how-to-parse-command-line-arguments/) erişebilirsin.

| Metod | Açıklama |
| :--- | :--- |
| `command` | Komut `node index.js komut1 komut2` |
| `option` | `--help` gibi ayarlar |
| `type` | Ayar tipi \(`'number'` ...\) |
| `alias` | `--help` yerine `-h` ayarlama |
| `description` | Yardım metnindeki \(`-h`\) açıklama |
|  |  |

#### Minimist ile Args Yönetme

* İlk olarak projeye dahil edilmeli `npm install -save minimist`

```javascript
// komut "yemreak param1 param2 -option param3 -abc -d"
minimist(process.argv.slice(2))
// { _:['param1', 'param2'], option: 'param3', a: true, b: true, c: true, d: true}
```

> Ek bağlantılar:
>
> * [CLI yapımı örneği](https://timber.io/blog/creating-a-real-world-cli-app-with-node/)
> * [Yargs ile argüman yönetimi](https://nodejs.org/en/knowledge/command-line/how-to-parse-command-line-arguments/)

### Bin Klasörü

Özel komutların tanımlanmasını sağlar.

* `<komut1>` Örnek komut ismidir
  * Örn: `yemreak`

**Dizin yapısı:**

```text
+ bin
  - <komut1>
  - <komut2>
- index.js
- README.md
```

**Dosya içeriği:**

```javascript
#!/usr/bin/env node // Bu satır node scripti olduğu anlamına gelir
require('../')() // Scriptin aslının olduğu dizini işaret eder
```

**Package json'a eklenecek ayar:**

Bu ayar ile bin dosyamız indirilip gerekli yere konumlandırılacaktır.

```javascript
"bin": {
    "<komut1>": "bin/<komut1>",
    "<komut2>": "bin/<komut2>"
},
```

## Paket Yapımı Örnekleri

* [Temel CLI Örneği](https://github.com/timberio/outside-cli) ve [açıklaması](https://timber.io/blog/creating-a-real-world-cli-app-with-node/)

## Paketleri Online Test Etme

* Paketleri indirmeden önce [buradan](https://npm.runkit.com) test edebilirsin.

## Paket Oluşturma ve Yayınlama

* İlk olarak npm hesabını [buradan](https://www.npmjs.com/signup) oluşturun
* `npm adduser` ile kullanıcı oluşturun
  * `npm login` komutunu da kullana bilirsiniz
  * Oluşturulan token bilgisine [buradan](https://www.npmjs.com/settings/yedhrab/tokens) bakabilirsiniz
* `npm version v1.0.0` ile paketin sürümünü tanımlayın
* `npm publish` ile [npm sitesine](https://www.npmjs.com/) yükleyebilirsiniz

### Paket için Package.json Ayarları

**Node sürümü ayarı:**

```javascript
"engines": {
    "node": ">=8"
}
```

**Global yükleme önerisi:**

```javascript
"preferGlobal": true
```

**Tam Örnek:**

```javascript
{
  "name": "ytools",
  "version": "1.0.0",
  "description": "Faydalı olacak araçların, toparlanmış hali",
  "main": "index.js",
  "scripts": {
    "test": "echo \"Error: no test specified\" && exit 1"
  },
  "engines": {
    "node": ">=8"
  },
  "preferGlobal": true,
  "bin": {
    "ytools": "bin/ytools"
  },
  "keywords": [
    "yemreak",
    "tools",
  ],
  "repository": {
    "type": "git",
    "url": "git+https://github.com/yedhrab/YTools.git"
  },
  "keywords": [
    "tools"
  ],
  "author": "yedhrab",
  "license": "MIT",
  "bugs": {
    "url": "https://github.com/yedhrab/YTools/issues"
  },
  "homepage": "https://github.com/yedhrab/YTools#readme",
  "dependencies": {
    "yargs": "^13.2.4"
  }
}
```

> Video örneğine [buradan](https://www.google.com/search?q=make+npm+module&oq=make+npm+module&aqs=chrome.0.0l6.2476j0j7&sourceid=chrome&ie=UTF-8#kpvalbx=1) erişebilirsin.

