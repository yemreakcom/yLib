---
description: >-
  Python kodunda gelen ImportError: attempted relative import with no known
  parent package sorunu için çözüm önerileri
---

# 🐞 Python için ImportError: attempted relative import with no known parent package

* Çalışma dizini üstündeki hiç bir dizinden `import` işlemi yapılamaz
* Çalışma dizini altındaki dizinler arası `import` işlemleri için, her kod dizinin içerisinde `__init__.py` dosyası oluşturularak kod dizini olduğu derleyiciye bildirilmelidir
* Test işlemlerinde gelmesi durumunda da gerekli dizinlerde `__init__.py` dosyası oluşturulur
* Dosyanın içi boş olabilir

<figure><img src="../.gitbook/assets/image.png" alt=""><figcaption></figcaption></figure>

{% embed url="https://python.yemreak.com/yazilar/importerror-attempted-relative-import-with-no-known-parent-package" %}
