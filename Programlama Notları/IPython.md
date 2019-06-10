# IPython <!-- omit in toc -->

<!-- TODO: Google Colab notlarını buraya taşı -->

## İçerikler <!-- omit in toc -->

- [Hızlı Notlar](#h%C4%B1zl%C4%B1-notlar)
- [Kullanıldığı Alanlar](#kullan%C4%B1ld%C4%B1%C4%9F%C4%B1-alanlar)
- [Progress Bar](#progress-bar)

## Hızlı Notlar

| Operatör   | Açıklama                       |
| ---------- | ------------------------------ |
| `<func>??` | Fonksiyonun kodlarını gösterir |
| `!`        | Terminal üzerinde çalıştırılır |
| `%`        | Magic function                 |

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
