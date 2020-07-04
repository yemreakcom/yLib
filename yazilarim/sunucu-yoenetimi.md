---
description: >-
  Uzak sunucu (server) yönetimi, kurulum, yapılandırma ve ssh ile şifresiz
  bağlanma işlemleri
---

# 💻 Sunucu Yönetimi

## 🔌 Sunucuya Bağlanma

* `ssh -l <username> <ip>` veya `ssh <user>:<IP>` komutu ile sunucuya bağlanılır ve şifre girilir
* Sunucuya bağlanma sırasında terminal oturumu açılmaktadır
* Oturum kapandığında terminal de sonlanır, yani bağlantıdan çıkarsanız tüm işler sonlanır
* Bunu engellemek için `sudo apt install tmux` komutu ile `tmux` aracını indirin \(`nohup` uğraştırıcı 😢\)
* `tmux` ile terminal oturumu içerisinde yeni bir process başlatılmakta ve oturum kapansa da devam etmektedir

{% hint style="info" %}
‍🧙‍♂ Detaylı bilgi için [How to run a Python script in the cloud?](https://medium.com/@andras1000_18467/how-to-run-a-python-script-in-the-cloud-e486eef96ac3) yazısına bakınız
{% endhint %}

## 🔒 Sunucuya Şifresiz Bağlanma

* ⏬ OpenSSH yüklü değil ise yükleyin \(`shh <user>@<ip>` komutu ile test edebilirsiniz\)
* 🔑 SSH key ile giriş yapılacağından `ssh-keygen` \(Linux için `ssh-keygen -t rsa`\) komutu ile keygen oluşturun
* 👷‍♂️ Windows için `Get-Service -Name ssh-agent | Set-Service -StartupType Manual` komutu PowerShell üzerinden ile SSH servisini başlatın \([detaylar](https://stackoverflow.com/a/53606760/9770490)\)
* 🚚 Sunucuya anlaşma işlemi için oluşturulan `.pub` uzantılı dosyayı `scp ~/.ssh/id_rsa.pub <user>@<ip>:` komutu ile kopyalayın
* 🔌 Sunucuya `ssh <user>@<ip>` komutu ile şifrenizle bağlanın
* 📃 Sunucu üzerine aktarılan `*.pub` dosyasını `.ssh/authorized_keys` dosyasına eklememiz gerekmekte
* 📂 Eğer `.ssh` dizini yoksa `mkdir .ssh` ile dizini oluşturun
* 📝 Ardından `cat <isim>.pub >> .ssh/authorized_keys` komutu ile dosyanın sonuna ekleyin
* 👮‍♂️ Son olarak `chmod 700` ~~`/.ssh`~~ve `chmod 600~/.ssh/authorized_keys` ile gerekli yetkilendirmeleri yapın, aksi durumda çalışmaz
* 🎉 Artık `logout` komutu ile sunucudan çıkabilirsiniz ve şifresiz bağlantı kurabilirsiniz

{% hint style="info" %}
‍🧙‍♂ Detaylı bilgi için 

* [SSH Login Without a Password](https://howchoo.com/g/mmu5ngfimjk/ssh-login-without-password) 
* [Starting ssh-agent on Windows 10 fails: “unable to start ssh-agent service, error :1058”](https://stackoverflow.com/a/53606760/9770490)

alanlarına bakabilirsin.
{% endhint %}

## 🕐 Zaman Ayarı Yapma

* NTP \(network time protocol\) ayarlarını yapmak için `apt-get install ntp ntpdate` komutu ile `ntpdate` paketini kurun
* `ntpdate time.ume.tubitak.gov.tr` ile Tubitak NTP sunucusuna bağlantı yapın
* `service ntp restart` komutu ile yeniden başlatın
* `date` komutu ile tarihi görüntüleyebilirsiniz
* `tzselect` komutu ile zaman bölgesini de seçebiliriz

{% hint style="info" %}
‍🧙‍♂ Detaylı bilgi için [Linux zaman sunucusu ayarlama](https://gencbilisim.net/linux-zaman-sunucusu-ayarlama/) alanına bakabilirsin.
{% endhint %}

## `⏳ tmux` ile Uzun Süreli İşlemler

* `tmux` komutu ile yeni bir terminal açtırın ve oraya komutunuzu yazın
* ✲ Ctrl + B, D kısayolu ile ana terminalinize geçin
* Artık oturumu kapatsanız bile `tmux` ile açılan terminaldeki işlemler devam etmektedir
* `tmux attach` komutu ile son terminale bağlanabilirsin
* Terminal işini sonlandırmak için ✲ Ctrl + B, : kısayoluna basıp `kill-session` komutunu yazın

{% hint style="info" %}
‍🧙‍♂ Detaylı bilgi için [Getting started with Tmux](https://linuxize.com/post/getting-started-with-tmux/) alanına bakabilirsin.
{% endhint %}

## 🐍 Python Kurulumu

* Sunucularda python default olarak olur ama `pip` ve `venv` kurulu olmaz
* `sudo apt install python3-pip` ile pip kurulur
* `sudo apt install python3-venv` ile sanal ortam oluşturma aracı kurulur
* `pip` python paketlerinin indirilmesine yardımcı olan araçtır
* `venv` sanal python ortamları oluşturarak sistemin python paketlerinin bozulmasını engeller

