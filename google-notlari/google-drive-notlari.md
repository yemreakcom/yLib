---
description: Google'ın sunduğu bulut hizmeti
---

# ⛅ Google Drive Notları

## Drive Depolama Notları

Drive öğrenci hesaplarına sınırsız depolama hakkı sunmaktadır.

## Drive Direct Link Oluşturma

Drive'a üzerindeki linkleri tek tıklama ile indirmek için \(wget vs\) [buradan](https://www.directlinkgenerator.com/) _direct link_'e çevirmen gerekmektedir.

**Direct Link Yapısı:**

```text
https://docs.google.com/uc?export=download&id=<YourIndividualID>
```

### El ile Oluşturmak İçin

URL'de `open?` yazan yere `uc?export=download&` yazıyoruz.

```python
def fix_drive_url(url):
  if "drive.google.com/open?" in url:
    return url.replace(r"open?", r"uc?export=download&")
  
```

## 🔗 Harici Bağlantılar



