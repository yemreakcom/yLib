# Activity Notları <!-- omit in toc -->

Android üzerinde her sayfa activity olarak adlandırılır, burada da onlar hakkında bilgilere yer verilecektir.

## Gecikmeli Activity Başlatma

```kt
Handler().postDelayed({    startActivity(Intent(this, SnakeActivity1::class.java))
}, 400)
```

## Arkaplanda Çalıştırma

```kt
override fun onCreate(savedInstanceState: Bundle?) {
    // Arkaplanda çalıştırma
    moveTaskToBack(true)
    super.onCreate(savedInstanceState)
    setContentView(R.layout.activity_share)

    ...
}
```

## Bütün Eski Activity'leri Sonlandırıp Yeni Activity Açma

```kt
val intent = Intent(this, MainActivity::class.java)
intent.flags = Intent.FLAG_ACTIVITY_NEW_TASK or Intent.FLAG_ACTIVITY_CLEAR_TASK // Tüm işlemleri bitirme
finish() // İşlemi sonlandırma
startActivity(intent)
```
