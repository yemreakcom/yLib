# Python ile Veri İşlemleri

Temel olarak pandas modülü ele alınacaktır.

## Dict'i CSV'ye Çevirme

```py
df = pd.DataFrame({'name': ['Raphael', 'Donatello'],
                   'mask': ['red', 'purple'],
                   'weapon': ['sai', 'bo staff']})

df.to_csv(index=False)
# 'name,mask,weapon\nRaphael,red,sai\nDonatello,purple,bo staff\n'
```

## Temel İşlemler

| DataFrame İşlemi                                   | Açıklama                                         |
| -------------------------------------------------- | ------------------------------------------------ |
| `loc[<i>] = <list>`                                | i. **indekse** değer atama                       |
| `iloc[<i>] = <list>`                               | i. **satıra** değer atama (çok tercih etme)      |
| `drop(DATA_FRAME.index, inplace=True)`             | Tüm verileri silme                               |
| `df.to_csv(<file | filename>, header=f.tell()==0)` | CSV'ye ekleme (`tell` dosyanın başı ise 0 verir) |
| `len(pandas.read_csv(<path_to_csv>))`              | Veri sayısını bulma                              |

> `df.iloc[0:0]` çalışmadı 🤔

## Ek Bilgiler

- Rar dosyalarını çakarma `!unrar e keylogs.rar`
- [Looping over Pandas](https://www.polymorphe.org/index.php/looping-over-pandas-data-mkd) (Yüksek miktarda veri için)
- [Online CSV GÖrüntüleme](http://www.convertcsv.com/csv-viewer-editor.htm)
- [10dk'dan Pandas](https://pandas.pydata.org/pandas-docs/stable/getting_started/10min.html)
- [dataframe.append() & loc[] , iloc[]](https://thispointer.com/python-pandas-how-to-add-rows-in-a-dataframe-using-dataframe-append-loc-iloc/)
