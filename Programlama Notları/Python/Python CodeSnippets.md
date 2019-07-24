# Python CodeSnippets

<!-- TODO: Sonradan bunlara başlık ekle -->

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
