---
description: Belirli komutların çalışma durumlarında tetiklenen scriptler
---

# ⚓ Git Hook

## 🎌 Kullanım Talimatları

* 📂 `git init` komutu ile oluşturulan `.git/hooks` dizininde bulunur
* 🧱 Hook Listesi alanındaki size lazım olan isimle dosya oluşturun
  * Örn: `pre-commit` \(dosyanın uzantısı **olmayacak**\)
  * Var olan scriptlerin sonlarındaki `.sample` isminin silinmesiyle içindeki kodlar aktif hale gelir
* [👨‍💻 Shell script](../../code/yardimci/shell.md) yapısı ile çalışmaktadır
* 👮‍♂️ Scriptler `0` dışında bir değer döndürürse, seçilen işlem **tamamlanmaz**.

{% page-ref page="../../code/yardimci/shell.md" %}

## 🧱 Hook Listesi

* [applypatch-msg](https://github.com/git/git/blob/master/templates/hooks--applypatch-msg.sample)
* [pre-applypatch](https://github.com/git/git/blob/master/templates/hooks--pre-applypatch.sample)
* [post-applypatch](https://www.git-scm.com/docs/githooks#_post_applypatch)
* [pre-commit](https://github.com/git/git/blob/master/templates/hooks--pre-commit.sample)
* [prepare-commit-msg](https://github.com/git/git/blob/master/templates/hooks--prepare-commit-msg.sample)
* [commit-msg](https://github.com/git/git/blob/master/templates/hooks--commit-msg.sample)
* [post-commit](https://www.git-scm.com/docs/githooks#_post_commit)
* [pre-rebase](https://github.com/git/git/blob/master/templates/hooks--pre-rebase.sample)
* [post-checkout](https://www.git-scm.com/docs/githooks#_post_checkout)
* [post-merge](https://www.git-scm.com/docs/githooks#_post_merge)
* [pre-receive](https://www.git-scm.com/docs/githooks#pre-receive)
* [update](https://github.com/git/git/blob/master/templates/hooks--update.sample)
* [post-receive](https://www.git-scm.com/docs/githooks#post-receive)
* [post-update](https://github.com/git/git/blob/master/templates/hooks--post-update.sample)
* [pre-auto-gc](https://www.git-scm.com/docs/githooks#_pre_auto_gc)
* [post-rewrite](https://www.git-scm.com/docs/githooks#_post_rewrite)
* [pre-push](https://www.git-scm.com/docs/githooks#_pre_push)

## 🔗 Harici Bağlantılar

{% embed url="https://githooks.com/" %}



