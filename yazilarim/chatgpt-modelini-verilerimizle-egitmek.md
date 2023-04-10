---
description: ChatGPT'yi kişisel verilerimizle Python ile nasıl eğitiriz ona bakalım
---

# 👨🏫 ChatGPT modelini verilerimizle eğitmek

## 🕊️ Eğer içeriğiniz ufaksa direkt bu yöntemi kullanarabilirsiniz

* `Article` sonrasındaki alana bilgiyi yazın
* `Questions` sonrasındaki alana da soruyu yazın

<figure><img src="../.gitbook/assets/image (17).png" alt=""><figcaption></figcaption></figure>

## 📚 Daha büyük verilerle eğitmek

### 🏜️ Projeniz içerisinde sanal ortam oluşturun ve bağımlılıkları kurun/text

```bash
# cd ile proje dizinine girin

python3 -m venv venv

# mac ve linux için Sanal ortamı aktif edin
# venv/Scripts/bin/activate # windows için
source venv/bin/activate

# pip'i güncelleyin
pip install -U pip

# Sadece gpt-index 0.4.24 sürümü için kod çalışascaktır
# openai==0.27.4
# gpt-index==0.4.24
# gradio==3.24.1
pip install openai gpt-index==0.4.24 gradio
```

> `grandio` basit bir web arayüzü oluşturup, local ve global olarak erişmenizi sağlar

### `📑 PDF` içerisindekileri metinleri okumak

* PyPDF2 ve PyCryptodome kullanabilirsiniz

```bash
pip install PyPDF2 PyCryptodome
```

### `🔑 OpenAI API Key` yoksa, [OpenAI](https://platform.openai.com/signup) sitesinden oluşturun

<figure><img src="../.gitbook/assets/image (32).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image (1).png" alt=""><figcaption></figcaption></figure>

> `API` kalan kullanımlarınızı [https://platform.openai.com/account/usage](https://platform.openai.com/account/usage) alanından görebilrisiniz

### ⚙️ Proje dizinine `.env` dosyası oluşturun ve içerisindeki gerekli alanları doldurun

* `OPENAI_API_KEY` OpenAI üzerinden oluşturduğun secret key’i buraya yapıştırın
* `DIRECTORY_PATH` olarak tanımlanan dizindeki ve alt dizinlerindeki tüm içerikler veri olarak alınacaktır

```bash
OPENAI_API_KEY=key-degerini-buraya-ekleyin
DIRECTORY_PATH=docs
```

### 👨‍💻 Eğitimi uygulayacağımız `main.py` dosyası içeriği

> Sanal ortamı aktif etmeyi unutmayın

```python
from gpt_index import (
    SimpleDirectoryReader,
    GPTSimpleVectorIndex,
    LLMPredictor,
    PromptHelper,
)
from langchain.chat_models import ChatOpenAI
import gradio as gr
from dotenv import load_dotenv
import os

load_dotenv()

def construct_index(directory_path):
    max_input_size = 4096
    num_outputs = 512
    max_chunk_overlap = 20
    chunk_size_limit = 600

    prompt_helper = PromptHelper(
        max_input_size,
        num_outputs,
        max_chunk_overlap,
        chunk_size_limit=chunk_size_limit,
    )

    llm_predictor = LLMPredictor(
        llm=ChatOpenAI(  # type: ignore
            temperature=0.7, model_name="gpt-3.5-turbo", max_tokens=num_outputs
        )
    )

    documents = SimpleDirectoryReader(directory_path, recursive=True).load_data()

    index = GPTSimpleVectorIndex(
        documents, llm_predictor=llm_predictor, prompt_helper=prompt_helper
    )

    index.save_to_disk("index.json")

    return index

def chatbot(input_text):
    index = GPTSimpleVectorIndex.load_from_disk("index.json")
    response = index.query(input_text, response_mode="compact")
    return response.response

iface = gr.Interface(
    fn=chatbot,
    inputs=gr.components.Textbox(lines=7, label="Enter your text"),
    outputs="text",
    title="Custom-trained AI Chatbot",
)

index = construct_index(os.getenv("DIRECTORY_PATH"))
iface.launch(share=True)
```

### 🖤 Eğitim sonrası `terminal` üzerindeki `... on local URL:` sonrasındaki adrese tıklayın

* Kapatmak için ⌃C yani Ctrl C kısayolunu kullanın

<figure><img src="../.gitbook/assets/image (25).png" alt=""><figcaption></figcaption></figure>

### 🌍 Local hosttaki websiteniz aşağıdaki gibi gözükecektir

* `flag` ile konuşmayı kayıt edebilirsiniz

<figure><img src="../.gitbook/assets/image (31).png" alt=""><figcaption></figcaption></figure>

{% embed url="https://beebom.com/how-train-ai-chatbot-custom-knowledge-base-chatgpt-api/" %}
