---
description: >-
  PyTest ile testlerinizi daha verimli hale getirin! Testlerinizi verimli bir
  şekilde düzenlemek için pytest-dependency ve pytest-order modüllerini
  kullanmayı keşfedin.
---

# 🧪 PyTest ile Testlerinizi Yönetin: Bağımlılıklar ve Sıralama

## 🔗 Bağımlılık Oluşturma

```python
pip install pytest-dependency
```

```python
class TestClass:
	@mark.dependency(name="test_init")
  async def test_init(self):
      ...

	@mark.dependency(depends=["test_init"])
  async def test_cancel_order_error(self):
      ...
```

* `name` ile teslerin adını tanımlarız
* `depends` alanındaki `name` ile tanımladığımız testler çalışmadan çalışmaz, atlanır
* Sırası çalıştırmak için `pytest-order` eklentisini kurmanız gerekir

## 🔢 Sıralamak

```python
pip install pytest-order
```

```python
import pytest

@pytest.mark.order(1)
def test_a():
    assert True

@pytest.mark.order(2)
def test_b():
    assert True

@pytest.mark.order(3)
def test_c():
    assert True
```

* Sırasıyla `1`, `2` ve `3`. testler çalışır
