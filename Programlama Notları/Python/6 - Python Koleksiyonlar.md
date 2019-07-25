# Python Koleksiyonlar <!-- omit in toc -->

## İçerikler <!-- omit in toc -->

- [Koleksiyonlar Nedir ? (Collection)](#koleksiyonlar-nedir--collection)
- [Namedtuple](#namedtuple)
  - [NamedTuple ile Üretilen Kod](#namedtuple-ile-%c3%9cretilen-kod)
- [Deque](#deque)
  - [Deque için Verimlilik Hesapbı](#deque-i%c3%a7in-verimlilik-hesapb%c4%b1)
- [Counter](#counter)
- [OrderedDict](#ordereddict)
- [DefaultDict](#defaultdict)
  - [DefaultDict Avantajı](#defaultdict-avantaj%c4%b1)

## Koleksiyonlar Nedir ? (Collection)

Python'da hazırlarnmış verimli veri yapılarıdır.

## Namedtuple

- Özel adlandırılmış tuple değerleridir
- `verbose=True` olursa üretilen kodu görürüz

> `namedtuple`, neredeyse hiç hafıza maliyeti olmadan kendi kendini belgeleyen kod oluşturmak için harika bir yoldur.

```python
from collections import namedtuple
Vector3 = namedtuple('Vector', ['x', 'y', 'z'], verbose=True)

vec = Vector3(1,2,3)
vec.x, vec.y, vec.z

vec.x = 5 # Çalışmaz, çünkü tuple idir. (Dict'ten varkı burada belli olur)


def tfunc(a,b,c):
    print(a,b,c)

tfunc(*vec)
```

### NamedTuple ile Üretilen Kod

```python
from builtins import property as _property, tuple as _tuple
from operator import itemgetter as _itemgetter
from collections import OrderedDict

class Vector(tuple):
    'Vector(x, y, z)'

    __slots__ = ()

    _fields = ('x', 'y', 'z')

    def __new__(_cls, x, y, z):
        'Create new instance of Vector(x, y, z)'
        return _tuple.__new__(_cls, (x, y, z))

    @classmethod
    def _make(cls, iterable, new=tuple.__new__, len=len):
        'Make a new Vector object from a sequence or iterable'
        result = new(cls, iterable)
        if len(result) != 3:
            raise TypeError('Expected 3 arguments, got %d' % len(result))
        return result

    def _replace(_self, **kwds):
        'Return a new Vector object replacing specified fields with new values'
        result = _self._make(map(kwds.pop, ('x', 'y', 'z'), _self))
        if kwds:
            raise ValueError('Got unexpected field names: %r' % list(kwds))
        return result

    def __repr__(self):
        'Return a nicely formatted representation string'
        return self.__class__.__name__ + '(x=%r, y=%r, z=%r)' % self

    def _asdict(self):
        'Return a new OrderedDict which maps field names to their values.'
        return OrderedDict(zip(self._fields, self))

    def __getnewargs__(self):
        'Return self as a plain tuple.  Used by copy and pickle.'
        return tuple(self)

    x = _property(_itemgetter(0), doc='Alias for field number 0')

    y = _property(_itemgetter(1), doc='Alias for field number 1')

    z = _property(_itemgetter(2), doc='Alias for field number 2')

```

## Deque

List objelerinin uç noktaları ile ilgilenen bir yapıdır.

- List'e göre optimize edilmiştir
  - List için $O(N)$ Dque için $O(1)$
  - ${Verim}_{O(1)} > {Verim}_{O(N)}$

```python
from collections import deque

d = deque([2,3,4,5]) # deque([2, 3, 4, 5])
d.append(10) # deque([2, 3, 4, 5, 10])
d.appendleft(20) # deque([20, 2, 3, 4, 5, 10])
```

### Deque için Verimlilik Hesapbı

> Süreleri **IPython**'da `%%timeit` kodu ile hesaplayabilirsin

```python
# %%timeit
d = deque()
for i in range(40000):
    d.appendleft(i)

# 3.76 ms ± 35.6 µs per loop (mean ± std. dev. of 7 runs, 100 loops each)
```

```python
# %%timeit
l_ = list()
for i in range(40000):
    l_.insert(0, i)

# 410 ms ± 5.94 ms per loop (mean ± std. dev. of 7 runs, 1 loop each)
```

```python
list(d) == l_ # True
```

## Counter

`list` objelerini sayar `dict` yapısında Anahtar-Miktar ikilisi döndürür.

- Olmayan anahtarlar için `0` değeri döndürülür
- En fazla tekrar eden anahtarlar için `most_common(<gösterilecek_anahtar_sayısı>)` fonksiyonu kullanılır

```python
from collections import Counter
ele = ['a','b','a','c','b','b','d']
c = Counter(ele)

# Counter({'b': 3, 'a': 2, 'c': 1, 'd': 1})

c['a'], c['z'] # (2, 0)
c.most_common(5) # [('b', 3), ('a', 2), ('c', 1), ('d', 1)]
```

## OrderedDict

Sıralanmış `dict` olarak geçmektedir

> Sıralandığı için $O(1)$ erişim hızına sahiptir.

## DefaultDict

`dict` verilerinde en önemli sorun olmayan anahtar (_key_) verileridir.

- Olmayan anahtarlar için varsayılan değer atanır
- Kodda daha temiz yapı sunar
- `defaultdict(<type>)` şeklinde tanımlanır

### DefaultDict Avantajı

```python
from collections import defaultdict
def count_default(x):
    count_dict = defaultdict(int)
    for ele in x:
        count_dict[ele] += 1 # count_dict'te olmayanların değeri 0 olduğundan 1 arttırılabilir
    return count_dict
count_default(ele)
```

```python
def count(x):
    count_dict = {}
    for ele in x:
        if ele in count_dict.keys():
            count_dict[ele] += 1
        else: # count_dict'te olmayan veriler için 1 atanmalıdır
            count_dict[ele] = 1
    return count_dict
count(ele)
```
