# Type Alias Gösterimi Sorunu ve Çözümü



![](https://prod-files-secure.s3.us-west-2.amazonaws.com/ee37cc61-925f-4001-b016-3854758f2639/3f4c3c80-0710-40b9-bac4-284a176e1b6a/DALLE\_2023-10-26\_23.53.04\_-\_illustration\_of\_a\_very\_cute\_cat\_with\_lineal\_colors\_lying\_down\_on\_a\_desk\_with\_programming\_books\_a\_cup\_with\_the\_TypeScript\_logo\_and\_type\_symbols.png?X-Amz-Algorithm=AWS4-HMAC-SHA256\&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD\&X-Amz-Credential=AKIAT73L2G45EIPT3X45%2F20231026%2Fus-west-2%2Fs3%2Faws4\_request\&X-Amz-Date=20231026T205738Z\&X-Amz-Expires=3600\&X-Amz-Signature=8cf3700b20f8f20790073e140540140c4d4aae5bb199e92cece2c70e6e8c4e9e\&X-Amz-SignedHeaders=host\&x-id=GetObject)

### İçerikte alttaki sorunlara çözüm bulacağız:

1. **"VS Code TypeScript type hover display issue"**
2. **"VS Code displaying type alias as template literal TypeScript"**
3. **"Change how VS Code shows TypeScript type aliases"**
4. **"TypeScript type resolution problem in VS Code hover"**
5. **"VS Code not resolving TypeScript type alias correctly"**

## TypeScript ile basit **`type`** yapıları tanımladığımızda yeni isim yerine detaylarını gösteriyor.

```typescript
export type PairId = Readonly<`${AssetSymbol}_${AssetSymbol}`>
```

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/ee37cc61-925f-4001-b016-3854758f2639/f4d6b9ef-98df-4b60-8ebd-da6f6e31e57b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256\&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD\&X-Amz-Credential=AKIAT73L2G45EIPT3X45%2F20231026%2Fus-west-2%2Fs3%2Faws4\_request\&X-Amz-Date=20231026T205739Z\&X-Amz-Expires=3600\&X-Amz-Signature=48bafb8050cb31f8da850acf25795e1024ac5a8bda9081e18397df8c247da674\&X-Amz-SignedHeaders=host\&x-id=GetObject)

## Sorunu çözmek için **`alias`** isimli ek bir **`type`** daha tanımlıyoruz.

```typescript
type alias<t> = t & { _: never }
export type PairId = alias<Readonly<`${AssetSymbol}_${AssetSymbol}`>>
```

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/ee37cc61-925f-4001-b016-3854758f2639/e5ba862e-7905-410c-917a-6ba9e8350861/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256\&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD\&X-Amz-Credential=AKIAT73L2G45EIPT3X45%2F20231026%2Fus-west-2%2Fs3%2Faws4\_request\&X-Amz-Date=20231026T205739Z\&X-Amz-Expires=3600\&X-Amz-Signature=5246e2220ac5515885be49649e3ffe54fd9728be0a8b4600e18203962b7e6d28\&X-Amz-SignedHeaders=host\&x-id=GetObject)

## Referanslar

{% embed url="https://github.com/microsoft/TypeScript/issues/31940#issuecomment-1555533360" %}
