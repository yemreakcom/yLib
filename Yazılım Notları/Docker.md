# 🐳 Docker

Uygulamaları kendi PC'ne kurmak | kaldırmak ve hatalarıyla | artıklarıyla uğraşmak istemiyorsan, doğru konumdasın :)<br />
<br />
Docker'ın ana sayfası için <a href="https://www.docker.com/" target="_blank">buraya</a> tıklayabilirsin.<br />
<i>Bu yazı detaylı anlatan blog yazısının özeti niteliğindedir, orijinali için&nbsp;<a href="https://gokhansengun.com/docker-nedir-nasil-calisir-nerede-kullanilir/" target="_blank">buraya</a>&nbsp;tıklamanı tavsiye ederim.</i><br />
<div>
<b>Nedir ve Neden Kullanmalıyım?</b></div>
<div>
<ul>
<li>Benim Makinemde Çalışıyor (Works on my Machine) Problemine Çözüm Sağlaması</li>
<li>Geliştirme Ortamı Standardizasyonu (Eşitlik) Sağlaması</li>
<li>Test ve Entegrasyon Ortamı Kurulumu ve Yönetimini Kolaylaştırması</li>
<li>Mikroservis Mimari için Kolay ve Hızlı Bir Şekilde Kullanıma Hazır Hale Getirilebilmesi</li>
<li>Kaynakların Etkili ve Efektif Bir Biçimde Kullanılmasını Sağlaması</li>
<li>Multitenant Sistemlerde Tenancy Mantığını Uygulama Seviyesinden Çıkarmayı Sağlaması</li>
</ul>
<ul>
<li>Vm teknolojisi gibi birden fazla kernel kullanmak yerine tek bir kernel yapısında birden fazla uygulama çalıştırmayı sağlar.</li>
<li>Tüm bu işlemler <i>image&nbsp;</i>&nbsp;adı verilen yüklemelerle olmakta.</li>
<ul>
<li><i>Image</i>'lerin diğer artısı da normal program kurulumları gibi yüksek yer kaplamamakta ve <i>docker</i>'ıa özel optimize edilmiş haldedirler. (Daha az performans ister)</li>
</ul>
<li>Tüm bunlara ek olarak kod paylaşımları hususunda da oldukça faydalıdır.&nbsp;</li>
<ul>
<li>Kod'un <i>docker </i>ortamında çalışabilir olması <i>docker</i>&nbsp;yüklü&nbsp;diğer bilgisayarda da çalışabilir olacağı anlamına gelir.</li>
</ul>
<li>Kolay kaldırılabilir.</li>
<ul>
<li><i>Docker </i>üzerinden <i>image</i>'leri silmeniz durumunda uygulama ve ona bağlı olan her şey silineceltir. (<i>Kendi bilgisayarımızda kaldırma işlemi sonucunda ardında artık dosya bırakmaktadır.)</i></li>
</ul>
</ul>
<div>
<i><br /></i></div>
<div>
<b>Nasıl Öğrenirim:</b></div>
<div>
<ul>
<li><a href="https://docs.docker.com/get-started/" target="_blank">Buraya</a> tıklayarak resmi dökümantasyonuna bakabilirsin.</li>
<li>Docker olayını özetleyen video için&nbsp;<a href="https://www.youtube.com/watch?v=YFl2mCHdv24&amp;t=622s" target="_blank">buraya</a>&nbsp;tıklayabilirsin.<br />
<div>
</div>
</li>
<li>Docker'ı&nbsp;<i>detaylı&nbsp;</i>anlatan&nbsp;<i>Türkçe&nbsp;</i>blog için&nbsp;<a href="https://gokhansengun.com/docker-nedir-nasil-calisir-nerede-kullanilir/" target="_blank">buraya</a>&nbsp;tıklayabilirsin. <span style="color: red;"><b>&lt;- Tavsiye</b></span></li>
</ul>
</div>
<div>
<br /></div>
<div>
<b>Aşırı kısa Özet:</b><br />
<ul>
<li>Container</li>
<ul>
<li>Docker Daemon tarafından Linux çekirdeği içerisinde birbirinden izole olarak çalıştırılan process’lerin her birine verilen isimdir.&nbsp;</li>
</ul>
<li>Image&nbsp;</li>
<ul>
<li>Container'ların çalışacağı işletim sistemi, programlar vs.</li>
</ul>
<li>Dockerfile</li>
<ul>
<li>Yapılandırma dosyaları</li>
</ul>
<li>Docker Daemon</li>
<ul>
<li>Birbirinden bağımsız Container'ları barındıran, sistemin kullanacağı RAM, CPU gibi ayarları yapan katman. (<a href="https://gokhansengun.com/resource/img/DockerPart1/DockerContainerArchitecture.png" target="_blank">Resimle </a>daha açık olacaktır)</li>
</ul>
<li>Docker CLI</li>
<ul>
<li>Docker Daemon ile iletişime geçtiğimiz kısım. CMD, Bash vs.. (<i>evet siyah ekran</i>)</li>
</ul>
<li>Docker Registry</li>
<ul>
<li>Container'larda çalışan Image'lerin bulunduğu kısım</li>
</ul>
<li>Docker Repository</li>
<ul>
<li>Bir grup Image’ın oluşturduğu yapı</li>
</ul>
</ul>
<div>
<br /></div>
</div>
<div>
<b>Kullanım:</b><br />
<ul>
<li>Docker'dan Image çekme</li>
<ul>
<li><i>docker pull &lt;<i><a href="https://hub.docker.com/" target="_blank">image_ismi</a></i>&gt;</i></li>
</ul>
<li>Image'leri görüntüleme</li>
<ul>
<li><i>docker images</i></li>
</ul>
<li>Image çalıştırma (Image ile container oluşturma)</li>
<ul>
<li>docker run &lt;<i><a href="https://hub.docker.com/" target="_blank">image_ismi</a>&gt;</i></li>
<li><i>docker run -p &lt;host_port&gt;:&lt;conotainer_port&gt; &lt;<i><a href="https://hub.docker.com/" target="_blank">image_ismi</a></i>&gt;</i></li>
<ul>
<li><i>İmage'i çalıştırıp<u> htttps:localhost:&lt;<i>host_port</i>&gt;</u>'unu, container'ın&nbsp;</i><i>&lt;conotainer_port&gt;'una bağlama.</i></li>
<li><i>docker run -p 8080:80 nginx</i></li>
</ul>
<li><i>Not: Eğer image yüklü değilse otomatik indirir!</i></li>
</ul>
</ul>
<b>Container İşlemleri:</b></div>
<div>
<ul>
<li>Çalışan containerları gösterme</li>
<ul>
<li><i>docker ps</i></li>
<li><i>docker ps -a</i></li>
</ul>
<li>Oluşturulan container'ı yeniden çalıştırma</li>
<ul>
<li><i>docker start &lt;container_id&gt;</i></li>
<ul>
<li><i>&lt;container_id&gt;'yi docker ps -a ile bulabilirsiniz.</i></li>
<ul>
</ul>
</ul>
<li><i>docker start -a &lt;container-id&gt;</i></li>
<ul>
<li><i>Terminale ekleyerek başlatma. (I/O girişi ile kontrol edebiliriz.)</i></li>
<ul>
</ul>
</ul>
</ul>
<li>Container kayıtlarını görüntüleme (loglar)</li>
<ul>
<li><i>docker logs &lt;container_id&gt;</i></li>
<ul>
</ul>
</ul>
<li>Container silme</li>
<ul>
<li><i>docker rm &lt;container-id&gt;</i></li>
<li><i>docker rm -f &lt;container-id&gt;</i></li>
<ul>
<li><i>Çalışır halde bile olsa silme (Forging)&nbsp;</i></li>
<ul>
</ul>
</ul>
</ul>
<li>Container üzerinde uygulama çalıştırma</li>
<ul>
<li><i>docker exec &lt;options&gt; &lt;container_id&gt; &lt;path&gt;</i></li>
<li><i>docker exec -it &lt;container_id&gt; /bin/bash</i></li>
<ul>
<li><i>-i interactive terminal demek</i></li>
<li><i>-t terminale bağlamak demek (attach)</i></li>
<li><i>-d bağlamadan çalıştır demek (deattach)</i></li>
<li>Container üzerinde çalışan işlemleri (process'leri) gösterme</li>
<ul>
<li><i>ps -ef</i></li>
<ul>
</ul>
</ul>
<li>Dosyayı terminale basma</li>
<ul>
<li><i>more &lt;path&gt;</i></li>
<li><i>more /etc/nginx/nginx.conf</i></li>
<li><i>more /etc/nginx/conf.d/default.conf</i></li>
</ul>
</ul>
</ul>
<li>Container'ı çıkışa zorlama</li>
<ul>
<li><i>docker kill &lt;container_id&gt;</i></li>
<ul>
</ul>
<li><i><br /></i></li>
</ul>
</ul>
<div>
<i><br /></i><i><br /></i>
<b>Karma Notları:</b><br />
<ul>
<li><a href="https://www.youtube.com/watch?v=YFl2mCHdv24" target="_blank">12 Dk'da Docker</a></li>
<li><a href="https://stackoverflow.com/questions/26982274/ps-command-doesnt-work-in-docker-container/26982502">Ps command not found</a></li>
<li><a href="https://www.digitalocean.com/community/tutorials/how-to-remove-docker-images-containers-and-volumes" target="_blank">Docker Verilerini Temizleme</a></li>
<li><a href="https://www.youtube.com/watch?v=1BI2W-PGkKw" target="_blank">Docker for Java Devs</a></li>
</ul>
<i><br /></i></div>
</div>
<div>
<b>Docker Cheat Sheats: (<a href="https://gokhansengun.com/docker-nedir-nasil-calisir-nerede-kullanilir/" target="_blank">alıntıdır</a>)</b><br />
<b><br /></b>
<b>*&nbsp;</b><a href="https://www.docker.com/sites/default/files/Docker_CheatSheet_08.09.2016_0.pdf" target="_blank">Cheat Sheets PDF</a><br />
<br /></div>
<div>
<div class="separator" style="clear: both; text-align: center;">
<a href="https://cdn-images-1.medium.com/max/1400/1*G_9c9ttl-09eSKoSazPnNQ.png" imageanchor="1" style="margin-left: 1em; margin-right: 1em;"><img border="0" data-original-height="403" data-original-width="800" height="322" src="https://cdn-images-1.medium.com/max/1400/1*G_9c9ttl-09eSKoSazPnNQ.png" width="640" /></a></div>
<i><br /></i></div>
<div>
<table style="background-color: #f8f8f8; border-collapse: collapse; border-spacing: 0px; box-sizing: border-box; color: #404040; font-family: &quot;PT Serif&quot;, Georgia, Times, &quot;Times New Roman&quot;, serif; font-size: 16px; padding: 0px;"><thead style="box-sizing: border-box;">
<tr style="background-color: white; border-top: 1px solid rgb(204, 204, 204); box-sizing: border-box; margin: 0px; padding: 0px;"><th style="border: 1px solid rgb(204, 204, 204); box-sizing: border-box; margin: 0px; padding: 6px 13px; text-align: left;">Komut</th><th style="border: 1px solid rgb(204, 204, 204); box-sizing: border-box; margin: 0px; padding: 6px 13px; text-align: left;">Açıklaması</th></tr>
</thead><tbody style="box-sizing: border-box;">
<tr style="background-color: white; border-top: 1px solid rgb(204, 204, 204); box-sizing: border-box; margin: 0px; padding: 0px;"><td style="border: 1px solid rgb(204, 204, 204); box-sizing: border-box; margin: 0px; padding: 6px 13px;"><code class="highlighter-rouge" style="background-color: #f9f2f4; border-radius: 4px; box-sizing: border-box; color: #c7254e; font-family: Menlo, Monaco, Consolas, &quot;Courier New&quot;, monospace; font-size: 14.4px; margin-bottom: 0px; margin-top: 0px; padding: 2px 4px;">docker images</code></td><td style="border: 1px solid rgb(204, 204, 204); box-sizing: border-box; margin: 0px; padding: 6px 13px;">Lokal registry’de mevcut bulunan Image’ları listeler</td></tr>
<tr style="border-top: 1px solid rgb(204, 204, 204); box-sizing: border-box; margin: 0px; padding: 0px;"><td style="border: 1px solid rgb(204, 204, 204); box-sizing: border-box; margin: 0px; padding: 6px 13px;"><code class="highlighter-rouge" style="background-color: #f9f2f4; border-radius: 4px; box-sizing: border-box; color: #c7254e; font-family: Menlo, Monaco, Consolas, &quot;Courier New&quot;, monospace; font-size: 14.4px; margin-bottom: 0px; margin-top: 0px; padding: 2px 4px;">docker ps</code></td><td style="border: 1px solid rgb(204, 204, 204); box-sizing: border-box; margin: 0px; padding: 6px 13px;">Halihazırda çalışmakta olan Container’ları listeler</td></tr>
<tr style="background-color: white; border-top: 1px solid rgb(204, 204, 204); box-sizing: border-box; margin: 0px; padding: 0px;"><td style="border: 1px solid rgb(204, 204, 204); box-sizing: border-box; margin: 0px; padding: 6px 13px;"><code class="highlighter-rouge" style="background-color: #f9f2f4; border-radius: 4px; box-sizing: border-box; color: #c7254e; font-family: Menlo, Monaco, Consolas, &quot;Courier New&quot;, monospace; font-size: 14.4px; margin-bottom: 0px; margin-top: 0px; padding: 2px 4px;">docker ps -a</code></td><td style="border: 1px solid rgb(204, 204, 204); box-sizing: border-box; margin: 0px; padding: 6px 13px;">Docker Daemon üzerindeki bütün Container’ları listeler</td></tr>
<tr style="border-top: 1px solid rgb(204, 204, 204); box-sizing: border-box; margin: 0px; padding: 0px;"><td style="border: 1px solid rgb(204, 204, 204); box-sizing: border-box; margin: 0px; padding: 6px 13px;"><code class="highlighter-rouge" style="background-color: #f9f2f4; border-radius: 4px; box-sizing: border-box; color: #c7254e; font-family: Menlo, Monaco, Consolas, &quot;Courier New&quot;, monospace; font-size: 14.4px; margin-bottom: 0px; margin-top: 0px; padding: 2px 4px;">docker ps -aq</code></td><td style="border: 1px solid rgb(204, 204, 204); box-sizing: border-box; margin: 0px; padding: 6px 13px;">Docker Daemon üzerindeki bütün Container’ların ID’lerini listeler</td></tr>
<tr style="background-color: white; border-top: 1px solid rgb(204, 204, 204); box-sizing: border-box; margin: 0px; padding: 0px;"><td style="border: 1px solid rgb(204, 204, 204); box-sizing: border-box; margin: 0px; padding: 6px 13px;"><code class="highlighter-rouge" style="background-color: #f9f2f4; border-radius: 4px; box-sizing: border-box; color: #c7254e; font-family: Menlo, Monaco, Consolas, &quot;Courier New&quot;, monospace; font-size: 14.4px; margin-bottom: 0px; margin-top: 0px; padding: 2px 4px;">docker pull &lt;repository_name&gt;/&lt;image_name&gt;:&lt;image_tag&gt;</code></td><td style="border: 1px solid rgb(204, 204, 204); box-sizing: border-box; margin: 0px; padding: 6px 13px;">Belirtilen Image’ı lokal registry’ye indirir. Örnek:&nbsp;<code class="highlighter-rouge" style="background-color: #f9f2f4; border-radius: 4px; box-sizing: border-box; color: #c7254e; font-family: Menlo, Monaco, Consolas, &quot;Courier New&quot;, monospace; font-size: 14.4px; margin-bottom: 0px; margin-top: 0px; padding: 2px 4px;">docker pull gsengun/jmeter3.0:1.7</code></td></tr>
<tr style="border-top: 1px solid rgb(204, 204, 204); box-sizing: border-box; margin: 0px; padding: 0px;"><td style="border: 1px solid rgb(204, 204, 204); box-sizing: border-box; margin: 0px; padding: 6px 13px;"><code class="highlighter-rouge" style="background-color: #f9f2f4; border-radius: 4px; box-sizing: border-box; color: #c7254e; font-family: Menlo, Monaco, Consolas, &quot;Courier New&quot;, monospace; font-size: 14.4px; margin-bottom: 0px; margin-top: 0px; padding: 2px 4px;">docker top &lt;container_id&gt;</code></td><td style="border: 1px solid rgb(204, 204, 204); box-sizing: border-box; margin: 0px; padding: 6px 13px;">İlgili Container’da&nbsp;<code class="highlighter-rouge" style="background-color: #f9f2f4; border-radius: 4px; box-sizing: border-box; color: #c7254e; font-family: Menlo, Monaco, Consolas, &quot;Courier New&quot;, monospace; font-size: 14.4px; margin-bottom: 0px; margin-top: 0px; padding: 2px 4px;">top</code>&nbsp;komutunu çalıştırarak çıktısını gösterir</td></tr>
<tr style="background-color: white; border-top: 1px solid rgb(204, 204, 204); box-sizing: border-box; margin: 0px; padding: 0px;"><td style="border: 1px solid rgb(204, 204, 204); box-sizing: border-box; margin: 0px; padding: 6px 13px;"><code class="highlighter-rouge" style="background-color: #f9f2f4; border-radius: 4px; box-sizing: border-box; color: #c7254e; font-family: Menlo, Monaco, Consolas, &quot;Courier New&quot;, monospace; font-size: 14.4px; margin-bottom: 0px; margin-top: 0px; padding: 2px 4px;">docker run -it &lt;image_id|image_name&gt; CMD</code></td><td style="border: 1px solid rgb(204, 204, 204); box-sizing: border-box; margin: 0px; padding: 6px 13px;">Verilen Image’dan terminal’i attach ederek bir Container oluşturur</td></tr>
<tr style="border-top: 1px solid rgb(204, 204, 204); box-sizing: border-box; margin: 0px; padding: 0px;"><td style="border: 1px solid rgb(204, 204, 204); box-sizing: border-box; margin: 0px; padding: 6px 13px;"><code class="highlighter-rouge" style="background-color: #f9f2f4; border-radius: 4px; box-sizing: border-box; color: #c7254e; font-family: Menlo, Monaco, Consolas, &quot;Courier New&quot;, monospace; font-size: 14.4px; margin-bottom: 0px; margin-top: 0px; padding: 2px 4px;">docker pause &lt;container_id&gt;</code></td><td style="border: 1px solid rgb(204, 204, 204); box-sizing: border-box; margin: 0px; padding: 6px 13px;">İlgili Container’ı duraklatır</td></tr>
<tr style="background-color: white; border-top: 1px solid rgb(204, 204, 204); box-sizing: border-box; margin: 0px; padding: 0px;"><td style="border: 1px solid rgb(204, 204, 204); box-sizing: border-box; margin: 0px; padding: 6px 13px;"><code class="highlighter-rouge" style="background-color: #f9f2f4; border-radius: 4px; box-sizing: border-box; color: #c7254e; font-family: Menlo, Monaco, Consolas, &quot;Courier New&quot;, monospace; font-size: 14.4px; margin-bottom: 0px; margin-top: 0px; padding: 2px 4px;">docker unpause &lt;container_id&gt;</code></td><td style="border: 1px solid rgb(204, 204, 204); box-sizing: border-box; margin: 0px; padding: 6px 13px;">İlgili Container&nbsp;<code class="highlighter-rouge" style="background-color: #f9f2f4; border-radius: 4px; box-sizing: border-box; color: #c7254e; font-family: Menlo, Monaco, Consolas, &quot;Courier New&quot;, monospace; font-size: 14.4px; margin-bottom: 0px; margin-top: 0px; padding: 2px 4px;">pause</code>&nbsp;ile duraklatılmış ise çalışmasına devam ettirilir</td></tr>
<tr style="border-top: 1px solid rgb(204, 204, 204); box-sizing: border-box; margin: 0px; padding: 0px;"><td style="border: 1px solid rgb(204, 204, 204); box-sizing: border-box; margin: 0px; padding: 6px 13px;"><code class="highlighter-rouge" style="background-color: #f9f2f4; border-radius: 4px; box-sizing: border-box; color: #c7254e; font-family: Menlo, Monaco, Consolas, &quot;Courier New&quot;, monospace; font-size: 14.4px; margin-bottom: 0px; margin-top: 0px; padding: 2px 4px;">docker stop &lt;container_id&gt;</code></td><td style="border: 1px solid rgb(204, 204, 204); box-sizing: border-box; margin: 0px; padding: 6px 13px;">İlgili Container’ı durdurur</td></tr>
<tr style="background-color: white; border-top: 1px solid rgb(204, 204, 204); box-sizing: border-box; margin: 0px; padding: 0px;"><td style="border: 1px solid rgb(204, 204, 204); box-sizing: border-box; margin: 0px; padding: 6px 13px;"><code class="highlighter-rouge" style="background-color: #f9f2f4; border-radius: 4px; box-sizing: border-box; color: #c7254e; font-family: Menlo, Monaco, Consolas, &quot;Courier New&quot;, monospace; font-size: 14.4px; margin-bottom: 0px; margin-top: 0px; padding: 2px 4px;">docker start &lt;container_id&gt;</code></td><td style="border: 1px solid rgb(204, 204, 204); box-sizing: border-box; margin: 0px; padding: 6px 13px;">İlgili Container’ı durdurulmuşsa tekrar başlatır</td></tr>
<tr style="border-top: 1px solid rgb(204, 204, 204); box-sizing: border-box; margin: 0px; padding: 0px;"><td style="border: 1px solid rgb(204, 204, 204); box-sizing: border-box; margin: 0px; padding: 6px 13px;"><code class="highlighter-rouge" style="background-color: #f9f2f4; border-radius: 4px; box-sizing: border-box; color: #c7254e; font-family: Menlo, Monaco, Consolas, &quot;Courier New&quot;, monospace; font-size: 14.4px; margin-bottom: 0px; margin-top: 0px; padding: 2px 4px;">docker rm &lt;container_id&gt;</code></td><td style="border: 1px solid rgb(204, 204, 204); box-sizing: border-box; margin: 0px; padding: 6px 13px;">İlgili Container’ı kaldırır fakat ilişkili Volume’lara dokunmaz</td></tr>
<tr style="background-color: white; border-top: 1px solid rgb(204, 204, 204); box-sizing: border-box; margin: 0px; padding: 0px;"><td style="border: 1px solid rgb(204, 204, 204); box-sizing: border-box; margin: 0px; padding: 6px 13px;"><code class="highlighter-rouge" style="background-color: #f9f2f4; border-radius: 4px; box-sizing: border-box; color: #c7254e; font-family: Menlo, Monaco, Consolas, &quot;Courier New&quot;, monospace; font-size: 14.4px; margin-bottom: 0px; margin-top: 0px; padding: 2px 4px;">docker rm -v &lt;container_id&gt;</code></td><td style="border: 1px solid rgb(204, 204, 204); box-sizing: border-box; margin: 0px; padding: 6px 13px;">İlgili Container’ı ilişkili Volume’lar ile birlikte kaldırır</td></tr>
<tr style="border-top: 1px solid rgb(204, 204, 204); box-sizing: border-box; margin: 0px; padding: 0px;"><td style="border: 1px solid rgb(204, 204, 204); box-sizing: border-box; margin: 0px; padding: 6px 13px;"><code class="highlighter-rouge" style="background-color: #f9f2f4; border-radius: 4px; box-sizing: border-box; color: #c7254e; font-family: Menlo, Monaco, Consolas, &quot;Courier New&quot;, monospace; font-size: 14.4px; margin-bottom: 0px; margin-top: 0px; padding: 2px 4px;">docker rm -f &lt;container_id&gt;</code></td><td style="border: 1px solid rgb(204, 204, 204); box-sizing: border-box; margin: 0px; padding: 6px 13px;">İlgili Container’ı zorlayarak kaldırır. Çalışan bir Container ancak&nbsp;<code class="highlighter-rouge" style="background-color: #f9f2f4; border-radius: 4px; box-sizing: border-box; color: #c7254e; font-family: Menlo, Monaco, Consolas, &quot;Courier New&quot;, monospace; font-size: 14.4px; margin-bottom: 0px; margin-top: 0px; padding: 2px 4px;">-f</code>&nbsp;ile kaldırılabilir</td></tr>
<tr style="background-color: white; border-top: 1px solid rgb(204, 204, 204); box-sizing: border-box; margin: 0px; padding: 0px;"><td style="border: 1px solid rgb(204, 204, 204); box-sizing: border-box; margin: 0px; padding: 6px 13px;"><code class="highlighter-rouge" style="background-color: #f9f2f4; border-radius: 4px; box-sizing: border-box; color: #c7254e; font-family: Menlo, Monaco, Consolas, &quot;Courier New&quot;, monospace; font-size: 14.4px; margin-bottom: 0px; margin-top: 0px; padding: 2px 4px;">docker rmi &lt;image_id|image_name&gt;</code></td><td style="border: 1px solid rgb(204, 204, 204); box-sizing: border-box; margin: 0px; padding: 6px 13px;">İlgili Image’ı siler</td></tr>
<tr style="border-top: 1px solid rgb(204, 204, 204); box-sizing: border-box; margin: 0px; padding: 0px;"><td style="border: 1px solid rgb(204, 204, 204); box-sizing: border-box; margin: 0px; padding: 6px 13px;"><code class="highlighter-rouge" style="background-color: #f9f2f4; border-radius: 4px; box-sizing: border-box; color: #c7254e; font-family: Menlo, Monaco, Consolas, &quot;Courier New&quot;, monospace; font-size: 14.4px; margin-bottom: 0px; margin-top: 0px; padding: 2px 4px;">docker rmi -f &lt;image_id|image_name&gt;</code></td><td style="border: 1px solid rgb(204, 204, 204); box-sizing: border-box; margin: 0px; padding: 6px 13px;">İlgili Image’ı zorlayarak kaldırır, başka isimlerle Tag’lenmiş Image’lar&nbsp;<code class="highlighter-rouge" style="background-color: #f9f2f4; border-radius: 4px; box-sizing: border-box; color: #c7254e; font-family: Menlo, Monaco, Consolas, &quot;Courier New&quot;, monospace; font-size: 14.4px; margin-bottom: 0px; margin-top: 0px; padding: 2px 4px;">-f</code>&nbsp;ile kaldırılabilir</td></tr>
<tr style="background-color: white; border-top: 1px solid rgb(204, 204, 204); box-sizing: border-box; margin: 0px; padding: 0px;"><td style="border: 1px solid rgb(204, 204, 204); box-sizing: border-box; margin: 0px; padding: 6px 13px;"><code class="highlighter-rouge" style="background-color: #f9f2f4; border-radius: 4px; box-sizing: border-box; color: #c7254e; font-family: Menlo, Monaco, Consolas, &quot;Courier New&quot;, monospace; font-size: 14.4px; margin-bottom: 0px; margin-top: 0px; padding: 2px 4px;">docker info</code></td><td style="border: 1px solid rgb(204, 204, 204); box-sizing: border-box; margin: 0px; padding: 6px 13px;">Docker Daemon’la ilgili özet bilgiler verir</td></tr>
<tr style="border-top: 1px solid rgb(204, 204, 204); box-sizing: border-box; margin: 0px; padding: 0px;"><td style="border: 1px solid rgb(204, 204, 204); box-sizing: border-box; margin: 0px; padding: 6px 13px;"><code class="highlighter-rouge" style="background-color: #f9f2f4; border-radius: 4px; box-sizing: border-box; color: #c7254e; font-family: Menlo, Monaco, Consolas, &quot;Courier New&quot;, monospace; font-size: 14.4px; margin-bottom: 0px; margin-top: 0px; padding: 2px 4px;">docker inspect &lt;container_id&gt;</code></td><td style="border: 1px solid rgb(204, 204, 204); box-sizing: border-box; margin: 0px; padding: 6px 13px;">İlgili Container’la ilgili detaylı bilgiler verir</td></tr>
<tr style="background-color: white; border-top: 1px solid rgb(204, 204, 204); box-sizing: border-box; margin: 0px; padding: 0px;"><td style="border: 1px solid rgb(204, 204, 204); box-sizing: border-box; margin: 0px; padding: 6px 13px;"><code class="highlighter-rouge" style="background-color: #f9f2f4; border-radius: 4px; box-sizing: border-box; color: #c7254e; font-family: Menlo, Monaco, Consolas, &quot;Courier New&quot;, monospace; font-size: 14.4px; margin-bottom: 0px; margin-top: 0px; padding: 2px 4px;">docker inspect &lt;image_id|image_name&gt;</code></td><td style="border: 1px solid rgb(204, 204, 204); box-sizing: border-box; margin: 0px; padding: 6px 13px;">İlgili Image’la ilgili detaylı bilgiler verir</td></tr>
<tr style="border-top: 1px solid rgb(204, 204, 204); box-sizing: border-box; margin: 0px; padding: 0px;"><td style="border: 1px solid rgb(204, 204, 204); box-sizing: border-box; margin: 0px; padding: 6px 13px;"><code class="highlighter-rouge" style="background-color: #f9f2f4; border-radius: 4px; box-sizing: border-box; color: #c7254e; font-family: Menlo, Monaco, Consolas, &quot;Courier New&quot;, monospace; font-size: 14.4px; margin-bottom: 0px; margin-top: 0px; padding: 2px 4px;">docker rm $(docker ps -aq)</code></td><td style="border: 1px solid rgb(204, 204, 204); box-sizing: border-box; margin: 0px; padding: 6px 13px;">Bütün Container’ları kaldırır</td></tr>
<tr style="background-color: white; border-top: 1px solid rgb(204, 204, 204); box-sizing: border-box; margin: 0px; padding: 0px;"><td style="border: 1px solid rgb(204, 204, 204); box-sizing: border-box; margin: 0px; padding: 6px 13px;"><code class="highlighter-rouge" style="background-color: #f9f2f4; border-radius: 4px; box-sizing: border-box; color: #c7254e; font-family: Menlo, Monaco, Consolas, &quot;Courier New&quot;, monospace; font-size: 14.4px; margin-bottom: 0px; margin-top: 0px; padding: 2px 4px;">docker stop $(docker ps -aq)</code></td><td style="border: 1px solid rgb(204, 204, 204); box-sizing: border-box; margin: 0px; padding: 6px 13px;">Çalışan bütün Container’ları durdurur</td></tr>
<tr style="border-top: 1px solid rgb(204, 204, 204); box-sizing: border-box; margin: 0px; padding: 0px;"><td style="border: 1px solid rgb(204, 204, 204); box-sizing: border-box; margin: 0px; padding: 6px 13px;"><code class="highlighter-rouge" style="background-color: #f9f2f4; border-radius: 4px; box-sizing: border-box; color: #c7254e; font-family: Menlo, Monaco, Consolas, &quot;Courier New&quot;, monospace; font-size: 14.4px; margin-bottom: 0px; margin-top: 0px; padding: 2px 4px;">docker rmi $(docker images -aq)</code></td><td style="border: 1px solid rgb(204, 204, 204); box-sizing: border-box; margin: 0px; padding: 6px 13px;">Bütün Image’ları kaldırır</td></tr>
<tr style="background-color: white; border-top: 1px solid rgb(204, 204, 204); box-sizing: border-box; margin: 0px; padding: 0px;"><td style="border: 1px solid rgb(204, 204, 204); box-sizing: border-box; margin: 0px; padding: 6px 13px;"><code class="highlighter-rouge" style="background-color: #f9f2f4; border-radius: 4px; box-sizing: border-box; color: #c7254e; font-family: Menlo, Monaco, Consolas, &quot;Courier New&quot;, monospace; font-size: 14.4px; margin-bottom: 0px; margin-top: 0px; padding: 2px 4px;">docker images -q -f dangling=true</code></td><td style="border: 1px solid rgb(204, 204, 204); box-sizing: border-box; margin: 0px; padding: 6px 13px;">Dangling (taglenmemiş ve bir Container ile ilişkilendirilmemiş) Image’ları listeler</td></tr>
<tr style="border-top: 1px solid rgb(204, 204, 204); box-sizing: border-box; margin: 0px; padding: 0px;"><td style="border: 1px solid rgb(204, 204, 204); box-sizing: border-box; margin: 0px; padding: 6px 13px;"><code class="highlighter-rouge" style="background-color: #f9f2f4; border-radius: 4px; box-sizing: border-box; color: #c7254e; font-family: Menlo, Monaco, Consolas, &quot;Courier New&quot;, monospace; font-size: 14.4px; margin-bottom: 0px; margin-top: 0px; padding: 2px 4px;">docker rmi $(docker images -q -f dangling=true)</code></td><td style="border: 1px solid rgb(204, 204, 204); box-sizing: border-box; margin: 0px; padding: 6px 13px;">Dangling Image’ları kaldırır</td></tr>
<tr style="background-color: white; border-top: 1px solid rgb(204, 204, 204); box-sizing: border-box; margin: 0px; padding: 0px;"><td style="border: 1px solid rgb(204, 204, 204); box-sizing: border-box; margin: 0px; padding: 6px 13px;"><code class="highlighter-rouge" style="background-color: #f9f2f4; border-radius: 4px; box-sizing: border-box; color: #c7254e; font-family: Menlo, Monaco, Consolas, &quot;Courier New&quot;, monospace; font-size: 14.4px; margin-bottom: 0px; margin-top: 0px; padding: 2px 4px;">docker volume ls -f dangling=true</code></td><td style="border: 1px solid rgb(204, 204, 204); box-sizing: border-box; margin: 0px; padding: 6px 13px;">Dangling Volume’ları listeler</td></tr>
<tr style="border-top: 1px solid rgb(204, 204, 204); box-sizing: border-box; margin: 0px; padding: 0px;"><td style="border: 1px solid rgb(204, 204, 204); box-sizing: border-box; margin: 0px; padding: 6px 13px;"><code class="highlighter-rouge" style="background-color: #f9f2f4; border-radius: 4px; box-sizing: border-box; color: #c7254e; font-family: Menlo, Monaco, Consolas, &quot;Courier New&quot;, monospace; font-size: 14.4px; margin-bottom: 0px; margin-top: 0px; padding: 2px 4px;">docker volume rm $(docker volume ls -f dangling=true -q)</code></td><td style="border: 1px solid rgb(204, 204, 204); box-sizing: border-box; margin: 0px; padding: 6px 13px;">Danling Volume’ları kaldırır</td></tr>
<tr style="background-color: white; border-top: 1px solid rgb(204, 204, 204); box-sizing: border-box; margin: 0px; padding: 0px;"><td style="border: 1px solid rgb(204, 204, 204); box-sizing: border-box; margin: 0px; padding: 6px 13px;"><code class="highlighter-rouge" style="background-color: #f9f2f4; border-radius: 4px; box-sizing: border-box; color: #c7254e; font-family: Menlo, Monaco, Consolas, &quot;Courier New&quot;, monospace; font-size: 14.4px; margin-bottom: 0px; margin-top: 0px; padding: 2px 4px;">docker logs &lt;container_id&gt;</code></td><td style="border: 1px solid rgb(204, 204, 204); box-sizing: border-box; margin: 0px; padding: 6px 13px;">İlgili Container’ın terminalinde o ana kadar oluşan çıktıyı gösterir</td></tr>
<tr style="border-top: 1px solid rgb(204, 204, 204); box-sizing: border-box; margin: 0px; padding: 0px;"><td style="border: 1px solid rgb(204, 204, 204); box-sizing: border-box; margin: 0px; padding: 6px 13px;"><code class="highlighter-rouge" style="background-color: #f9f2f4; border-radius: 4px; box-sizing: border-box; color: #c7254e; font-family: Menlo, Monaco, Consolas, &quot;Courier New&quot;, monospace; font-size: 14.4px; margin-bottom: 0px; margin-top: 0px; padding: 2px 4px;">docker logs -f &lt;container_id&gt;</code></td><td style="border: 1px solid rgb(204, 204, 204); box-sizing: border-box; margin: 0px; padding: 6px 13px;">İlgili Container’ın terminalinde o ana kadar oluşan çıktıyı gösterir ve&nbsp;<code class="highlighter-rouge" style="background-color: #f9f2f4; border-radius: 4px; box-sizing: border-box; color: #c7254e; font-family: Menlo, Monaco, Consolas, &quot;Courier New&quot;, monospace; font-size: 14.4px; margin-bottom: 0px; margin-top: 0px; padding: 2px 4px;">-f</code>&nbsp;follow parametresi ile o andan sonra oluşan logları da göstermeye devam eder</td></tr>
<tr style="background-color: white; border-top: 1px solid rgb(204, 204, 204); box-sizing: border-box; margin: 0px; padding: 0px;"><td style="border: 1px solid rgb(204, 204, 204); box-sizing: border-box; margin: 0px; padding: 6px 13px;"><code class="highlighter-rouge" style="background-color: #f9f2f4; border-radius: 4px; box-sizing: border-box; color: #c7254e; font-family: Menlo, Monaco, Consolas, &quot;Courier New&quot;, monospace; font-size: 14.4px; margin-bottom: 0px; margin-top: 0px; padding: 2px 4px;">docker exec &lt;container_id&gt; &lt;command&gt;</code></td><td style="border: 1px solid rgb(204, 204, 204); box-sizing: border-box; margin: 0px; padding: 6px 13px;">Çalışan bir Container içinde bir komut koşturmak için kullanılır</td></tr>
<tr style="border-top: 1px solid rgb(204, 204, 204); box-sizing: border-box; margin: 0px; padding: 0px;"><td style="border: 1px solid rgb(204, 204, 204); box-sizing: border-box; margin: 0px; padding: 6px 13px;"><code class="highlighter-rouge" style="background-color: #f9f2f4; border-radius: 4px; box-sizing: border-box; color: #c7254e; font-family: Menlo, Monaco, Consolas, &quot;Courier New&quot;, monospace; font-size: 14.4px; margin-bottom: 0px; margin-top: 0px; padding: 2px 4px;">docker exec -it &lt;container_id&gt; /bin/bash</code></td><td style="border: 1px solid rgb(204, 204, 204); box-sizing: border-box; margin: 0px; padding: 6px 13px;">Çalışan bir Container içinde terminal açmak için kullanılır. İlgili Image’da /bin/bash bulunduğu varsayımı ile</td></tr>
<tr style="background-color: white; border-top: 1px solid rgb(204, 204, 204); box-sizing: border-box; margin: 0px; padding: 0px;"><td style="border: 1px solid rgb(204, 204, 204); box-sizing: border-box; margin: 0px; padding: 6px 13px;"><code class="highlighter-rouge" style="background-color: #f9f2f4; border-radius: 4px; box-sizing: border-box; color: #c7254e; font-family: Menlo, Monaco, Consolas, &quot;Courier New&quot;, monospace; font-size: 14.4px; margin-bottom: 0px; margin-top: 0px; padding: 2px 4px;">docker attach &lt;container_id&gt;</code></td><td style="border: 1px solid rgb(204, 204, 204); box-sizing: border-box; margin: 0px; padding: 6px 13px;">Önceden detached modda&nbsp;<code class="highlighter-rouge" style="background-color: #f9f2f4; border-radius: 4px; box-sizing: border-box; color: #c7254e; font-family: Menlo, Monaco, Consolas, &quot;Courier New&quot;, monospace; font-size: 14.4px; margin-bottom: 0px; margin-top: 0px; padding: 2px 4px;">-d</code>&nbsp;başlatılan bir Container’a attach olmak için kullanılır</td></tr>
</tbody></table>
</div>
<div>
<i><br /></i></div>
</div>
<div>
<i><br /></i></div>
<div>
<br /></div>
