# NPM <!-- omit in toc -->

## İçerikler <!-- omit in toc -->

- [CLI Uygulaması Yapma](#CLI-Uygulamas%C4%B1-Yapma)
  - [CLI Args (Komut Argümanları)](#CLI-Args-Komut-Arg%C3%BCmanlar%C4%B1)
    - [Yargs ile Args Yönetme](#Yargs-ile-Args-Y%C3%B6netme)
    - [Minimist ile Args Yönetme](#Minimist-ile-Args-Y%C3%B6netme)
  - [Bin Klasörü](#Bin-Klas%C3%B6r%C3%BC)
- [Paket Yapımı Örnekleri](#Paket-Yap%C4%B1m%C4%B1-%C3%96rnekleri)
- [Paketleri Online Test Etme](#Paketleri-Online-Test-Etme)
- [Paket Oluşturma ve Yayınlama](#Paket-Olu%C5%9Fturma-ve-Yay%C4%B1nlama)
  - [Paket için Package.json Ayarları](#Paket-i%C3%A7in-Packagejson-Ayarlar%C4%B1)

## CLI Uygulaması Yapma

### CLI Args (Komut Argümanları)

Komut argümanları `node index.js arg1 arg2 ...` ile verilir.

- `process.argv` ile erişilir
- `process.argv[0]` Node'un yolu
- `process.argv[1]` Script'in yolu
- Geri kalanları kullanıcının yazıdığı parametrelerdir
- `process.argv.slice(2)` ile kullanıcı parametrelerine erişilir

#### Yargs ile Args Yönetme

Nodejs sitesindenki açıklamaya [buradan][Command Arguments Handler - Yargs] erişebilirsin.

| Metod         | Açıklama                            |
| ------------- | ----------------------------------- |
| `command`     | Komut `node index.js komut1 komut2` |
| `option`      | `--help` gibi ayarlar               |
| `type`        | Ayar tipi (`'number'` ...)          |
| `alias`       | `--help` yerine `-h` ayarlama       |
| `description` | Yardım metnindeki (`-h`) açıklama   |
|               |

#### Minimist ile Args Yönetme

- İlk olarak projeye dahil edilmeli `npm install -save minimist`

```js
// komut "yemreak param1 param2 -option param3 -abc -d"
minimist(process.argv.slice(2))
// { _:['param1', 'param2'], option: 'param3', a: true, b: true, c: true, d: true}
```

> Ek bağlantılar:
>
> - [CLI yapımı örneği][Creating CLI App Example]
> - [Yargs ile argüman yönetimi][Command Arguments Handler - Yargs]

### Bin Klasörü

Özel komutların tanımlanmasını sağlar.

- `<komut1>` Örnek komut ismidir
  - Örn: `yemreak`

**Dizin yapısı:**

```txt
+ bin
  - <komut1>
  - <komut2>
- index.js
- README.md
```

**Dosya içeriği:**

```js
#!/usr/bin/env node // Bu satır node scripti olduğu anlamına gelir
require('../')() // Scriptin aslının olduğu dizini işaret eder
```

**Package json'a eklenecek ayar:**

Bu ayar ile bin dosyamız indirilip gerekli yere konumlandırılacaktır.

```json
"bin": {
    "<komut1>": "bin/<komut1>",
    "<komut2>": "bin/<komut2>"
},
```

## Paket Yapımı Örnekleri

- [Temel CLI Örneği](https://github.com/timberio/outside-cli) ve [açıklaması](https://timber.io/blog/creating-a-real-world-cli-app-with-node/)

## Paketleri Online Test Etme

- Paketleri indirmeden önce [buradan][Npm runkit] test edebilirsin.

## Paket Oluşturma ve Yayınlama

- İlk olarak npm hesabını [buradan][Npm Signup] oluşturun
- `npm adduser` ile kullanıcı oluşturun
  - `npm login` komutunu da kullana bilirsiniz
  - Oluşturulan token bilgisine [buradan][Npm Token] bakabilirsiniz
- `npm version v1.0.0` ile paketin sürümünü tanımlayın
- `npm publish` ile [npm sitesine][Npm] yükleyebilirsiniz

### Paket için Package.json Ayarları

**Node sürümü ayarı:**

```json
"engines": {
    "node": ">=8"
}
```

**Global yükleme önerisi:**

```json
"preferGlobal": true
```

**Tam Örnek:**

```json
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

[Npm]: https://www.npmjs.com/
[Npm Signup]: https://www.npmjs.com/signup
[Npm Token]: https://www.npmjs.com/settings/yedhrab/tokens
[Npm runkit]: https://npm.runkit.com

[Creating CLI App Example]: https://timber.io/blog/creating-a-real-world-cli-app-with-node/
[Command Arguments Handler - Yargs]: https://nodejs.org/en/knowledge/command-line/how-to-parse-command-line-arguments/
