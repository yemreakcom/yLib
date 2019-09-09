# Komut İsteminden Python (CLI)

Kullanıcı cmd üzerinden `python <dosya_adı> <argümanlar>` gibi komutlarla programımızı kullanabilir

> Terminal (komut istemi) komutları yazmak için `os.system('<komut>')`

## 🕹 Komut İstemi Paremetre Yönetimi

| Modül                                               | Açıklama                                        |
| --------------------------------------------------- | ----------------------------------------------- |
| argparse                                            | Komut isteminden parametre alma                 |
| [argcomplate](https://stackoverflow.com/a/15289025) | Komut istemi tamamlaması (**linux shell** için) |

## ✨ Komut İsteminde Görsel Bileşenler

| Modül                                                      | Açıklama                    |
| ---------------------------------------------------------- | --------------------------- |
| [string-color](https://gitlab.com/shindagger/string-color) | Rekli consol çıktırları     |
| [tqdm](https://github.com/tqdm/tqdm)                       | İşlem çubuğu (progress bar) |


## Argparse Modülü Detayları

- Argüman ekleme işlemi `parser = argparse.ArgumentParser(...)` ile yapılmaktadır.
- Parametrelerin kullanımı `argparse.ArgumentParser(description='yok')` şeklindedir.

| Parametre     | Açıklama                               |
| ------------- | -------------------------------------- |
| `description` | Uygulama ile alakalı açıklama metnidir |

## Argüman Ekleme

- Argüman ekleme işlemi `parser.add_argument(...)` ile yapılmaktadır.

| Parametre    | Açıklama                                    |
| ------------ | ------------------------------------------- |
| 1. parametre | Kısa kullanım komutunu içerir               |
| 2. Parametre | Orjinal kullanım komutunu içerir            |
| `help`       | `-h` yazıldığında çıkacak olan yardım metni |
| `action`     | Davranışı belirler                          |
| `type`       | Tip bilgisini içerir (int, string ...)      |
| `default`    | Varsayılan değer                            |
| `dest`       | Verinin aktarılacağı değişken ismi          |
| `nargs`      | Çoklu veri alma                             |
| `required`   | Parametre girilmezse program çalışmaz       |

### Nargs Formatı

`nargs='<operatör>+'` şeklinde kullanılır

| Operatör | Açıklama  |
| -------- | --------- |
| `+`      | 1 or more |
| `*`      | 0 or more |
| `?`      | 0 or 1    |

## Argüman Action Özelliği

| Parametre      | Açıklama                                                                |
| -------------- | ----------------------------------------------------------------------- |
| `'store_true'` | Flag\* değeri olur ve komutta içerilirse `True` değeri alır (`-h` gibi) |
| `count`        | Kaç kere yazıldığı bilgisini tutar (-vvv için 3)                        |

```python
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("--verbose", help="increase output verbosity",
                    action="store_true")
args = parser.parse_args()
if args.verbose:
    print("verbosity turned on")
```

**Çıktısı:**

```sh
$ python3 prog.py --verbose
verbosity turned on

$ python3 prog.py --verbose 1
usage: prog.py [-h] [--verbose]
prog.py: error: unrecognized arguments: 1

$ python3 prog.py --help
usage: prog.py [-h] [--verbose]

optional arguments:
  -h, --help  show this help message and exit
  --verbose   increase output verbosity
```

## Örnek CLI Kodu

```python
from argparse import ArgumentParser

parser = ArgumentParser(description='A simple CLI.')
# python <file> a b c için args.paths = ["a", "b", "c"]
parser.add_argument(
        'paths',
        nargs="+",
        metavar='paths',
        help='Projelerin yolları',
    )
parser.add_argument(
        '--log-file',
        '-o',
        default=os.path.join(os.getcwd(), 'output.log'),
        dest="logFile",
        help='Save the output in this file.',
        type=str,
        )
parser.add_argument(
        '--clean-file',
        action='store_true',
        default=False,
        help='Clear the log file on startup.Default is No',
        )
parser.add_argument(
        '--cancel-key',
        help='A single key that use as the cancel key, Default is ` (backtick)',
        )
parser.add_argument('--nargs', nargs='+')

args = parser.parse_args()
```

## Argparse ile `nargs` Detayları

Kaynak için [Argparse option for passing a list as option](https://stackoverflow.com/a/15753721/9770490) alanına bakabilirsin

```py
import argparse

parser = argparse.ArgumentParser()

# By default it will fail with multiple arguments.
parser.add_argument('--default')

# Telling the type to be a list will also fail for multiple arguments,
# but give incorrect results for a single argument.
parser.add_argument('--list-type', type=list)

# This will allow you to provide multiple arguments, but you will get
# a list of lists which is not desired.
parser.add_argument('--list-type-nargs', type=list, nargs='+')

# This is the correct way to handle accepting multiple arguments.
# '+' == 1 or more.
# '*' == 0 or more.
# '?' == 0 or 1.
# An int is an explicit number of arguments to accept.
parser.add_argument('--nargs', nargs='+')

# To make the input integers
parser.add_argument('--nargs-int-type', nargs='+', type=int)

# An alternate way to accept multiple inputs, but you must
# provide the flag once per input. Of course, you can use
# type=int here if you want.
parser.add_argument('--append-action', action='append')

# To show the results of the given option to screen.
for _, value in parser.parse_args()._get_kwargs():
    if value is not None:
        print(value)
```

```py
$ python arg.py --default 1234 2345 3456 4567
...
arg.py: error: unrecognized arguments: 2345 3456 4567

$ python arg.py --list-type 1234 2345 3456 4567
...
arg.py: error: unrecognized arguments: 2345 3456 4567

$ # Quotes won't help here... 
$ python arg.py --list-type "1234 2345 3456 4567"
['1', '2', '3', '4', ' ', '2', '3', '4', '5', ' ', '3', '4', '5', '6', ' ', '4', '5', '6', '7']

$ python arg.py --list-type-nargs 1234 2345 3456 4567
[['1', '2', '3', '4'], ['2', '3', '4', '5'], ['3', '4', '5', '6'], ['4', '5', '6', '7']]

$ python arg.py --nargs 1234 2345 3456 4567
['1234', '2345', '3456', '4567']

$ python arg.py --nargs-int-type 1234 2345 3456 4567
[1234, 2345, 3456, 4567]

$ # Negative numbers are handled perfectly fine out of the box.
$ python arg.py --nargs-int-type -1234 2345 -3456 4567
[-1234, 2345, -3456, 4567]

$ python arg.py --append-action 1234 --append-action 2345 --append-action 3456 --append-action 4567
['1234', '2345', '3456', '4567']
```
