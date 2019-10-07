---
description: Programların kendi işletim sistemimizden bağımsız olarak çalışabilmesini sağlayan bir sistemdir
---

# 🐳 Docker

## 🗽 Açıklama

Uygulamaları kendi PC'ne kurmak, kaldırmak, hatalarıyla veya artıklarıyla uğraşmak istemiyorsan, doğru konumdasın :)

- Docker'ın ana sayfası için [buraya](https://www.docker.com/) tıklayabilirsin.

> Bu yazı detaylı anlatan blog yazısının özeti niteliğindedir, orijinali için [buraya](https://gokhansengun.com/docker-nedir-nasil-calisir-nerede-kullanilir/) tıklamanı tavsiye ederim.

## ❔ Nedir ve Neden Kullanmalıyım?

- Benim Makinemde Çalışıyor (Works on my Machine) Problemine Çözüm Sağlaması
- Geliştirme Ortamı Standardizasyonu (Eşitlik) Sağlaması
- Test ve Entegrasyon Ortamı Kurulumu ve Yönetimini Kolaylaştırması
- Mikroservis Mimari için Kolay ve Hızlı Bir Şekilde Kullanıma Hazır Hale Getirilebilmesi
- Kaynakların Etkili ve Efektif Bir Biçimde Kullanılmasını Sağlaması
- Multitenant Sistemlerde Tenancy Mantığını Uygulama Seviyesinden Çıkarmayı Sağlaması
- Vm teknolojisi gibi birden fazla kernel kullanmak yerine tek bir kernel yapısında birden fazla uygulama çalıştırmayı sağlar.
- Tüm bu işlemler `image` adı verilen yüklemelerle olmakta.
  - `Image`'lerin diğer artısı da normal program kurulumları gibi yüksek yer kaplamamakta ve docker'ıa özel optimize edilmiş haldedirler. (Daha az performans ister)
- Tüm bunlara ek olarak kod paylaşımları hususunda da oldukça faydalıdır. 
  - Kod'un docker ortamında çalışabilir olması docker yüklü diğer bilgisayarda da çalışabilir olacağı anlamına gelir.
- Kolay kaldırılabilir.
  - Docker üzerinden `image`'leri silmeniz durumunda uygulama ve ona bağlı olan her şey silineceltir. (Kendi bilgisayarımızda kaldırma işlemi sonucunda ardında artık dosya bırakmaktadır.)

## 🕵️‍ Nasıl Öğrenirim

- [Buraya](https://docs.docker.com/get-started/) tıklayarak resmi dökümantasyonuna bakabilirsin.
- Docker olayını özetleyen video için [buraya](https://www.youtube.com/watch?v=YFl2mCHdv24&t=622s) tıklayabilirsin.
- Docker'ı detaylı anlatan Türkçe blog için [buraya](https://gokhansengun.com/docker-nedir-nasil-calisir-nerede-kullanilir/) tıklayabilirsin. 👈 Tavsiye

## 🤸‍ Kısa Özet

[Docker Cheet Sheats](https://www.docker.com/sites/default/files/Docker_CheatSheet_08.09.2016_0.pdf)'e bakmanda fayda var.

| Terim             | Açıklama                                                                                                                                |
| ----------------- | --------------------------------------------------------------------------------------------------------------------------------------- |
| Container         | Docker Daemon tarafından Linux çekirdeği içerisinde birbirinden izole olarak çalıştırılan process’lerin her birine verilen isimdir.     |
| Image             | Container'ların çalışacağı işletim sistemi, programlar vs.                                                                              |
| Dockerfile        | Yapılandırma dosyaları                                                                                                                  |
| Docker Daemon     | Birbirinden bağımsız Container'ları barındıran, sistemin kullanacağı RAM, CPU gibi ayarları yapan katman. (Resimle daha açık olacaktır) |
| Docker CLI        | Docker Daemon ile iletişime geçtiğimiz kısım. CMD, Bash vs.. (evet siyah ekran)                                                         |
| Docker Registry   | Container'larda çalışan Image'lerin bulunduğu kısım                                                                                     |
| Docker Repository | Bir grup Image’ın oluşturduğu yapı                                                                                                      |

## 👨‍💻 Kullanım

### ⭐ Temel İşlemler

- Docker'dan Image çekme
  - `docker pull <image_ismi>`
- Image'leri görüntüleme
  - `docker images`
- Image çalıştırma (Image ile container oluşturma)
  - `docker run <image_ismi>`
  - `docker run -p <host_port>:<conotainer_port> <image_ismi>`
    - İmage'i çalıştırıp htttps:localhost:<host_port>'unu, container'ın <conotainer_port>'una bağlama.
    - docker run -p 8080:80 nginx

> 💡 Eğer image yüklü değilse otomatik indirir!

### 📂 Conteiner İşlemleri

- Çalışan containerları gösterme
  - `docker ps`
  - `docker ps -a`
- Oluşturulan container'ı yeniden çalıştırma
  - `docker start <container_id>`
    - `<container_id>`'yi `docker ps -a` ile bulabilirsiniz.
  - `docker start -a <container-id>`
    - Terminale ekleyerek başlatma. (I/O girişi ile kontrol edebiliriz.)
- Container kayıtlarını görüntüleme (loglar)
  - `docker logs <container_id>`
- Container silme
  - `docker rm <container-id>`
  - `docker rm -f <container-id>`
    - Çalışır halde bile olsa silme (Forging)
- Container üzerinde uygulama çalıştırma
  - `docker exec <options> <container_id> <path>`
  - `docker exec -it <container_id> /bin/bash`
    - `-i` interactive terminal demek
    - `-t` terminale bağlamak demek (attach)
    - `-d` bağlamadan çalıştır demek (deattach)
    - Container üzerinde çalışan işlemleri (process'leri) gösterme
      - `ps -ef`
    - Dosyayı terminale basma
      - `more <path>`
      - `more /etc/nginx/nginx.conf`
      - `more /etc/nginx/conf.d/default.conf`
- Container'ı çıkışa zorlama
  - `docker kill <container_id>`

## 🖤 Tüm Docker Komutları

![docker_command](https://cdn-images-1.medium.com/max/1400/1*G_9c9ttl-09eSKoSazPnNQ.png)

| Komut                                                       | Açıklaması                                                                                                                                              |
| ----------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `docker images                                            ` | Lokal registry’de mevcut bulunan Image’ları listeler                                                                                                    |
| `docker ps                                                ` | Halihazırda çalışmakta olan Container’ları listeler                                                                                                     |
| `docker ps -a                                             ` | Docker Daemon üzerindeki bütün Container’ları listeler                                                                                                  |
| `docker ps -aq                                            ` | Docker Daemon üzerindeki bütün Container’ların ID’lerini listeler                                                                                       |
| `docker pull <repository_name>/<image_name>:<image_tag>   ` | Belirtilen Image’ı lokal registry’ye indirir. Örnek: docker pull gsengun/jmeter3.0:1.7                                                                  |
| `docker top <container_id>                                ` | İlgili Container’da top komutunu çalıştırarak çıktısını gösterir                                                                                        |
| `docker run -it <image_id veya image_name> CMD            ` | Verilen Image’dan terminal’i attach ederek bir Container oluşturur                                                                                      |
| `docker pause <container_id>                              ` | İlgili Container’ı duraklatır                                                                                                                           |
| `docker unpause <container_id>                            ` | İlgili Container pause ile duraklatılmış ise çalışmasına devam ettirilir                                                                                |
| `docker stop <container_id>                               ` | İlgili Container’ı durdurur                                                                                                                             |
| `docker start <container_id>                              ` | İlgili Container’ı durdurulmuşsa tekrar başlatır                                                                                                        |
| `docker rm <container_id>                                 ` | İlgili Container’ı kaldırır fakat ilişkili Volume’lara dokunmaz                                                                                         |
| `docker rm -v <container_id>                              ` | İlgili Container’ı ilişkili Volume’lar ile birlikte kaldırır                                                                                            |
| `docker rm -f <container_id>                              ` | İlgili Container’ı zorlayarak kaldırır. Çalışan bir Container ancak -f ile kaldırılabilir                                                               |
| `docker rmi <image_id veya image_name>                    ` | İlgili Image’ı siler                                                                                                                                    |
| `docker rmi -f <image_id veya image_name>                 ` | İlgili Image’ı zorlayarak kaldırır, başka isimlerle Tag’lenmiş Image’lar -f ile kaldırılabilir                                                          |
| `docker info                                              ` | Docker Daemon’la ilgili özet bilgiler verir                                                                                                             |
| `docker inspect <container_id>                            ` | İlgili Container’la ilgili detaylı bilgiler verir                                                                                                       |
| `docker inspect <image_id veya image_name>                ` | İlgili Image’la ilgili detaylı bilgiler verir                                                                                                           |
| `docker rm $(docker ps -aq)                               ` | Bütün Container’ları kaldırır                                                                                                                           |
| `docker stop $(docker ps -aq)                             ` | Çalışan bütün Container’ları durdurur                                                                                                                   |
| `docker rmi $(docker images -aq)                          ` | Bütün Image’ları kaldırır                                                                                                                               |
| `docker images -q -f dangling=true                        ` | Dangling (taglenmemiş ve bir Container ile ilişkilendirilmemiş) Image’ları listeler                                                                     |
| `docker rmi $(docker images -q -f dangling=true)          ` | Dangling Image’ları kaldırır                                                                                                                            |
| `docker volume ls -f dangling=true                        ` | Dangling Volume’ları listeler                                                                                                                           |
| `docker volume rm $(docker volume ls -f dangling=true -q) ` | Danling Volume’ları kaldırır                                                                                                                            |
| `docker logs <container_id>                               ` | İlgili Container’ın terminalinde o ana kadar oluşan çıktıyı gösterir                                                                                    |
| `docker logs -f <container_id>                            ` | İlgili Container’ın terminalinde o ana kadar oluşan çıktıyı gösterir ve -f follow parametresi ile o andan sonra oluşan logları da göstermeye devam eder |
| `docker exec <container_id> <command>                     ` | Çalışan bir Container içinde bir komut koşturmak için kullanılır                                                                                        |
| `docker exec -it <container_id> /bin/bash                 ` | Çalışan bir Container içinde terminal açmak için kullanılır. İlgili Image’da /bin/bash bulunduğu varsayımı ile                                          |
| `docker attach <container_id>                             ` | Önceden detached modda -d başlatılan bir Container’a attach olmak için kullanılır                                                                       |

## 🔗 Harici Bağlantılar

- [12 Dk'da Docker](https://www.youtube.com/watch?v=YFl2mCHdv24)
- [Ps command not found](https://stackoverflow.com/questions/26982274/ps-command-doesnt-work-in-docker-container/26982502)
- [Docker Verilerini Temizleme](https://www.digitalocean.com/community/tutorials/how-to-remove-docker-images-containers-and-volumes)
- [Docker for Java Devs](https://www.youtube.com/watch?v=1BI2W-PGkKw)
