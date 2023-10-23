# TypeScript | Readonly Async Property Tanımlama

Aşağıda, `readonly` olan ama sonradan asenkron olarak yüklenecek bir özellik nasıl tanımlanabileceğine dair bir TypeScript kodu bulabilirsiniz.

```typescript
class MyClass {
  private _myProp: string | null = null;

  get myProp(): Promise<string> {
    if (this._myProp) {
      return Promise.resolve(this._myProp);
    }
    return this.loadMyProp();
  }

  private async loadMyProp(): Promise<string> {
    // Simulate async operation
    this._myProp = await new Promise((resolve) => setTimeout(() => resolve("Loaded Value"), 1000));
    return this._myProp;
  }
}

// Usage
(async () => {
  const myInstance = new MyClass();
  console.log(await myInstance.myProp);  // Outputs "Loaded Value"
})();
```

* `myProp` aslında bir getter fonksiyonu ve ilk çağrıldığında `_myProp`'u yüklemek için `loadMyProp`'u çağırıyor.
* `_myProp` ilk yüklendikten sonra, herhangi bir yeniden yükleme olmadan aynı değeri kullanacak.
* `myProp` `readonly` olarak kabul edilebilir çünkü dışarıdan değiştirilemez; yalnızca sınıf içerisinden güncellenebilir.

Not: Sınıfın dışından doğrudan `_myProp`'a erişilemediği ve değiştirilemediği için, `myProp` sınıf dışı için `readonly` olarak kabul edilebilir.
