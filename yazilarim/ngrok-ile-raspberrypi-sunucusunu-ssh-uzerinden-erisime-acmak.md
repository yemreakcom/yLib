# 🌍 Ngrok ile raspberrypi sunucusunu SSH üzerinden erişime açmak

## Ngrok’u İndirmek

*   `snap` ile indirin (önerilen)

    ```bash
    snap install ngrok
    ```

    [ngrok - download](https://ngrok.com/download)
* Manuel indirmek
  * Raspberry için `Linux` `ARM64` (32 bit ise veya bilmiyorsanız `ARM32`) seçip indirin

## Ngrok’a Kayıt Olmak

* Kayıt olduğunuz zaman site üzerinden `IP address` değerini görebilirsiniz
* [Sign Up](https://ngrok.com/signup) alanından kayıt olun
* [Your Authtoken](https://dashboard.ngrok.com/get-started/your-authtoken) alanındaki token bilginizi kopyalayın

## Ngrok’u arkaplanda çalıştırma

*   [https://github.com/YEmreAk/systemd-ngrok](https://github.com/YEmreAk/systemd-ngrok) projesini klonlayın

    ```bash
    TOKEN=""  # Token bilginizi buraya yazın
    git clone <https://github.com/YEmreAk/systemd-ngrok>
    cd system-ngrok
    sudo ./install.sh $TOKEN
    rm -rf system-ngrok
    ```
*   `process`'i iptal etmek için

    ```bash
    kill -9 "$(pgrep ngrok)"
    ```

[Daemon / Silent Mode · Issue #57 · inconshreveable/ngrok](https://github.com/inconshreveable/ngrok/issues/57#issuecomment-811814006)

## SSH ile bağlanmak

* `ssh` için 22 portu kullanılır
* [Ngrok \~ Agents](https://dashboard.ngrok.com/tunnels/agents) üzerinden `IP` alanı altındaki adrese tıklayıp `tunnel` değerinizi alın

```bash
# tcp://2213.tcp.eu.ngrok.io:16323 için
USERNAME=""
ssh $USERNAME@2213.tcp.eu.ngrok.io -p 16323
```

## VNC ile Bağlanmak

* `VNC` için 5900 portu kullanılır
*   [Ngrok \~ Agents](https://dashboard.ngrok.com/tunnels/agents) üzerinden `IP` alanı altındaki adrese tıklayıp `tunnel` değerinizi alın

    ```bash
    # tcp://2213.tcp.eu.ngrok.io:16323
    2213.tcp.eu.ngrok.io:16323
    ```

## Referanslar

[https://github.com/vincenthsu/systemd-ngrok](https://github.com/vincenthsu/systemd-ngrok)

[How to set auto run after boot on raspberry pi? · Issue #345 · inconshreveable/ngrok](https://github.com/inconshreveable/ngrok/issues/345#issue-158700406)

[Connect to your Raspberry Pi from anywhere using ngrok](https://medium.com/@gaelollivier/connect-to-your-raspberry-pi-from-anywhere-using-ngrok-801e9fd1dd46)

[SSH into Remote Linux Machine Using ngrok](https://www.endtoend.ai/tutorial/ngrok-ssh-forwarding/)

[Raspberry Pi - SSH, VNC Access from every whare using ngrok and crontab](https://www.youtube.com/watch?v=js1lxR12hHo)
