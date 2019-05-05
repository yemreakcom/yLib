# Shell Script <!-- omit in toc -->

Unix işletim sistemlerinin ortak programlama dilidir.

## İçerikler <!-- omit in toc -->

- [Yazdırma İşlemleri (Echo)](#yazd%C4%B1rma-i%CC%87%C5%9Flemleri-echo)
- [Cat ile Yazdırma İşlemi](#cat-ile-yazd%C4%B1rma-i%CC%87%C5%9Flemi)
- [Değişkenler](#de%C4%9Fi%C5%9Fkenler)
- [İf-Else Yapısı](#i%CC%87f-else-yap%C4%B1s%C4%B1)
- [For Döngüsü](#for-d%C3%B6ng%C3%BCs%C3%BC)
- [Terminalde Seçim Yaptırma](#terminalde-se%C3%A7im-yapt%C4%B1rma)
  - [Switch - Case Yapısı](#switch---case-yap%C4%B1s%C4%B1)
  - [Select Yapısı](#select-yap%C4%B1s%C4%B1)
  - [İç İçe Seçim Yapısı](#i%CC%87%C3%A7-i%CC%87%C3%A7e-se%C3%A7im-yap%C4%B1s%C4%B1)
- [Terminalde For Döngüsü (For Loop)](#terminalde-for-d%C3%B6ng%C3%BCs%C3%BC-for-loop)
  - [Her Dizine For Döngüsü](#her-dizine-for-d%C3%B6ng%C3%BCs%C3%BC)
    - [Alt Dizinler Dahil Değil](#alt-dizinler-dahil-de%C4%9Fil)
    - [Alt Dizinler Dahil](#alt-dizinler-dahil)
- [Fonksiyonlar](#fonksiyonlar)
  - [Fonksiyonların Kullanımı](#fonksiyonlar%C4%B1n-kullan%C4%B1m%C4%B1)
  - [Parametreli Fonksiyonlar](#parametreli-fonksiyonlar)
- [Dosya İşlemleri](#dosya-i%CC%87%C5%9Flemleri)
  - [Dosya Okuma](#dosya-okuma)
  - [Dosyadan URL ile İndirme](#dosyadan-url-ile-i%CC%87ndirme)
- [Harici Bağlantılar](#harici-ba%C4%9Flant%C4%B1lar)

## Yazdırma İşlemleri (Echo)

| Komut                            | Açıklama                                                      |
| -------------------------------- | ------------------------------------------------------------- |
| `echo "<metin>"`                 | Ekrana metni olduğu gibi basma                                |
| `echo -e "<metin>"`              | Ekrana metni formatlı basma (\n \t gibi karakterler çalışır)  |
| `echo $<değişken>`               | Ekrana değişken basma                                         |
| `echo $(<komut>)`                | Ekrana komut çıktısını basma                                  |
| `echo "<metin>" > <dosya_yolu>`  | Verilen metni dosyanın üzerine yazma, yoksa dosyayı oluşturma |
| `echo "<metin>" >> <dosya_yolu>` | Verilen metni dosyaya ekleme                                  |
| `@Echo off`                      | Çıktıları gizleme                                             |

- `<metin>` Ekrana basılacak metin
  - Örn: `yemreak`
- `<değişken>` Linux değişkenleri (ortam değişkenleri vs.)
  - Örn: `PYTHONPATH`, `HOME`
- `<komut>` Linux komutları
  - Örn: `pwd`
- `<dosya_yolu>` Metnin yazılacağı dosyanın yolu
  - Örn: `yemreak.txt`, `../yemreak.sh`, `~/yemreak.ini`

## Cat ile Yazdırma İşlemi

Dosyaya EOT gelene kadar yazma

```sh
cat << <sonlandırma_metni> >> <dosya_yolu>
satır1
satır2
<sonlandırma_metni>
```

- `<sonlandırma_metni>` Bu metin geldiğinde yazma işlemini sonlandırır
  - Örn: `A` olursa `YemreAK` yazıldığında sonlanmaz, `A` yazıldığında sonlanır.
- `<dosya_yolu>` Metnin yazılacağı dosyanın yolu
  - Örn: `yemreak.txt`, `../yemreak.sh`, `~/yemreak.ini`

## Değişkenler

- Değişkenler kod içerisin `$` ön eki ile kullanılır
- Değişkenlere atama yapılırken `=` sonrası ve öncesinde boşluk bırakılmaz
  - Boşluk olursa her metni komut gibi işlemeye çalışır ve hata verir
- Değişkenlerle aritmatik işlemler `let "<işlem>"` komutuyla yapılır
  - `let "myvar = 5"` çalışırken, `mayvar = 5` hata verir

```sh
file="help"
let "file = 'wow'"
echo $file
```

> Let komutu hakkında daha fazla bilgi için [buraya][Let Komutu] bakabilirsin.

## İf-Else Yapısı

Temel açıklamaya [buradan][If Else Yapısı] erişebilirsin.

## For Döngüsü

Temel açıklamaya [buradan][For Döngüsü] erişebilirsin.

## Terminalde Seçim Yaptırma

### Switch - Case Yapısı

```sh
while true; do
    read -p "Do you wish to install this program?" yn
    case $yn in
        [Yy]* ) make install; break;;
        [Nn]* ) exit;;
        * ) echo "Please answer yes or no.";;
    esac
done
```

### Select Yapısı

```sh
echo "Do you wish to install this program?"
select yn in "Yes" "No"; do
    case $yn in
        Yes ) make install; break;;
        No ) exit;;
    esac
done
```

### İç İçe Seçim Yapısı

```sh
while true; do
    read -p "Xammp kurmak ister misin [y/n] " # -n 1 -r
    case $REPLY in
        [Yy]* ) {
            # İstenen kodlar

            while true; do
		        read -p "Xammp komutları tanımlansın mı (xampp ve mysql) [y/n] " # -n 1 -r
		        case $REPLY in
		            [Yy]* ) {
		                # İstenen kodlar
		                break
		            };;
		            [Nn]* ) break;;
		        esac
            done

            while true; do
		        read -p "Wordpress kurmak ister misin [y/n] " # -n 1 -r
		        case $REPLY in
		            [Yy]* ) {
                        # İstenen kodlar
		                break
		            };;
		            [Nn]* ) break;;
		        esac
            done

            break
        };;
        [Nn]* ) break;;
    esac
done
```

## Terminalde For Döngüsü (For Loop)

```sh
for f in *; do
    echo "-> $f"
done
```

### Her Dizine For Döngüsü

#### Alt Dizinler Dahil Değil

```sh
for D in *; do
    if [ -d "${D}" ]; then
        echo "${D}"   # your processing here
    fi
done
```

```sh
for D in *; do [ -d "${D}" ] && my_command; done
```

```sh
for D in */; do my_command; done
```

#### Alt Dizinler Dahil

```sh
for D in `find . -type d`
do
    //Do whatever you need with D
done
```

## Fonksiyonlar

```sh
dowload_with_name() {
    var='hello'
	return $var
}
```

### Fonksiyonların Kullanımı

```sh
dowload_with_name # Fonksiyonlar isimleri ile kullanılır
echo $? # Return değeri '$?' olarak tanımlanır. Hello basar
```

> Temel fonksiyon kaynağı için [buraya][Temel Fonksiyonlar] bakabilirsin.

### Parametreli Fonksiyonlar

```sh
fonksiyon(){
    arg1=$1 # 1. parametre
    arg2=$2 # 2. parametre
    echo "1. $arg1, 2. $arg2"
}

# Kullanımı
fonksiyon arguman1 arguman2 # 1. arguman1, 2. arguman2
```

## Dosya İşlemleri

### Dosya Okuma

> Kaynak için [buraya](https://www.cyberciti.biz/faq/unix-howto-read-line-by-line-from-file/) bakabilirsin.

```sh
filepath='img0.jpg' # Dosyanın yolu
filestr='' # Okunan verilerin kayıt edileceği değişken

while IFS= read line # Dosya sonuna kadar okuma
do
    let "filestr += $line" # Satır satır dosyayı okuma
done < "$filepath" # Okunacak dosyanın yolunu verme
```

### Dosyadan URL ile İndirme

```sh
prefix='img' # Ön ek
ext='.jpg' # Dosya uzantısı
num=0 # Sayaç
while IFS= read line
do
    wget -O $prefix$num$ext "$line"
    let "num += 1"
done < "../$file"
```

## Harici Bağlantılar

- [Bash Script]
- [Let Komutu]
- [Temel Fonksiyonlar]
- [Fonksiyon Parametreleri]
- [If Else Yapısı]
- [For Döngüsü]
- [Dosyayı satır satır okuma]
- [Zaman işlemleri]

[Bash Script]: http://tldp.org/HOWTO/Bash-Prog-Intro-HOWTO.html#toc11
[Let Komutu]: https://www.computerhope.com/unix/bash/let.htm
[Temel Fonksiyonlar]: https://linuxize.com/post/bash-functions/
[Fonksiyon Parametreleri]: https://bash.cyberciti.biz/guide/Pass_arguments_into_a_function
[If Else Yapısı]: http://codewiki.wikidot.com/shell-script:if-else
[For Döngüsü]: https://www.cyberciti.biz/faq/bash-for-loop/
[Dosyayı satır satır okuma]: https://www.cyberciti.biz/faq/unix-howto-read-line-by-line-from-file/
[Zaman işlemleri]: https://stackoverflow.com/a/1401495/9770490