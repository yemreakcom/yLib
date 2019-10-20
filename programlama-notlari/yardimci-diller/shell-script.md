---
description: Unix işletim sistemlerinin ortak programlama dilidir.
---

# 👨‍💻 Shell Script

## Önemli Bilgiler

* `sh` uzantılı dosyalara yazılırlar
* Dosyaların ilk satırlarına [shebang](http://dcjtech.info/topic/list-of-shebang-interpreter-directives/) olarka ifade edilen satır yazılır
  * Kodlar derlenmeden önce bu satıra bakılır ve yapısına karar verilir \([kaynak](https://www.shellscript.sh/tips/shebang/)\)
* Dosyanın ilk satırına _shell script_ olduğunu belli etmesi için `#!/bin/bash` yazılır
* Terminal üzerinden `bash <dosya>` olarak çalıştırılabilirler

## VsCode Eklentileri

* [Bash Beautify](https://marketplace.visualstudio.com/items?itemName=shakram02.bash-beautify)

## Temel Operatörler

| Operatör | Açıklama |  |  |
| :--- | :--- | :--- | :--- |
| `-` | Son çalışan dizine gitme |  |  |
| `~` | Home dizini |  |  |
| `<komut>; <komut>;` | Birden fazla komut işleme \(birbirlerini beklemez\) |  |  |
| `<komut> & <komut>` | Birden fazla komut işleme \(sırayla işler\) |  |  |
| `<komut> && <komut>` | 1. komut çalışırsa 2.'yi işleme |  |  |
| \` |  | \` | 1. olmazsa 2. komutu işleme |
| \` | \` | 2. komutu ilk komutun çıktısında çalıştırma \(pipeline\) |  |
| `>` | Yönlendirme \(yoksa oluşturur\) |  |  |
| `>>` | Eklemeli yönlendirme \(üzerine yazmaz, ekler\) |  |  |
| `!$` | Bir önce kullanılan değişkeni kullanma |  |  |
| `!!` | Bir önceki komutu kullanma |  |  |

## Bash Komutu

| Komut | Açıklama |
| :--- | :--- |
| `bash <dosya>` | Dosyadaki komutları terminalde gerçekleştirir |
| `bash -c "<komut>"` | Verilen komutu terminalde gerçekleştirir |

## Yazdırma İşlemleri \(Echo\)

| Komut | Açıklama |
| :--- | :--- |
| `echo "<metin>"` | Ekrana metni olduğu gibi basma |
| `echo -e "<metin>"` | Ekrana metni formatlı basma \(\n \t gibi karakterler çalışır\) |
| `echo $<değişken>` | Ekrana değişken basma |
| `echo $(<komut>)` | Ekrana komut çıktısını basma |
| `echo $(<komut>)' metin '$(<komut>)` | Ekrana komut çıktısını ve metni basma |
| `echo "<metin>" > <dosya_yolu>` | Verilen metni dosyanın üzerine yazma, yoksa dosyayı oluşturma |
| `echo "<metin>" >> <dosya_yolu>` | Verilen metni dosyaya ekleme |
| `sudo bash -c echo "<metin>" > <root_dosya>` | Root dosyasının üzerine yazma, yoksa dosyayı oluşturma |
| `<komut> &> /dev/null` | Çıktıları gizleme |

> `>` ile yapılan yönlendirme işlemleri `echo` tarafından değil `shell` tarafından yapılır. Yetki sorunları olursa `echo`'ya değil `shell`'e yetki verilmelidir.

* `<metin>` Ekrana basılacak metin
  * Örn: `yemreak`
* `<değişken>` Linux değişkenleri \(ortam değişkenleri vs.\)
  * Örn: `PYTHONPATH`, `HOME`
* `<komut>` Linux komutları
  * Örn: `pwd`
* `<dosya_yolu>` Metnin yazılacağı dosyanın yolu
  * Örn: `yemreak.txt`, `../yemreak.sh`, `~/yemreak.ini`

## Cat ile Yazdırma İşlemi

Dosyaya EOT gelene kadar yazma

```bash
cat << <sonlandırma_metni> >> <dosya_yolu>
satır1
satır2
<sonlandırma_metni>
```

* `<sonlandırma_metni>` Bu metin geldiğinde yazma işlemini sonlandırır
  * Örn: `A` olursa `YemreAK` yazıldığında sonlanmaz, `A` yazıldığında sonlanır.
* `<dosya_yolu>` Metnin yazılacağı dosyanın yolu
  * Örn: `yemreak.txt`, `../yemreak.sh`, `~/yemreak.ini`

## Değişkenler

* Değişkenler kod içerisin `$` ön eki ile kullanılır
* Değişkenlere atama yapılırken `=` sonrası ve öncesinde boşluk bırakılmaz
  * Boşluk olursa her metni komut gibi işlemeye çalışır ve hata verir
* Değişkenlerle aritmatik işlemler `let "<işlem>"` komutuyla yapılır
  * `let "myvar = 5"` çalışırken, `mayvar = 5` hata verir

```bash
file="help"
let "file = 'wow'"
echo $file
```

> Let komutu hakkında daha fazla bilgi için [buraya](https://www.computerhope.com/unix/bash/let.htm) bakabilirsin.

## Kullanıcıdan Girdi \(Input\) Alma

```bash
read varname
echo $varname

read -p 'Username: ' uservar # Girdide yorum gösterme
read -sp 'Password: ' passvar # Gizli girdi
echo
echo Thankyou $uservar we now have your login details
```

> [Bash User Inputs](https://ryanstutorials.net/bash-scripting-tutorial/bash-input.php)

## String İşlemleri

```bash
${#var} # Var string'inin uzunluğunu hesaplama
${var#*.} # .'ya kadar tüm metni siler

# String Kıyaslama
if [ $kelime == "yemreak" ]; then
    echo "Eşdeğer"
fi

# String içinde alt stirng arama (cümle'de kelime varsa 1) (2 tane [ olduğuna dikkat)
if [[ "$cumle" =~ "$kelime" ]]; then
    echo "Bulundu"
else
    echo "Bulunamadı"
fi

# Stringdeki i. sıradaki kelimeyi alma
let "word = $(echo $WID | awk '{print $1}')" # İlk olanı alma $word1 = ilk kelime
let "word = $(echo $WID | awk '{print $i}')" # i. olanı alma

# Boşluklarla ayrılan cümledenki kelimeleri alma
for kelime in $cumle; do
    echo $kelime
done
```

## İf-Else Yapısı

Temel açıklamaya [buradan](http://codewiki.wikidot.com/shell-script:if-else) erişebilirsin.

```bash
[ $1 ] || { echo "Usage: $0 file1.wma file2.wma"; exit 1; } # 1.parametre yoksa çıkma
```

## For Döngüsü

Temel açıklamaya [buradan](https://www.cyberciti.biz/faq/bash-for-loop/) erişebilirsin.

## Terminalde Seçim Yaptırma

### Switch - Case Yapısı

```bash
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

```bash
echo "Do you wish to install this program?"
select yn in "Yes" "No"; do
    case $yn in
        Yes ) make install; break;;
        No ) exit;;
    esac
done
```

### İç İçe Seçim Yapısı

```bash
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

## Terminalde For Döngüsü \(For Loop\)

```bash
for f in *; do
    echo "-> $f"
done
```

### Her Dizine For Döngüsü

#### Alt Dizinler Dahil Değil

```bash
for D in *; do
    if [ -d "${D}" ]; then
        echo "${D}"   # your processing here
    fi
done
```

```bash
for D in *; do [ -d "${D}" ] && my_command; done
```

```bash
for D in */; do my_command; done
```

#### Alt Dizinler Dahil

```bash
for D in `find . -type d`
do
    //Do whatever you need with D
done
```

## Fonksiyonlar

```bash
dowload_with_name() {
    var='hello'
    return $var
}
```

### Fonksiyonların Kullanımı

```bash
dowload_with_name # Fonksiyonlar isimleri ile kullanılır
echo $? # Return değeri '$?' olarak tanımlanır. Hello basar
```

> Temel fonksiyon kaynağı için [buraya](https://linuxize.com/post/bash-functions/) bakabilirsin.

### Parametreler

* `$1` 1. parametre
* `$2` 2. parametre
* `$0` Fonksiyonun ismi
* `$@` Tüm parametreler \(dizi\)

### Parametreli Fonksiyonlar

```bash
fonksiyon(){
    arg1=$1 # 1. parametre
    arg2=$2 # 2. parametre
    echo "1. $arg1, 2. $arg2"
}

# Kullanımı
fonksiyon arguman1 arguman2 # 1. arguman1, 2. arguman2
```

## Dosya İşlemleri

### Kontrol Bayrakları

Kullanım şekli `[ <bayrak> <string> ]`

* `[ -f "$1" ] || {echo "$1 dosyadır"}`

| Bayrak | Açıklama |
| :--- | :--- |
| `-f` | Dosya kontrolü \(File\) |
| `-d` | Dizin kontrolü \(Directory\) |

### Dosya Okuma

> Kaynak için [buraya](https://www.cyberciti.biz/faq/unix-howto-read-line-by-line-from-file/) bakabilirsin.

```bash
filepath='img0.jpg' # Dosyanın yolu
filestr='' # Okunan verilerin kayıt edileceği değişken

while IFS= read line # Dosya sonuna kadar okuma
do
    let "filestr += $line" # Satır satır dosyayı okuma
done < "$filepath" # Okunacak dosyanın yolunu verme
```

### Dosyadan URL ile İndirme

```bash
prefix='img' # Ön ek
ext='.jpg' # Dosya uzantısı
num=0 # Sayaç
while IFS= read line
do
    wget -O $prefix$num$ext "$line"
    let "num += 1"
done < "../$file"
```

### Sıkıştırma \(Arşivleme\) İşlemleri

**Dosya sıkıştırma:**

```bash
filename="dosya yolu"
out="Çıktı yolu.zip"
zip "$out" "$filename$"

zip -R $out "*.c" $ # '.c' ile biten düm dosyaları sıkıştırır (alt dizinlerde de arar /dir1/file.c /dir2/file.c)
```

**Dizin Sıkıştırma:**

```bash
dirname="dizin_yolu"
out="Çıktı yolu.zip" # Boşluk kabul eder
zip -r "$out" "$dirname$"
```

## Harici Bağlantılar

* [Bash Script](http://tldp.org/HOWTO/Bash-Prog-Intro-HOWTO.html#toc11)
* [Let Komutu](https://www.computerhope.com/unix/bash/let.htm)
* [Temel Fonksiyonlar](https://linuxize.com/post/bash-functions/)
* [Fonksiyon Parametreleri](https://bash.cyberciti.biz/guide/Pass_arguments_into_a_function)
* [If Else Yapısı](http://codewiki.wikidot.com/shell-script:if-else)
* [For Döngüsü](https://www.cyberciti.biz/faq/bash-for-loop/)
* [Dosyayı satır satır okuma](https://www.cyberciti.biz/faq/unix-howto-read-line-by-line-from-file/)
* [Zaman işlemleri](https://stackoverflow.com/a/1401495/9770490)

