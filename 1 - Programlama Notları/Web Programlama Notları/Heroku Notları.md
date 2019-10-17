# Heroku 

Detaylı bilgiler için [buraya](https://devcenter.heroku.com/articles/getting-started-with-nodejs) tıklayabilirsin.

## Heroku Önemli Notlar

### Heroku varsayılan atamaları

```bash
NPM_CONFIG_LOGLEVEL=error
NODE_ENV=production
NODE_MODULES_CACHE=true
NODE_VERBOSE=false
```

> Bu atamalara kod içerisinden `process.env.<üsttekilerden biri>` şeklinde erişilebilir. 
> 
> *console.log(process.env.NODE_ENV) gibi*

### Heroku Script Çalıştırma

- Heroku aldığı node.js uygulamasındaki **start scriptini** çalıştırır. Yani `npm run start` komutunu işler
- Bu sebeple **package.json** dosyası olmak zorunda ve **start scriptini** içermek zorundadır
- Artık heroku yükleme işleminin hemen ardından `build` scriptini çalıştırmaya başlayacak
  - Tarihi ve detaylı bilgi için [buraya](https://devcenter.heroku.com/changelog-items/1557) tıklayabilirsin

Örnek package.json dosyası

```javascript
{
  "name": "temp",
  "version": "1.0.0",
  "description": "",
  "main": "index.js",
  "directories": {
    "lib": "lib"
  },
  "scripts": {
    "start": "node index.js",
    "test": "echo \"Error: no test specified\" && exit 1"
  },
  "author": "",
  "license": "ISC"
}
```

### Heroku port ayarı

```javascript
port = process.env.PORT || 5000
```

> Heroku kendiliğinden port atama işlemi yapmaktadır. Bu sebeple dinlediğimiz portu **process.env.PORT** yapmak zorundayız.

## Heroku Komutları

---

### Bu komutların çalışması için heroku-cli'nin yüklü olması lazım

```sh
npm install -g heroku
```

> Npm üzerinden heroku yükleme işlemi

### Heroku'ya giriş yapma

```cmd
heroku login
```

> Email ve şifre istenecektir. Siteye kayıt olduğunuz bilgileri girin

### Depo (repository) kopyalama işlemi

```cmd
heroku git:clone -a [herokudaki uygulama adı] [kopyalanacağı dizin yolu]
cd [kopyalanacağı dizin yolu]
```

- herokudaki uygulama adı: mytempsite
- kopyalanacağı dizin yolu: C:\Desktop\Temp

> Heroku'da bulunan uygulamayı istediğimiz dizinin içine kopyalıyoruz. Sonrasında kopyalama işleminin olduğu dizine giriyoruz.

### Değişiklikleri karşıya yükleme

```cmd
git add .
git commit -am "Mesaj"
git push heroku master
```

> Değişkliklikler heroku uygulmamıza eklenecektir.

### Uygulamayı başlatma

```cmd
heroku open
```

### Hata raporlarını görüntüleme

```cmd
heroku logs --tail -a [uygulama adı]
```

* uygulama adı: mytempsite (herokudaki uygulama adımız)

> Uygulmamız çalışırken yapılan işlemleri raporlar


## Heroku Ek Ayarlar

---
Babel gibi ek uygulamalar kullanıyorsanız bu kısım sizin için oldukça önemlidir.

> **Not**: Tüm es5 olmayan dosyaları *babel* ile es5'e çevirip herokuya yüklemek performans açısından daha sağlıklıdır.

### Heroku üretim modunu kapatma

```cmd
heroku config:set NPM_CONFIG_PRODUCTION=false
```

> Üretim modunu kapatır. Bu sayede heroku **package.json** dosyasındaki **dev-dependencies** içindekilerini
> indirir. Ardından tekrar bu mod isteğe bağlı açılabilir

### Heroku Bash Erişimi

```cmd
heroku run bash
```

> Bu komut ile terminale erişmiş oluruz. Bu sayede npm komutlarımızı çalıştırabiliriz.

```cmd
npm install
```

> Yukarıdaki komut ile gerekli olan uygulamaları (dev-dependencies) kendimiz indirebiliriz.

