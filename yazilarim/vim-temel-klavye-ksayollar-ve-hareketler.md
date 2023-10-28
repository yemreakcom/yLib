![1200px-Vimlogo.svg.png](https://upload.wikimedia.org/wikipedia/commons/thumb/9/9f/Vimlogo.svg/1200px-Vimlogo.svg.png)

# Vim Temel Klavye Kısayolları ve Hareketler

# **İçerikte Neler Var?**

- Vim klavye kısayolları
- Vim'de hareket için tuşlar
- Vim'de eylem kısayolları nasıl kullanılır
- Vim mod değişiklikleri
- Vim'de metni nasıl ararım
- Vim geri alma ve tekrar komutları
- Vim ekstra hareket kısayolları
- Vim'de yön tuşları alternatifleri
- Vim kelimeler arasında hareket etme
- Vim dosya başı ve sonuna nasıl gidilir

# 1. Hareket:

- `hjkl`: **Yön tuşları** gibi düşünün.
  - `h`: Sola hareket.
  - `j`: Aşağı hareket.
  - `k`: Yukarı hareket.
  - `l`: Sağa hareket.
  - Bilgisayar mühendisliğinin ilk zamanlarında bu tuşlar yön tuşları olarak kullanılıyordu.
- `w`, `b`, `e`: **Kelimeler arasında hareket**.
  - `w`: Sonraki kelimenin başına git (**W**ord).
  - `b`: Önceki kelimenin başına git (**B**eginning).
  - `e`: Şu anki kelimenin sonuna git (**E**nd).

# 2. Eylem

- `d`: **Silme** eylemi (Delete).
  - `dw`: Bir kelimeyi sil.
  - `dd`: Şu anki satırı sil.
- `c`: **Değiştirme** eylemi (Change).
  - `cw`: Bir kelimeyi değiştir.
- `y`: **Kopyalama** eylemi (Yank).
  - `yy`: Şu anki satırı kopyala.
  - `yw`: Bir kelimeyi kopyala.
- `p`: **Yapıştırma** eylemi (Paste).
  - Son kopyalanan veya silinen içeriği yapıştır.

# 3. Mod Değişiklikleri

- `i`: **Ekleme moduna** geç (Insert).
- `v`: **Görsel modda metin seçimi** yap (Visual).
  - `V`: Şu anki satırı seç.
- `:`: **Komut moduna** geç.

# 4. Arama

- `/`: **Metni ara**.
  - `/kelime`: "kelime"yi ara.
  - `n`: Son aramada sonraki sonuca git.
  - `N`: Son aramada önceki sonuca git.

# 5. Geri Alma & Tekrar

- `u`: **Geri alma** (Undo).
- `Ctrl + r`: **Geri alınanı geri getir** (Redo).

# 6. Ekstra Kısayollar

- `gg`: Dosyanın **başına** git.
- `G`: Dosyanın **sonuna** git.
- `^`: Satırın ilk karakterine git.
- `$`: Satırın sonuna git.
