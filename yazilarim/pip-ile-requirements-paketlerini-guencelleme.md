# ✨ pip ile requirements paketlerini güncelleme

## Pip-Upgrader ile Yapmak

* Otomatik olarak

```bash
pip install pip-upgrader
pip-upgrade
```

## Terminal Üzerinden Yapmak

```python
pip list --outdated --format=freeze | grep -v '^\\-e' | cut -d = -f 1  | xargs -n1 pip install -U
```

[Upgrade python packages from requirements.txt using pip command](https://stackoverflow.com/a/43642296/9770490)

[How to upgrade all Python packages with pip?](https://stackoverflow.com/a/3452888/9770490)
