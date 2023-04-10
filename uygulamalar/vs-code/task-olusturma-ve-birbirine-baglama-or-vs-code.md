---
description: VSCode, tasks.json ile task oluşturma ve birbirine bağlama
---

# 🤹♂ Task oluşturma ve birbirine bağlama | VS Code

```bash
{
    "version": "2.0.0",
    "tasks": [
        {
            "label": "build and run",
            "type": "shell",
            "command": "npm run build",
            "args": [],
            "options": {
                "cwd": "${workspaceFolder}"
            },
            "problemMatcher": [],
            "group": {
                "kind": "build",
                "isDefault": true
            },
            "dependsOn": ["build"],
            "dependsOrder": "sequence",
						"presentation": {
                "echo": false,
                "reveal": "silent",
                "focus": false,
                "panel": "shared",
                "showReuseMessage": false,
                "clear": true,
                "close": true
            },
        },
        {
            "label": "build",
            "type": "shell",
            "command": "npm run build",
            "args": [],
            "options": {
                "cwd": "${workspaceFolder}"
            },
            "problemMatcher": []
        },
        {
            "label": "run",
            "type": "shell",
            "command": "npm run start",
            "args": [],
            "options": {
                "cwd": "${workspaceFolder}"
            },
            "problemMatcher": []
        }
    ]
}
```

* `dependsOn` komutu ile diğer taskları çalıştırabiliriz
  * `sequence` ardışık olarak taskları çalıştırır
*   `presentation` ile `task`ın çalışma şekilini ayarlarız

    * Sessiz bir çalışma için

    ```bash
    "presentation": {
        "echo": false,
        "reveal": "silent",
        "focus": false,
        "panel": "shared",
        "showReuseMessage": false,
        "clear": true,
        "close": true
    },
    ```
*   `kind` yapısı ile grup belirleriz, bu sayede kısayollarla hızlıca kullanabiliriz

    * `build` grubunun kısayolu $⌘⇧B$
    * `isDefault` ile de direkt çalışmasını sağlarız
    * Yapmazsak, `build` `tasks` arasından seçim yapmamızı ister

    ```bash
    "group": {
        "kind": "build",
        "isDefault": true
    },
    ```

## 📑 References

* “vscode task that use two command” → [ChatGPT](https://chat.openai.com/chat)
