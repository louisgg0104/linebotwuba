from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)

app = Flask(__name__)

line_bot_api = LineBotApi(
    'QQfRtT616WDzpgdI4nqi35t2yNOm1Wl7o38JgTkkUhX4LshwXxVCMyTE6i4rg7TuP7hV3h5R4wQmn1yvnVs+z2VGnHPqOODe4q42U5vzHFxaK9NC7kFE0sePKgaEFVHHd0T3xNEpZCab1AJ8FD0yTQdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('0f0acb797b22a4bc0cdf6f76d927dc2a')


@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=event.message.text))


if __name__ == "__main__":
    app.run()
