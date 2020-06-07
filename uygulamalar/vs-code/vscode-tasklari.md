# 👷‍♂️ Tasks \| VS Code

## 👪 Birden Fazla Task Çalıştırma

* 🔗 `dependsOn` anahtarı ile birden fazla task çalıştırabilirsiniz

```javascript
{
    "version": "2.0.0",
    "tasks": [
        {
            "label": "Echo 1",
            "command": "echo",
            "type": "shell",
            "args": [ "echo1" ],
            "group": {
                "kind": "build",
                "isDefault": true
            },
            "dependsOn":["Echo 2"]
        },
        {
            "label": "Echo 2",
            "type": "shell",
            "command": "echo",
            "args": [ "echo2" ],
            "group": "build"
        }
    ]
}
```

{% hint style="info" %}
‍🧙‍♂ Detaylı bilgi için [How to run multiple tasks in VS Code on build?](https://stackoverflow.com/questions/52238171/how-to-run-multiple-tasks-in-vs-code-on-build) alanına bakabilirsin.
{% endhint %}

