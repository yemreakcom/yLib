# 📧 Python ve Twilio ile SMS server oluşturma

## Twilio ile SMS server oluşturma

```python
from flask import Flask, request, redirect
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

@app.route("/sms", methods=['POST'])
def sms_reply():
    """Respond to incoming calls with a simple text message."""
    
    # Use this data in your application logic
    from_number = request.form['From']
    to_number = request.form['To']
    body = request.form['Body']

    # Start our TwiML response
    resp = MessagingResponse()

    # Add a message
    resp.message("The Robots are coming! Head for the hills!")

    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)
```

* [Hata reporalarını](https://console.twilio.com/us1/monitor/logs/debugger/errors) kontrol ederek takip yapabilirsiniz
* `ngrok config add-authtoken <token>` ile giriş yapın, aksi halde `response` döndüremezsiniz
* `ngrok http 5000` ile tuneli açın
* [Active numbers](https://console.twilio.com/us1/develop/phone-numbers/manage/incoming?frameUrl=%2Fconsole%2Fphone-numbers%2Fincoming%2FPN1355a013e02e8b9510d64b4aa9ba365e%3Fx-target-region%3Dus1) alanı üzerinden Messaging kısmında A MESSAGE COMES IN alanına `<tunnel>/sms`
  * `https://a501237-20-229-74-178.eu.ngrok.io/sms`
* [Geo Location izni](https://console.twilio.com/us1/develop/sms/settings/geo-permissions) verin aksi halde SMS gönderemez

{% hint style="info" %}
🚨 Türkiyeden yurt dışına SMS göndermek pahalı, twilio Turkiye numarası sunmuyor!
{% endhint %}

## References

[Receiving and processing an SMS with Twilio in Python](https://stackoverflow.com/a/50082747/9770490)

[How to Receive an SMS in Python with Twilio](https://youtu.be/cZeCz\_QOoXw)
