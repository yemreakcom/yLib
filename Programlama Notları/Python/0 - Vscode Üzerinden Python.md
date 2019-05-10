# VsCode Üzerinde Python <!-- omit in toc -->

Başlangıç dökümanı için [buraya](https://code.visualstudio.com/docs/python/python-tutorial) bakabilirsin.

## İçerikler <!-- omit in toc -->

- [Python Eklentileri](#python-eklentileri)
- [Python Kodlarını Formatlama](#python-kodlar%C4%B1n%C4%B1-formatlama)
- [Debug Yapılandırması](#debug-yap%C4%B1land%C4%B1rmas%C4%B1)
- [Jupyter Desteği](#jupyter-deste%C4%9Fi)
- [Python Derleyicisi Ayarlama](#python-derleyicisi-ayarlama)
- [PYTHONPATH Oluşturma](#pythonpath-olu%C5%9Fturma)
- [PYTHONPATH Örneği](#pythonpath-%C3%B6rne%C4%9Fi)
- [Ek Python Ayarları](#ek-python-ayarlar%C4%B1)
- [Anaconda üzerindeki Python'ı Desteklemeyen Eklentiler](#anaconda-%C3%BCzerindeki-python%C4%B1-desteklemeyen-eklentiler)
- [Python Kısayolları](#python-k%C4%B1sayollar%C4%B1)

## Python Eklentileri

| Eklenti                                                  | Açıklama                                                   |
| -------------------------------------------------------- | ---------------------------------------------------------- |
| [Python][Python ext]                                     | Dil desteği                                                |
| [Kite][Kite]                                             | AI destekli kod tamamlama                                  |
| [Visual Studio IntelliCode - **Preview**][vsintellicode] | Sık kullanılan kod önerileri (**eksik öneriler olabilir**) |
| [autoDocstring][autdocstring]                            | Dökümantasyon parçaları sağlayan eklenti                   |
| [Better Comment][bettercomment]                          | Yorum satırı renklediricisi                                |

## Python Kodlarını Formatlama

- `CTRL` + `SHIFT` + `P` yapın
- Çıkan alana `Python: Select Linter` yazın
- `pylint` düzenleyicisini seçin
  - `pylint` aynı dizindeki modulleri bulamamakta, bu hatananın çözümü için `.pylintrc` dosyasını düzenlemek gerekmekte
  - <!-- TODO echolu koda çevir -->
  - `pylint --generate-rcfile .pylintrc` komutunu çalışma dizininde yazdıktan sonra, içini açıp `#init-hook` satırını `init-hook='import sys; system.path.append("${workspaceFolder}")'` ile değiştirin. (Yorum satırı olmaktan kaldırın)
  - Eğer girintiyi <kbd>TAB</kbd> ile yapıyorsanız `pylint`'de *bug*'a sebebiyet vermekte, <kbd>SPACE</kbd> kullanın
- Python derleyicinize `autopep8` paketini aşağıdaki komutlarla veya vscode arayüzü ile yükleyin
  - pip install autopep8
  - conda install autopep8
- Artık `SHIFT` + `ALT` + `F` ile kodları düzenleyebilirsiniz.
- Dosyaya sağ tıklayarak derleyebilirsiniz.

## Debug Yapılandırması

Detaylar için [buraya](https://code.visualstudio.com/docs/python/debugging) bakabilirsin.

- `CTRL` + `SHIFT` + `D` ile debug ekranını açın
- Sol üstte açılan ekrandan `ayarlar butonuna` tıklayın
- `Python` kısmını seçin

## Jupyter Desteği

Detaylar için [buraya](https://code.visualstudio.com/docs/python/jupyter-support) bakabilirsin.

- Kod alanının üstüne `#%%` yazarak olutşurabilirsiniz.

## Python Derleyicisi Ayarlama

Aktif olan derleyici ortamı, en altta bulunan durum çubuğunun solunda gösterilmektedir. Değiştirmek için:

- `CTRL` + `SHIFT` + `P` tuş kombinasyonuna basın
- Çıkan alana `Python: Select Interpreter` yazınız
- Çıkan ekrandan istediğiniz derleyiciyi seçiniz

## PYTHONPATH Oluşturma

- Çalışma dizininde `.env` dosyası oluşturun
- `.env` dosyasının içerisine `PYTHONPATH=` satırını ekleyin
  - Örnek için bir alttaki başlığa bakınız
- Vscode ayarlarına `"python.envFile": "${workspaceFolder}/.env"` satırını ekleyin
- Vscode'u yeniden başlatın

> Kaynak için [buraya](https://github.com/Microsoft/vscode-python/issues/3840#issuecomment-463789294) bakabilirsin. Ek olarak [buraya](https://stackoverflow.com/a/54083402/9770490) bakmanda da fayda var.

## PYTHONPATH Örneği

Resmi döküman için [buraya](https://code.visualstudio.com/docs/python/environments#_environment-variable-definitions-file) bakabilirsin.

- VsCode birden fazla satıra sahip değişken değerlerini kabul etmez
- Ortam değişklenleri oluşturmak için proje ayarlarından **env file** seçmemiz gerekmekte
- Ardından içine değişkenlerimizi tanımlamamız gerkemekte

```json
"python.envFile": "${workspaceFolder}/prod.env"
```

```sh
# prod.env
# Python kaynak dizinleri
RESEARCH_FOLDER=C:/Users/YEmre/Documents/Tensorflow/models/research
OBJECT_FOLDER=C:/Users/YEmre/Documents/Tensorflow/models/research/object_detection
SLIM_FOLDER=C:/Users/YEmre/Documents/Tensorflow/models/research/slim
SCRIPT_FOLDER=C:/Users/YEmre/Documents/Tensorflow/scripts

# Python modül yolu
PYTHONPATH=${RESEARCH_FOLDER}:${OBJECT_FOLDER}:${SLIM_FOLDER}:${SCRIPT_FOLDER}
```

```sh
PYTHONPATH=./src:${PYTHONPATH}
```

> Kaynak için [buraya](https://code.visualstudio.com/docs/python/environments#_use-of-the-pythonpath-variable) bakabilirsin.

## Ek Python Ayarları

Ek python ayarları için [buradaki](https://code.visualstudio.com/docs/python/settings-reference) resmi dökümana bakabilirsin.

## Anaconda üzerindeki Python'ı Desteklemeyen Eklentiler

| Eklenti                                                                                      | Açıklama                 |
| -------------------------------------------------------------------------------------------- | ------------------------ |
| [AREPL for python](https://marketplace.visualstudio.com/items?itemName=almenon.arepl)        | Anlık çıktıları gösterme |
| [Code Runner](https://marketplace.visualstudio.com/items?itemName=formulahendry.code-runner) | Kod koşturucusu          |

## Python Kısayolları

Alttaki kısayollar `keybindings.json` dosyası içerisinde bulunmalıdır.

```json
// Place your key bindings in this file to override the defaultsauto[]
[
  {
    // Kod parçasını metoda çevirme
    "key": "ctrl+shift+m ctrl+shift+m",
    "command": "python.refactorExtractMethod"
  },
  {
    // Kod parçasını metoda taşıma
    "key": "ctrl+shift+v ctrl+shift+v",
    "command": "python.refactorExtractVariable"
  },
  {
    // İmport'ları sıralama
    "key": "ctrl+shift+s ctrl+shift+s",
    "command": "python.sortImports"
  },
  {
    "key": "shift+f10",
    "command": "python.execInTerminal"
  }
]
```

<!-- ## Harici Bağlantılar -->

[Python ext]: https://marketplace.visualstudio.com/items?itemName=ms-python.python
[vsintellicode]: https://marketplace.visualstudio.com/items?itemName=VisualStudioExptTeam.vscodeintellicode
[autdocstring]: https://marketplace.visualstudio.com/items?itemName=njpwerner.autodocstring
[bettercomment]: https://marketplace.visualstudio.com/items?itemName=aaron-bond.better-comment
[Kite]: https://marketplace.visualstudio.com/items?itemName=kiteco.kite