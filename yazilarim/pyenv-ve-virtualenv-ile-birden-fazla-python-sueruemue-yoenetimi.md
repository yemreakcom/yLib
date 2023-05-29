# 👨💼 pyenv ve virtualenv ile birden fazla python sürümü yönetimi

## PyEnw ve VirtualEnv Eklentisi Kurulumu

* `git` ile indirme işlemini yapacağız

```bash
# sudo apt install git
git clone  <https://github.com/pyenv/pyenv.git> ~/.pyenv

# Pyenv içerisine virtual-env eklentisini kuruyoruz
git clone <https://github.com/pyenv/pyenv-virtualenv.git> $(pyenv root)/plugins/pyenv-virtualenv
```

## Bash İçerisine Dahil Etme

* `bashrc` (mac için `zshrc`) sonuna aşağıdaki alanı ekleyin
* Bu sayede `pyenv`'i  `PATH`'e ekliyoruz

```bash
# Pyenv settings
export PYENV_ROOT="${HOME}/.pyenv"
if [ -d "${PYENV_ROOT}" ]; then
    export PATH=${PYENV_ROOT}/bin:$PATH  
    eval "$(pyenv init -)"
		eval "$(pyenv virtualenv-init -)"
fi
```

## PyEnv ile Python Kurulumu

*   `Ubuntu / Debian` için gereksinimlerin kurulumu

    ```bash
    sudo apt-get install -y make build-essential libssl-dev zlib1g-dev \\
    libbz2-dev libreadline-dev libsqlite3-dev wget curl llvm libncurses5-dev \\
    libncursesw5-dev xz-utils tk-dev libffi-dev liblzma-dev python-openssl
    ```
*   `RaspberryPi` için gereksinimlerin kurulumu

    ```bash
    sudo apt-get install -y make build-essential libssl-dev zlib1g-dev libbz2-dev libreadline-dev libsqlite3-dev wget curl llvm libncurses5-dev libncursesw5-dev xz-utils tk-dev libffi-dev liblzma-dev

    sudo apt-get install -y make build-essential libssl-dev zlib1g-dev libbz2-dev libreadline-dev libsqlite3-dev wget curl llvm libncurses5-dev libncursesw5-dev
    ```
* `-l` komutu indirilebilenleri listeler
* `grep` ile python 3.11 sürümlerini filtreliyoruz

```bash
pyenv rehash
pyenv install -l | grep 3.11
pyenv install 3.11.0

# PyEnv ile Kurulan Python’ı Default Yapma
pyenv global 3.11.0
python --version
# 3.11.0
```

## VirtualEnv Oluşturma

```bash
pyenv virtualenv 3.11.0 MyProjects
# created virtual environment CPython3.11.0.final.0-64 in 1830ms...

# Virtrualenv aktif etme
pyenv activate MyProjects

# Virtualenv'leri listeleme
pyenv virtualenvs

# Virtualenv kaldırma
pyenv uninstall MyProjects
```

## Bağlantılar

[What is the difference between venv, pyvenv, pyenv, virtualenv, virtualenvwrapper, pipenv, etc?](https://stackoverflow.com/questions/41573587/what-is-the-difference-between-venv-pyvenv-pyenv-virtualenv-virtualenvwrappe)

[Raspberry Pi Tips](https://fabacademy.org/2020/labs/kannai/students/tatsuro-homma/project/RaspPi\_P\_01\_setupPyenv.html)

[Managing Multiple Python Versions With pyenv - Real Python](https://realpython.com/intro-to-pyenv/)
