# Drive Notları <!-- omit in toc -->

Google Drive notları

## Drive Depolama Notları

Drive öğrenci hesaplarına sınırsız depolama hakkı sunmaktadır.

## Drive Direct Link Oluşturma

Drive'a üzerindeki linkleri tek tıklama ile indirmek için (wget vs) [buradan][direct link generator] _direct link_'e çevirmen gerekmektedir.

**Direct Link Yapısı:**

```url
https://docs.google.com/uc?export=download&id=<YourIndividualID>
```

### El ile Oluşturmak İçin

URL'de `open?` yazan yere `uc?export=download&` yazıyoruz.

```py
def fix_drive_url(url):
  if "drive.google.com/open?" in url:
    return url.replace(r"open?", r"uc?export=download&")
```

[direct link generator]: https://www.directlinkgenerator.com/
