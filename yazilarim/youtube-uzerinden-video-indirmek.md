---
description: >-
  YouTube üzerinden hızlıca video indirme, youtube-dl alternatifi yt-dlp ile
  video indirme
---

# ⬇ Youtube Üzerinden Video İndirmek

## 🖤 Komut ile İndirme

* Öncellikle [yt-dlp](https://github.com/yt-dlp/yt-dlp#recommended)'yi indirmeniz gerekir
* Ardından indirdiğiniz dizinde `terminal` veya `komut istemi` açın
* Alttaki komutlarla indirme işleminizi yapabilirsiniz

```
yt-dlp <url> # Video'yu indirme
yt-dlp -F <url> # İndirlir formatları gösterir
yt-dlp -f <format> <url> # Verilen formatı indirme
yt-dlp --write-thumbnail --skip-download <url> # Thumbnail indirme
yt-dlp -a <file>
yt-dlp --get-filename -o '%(title)s.%(ext)s' BaW_jenozKc
yt-dlp test video ''_ä↭𝕐.mp4    # All kinds of weird characters

yt-dlp --get-filename -o '%(title)s.%(ext)s' BaW_jenozKc --restrict-filenames
yt-dlp_test_video_.mp4          # A simple file name

# Download YouTube playlist videos in separate directory indexed by video order in a playlist
yt-dlp -o '%(playlist)s/%(playlist_index)s - %(title)s.%(ext)s' https://www.youtube.com/playlist?list=PLwiyx1dc3P2JR9N8gQaQN_BCvlSlap7re

# Download all playlists of YouTube channel/user keeping each playlist in separate directory:
yt-dlp -o '%(uploader)s/%(playlist)s/%(playlist_index)s - %(title)s.%(ext)s' https://www.youtube.com/user/TheLinuxFoundation/playlists

# Download Udemy course keeping each chapter in separate directory under MyVideos directory in your home
yt-dlp -u user -p password -o '~/MyVideos/%(playlist)s/%(chapter_number)s - %(chapter)s/%(title)s.%(ext)s' https://www.udemy.com/java-tutorial/

# Download entire series season keeping each series and each season in separate directory under C:/MyVideos
yt-dlp -o "C:/MyVideos/%(series)s/%(season_number)s - %(season)s/%(episode_number)s - %(episode)s.%(ext)s" https://videomore.ru/kino_v_detalayah/5_sezon/367617

# Stream the video being downloaded to stdout
yt-dlp -o - BaW_jenozKc
```

## 🐍 Python Kodu ile Kullanma

* `pip install yt-dlp` ile gerkeli paketi kurun

```python
# import the library 
import yt_dlp

# create yt-dlp options
mp3_options = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
    'outtmpl': '%(playlist)s/%(playlist_index)s - %(title)s.%(ext)s',
    # 'playliststart': 1,
    # 'playlistend': 5,
}
best_options = {
    'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]',
    'outtmpl': '%(playlist)s/%(playlist_index)s - %(title)s.%(ext)s',
    # 'playliststart': 1,
    # 'playlistend': 5,
}

# the youtube playlist url
urls = []  # <-------- Buraya linkleri "" arasında yazın
with yt_dlp.YoutubeDL(best_options) as ydl:
    ydl.download(urls)

```

## 👨🏻‍💻 Youtube İndirici Web Sitesi Kodlama

* Örnek amaçlı hazırladığım [YoutubeDownloader](https://github.com/YEmreAk/YoutubeDownloader) projemi inceleyebilirsin
* Direkt olarak indirmek yerine player'a yönlendirme sebebi tarayıcalardaki CORs güvenlik tedbiridir

## 🎙 Soz Sözlerim

* Eskiden [`Youtube-dl` üzerine sayfa](https://lib.yemreak.com/uygulamalar/youtube) hazırlamıştım lakin artık o yavaş çalışmaktadır, o sayfa verimsizdir
* Bu bahsettiğim tool daha hızlı indirmektedir ve güncel durumdadır
