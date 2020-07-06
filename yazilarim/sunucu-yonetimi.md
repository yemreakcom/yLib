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

{% tabs %}
{% tab title="✴️ Windows" %}
{% code title="ConnectServer.ps1" %}
```aspnet
#requires -PSEdition Core

$USER = Read-Host 'Username'
$IP = Read-Host 'IP adress'
$KEY_PATH = Read-Host 'Key path (./.ssh/id_rsa)'
ssh-keygen -t ecdsa -b 521 -f ${KEY_PATH}
Get-Service -Name ssh-agent | Set-Service -StartupType Manual
Start-Service ssh-agent
ssh-add ${KEY_PATH}

$pub = (Get-Content ~/${KEY_PATH}.pub)
ssh ${USER}@${IP} "\
    mkdir -p ~/.ssh && \
    echo $pub >> .ssh/authorized_keys && \
    chmod 700 ~/.ssh && \
    chmod 600 ~/.ssh/authorized_keys"

```
{% endcode %}
{% endtab %}

{% tab title="🐧 Linux" %}
{% code title="connect-server.sh" %}
```bash
#!/usr/bin/bash

read -p 'Username: ' USER
read -p 'IP adress: ' IP
read -p 'Key path (./.ssh/id_rsa): ' KEY_PATH
ssh-keygen -t ecdsa -b 521 -f ${KEY_PATH}
ssh ${USER}@${IP} "\
    mkdir -p ~/.ssh && \
    echo \"`cat ~/.ssh/id_rsa.pub`\" && \
    chmod 700 ~/.ssh && \
    chmod 600 ~/.ssh/authorized_keys"
```
{% endcode %}
{% endtab %}
{% endtabs %}

* 🧐 `ssh ${USER}@${IP}`komutu ile `OpenSSH` varlığını kontrol edil, tepki veriyorsa vardır
* 🔑 `ssh-keygen -t ecdsa -b 521 -f ${KEY_PATH}` komutu ile `ssh` anahtarı oluşturun
  * SSH, secure shell anlamına gelir ve uzaktan terminal yönetim protokoldür
  * SSH anahtarlarından `pub` uzantılı olan açık anahtardır ve sunucuya aktarılması gerekir
  * Diğer anahtar kapalı olandır ve **paylaşılmaması** gerekmektedir
* ✴️ Bu adımlar **sadece Windows kullanıcıları** tarafından `powershell` üzerinden yapılmalıdır
  * 📢 `Get-Service -Name ssh-agent | Set-Service -StartupType Manual` komutu ile `ssh` servisini elle başlatabilmek için yapılandırın
  * ⚙️ `Start-Service ssh-agent` komutu ile `ssh` servisini başlatın
  * ➕ `ssh-add ${KEY_PATH}` komut ile `ssh`anhtarını  `keystores` içerisine anahtarınızı ekleyin
  * Kapalı anahtarınız `keystores` içerinde saklanır
  * Sunucu bağlantılarında bu anahtar deposu kullanılır
* 🚚 `ssh ${USER}@${IP} "\` komutunu yazın ve ardından alttaki komutları girin
  * 📂`mkdir -p ~/.ssh && \` ile sunucuda `ssh`antahtarları dizini yoksa oluşturun
  * ➕`echo (Get-Content ~/${KEY_PATH}.pub) >> .ssh/authorized_keys && \` ile açık anahtarınızı sunucuda onaylı anahtar listesine ekleyin
  * 🐧`echo \"cat ~/.ssh/id_rsa.pub\" && \` komutu ile **Linux işletim sistemini kullananlar** açık anahtarı ekleyebilir
  * 👮‍♂️ `chmod 700 ~/.ssh && \` komutu ile `ssh`dizinini yetkilendirin
  * 👮‍♂️ `chmod 600 ~/.ssh/authorized_keys"` komutu ile anahtarların olduğu dosyaya okunabilmesi için izinleri verin

{% hint style="info" %}
‍🧙‍♂ Detaylı bilgi için 

* [SSH Login Without a Password](https://howchoo.com/g/mmu5ngfimjk/ssh-login-without-password) 
* [Starting ssh-agent on Windows 10 fails: “unable to start ssh-agent service, error :1058”](https://stackoverflow.com/a/53606760/9770490)
* [How to append authorized\_keys on the remote server with id\_rsa.pub key](https://stackoverflow.com/a/23599377/9770490)
* [ssh-agent: agent returned different signature type](https://github.com/PowerShell/Win32-OpenSSH/issues/1263#issuecomment-590947232)

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

