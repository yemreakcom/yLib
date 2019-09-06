# 🗃 Raporlama İşlemleri (Logging)

Raporlama işlemleri için `logging` modülü kullanılır

```python
import logging

message = "Raporlanacak"
LOG_DIR = "dosya/dizini"
LOG_FILE = "dosya.log"
FLAG = "w" # a+, r
ENCODING = "utf-8"

# Rapolamayı tanımlama
logging.basicConfig(handlers=[logging.FileHandler(LOG_DIR + LOG_FILE, FLAG, ENCODING)], level=logging.DEBUG, format='%(asctime)s: %(message)s')

logging.info("mesaj") # Raporu yazma

```
