# 💫 Linux Genel Notlar 

## Dosya Paylaşımı

### Telefon ile PC Arasında Dosya Paylaşımı

- Telefonunuza [Share Music & Transfer Files - Mi Drop] uygulamasını indirin
- Uygulamaya **sadece Dosya Erişim İzni** vermeniz yeterlidirs
- PC ile aynı WiFi ağına bağlanın
- İndirdiğiniz uygulamanın arayüzünden:
  - Sol üstteki buton
  - Connect to Computer
  - Start
  - Portable
- Telefonunzda gözüken `ftp://...` ile başlayan veriyi aklınızda tutun
- Uygulamayı **kapatmadan** ve sol üstteki **geri tuşuna basmadan**, aşağı alabilirsiniz
- Dosya gezgini (`nautilus`) açın
  - `Other Locations`
  - *Connect to Server* alanına **ftp** adresini yazın
  - `Connect`
- Artık `Other Locations` üzerinden direkt olarak erişebilirsiniz

## Ekran Paylaşımı

- [Web üzerinden ekran paylaşma](https://askubuntu.com/questions/335158/share-desktop-via-web-browser/536958)
- [guacamole ile web üzerinden paylaşma](http://guacamole.apache.org/)

## Uygulama Notları

### Gedit Metin Editörü

| Renklendirme Tipi | Hangi uzantılar için   |
| ----------------- | ---------------------- |
| `Modelica`        | `ini`, `cfg`, `config` |

[Share Music & Transfer Files - Mi Drop]: https://play.google.com/store/apps/details?id=com.xiaomi.midrop

### FFMPEG

#### MP4'ü MP3'e çevirme

**FFmpeg with Constant Bitrate Encoding (CBR):**

```sh
ffmpeg -i video.mp4 -vn \
    -acodec libmp3lame -ac 2 -ab 160k -ar 48000 \
    audio.mp3
```

**FFmpeg with Variable Bitrate Encoding (VBR):**

```sh
ffmpeg -i video.mp4 -vn \
    -acodec libmp3lame -ac 2 -qscale:a 4 -ar 48000 \
    audio.mp3
```

> The VBR example has a target bitrate of 165 Kbit/s with a bitrate range of 140...185. [Kaynak](https://askubuntu.com/a/84633/898692)

#### MP3 Sıkıştırma

```sh
ffmpeg -i input.file -map 0:a:0 -b:a 96k output.mp3
```

## Hata Notları

### Failed to load module “canberra-gtk-module”

```sh
sudo apt install libcanberra-gtk-module
```

[vcxsrv]: https://github.com/ArcticaProject/vcxsrv/releases
