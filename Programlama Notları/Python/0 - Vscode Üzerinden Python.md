# VsCode Üzerinde Python <!-- omit in toc -->

Başlangıç dökümanı için [buraya](https://code.visualstudio.com/docs/python/python-tutorial) bakabilirsin.

## İçerikler <!-- omit in toc -->

- [Python Eklentileri](#Python-Eklentileri)
- [Python Kodlarını Formatlama](#Python-Kodlar%C4%B1n%C4%B1-Formatlama)
- [Debug Yapılandırması](#Debug-Yap%C4%B1land%C4%B1rmas%C4%B1)
- [Jupyter Desteği](#Jupyter-Deste%C4%9Fi)
- [Python Derleyicisi Ayarlama](#Python-Derleyicisi-Ayarlama)
- [PYTHONPATH Oluşturma](#PYTHONPATH-Olu%C5%9Fturma)
- [PYTHONPATH Örneği](#PYTHONPATH-%C3%96rne%C4%9Fi)
- [Ek Python Ayarları](#Ek-Python-Ayarlar%C4%B1)
- [Python Kısayolları](#Python-K%C4%B1sayollar%C4%B1)

## Python Eklentileri

| Eklenti                                                                               | Açıklama                                                   |
| ------------------------------------------------------------------------------------- | ---------------------------------------------------------- |
| [Python][python ext]                                                                  | VsCode Dil desteği                                         |
| [Kite][kite]                                                                          | AI destekli kod tamamlama                                  |
| [Visual Studio IntelliCode - **Preview**][vsintellicode]                              | Sık kullanılan kod önerileri (**eksik öneriler olabilir**) |
| [AREPL for python](https://marketplace.visualstudio.com/items?itemName=almenon.arepl) | Anlık çıktıları gösterme                                   |
| [autoDocstring][autdocstring]                                                         | Dökümantasyon parçaları sağlayan eklenti                   |
| [Better Comment][bettercomment]                                                       | Yorum satırı renklediricisi                                |

## Python Kodlarını Formatlama

- `CTRL` + `SHIFT` + `P` yapın
- Çıkan alana `Python: Select Linter` yazın
- `pylint` düzenleyicisini seçin
  - `pylint` aynı dizindeki modulleri bulamamakta, bu hatananın çözümü için `.pylintrc` dosyasını düzenlemek gerekmekte
  - <!-- TODO echolu koda çevir -->
  - `pylint --generate-rcfile .pylintrc` komutunu çalışma dizininde yazdıktan sonra, içini açıp `#init-hook` satırını `init-hook='import sys; system.path.append("${workspaceFolder}")'` ile değiştirin. (Yorum satırı olmaktan kaldırın)
  - Eğer girintiyi <kbd>TAB</kbd> ile yapıyorsanız `pylint`'de _bug_'a sebebiyet vermekte, <kbd>SPACE</kbd> kullanın
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

> Değişkenin objelerini ve değerlerini öğrenmek için debug çok faydalıdır 🌟

## Jupyter Desteği

Detaylar için [buraya](https://code.visualstudio.com/docs/python/jupyter-support) bakabilirsin.

- Kod alanının üstüne `#%%` yazarak oluturabilirsiniz.

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

[python ext]: https://marketplace.visualstudio.com/items?itemName=ms-python.python
[vsintellicode]: https://marketplace.visualstudio.com/items?itemName=VisualStudioExptTeam.vscodeintellicode
[autdocstring]: https://marketplace.visualstudio.com/items?itemName=njpwerner.autodocstring
[bettercomment]: https://marketplace.visualstudio.com/items?itemName=aaron-bond.better-comment
[kite]: https://marketplace.visualstudio.com/items?itemName=kiteco.kite
