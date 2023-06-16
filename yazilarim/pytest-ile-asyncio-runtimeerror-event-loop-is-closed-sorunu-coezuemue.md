---
description: >-
  PyTest ve AsyncIO kullanan uygulamanızda 'Event loop is closed' sorunu mu
  yaşıyorsunuz? Bu rehberde, session kapsamında ortak bir event_loop kullanarak
  bu hatayı nasıl çözeceğinizi öğrenin.
---

# 🔄 pytest ile asyncio RuntimeError: Event loop is closed sorunu çözümü

* Tüm `session` içerisinde ortak `event_loop` kullanmamız gerekir
* `pytestmark` işleminden önce gelmesine dikkat edin

```python
from pytest import mark, fixture
from asyncio import get_event_loop_policy
from typing import Any

@fixture(scope="session")
def event_loop(request: Any):
    loop = get_event_loop_policy().new_event_loop()
    yield loop
    loop.close()

pytestmark = mark.asyncio(timeout=5, scope="session")
```
