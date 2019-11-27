# 🚀 İlk Uygulama

## 👣 Temel İşleyiş

* `<module_name>` adında dizin oluşturulur
* `<module_name>.c` adında yeni dosya oluşturulur
* `<module_name>_main` adındaki main fonksiyonu altında işlemler yapılır
* Aynı dizine  `CMakeLists.txt` adında cmake dosyası oluşturulur

```c
px4_add_module(
    MODULE examples__px4_simple_app
    MAIN px4_simple_app
    STACK_MAIN 2000
    SRCS
        px4_simple_app.c
    DEPENDS
    )
```

{% hint style="warning" %}
📢 CMakeList dosyasının formatı [buradaki](https://github.com/PX4/Firmware/blob/v1.9.0/cmake/px4_add_module.cmake) yapıya uygun olmalıdır
{% endhint %}

## 🛫 FixedWing

{% embed url="https://github.com/PX4/Firmware/blob/master/src/examples/fixedwing\_control/main.cpp" %}

## 🔗 Ayrıntılı Açıklama

{% embed url="https://dev.px4.io/v1.9.0/en/apps/hello\_sky.html" %}

