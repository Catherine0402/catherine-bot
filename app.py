import os
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

line_bot_api = LineBotApi('DxjD3LIA5vDUTMbRLhemnNFnYBXevqtImM4SH5OQ5CrCQjpMo0PxokDjyovrkGkW1GKbQdlc4AB3S+z1ByDWR9pXGcYsky6TM05dRWTFDNRnP0+WY9DDTdYFLkup57HsqEHJmdXQ1Pb8d9G9mgVtvgdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('660d9b02343eaed5c6465c5a6c121ab9')


@app.route("/callback", methods=['POST'])
def callback():
    # Get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # Get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # Handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    
    
    text=event.message.text


    if (text=="Hi"):
        reply_text = "Hello"
    elif(text=="妳好"):
        reply_text = "哈囉"
    elif(text=="機器人"):
        reply_text = "叫我嗎"
    elif(text=="aaaa"):
        reply_text = "bbbb"
    elif:
        reply_text = text
#如果非以上的選項，就會學妳說話
    message = TextSendMessage(reply_text)
    line_bot_api.reply_message(event.reply_token, message)
