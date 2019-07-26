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
- [PW3 Postal Codes](#pw3-postal-codes)

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

## PW3 Postal Codes

<details>

<summary>Göster</summary>

```python
[('B11 4BW', 20673),
 ('B18 7AL', 19001),
 ('B21 9RY', 29103),
 ('B23 6DJ', 24859),
 ('B70 7AW', 36531),
 ('BB11 2DL', 34356),
 ('BB2 1AX', 28254),
 ('BB3 1PY', 54514),
 ('BB4 5SL', 29388),
 ('BB7 2JG', 44585),
 ('BB8 0JZ', 54380),
 ('BB9 7SR', 38224),
 ('BD3 8QH', 21010),
 ('BH18 8EE', 39413),
 ('BH23 3AF', 32545),
 ('BL1 8TU', 26132),
 ('BL3 5HP', 27147),
 ('BL9 0NJ', 32062),
 ('BL9 0SN', 35275),
 ('CB9 8HF', 51337),
 ('CH1 4DS', 34915),
 ('CH65 6TG', 25090),
 ('CT11 8AD', 44358),
 ('CV1 4FS', 37210),
 ('CW1 3AW', 64104),
 ('CW5 5NX', 38797),
 ('CW7 1AT', 43164),
 ('DA1 2HA', 26075),
 ('DA11 8BZ', 24090),
 ('DN22 7XF', 43091),
 ('DN34 4GB', 48013),
 ('FY2 0JG', 69118),
 ('FY4 1TJ', 62886),
 ('FY5 2TZ', 44258),
 ('FY7 8GU', 34473),
 ('GL1 3PX', 38120),
 ('GL50 4DP', 74822),
 ('GU9 9QS', 32131),
 ('HA0 4UZ', 22755),
 ('HA3 7LT', 32113),
 ('HG1 5AR', 32684),
 ('HU7 4DW', 49107),
 ('KT14 6DH', 26758),
 ('KT6 6EZ', 38975),
 ('L31 0DJ', 32065),
 ('L36 7XY', 22965),
 ('L5 0QW', 24676),
 ('L7 6HD', 42569),
 ('LA1 1PN', 47335),
 ('LE10 1DS', 49335),
 ('LE18 2EW', 37144),
 ('LE5 3GH', 28654),
 ('LN2 2JP', 46173),
 ('LS9 9EF', 48051),
 ('M11 4EJ', 23166),
 ('M26 2SP', 37718),
 ('M30 0NU', 25597),
 ('M35 0AD', 37632),
 ('ME8 8AA', 25257),
 ('N9 7HD', 30706),
 ('NE10 9QG', 39882),
 ('NE24 1DX', 50491),
 ('NE37 2PU', 57500),
 ('NE38 7NQ', 52803),
 ('NG7 3GW', 17698),
 ('NG7 5HY', 24903),
 ('NN16 8DN', 50771),
 ('NW10 8RY', 21553),
 ('OL1 1NL', 41046),
 ('OL11 1DN', 21567),
 ('OL4 1YN', 24687),
 ('OL9 7AY', 28394),
 ('PL7 1AD', 65051),
 ('RM3 9SU', 25476),
 ('S63 9EH', 34787),
 ('S65 1DA', 71683),
 ('S74 9AF', 55305),
 ('SE1 6JP', 45030),
 ('SE15 5LJ', 15258),
 ('SK11 6JL', 110071),
 ('SK6 1ND', 28313),
 ('SM3 8EP', 24965),
 ('SM6 0HY', 46016),
 ('SR4 7XF', 49843),
 ('SR5 2LT', 44895),
 ('SS0 7AF', 21569),
 ('SS13 3HQ', 38513),
 ('SS8 0JA', 45848),
 ('SS9 5UU', 26095),
 ('ST1 4PB', 24227),
 ('ST3 6AB', 38705),
 ('ST8 6AG', 34516),
 ('TN24 0GP', 16955),
 ('TN34 1BA', 47440),
 ('TR1 2JA', 40194),
 ('TS1 2NX', 47623),
 ('TS10 4NW', 45161),
 ('TS17 0EE', 68388),
 ('TS23 2DG', 31646),
 ('TS24 7PW', 58207)]
```

</details>
