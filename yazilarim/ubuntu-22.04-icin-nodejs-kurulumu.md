# 🐧 Ubuntu 22.04 icin Nodejs Kurulumu

* [Nodesource Node.js DEB](https://deb.nodesource.com/) uzerinden kurulumu yapabilirsiniz

<figure><img src="../.gitbook/assets/image (58).png" alt=""><figcaption></figcaption></figure>

## Hata almaniz durumunda mevcut paketleri kaldirip bastan kurun

> Bu işlem, `libnode-dev` paketine bağımlı olan diğer paketleri etkileyebilir.

```
sudo apt-get remove libnode-dev
sudo apt-get install -f
sudo apt-get update
sudo apt-get install nodejs
```

### Bir diger secenek de (**onermiyorum**)

```
sudo dpkg -i --force-overwrite /var/cache/apt/archives/nodejs_20.8.1-1nodesource1_amd64.deb
sudo apt-get install -f
```

> Son denenme tarihi 23 Oct 2023 at 20:30:38
