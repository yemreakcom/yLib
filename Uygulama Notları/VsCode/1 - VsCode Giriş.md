# Vscode Giriş <!-- omit in toc -->

## içerikler <!-- omit in toc -->

- [VsCode için Önemli Notlar](#vscode-i%c3%a7in-%c3%96nemli-notlar)
- [VsCode kısayolları](#vscode-k%c4%b1sayollar%c4%b1)
  - [Sık Kullanılan Kısayollar](#s%c4%b1k-kullan%c4%b1lan-k%c4%b1sayollar)
  - [Verimlilik Kısayolları](#verimlilik-k%c4%b1sayollar%c4%b1)
  - [Aksiyon Penceresi](#aksiyon-penceresi)
  - [İmleç Kısayolalrı](#%c4%b0mle%c3%a7-k%c4%b1sayolalr%c4%b1)
  - [Metin Kısayolları](#metin-k%c4%b1sayollar%c4%b1)
  - [Editör Kısayolları](#edit%c3%b6r-k%c4%b1sayollar%c4%b1)
  - [Görünüm Kısayolları](#g%c3%b6r%c3%bcn%c3%bcm-k%c4%b1sayollar%c4%b1)
- [Debug Ayarları](#debug-ayarlar%c4%b1)
- [Harici Bağlantılar](#harici-ba%c4%9flant%c4%b1lar)

## VsCode için Önemli Notlar

VsCode dünyanın en çok kullanılan text editörü olarak geçmektedir.

- İlk defa VsCode kullanıyor isen [buradaki][vscode intro videos] videoları izlemen ve açıklamaları okuman oldukça önemli (okumadan öğrenemezsin 😔)
- VsCode'a başlamadan önce [buradan][vscode doc] üzerinden, hangi dile odaklı çalışacaksanız onun dökümasyanunu okuyun
- Ardından gerekli olan eklentileri, eklenti mağazasından indirin (<kbd>CTRL</kbd> + <kbd>SHIFT</kbd> + <kbd>X</kbd>)
- Sağ taraftaki kodların ön izlesinin olduğu alanı (minimap) kaldırmak için `"editor.minimap.enabled": false`

## VsCode kısayolları

PDF dökümanı için [buraya](..%5C..%5Cpdfs%5CVisual%20Studio%20Code%20Shortcuts.pdf) bakabilirsin.

- [Vscode ipuçları](https://code.visualstudio.com/docs/getstarted/tips-and-tricks#_files-and-folders)
- [Snipped](https://code.visualstudio.com/docs/getstarted/tips-and-tricks#_snippets)

### Sık Kullanılan Kısayollar

| Kısayol                                           | Açıklama                               |
| ------------------------------------------------- | -------------------------------------- |
| <kbd>CTRK</kbd> + <kbd>F</kbd>                    | Dosyada kelime arama                   |
| <kbd>CTRL</kbd> + <kbd>H</kbd>                    | Dosyada kelime arama ve değiştirme     |
| <kbd>CTRL</kbd> + <kbd>SHIFT</kbd> + <kbd>F</kbd> | Tüm projede kelime arama               |
| <kbd>CTRL</kbd> + <kbd>SHIFT</kbd> + <kbd>H</kbd> | Tüm projede kelime arama ve değiştirme |

### Verimlilik Kısayolları

- Zen Mode <kbd>CTRL</kbd> + <kbd>K</kbd> + <kbd>Z</kbd>

### Aksiyon Penceresi

`CTRL` + `P` ile aksiyon penceresiini erişebilirsiniz.

| Kısayol    | Açıklama                                             | Kısayol                                                 |
| ---------- | ---------------------------------------------------- | ------------------------------------------------------- |
| `#`        | Çalışma dizininde arama                              |
| `@` & `@:` | Dosya içerisnde sembole özgü arama (gruplu gösterme) | <kbd> CTRL </kbd> + <kbd> SHIFT </kbd> + <kbd> O </kbd> |
| `>`        | Komutlarda arama                                     | <kbd>CTRL</kbd> + <kbd>SHIFT</kbd> + <kbd>P</kbd>       |
| `:`        | Satıra yönelme                                       |
| `?`        | Yardım                                               |

### İmleç Kısayolalrı

- <kbd>ALT</kbd> Birden fazla işaretçi belirleme
- <kbd>CTRL</kbd> + <kbd>SHIFT</kbd> + <kbd>Yukarı yada Aşağı Tuşu</kbd> İşaretçi sayısını arttırma
- <kbd>CTRL</kbd> + <kbd>U</kbd> Bir önceki imleci seçer

### Metin Kısayolları

- <kbd>SHIFT</kbd> + <kbd>ALT</kbd> + <kbd>Sağ veya Sol</kbd> Bir sonraki bloğu seçme
- <kbd>SHIFT</kbd> + <kbd>ALT</kbd> + <kbd>Yukarı veya Aşağı</kbd> Satırı çoğaltma
- <kbd>CTRL</kbd> + <kbd>D</kbd> Kelimeyi seçme
  - Birden fazla tekrarlanırsa aynı metinleri seçer yanlarına imleç getirir
  - Değişkenleri yeniden adlandırmada çok faydalıdır
- <kbd>CTRL</kbd> + <kbd>L</kbd> Satırı seçme
- <kbd>CTRL</kbd> + <kbd>X</kbd> Satırı kesme
- <kbd>ALT</kbd> + <kbd>Yukarı yada Aşağı Tuşu</kbd> Satırı taşıma
  - Sırasıya: Kelime, Satır, Kod bloğu, ..., Tüm metin

### Editör Kısayolları

- <kbd>ALT</kbd> tuşuna basılı tutarak dosyalara tıklarsan yan panelde açılır
- <kbd>CTRL</kbd> + <kbd>ALT</kbd> + <kbd>Sağ veya Sol</kbd> Pencereyi sağa veya sola alır
- <kbd>CTRL</kbd> + <kbd>SHIFT</kbd> + <kbd>A</kbd> Seçili alanı yorum satırı yapma
- Tüm kodları gizleme (_fold all_)
  - Windows and Linux için <kbd>Ctrl</kbd> + <kbd>K</kbd>, <kbd>Ctrl</kbd> + <kbd>0</kbd> (sıfır)
  - macOS için <kbd>⌘</kbd> + <kbd>K</kbd>, <kbd>⌘</kbd> + <kbd>0</kbd> (sıfır)
- Kodları seviyeye göre gizleme
  - <kbd>Ctrl</kbd> + <kbd>K</kbd>, <kbd>Ctrl</kbd> + <kbd><sayı></kbd>
  - Örn: <kbd>Ctrl</kbd> + <kbd>K</kbd>, <kbd>Ctrl</kbd> + <kbd>2</kbd>
- Tüm kodları gösterme (_unfold all_)
  - Windows and Linux için <kbd>Ctrl</kbd> + <kbd>K</kbd>, <kbd>Ctrl</kbd> + <kbd>J</kbd> (sıfır)
  - macOS için <kbd>⌘</kbd> + <kbd>K</kbd>, <kbd>⌘</kbd> + <kbd>J</kbd>

### Görünüm Kısayolları

- <kbd>CTRL</kbd> + <kbd>Yukarı yada Aşağı Tuşu</kbd> Görünen ekranı kaydırma
- <kbd>CTRL</kbd> + <kbd>SHIFT</kbd> + <kbd>V</kbd> _Markdown preview_'i açar
- <kbd>CTRL</kbd> + <kbd>J</kbd> Alt paneli görünür kılar

## Debug Ayarları

Debug ayarlarına erişmek için:

- `CTRL` + `SHIFT` + `D` ile debug sekmesini açın
  - İsterseniz soldaki **activity bar** üzerinden erişebilirsiniz
- Sağ üstteki `ayarlar ikonuna` tıklayın
- `Launch.json` dosyası açılacaktır

## Harici Bağlantılar

- [VsCode ile Yapılabilecekler](https://vscodecandothat.com/)
- [Debugging ES6 in Visual Studio Code](https://medium.com/@drcallaway/debugging-es6-in-visual-studio-code-4444db797954)
