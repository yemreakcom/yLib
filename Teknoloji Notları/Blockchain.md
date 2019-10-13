---
description: Popüler bir güvenlik sistemi olan yapı hakkındaki notlarım
---

# 🔐 Blockchain

## ❔ Blockchain Nedir

Peer to peer (aracısız) mantığını güden bu yapıda, bilgiler zincir olarak saklanır. Her bir bilgi bir öncekinin hash'ini (kimliğini) tutar.

## ⛓ Zincir Yapısının Korunması

Dışarıdan müdahale ile yapılan Olası bir veri değişikliğinde zincir yapısı bozulur.

- Hash işlemi, bloğun içerdiği bilgilerin hepsini ele alarak hesaplanır ve veri değişmesi kimliğini değiştirir. Blok kullanılırken hesaplanan yeni kimlik ile eski kimlik birbirine uymaz.
- Kimlik değeri bir şekilde elden atanır ise, bir sonrasındaki blokta tutulan şu anki bloğumuzun kimliği ile yeni kimlik uyuşmaz ve zincir yapısı bozulur.
- Zincirin bütünü değiştirilirse; zincir diğer kopyalarına bakılır ve değişim %50'den fazla baskınlığa sahip değilse kabul edilmez ve eski yapıya dönülür.
- Değiştirilen zincirin çok sayıda kopyalanmasını engellemek için blockchain'in blok üretme zorluğu vardır ve "**Proof of Work**" diye adlandırılır.

## 🥴 Karma Notlar

- Blockchain sistemini kullanan platformlarda (bitcoin gibi), hesapta para değeri saklanmaz. Her bir zincir incelenir ve sizin net para değeriniz hesaplanır.
- Her bir işlem sıraya alınır ve belli süre içerisinde blok yapım sayısı sınırlandırılmıştır. (her 10dk en fazla 1 blok gibi)

## 👨‍💻 Örnek Algroitma

JavaScript ile kodladığım örnek kod için [buraya](https://github.com/yedhrab/YBlockchain) tıklayabilir veya nasıl yapıldığını anlatan video serisine [buradan](https://www.youtube.com/watch?v=zVqczFZr124&list=PLzvRQMJ9HDiTqZmbtFisdXFxul5k0F-Q4) ulaşabilirsin.
