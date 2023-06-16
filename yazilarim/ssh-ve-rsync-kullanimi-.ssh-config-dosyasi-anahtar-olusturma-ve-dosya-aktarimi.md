---
description: >-
  SSH bağlantıları, anahtar oluşturma, dosya indirme ve rsync kullanarak dosya
  aktarımı gibi konuları detaylıca anlatan bir kılavuz.
---

# 🔐 SSH ve Rsync Kullanımı: .ssh/config Dosyası, Anahtar Oluşturma ve Dosya Aktarımı

## 📁 `.ssh/config` dosyası ne işe yarar

```python
Host my.host
    HostName 123.123.32.231
    User username
		IdentityFile ".ssh/rsa.pem"
		ForwardAgent yes

# Tüm sunucular için ortak ayarlar
Host *
  ForwardAgent yes
  AddKeysToAgent yes
```

* `.ssh/config` dosyasına sunuculara bağlanmak için gerekli bilgileri kaydederiz
* `HostName` sunucunun IP adresi
* `User` sunucudaki kullanıcı adı
* `IdentityFile` sunucuya bağlanmak için kullanılacak anahtar dosya
* `AddKeysToAgent` tekrardan bağlantılar için anahtarı saklar
*   `ForwardAgent` lokal **agent** bilgilerini uzan sunucuya aktarır

    * **Git SSH auth** varsa eğer lokalde, karşı sunucuya da bu aktarılır

    [What is SSH Agent Forwarding and How Do You Use It?](https://www.howtogeek.com/devops/what-is-ssh-agent-forwarding-and-how-do-you-use-it/)

> `ssh my.host` komutu ile aslında `ssh -A username@123.123.32.231 -i .ssh/rsa.pem` kodunu yazmış oluruz

## 🔑 SSH key oluşturup sunucuya yüklemek

```bash
#!/usr/bin/env zsh

ADDRESS="yia@raspberrypi.local"
KEY_ID="raspi"

# SSH key oluşturma
KEY_PATH="$HOME/.ssh/${KEY_ID}_ecdsa"  # veya _rsa
ssh-keygen -t ecdsa -b 521 -f ${KEY_PATH}

# SSH keyi sunucuya kopyalama ve yetkilendirme
ssh-copy-id -i $KEY_PATH.pub $ADDRESS
# cat $KEY_PATH.pub | $ADDRESS "mkdir -p ~/.ssh; cat >> ~/.ssh/authorized_keys"

# SSH keyi yerel anahtarlara ekleme (eğer şifre istenirse anahtar eklenmeli)
ssh-add $KEY_PATH

# SSH ile adrese bağlanma
ssh $ADDRESS -A

# Apple keychain üzerine ekleme
# chmod 400 $KEY_PATH
ssh-add --apple-use-keychain $KEY_PATH  # Sadece passphrase için çalışır
```

[How can I permanently add my SSH private key to Keychain so it is automatically available to ssh?](https://apple.stackexchange.com/a/250572)

## ⬇️ Sunucu üzerinden hızlıca dosya indirme

```bash
REMOTE="username@ip.adress"
SOURCE="path"
DESTINATION="path"

scp -r $REMOTE:$SOURCE $DESTINATION
rsync -avzrt --progress "$REMOTE:$SOURCE" "$DESTINATION" 
```

## 🔄 `rsync` kullanarak dosya aktarımı

## ❌ Bazı Dosyaları Hariç Tutma

* **`rsync`** kullanarak hariç tutulacak dosya desenlerini belirtmek için aşağıdaki örnekleri kullanabilirsiniz:
  * **`.log`**: .log uzantılı tüm dosyaları hariç tutar.
  * **`.png`**: .png uzantılı tüm dosyaları hariç tutar.
  * **`/dirname/`**: dirname dizinini hariç tutar.
  * **`/dirname/*`**: dirname dizinindeki tüm dosyaları hariç tutar.
  * **`/dirname/file.txt`**: dirname dizinindeki file.txt dosyasını hariç tutar.
*   **`rsync`** için birden fazla desen belirtebilirsiniz **`--exclude`** seçeneği ile, örneğin:

    * Bu `.pyc` ve `.log` uzantılı tüm dosyaları, ayrıca /tmp/ dizinini hariç tutacaktır.

    ```bash
    rsync -av --exclude=*.pyc --exclude=*.log --exclude=/tmp/ . /path/to/destination
    ```
*   Ayrıca, **`--exclude-from`** seçeneğiyle hariç tutulacak dosyaları içeren bir dosya belirtebilirsiniz

    * `exclude-list.txt` dosyasında listelenen desenlerle eşleşen tüm dosyaları hariç tutacaktır.
    * Dosya, her satıra bir `pattern` içermelidir

    ```bash
    rsync -av --exclude-from=exclude-list.txt . /path/to/destination
    ```

## 💡 Örnek Kullanım

* Bu komut `exclude-list.txt` dosyasında listelenen dosyaları ve dizinleri hariç tutacaktır
* **`a`** seçeneği arşivleme modunu etkinleştirir, yani dosya meta verilerini (öznitelikleri, izinleri, vb.) korur.
* **`v`** seçeneği etkinleştirilirse, rsync'in ne yaptığını gösterir.
* **`z`** seçeneği etkinleştirilirse, dosyaları sıkıştırır ve yükleme sırasında çıkarır.
* **`e ssh`** seçeneği rsync'in SSH ile nasıl bağlantı kuracağını belirtir.
* `E`, ile dosya içerisindeki `Icon` gibi bilgiler de aktarılır
* `r`, ile alt dizinlerde de ilerler
* `t`, dosyanın son değişiklik bilgisini korur

```bash
rsync -avz --exclude-from=exclude-list.txt -e ssh /local/path/ user@remote-server:/path/to/destination
```

```bash
*.log
/tmp/
```

## 📚 References

* [ChatGPT 💁‍♂️](https://chat.openai.com/chat)
