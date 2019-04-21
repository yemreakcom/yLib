# PHP <!-- omit in toc -->

> `HOME` tuşu ile yukarı yönlenebilrsiniz.

- [Debugger Setup](#debugger-setup)
  - [Xdebug Remote Debug via Chrome](#xdebug-remote-debug-via-chrome)
  - [Checking Php Version and Bit](#checking-php-version-and-bit)

## Debugger Setup

Click [here](https://www.jetbrains.com/help/phpstorm/configuring-xdebug.html) from setup instructions.

### Xdebug Remote Debug via Chrome

Install extension from [this](https://chrome.google.com/webstore/detail/xdebug-helper/eadndfjplgieldjbigjakmdgkmoaaaoc?hl=tr) link, and after do these;

- `Edit configuration`
- `+`
- `Php Remote Debug`
- `Server: 127.0.0.1`
- `IDE key(sesion id): PHPSTORM`
- `OK`

### Checking Php Version and Bit

```cmd
php -r "echo PHP_INT_SIZE";
```
