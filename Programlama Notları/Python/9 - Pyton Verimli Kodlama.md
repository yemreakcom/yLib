# Python Verimli Kodlama Notlarım <!-- omit in toc -->

## İçerikler <!-- omit in toc -->

- [Koşullu İç İçe For Döngüsü](#ko%C5%9Fullu-i%CC%87%C3%A7-i%CC%87%C3%A7e-for-d%C3%B6ng%C3%BCs%C3%BC)

## Koşullu İç İçe For Döngüsü

Alttaki yapı yerine, bir sonraki yapıyı kullanarak daha **verimli ve anlaşılır** kod yazabilrisin 😊

```py
KOSUL1 = 1
KOSUL2 = 1
KOSUL3 = 0

if "kosul1" in line:
    # yapılacaklar
    pass
elif "kosul2" in line:
    # yapılacaklar
    pass
elif "kosul3" in line:
    # yapılacaklar
    pass

```

```py
conditions = []
conditions.add(('kosul1:', KOSUL1)) if KOSUL1 != 0
conditions.add(('kosul2:', KOSUL2)) if KOSUL2 != 0
patteconditionsrns.add(('kosul3:', KOSUL3)) if KOSUL3 != 0

for condition in conditions:
    if condition[0] in line:
        # Yapılacak işlemler
        break
```
