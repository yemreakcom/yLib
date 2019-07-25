# Python CodeSnippets <!-- omit in toc -->

<!-- TODO: Sonradan bunlara başlık ekle -->

## İçerikler <!-- omit in toc -->

- [List İşlemleri](#list-%c4%b0%c5%9flemleri)
- [Verileri Sınıflara Göre Gruplama](#verileri-s%c4%b1n%c4%b1flara-g%c3%b6re-gruplama)
- [İstatistik](#%c4%b0statistik)
- [Dict](#dict)
- [Yüksek Miktardaki Verilerle İşlemler](#y%c3%bcksek-miktardaki-verilerle-%c4%b0%c5%9flemler)
  - [Verilerin Formatı](#verilerin-format%c4%b1)
  - [Verilerin İşlenmesi](#verilerin-%c4%b0%c5%9flenmesi)

## List İşlemleri

```python
[x for x in iter if x = 1]
```

```python
sum([obj["items"] for obj in groups[name]]
```

```python
[(name, sum([obj["items"] for obj in groups[name]])) for name in groups]
```

```python
lis = [("a",1) ...]
max(lis, key=lambda x:x[1]) # 2. elemana göre hesaplama
```

## Verileri Sınıflara Göre Gruplama

```python
def group_by_field(data, fields):

    def generate_keys(data, field):
        yield set([x[field] for x in data])

    groups = {}
    for field in fields:
        group = {name: [] for name in generate_keys(data, field)}
        groups[field] = group

    for x in data:
        groups[field][x[field]].append(data)

    return groups
```

## İstatistik

```python
import math
import statistics

def grap_data(scripts, key):
    return [script[key] for script in scripts]

def standart_deviation(datas, avg):
    nominator = 0
    for data in datas:
        nominator += (data - avg) ** 2

    return math.sqrt(nominator / len(datas))

def median(datas, quartile = 2):
    center = len(datas) // 2

    if quartile == 1:
        center = center // 2
    if quartile == 3:
        center += center // 2

    datas = sorted(datas)

    if len(datas) % 2 == 0:
        med = (datas[center - 1] + datas[center]) / 2
    else:
        med = datas[center]

    return med

def describe(key):

    datas = grap_data(scripts, key)

    total = sum(datas)
    avg = total / len(datas)
    s = standart_deviation(datas, avg)

    med = median(datas)
    q25 = median(datas, 1)
    q75 = median(datas, 3)

    return (total, avg, s, q25, med, q75)
```

## Dict

```python
for field in groups:
    # print(field)
    for name in groups[field]:
        # print(name)
        for data in groups[field][name]:
            print(data)
            break
        break
    break
```

## Yüksek Miktardaki Verilerle İşlemler

### Verilerin Formatı

```python
{
    field: {
        name : [ # Be careful it's list (not dict)
            data: {
                "items": 5 # some value
            },
            ...
        ],
        ...
    },
    ...
}
```

### Verilerin İşlenmesi

```python
def group_by_field(data, fields):

    def create_keys(data, field):
        return set([x[field] for x in data])

    groups = {}
    for field in fields:
        group = {name: [] for name in create_keys(data, field)}
        groups[field] = group

    for x in data:
        groups[field][x[field]].append(x)

    return groups

def get_max_item(groups, attribute):
    max_items = []
    for group in groups:
        field = groups[group]

        sums = []
        for name in field:
            sums.append((name, sum([data[attribute] for data in field[name]])))

        max_items.append(max(sums, key=lambda x:x[1]))

    return max_items
```
