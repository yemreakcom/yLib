---
description: Tarayıcılar üzerinde otomatize işler yapmak için kullanılan bir araçtır.
---

# 🤖 Selenium

##  🗽 Açıklama

* Selenium'un python dokümantasyonu için [buraya](https://selenium-python.readthedocs.io/index.html) bakabilirsin
  * İtici bir dokümantasyon arıyorsan [buraya](https://seleniumhq.github.io/selenium/docs/api/py/api.html) bakabilirsin 😒

> **Python** dili ve **Chromedriver** baz alınmıştır.

## Seleinium Kurulumu

Selenium tarayıcı driver'ı kullanarak çalışmaktadır

* ChromeDriver'ı [buradan](http://chromedriver.chromium.org/) indirin
* ChromeDriver'ınızı uygun bir konuma koyun, ileride yol verisi selenium'a aktarılacaktır

> Projenizin içerisinde `utils` dizini açıp içine `chromedriver` adlı dosyayı atabilirsiniz, ileride bu şekilde değerlendirilecektir

### Conda Üzerinden Kurulum

Selenium için özel ortam oluştururak kurulum yapmak daha sağlıklıdır.

```bash
conda create -n selenium selenium
```

> Kurulum sonrasında ortamı `conda activate selenium` ile aktif etmeyi unutmayın.

## Chromedriver'ı Yapılandırma

### Arayüz Olmadan Chromedriver'ı Kullanma \(İsteğe Bağlı\)

Selenium aracı chrome üzerinde çeşitli özelliklerle çalışabilmekte \(örn: arayüz olmadan, sessizce çalışabilir\)

> [Google colab](https://colab.research.google.com/) üzerinde kullanmak istersen bu ayarlar zorunludur, kaynağa [buradan](https://stackoverflow.com/a/54077842) erişebilirsin.

```python
options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-gpu')
options.add_argument('--disable-setuid-sandbox')
```

### Chromedriver'ı oluşturma

Chromedriver öğesini oluşturmak için alttaki yapıyı kullanmak zorundayız:

> Tüm işlemleri oluşturduğumuz `driver` objesi ile yapmaktayız.

```python
# Modülü dahil etme
from selenium import webdriver

driver = webdriver.Chrome(
    executable_path=<chromedriver_yolu>,
    options=<ek_ayarlar>
)
```

* `<chromedriver_yolu>` Chromedriver dosyasının yolu
  * Örn: `"utils/chromedriver"`
* `<ek_ayarlar>` Ek yapılandırma ayarları \(İsteğe bağlı\)
  * Örn: Yukarıdaki alanda tanımlanan `options` objesi

### Websitesine Erişme

```python
driver.get(<URL>)
```

* `<URL>` Girmek istediğimiz sitenin adresi
  * Örn: `"www.yemreak.com"`

### Websitesinde Eleman Bulma

Kullanım şekli `driver.<eleman_bulma_metodu>` şeklindedir.

> Kaynak için [buraya](https://selenium-python.readthedocs.io/locating-elements.html#locating-elements) bakabilirsin.

* find\_element\_by\_id
* find\_element\_by\_name
* find\_element\_by\_xpath
* find\_element\_by\_link\_text
* find\_element\_by\_partial\_link\_text
* find\_element\_by\_tag\_name
* find\_element\_by\_class\_name
* find\_element\_by\_css\_selector

#### Websitesinde Çoklu Eleman Bulma

* find\_elements\_by\_name
* find\_elements\_by\_xpath
* find\_elements\_by\_link\_text
* find\_elements\_by\_partial\_link\_text
* find\_elements\_by\_tag\_name
* find\_elements\_by\_class\_name
* find\_elements\_by\_css\_selector

### Websitesine İçerik Bekleyerek Erişme

Bazen websiteleriindeki içerikler yüklenmeden işlem yapmak istemeyiz. Bunun için `WebDriverWait` objesini kullanmaktayız.

**Temel kullanım:**

```python
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

WebDriverWait(driver, <bekleme_süresi>).<bekleme_şekli>(
    EC.<koşul>(<tanımlayıcı>)
)
```

* `<bekleme_süresi>` En uzun bekleme süresi. Eğer bu vakte kadar istenen sağlanmazsa hata fırlatır \(TimoutException\)
  * Örn: `10` 10 saniye bekler, koşul sağlanmazsa hata fırlatır
* `<bekleme_şekli>` Koşul olana kadar ya da olmayana kadar bekleme
  * `until` Koşul olana kadar bekle
  * `until_not` Koşul olmayana kadar bekle
* `<koşul>` Selenium'a özgü bekleme koşulu
  * Selenium koşullarının listesine [buradan](https://selenium-python.readthedocs.io/waits.html) erişebilirsin.
  * Selenium bekleme koşullarının detayı için [buraya](https://seleniumhq.github.io/selenium/docs/api/py/webdriver_support/selenium.webdriver.support.expected_conditions.html?highlight=expected_conditions) bakabilirsin.
  * Örn: `presence_of_element_located` Eleman oluşana kadar bekleme

> Tüm işlemler `try` - `except` bloğu arasında yapılamlıdır, aksi takdirde ufak sorunlarda programınız kapanacaktır.

#### Eleman Oluşana Kadar Bekleme

```python
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

try:
    driver.get(config.URL) # Siteye erişme

    # ID'si verilen elemanın oluşmasını bekleme
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "yemreak"))
    )

    # Class ismi verilen elemanın oluşmasını bekleme
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "active"))
    )

    # CSS'i verilen elemanın oluşmasını bekleme
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "div.yemreak"))
    )
finally:
    driver.close() # Driver'ı kapatma
```

## Websitesinde Javascript Derleme

Javascript'i `driver.execute_script("<script>")` metodu ile derleyebilirsin.

* `<script>` Javascript metni

### Dosyadan Javascript Derleme

Dosyada javascript derlemek için dosyayı `jsmin` modülü ile **minify** etmen gerekmektedir.

```python
from jsmin import jsmin

def minify(file_path):
    """ Dosyayı minify etme
    """
    with open(file_path) as js_file:
        return jsmin(js_file.read(), quote_chars="'\"`")

driver.execute_script(minify(<dosya_yolu>))
```

* `<dosya_yolu>` Minify edilecek ve derlenecek dosyanın yolu
  * Örn: `javascripts/yemreak.js`

### Javascript İşlemleri

Javascript için önemli notlar:

* Javascript objelerinin tanımlanması için `window.` ön eki ile yapman gerekmekte, aksi takdirde selenium içerisinde kullanamazsın.
  * Objeleri kullanırken `window.` ön ekini kullanmana gerek yoktur.
* Javascript verilerini python koduna almak için scriptine `return` anahtar kelimesi eklemen gerekmektedir.

```javascript
// main.js dosyası
window.temp = () => {
    console.log("Yemreak")
}

window.deger = 5

function calismas() {
    console.log("Bu metodu selenium bulamaz")
}
```

```python
driver.execute_script(minify("main.js"))) # Javascript dosyasını derler
driver.execute_script("temp()") # Yemreak yazar
driver.execute_script("calismaz()") # Metod bulunamadı hatası verir
driver.execute_script("return deger") # 5 değerini döndürür
```

## Harici Bağlantılar

* [Colab üzerinden selenium kullanmak](https://stackoverflow.com/a/54077842)
* [Selenium Örnekleri](https://www.seleniumhq.org/docs/03_webdriver.jsp)

