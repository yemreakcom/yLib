# 🌌 virtualenv ile sanal ortamlarda çalışmak

* `virtualenv`, `venv`'den daha verimli bir pakettir ama standart olarak gelmez
* `pip` ile güncellenebilir ve [diğer farklı avantajları](https://virtualenv.pypa.io/en/latest/) vardır

## 🏜️ Sanal Ortamı Oluşturma

```bash
# Sanal ortamı belirli python sürüümü için indirme
python3.11 -m pip install virtualenv

# Sanal ortam oluşturma
virtualenv venv

# Sanal ortamı belirli python sürümü için oluşturma
virtualenv -p /usr/bin/python3 venv
virtualenv -p /opt/homebrew/bin/python3.11

# Aktif - deaktif etme
source venv/bin/activate
deactivate

# Sanal oratamı kaldırma
rm -rf venv
```

## 📦️ Bağımlılıklar Üzerine Çalışma

* `locel` ile sadece yerel bağımlılıkları ele alırız, sistemde yüklü olan diğerlerini ele almaz

```bash
# Proje bağımlılıklarını dosyaya aktarma
pip freeze --local > requirements.txt

# Proje bağımlılıklarını dosyadan indirme
pip install -r requirements.txt
```

## Bağlantılar

[What is the difference between venv, pyvenv, pyenv, virtualenv, virtualenvwrapper, pipenv, etc?](https://stackoverflow.com/questions/41573587/what-is-the-difference-between-venv-pyvenv-pyenv-virtualenv-virtualenvwrappe)
