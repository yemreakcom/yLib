# JavaFX ile GUI <!-- omit in toc -->

## İçerikler <!-- omit in toc -->

- [IntelliJ için JavaFx Kurulumu](#IntelliJ-i%C3%A7in-JavaFx-Kurulumu)

## IntelliJ için JavaFx Kurulumu

- İlk olarak [IntelliJ][intellij]'yi indirin
- Resmi sitesinden [JavaFX SDK][javafx sdk]'sını indirin
- İndirdiğiniz arşivdeki çıkartın
- Arşivdeki `javafx-sdk-12.0.1` dosyasını `C:\Program Files\Java` dizinine taşıyın
- GUI düzenleme aracı olan [Scene Builder][scene builder]'ı indirin
- IntelliJ üzerinden `File` - `Settings` - `Languages & Frameworks` - `JavaFx` kısmına [Scene Builder][scene builder]'ın yolunu yazın.
  - Örn: _C:\Program Files\SceneBuilder\SceneBuilder.exe_
- IntelliJ üzerinden `File` - `New` - `Project` - `JavaFX` - `Next` - `Finish` ile projenizi oluşturun
- Son olarak `File` - `Project Structure` - `Modules`
- Açılan ekranda `+` - `Library` - `Java`
- Çıkan ekran ile `C:\Program Files\Java\javafx-sdk-12.0.1\lib` kütüphanesini ekleyin
- İyi kodlamalar ✨

> Not sizin sürümünüz ve yolunuz farklı ise ona göre ayalayın `<yol>\javafx-sdk-<version>\lib`

[intellij]: https://www.jetbrains.com/idea/download/#section=windows
[javafx sdk]: https://gluonhq.com/products/javafx/
[scene builder]: https://gluonhq.com/products/scene-builder/
