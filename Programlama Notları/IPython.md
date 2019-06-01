# IPython <!-- omit in toc -->

## İçerikler <!-- omit in toc -->

- [Kullanıldığı Alanlar](#kullan%C4%B1ld%C4%B1%C4%9F%C4%B1-alanlar)
- [Progress Bar](#progress-bar)

## Kullanıldığı Alanlar

- Jupyter notebook
- Google colabratory

## Progress Bar

```py
from IPython.display import HTML, display
import time

def progress(value, max=100):
    return HTML("""
        <progress
            value='{value}'
            max='{max}',
            style='width: 100%'
        >
            {value}
        </progress>
    """.format(value=value, max=max))

out = display(progress(0, 100), display_id=True)
for ii in range(101):
    time.sleep(0.02)
    out.update(progress(ii, 100))
```

> [Kaynak](https://stackoverflow.com/questions/46939393/how-do-i-use-updatable-displays-on-colab)
