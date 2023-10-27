# Type Alias Gösterimi Sorunu ve Çözümü

<figure><img src="../.gitbook/assets/DALL·E 2023-10-26 23.53.04 - illustration of a very cute cat with lineal colors lying down on a desk with programming books, a cup with the TypeScript logo, and type symbols.png" alt=""><figcaption></figcaption></figure>

### İçerikte alttaki sorunlara çözüm bulacağız:

1. "VS Code TypeScript type hover display issue"
2. "VS Code displaying type alias as template literal TypeScript"
3. "Change how VS Code shows TypeScript type aliases"
4. "TypeScript type resolution problem in VS Code hover"
5. "VS Code not resolving TypeScript type alias correctly"

## TypeScript ile basit **`type`** yapıları tanımladığımızda yeni isim yerine detaylarını gösteriyor.

```typescript
export type PairId = Readonly<`${AssetSymbol}_${AssetSymbol}`>
```

<figure><img src="../.gitbook/assets/image.png" alt=""><figcaption></figcaption></figure>

## Sorunu çözmek için **`alias`** isimli ek bir **`type`** daha tanımlıyoruz.

```typescript
type alias<t> = t & { _?: never }
export type PairId = alias<Readonly<`${AssetSymbol}_${AssetSymbol}`>>
```

<figure><img src="../.gitbook/assets/image (1).png" alt=""><figcaption></figcaption></figure>

## Referanslar

{% embed url="https://github.com/microsoft/TypeScript/issues/31940#issuecomment-1555533360" %}
