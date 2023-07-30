# ℹ aiohttp.ClientSession() içerisideki params, data ve json ne işe yarar

1.  📋 `params`: URL'nin sonunda bir soru işaretiyle başlayan ve genellikle anahtar-değer çiftlerinden oluşan sorgu dizelerini oluşturmak için kullanılır.

    ```python
    params = {'tür': 'komedi'}
    async with session.get('<http://filmtadında.com/>', params=params) as resp:
        data = await resp.text()

    ```
2.  📦 `data`: HTTP isteğinin gövdesinde göndermek istediğiniz veriyi belirtir. POST isteklerinde sıklıkla kullanılır.

    ```python
    data = {'name': 'John', 'email': 'john@example.com', 'password': 'secret'}
    async with session.post('<http://website.com/api/users>', data=data) as resp:
        data = await resp.text()

    ```
3.  📄 `json`: HTTP isteğinin gövdesinde göndermek istediğiniz JSON verisini belirtir. JSON formatındaki veriyi otomatik olarak ayarlar ve sunucuya iletir.

    ```python
    json_data = {'name': 'John', 'email': 'john@example.com', 'password': 'secret'}
    async with session.post('<http://website.com/api/users>', json=json_data) as resp:
        data = await resp.text()

    ```

> Yukarıdaki kod parçaları, `aiohttp` kütüphanesi kullanılarak bir aiohttp.ClientSession nesnesi (`session`) içinde çalışacak şekilde tasarlanmıştır. Asenkron I/O, özellikle ağ isteklerinde yüksek performans sağlar. Bu kod parçalarını çalıştırmadan önce, `aiohttp` kütüphanesini kurmanız ve bir `aiohttp.ClientSession`oluşturmanız gerekmektedir.
