# Telegram <!-- omit in toc -->

Telegram ile ilgili notlarım.

## İçerikler <!-- omit in toc -->

- [Telegram Nedir?](#Telegram-Nedir)
- [Telegram Bot Oluşturma](#Telegram-Bot-Olu%C5%9Fturma)
  - [Telegram bot için `chat_id` alma](#Telegram-bot-i%C3%A7in-chatid-alma)
- [Harici Bağlantılar](#Harici-Ba%C4%9Flant%C4%B1lar)

## Telegram Nedir?

Whatapp alternatifi mesajlaşma uygulamasıdır.

- Kişisel botlar
- Sınırsız grup sayısı

gibi avantajları vardir.

> Özetle, scriptçi (yazılımcı) isen tam senlik 🤓

## Telegram Bot Oluşturma

- İlk telegram'a giriş yapman lazım
- Ardından telegram [BotFather](https://telegram.me/botfather)'a giriş yap
- Sırasıyla alttaki komutları ver:
  - `/start`
  - `/newbot`
- Bot için herhangi bir isim yaz
  - Sonunda `bot` metni olmak zorundadır
  - Örn: `ybot`, `y_bot` vs.
- Ardından sana **token** verilecektir.
  - `12345:TOKEN_DEVAMI`
- Botuna erişmek için `t.me/<bot_ismi>` linkine tıklamalısın

### Telegram bot için `chat_id` alma

- https://api.telegram.org/botXXX:YYYY/getUpdates
  - `XXX:YYYY` yazan kısma **token** verinizi kopyalayın
  - Örn: `https://api.telegram.org/bot12345:TOKEN_DEVAMI/getUpdates`
- Döndürülen metinde `id:...` olarak karşınıza çıkacaktır.

```json
{"ok":true,"result":[{"update_id":...,
"message":{"message_id":...,"from":{"id":123123213,"is_bot":false,"first_name":"... \ud83c\udf41","username":"...","language_code":"en"},"chat":{"id":123123213,"first_name":"... \ud83c\udf41","username":"...","type":"private"},"date":...,"text":"..."}},{"update_id":...,]}
```

> Kaynak [Get Chat id For Telegram](https://pupli.net/2019/02/02/get-chat-id-from-telegram-bot/)

## Harici Bağlantılar

- [5dk'da Telegram Bot'u Oluşturma](https://medium.com/@fatihsarhan/5-dk-da-telegram-botu-nasil-yapilir-1873f18bf59b)
