# 🌈 Workflow \| GitHub

## 🎈 Ne İşe Yarar

* 🔄 Repoları denetleyen ve belirli durumlarda tetiklenen eylemlerdir
* 🤖 İşlemleri otomatikleştirme olayı ile çalışma hızınızı artırır

## 🌟 Önerilen Yapılar

| 💎 Workflow | 📝 Açıklama |
| :--- | :--- |
| [Pull](https://github.com/apps/pull) | Forklanan repoları güncel tutar |
| [GitHub Push](https://github.com/marketplace/actions/github-push) | Push işleminde tetiklenir |
| [Pre Commit](https://github.com/marketplace/actions/pre-commit) | Commit işlemleri ve PR'lardan önce tetiklenir |

## 🤫 GitHub Secret

* 🚛 GitHub workflow yapılarına veri aktarmayı sağar
* 👮‍♂️ Gizli verileri workflow üzerinde kullanmak için tercih edilir
  * 🔑 API key gibi verileri
  * 🔏 Kullanıcı adı ve şifre bilgileri
* 👁️ Oluşturulduktan sonra tekrar görülemezler
* ⚙️ `settings/secrets` alanından oluşturulur
* 🐣 `${{ secrets.<secret_name> }}` yapısı ile workflow üzerinden erişilir

