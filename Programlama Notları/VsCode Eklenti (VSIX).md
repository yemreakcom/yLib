# Vscode Eklentisi VSIX Programlama <!-- omit in toc -->

## İçerikler <!-- omit in toc -->

- [Temel Gereksinimler](#temel-gereksinimler)
- [Giriş Kalıbını Oluşturma](#giri%C5%9F-kal%C4%B1b%C4%B1n%C4%B1-olu%C5%9Fturma)
  - [Eklentiyi Paylaşma](#eklentiyi-payla%C5%9Fma)
    - [Package JSON Örneği](#package-json-%C3%B6rne%C4%9Fi)

## Temel Gereksinimler

- Nodejs
- Javascript bilgisi

## Giriş Kalıbını Oluşturma

Video anlatımı için [buraya][VsCode Create Theme Extension in 1 min - Shows all steps] bakabilirsin.

- Terminal'i yada cmd'yi açın
- `npm i -g yo generator-code` ile kalıp oluşturucuyu indirin
- Kalıbın oluşmasını istediğiniz dizine `cd` ile gidin
- `yo code` ile gerekli seçenekleri işaretleyerek kalıbı oluşturun
- Tüm kalıp otomatik olarak kurulacaktır, kalıp içerisinde otomatik tanımlananlar:
  - Debug aracı
  - Ek açıklamalar
  - Package.json

### Eklentiyi Paylaşma

- Öncelikle [buradan][Token oluşturma] token oluşturmanız gerekmekte
  - `New Token` -> Organizatin **All accessiable organization**'ı seçin
- `npm install -g vsce` ile `vsix` oluşturucuyu indirin
- `vsce login <id>`
- Package json'u [örnekteki][Package JSON Örneği] gibi ayarların
- [VsCode Marketplace](https://marketplace.visualstudio.com/manage/publishers/)'den vsix uzantılı dosyanızı yükleyin

#### Package JSON Örneği

```json
{
    "publisher": "Buraya vsce ile girdiğiniz hesabı yazın",
    "icon": "resim yolu",
    "license": "SEE LICENSE IN LICENSE.txt",
    "keywords": [
        "anahtar",
        "helimeler"
    ],
    "repository": {
        "type": "git",
        "url": "github_proje urli"
    },
}
```

> Ek Notlar
>
> <https://code.visualstudio.com/api/working-with-extensions/publishing-extension#common-questions>

[Özel tema oluşturma]: https://www.youtube.com/watch?v=3Ju74i1MyBg
[Token oluşturma]: https://dev.azure.com/yedhrab/_usersSettings/tokens
[Package JSON Örneği]: #package-json-%C3%B6rne%C4%9Fi
[VsCode Create Theme Extension in 1 min - Shows all steps]: https://youtu.be/z_D_86WjXg4
