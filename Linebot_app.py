'''
Step 1. 了解 Flask 基本架構

宣告 Flask 物件
    from flask import Flask  <--- 導入 Flask 類別
    app = Flask(__name__)    <--- 建立 Flash 物件, 物件名稱通常取名 app

建立路由(route)
    路由(route)是flask的主體, 主要是處理客戶端連線的請求和執行回應, 建立的語法如下:
    
    @app.route("網頁路徑")  @是裝飾器的概念
    def 函數名稱():
        函數主體內容
        return

啟動 Flask 伺服器
    使用 run() 方法啟動, 一般設計如下:

    if __name__ = '__main__'
        app.run()
'''
# from flask import Flask

# app = Flask(__name__)

# @app.route('/')
# def hello():
#     return 'Hello Flask'

# if __name__ == "__main__":
#     app.run()


'''
Step 2 建立Line帳號的伺服程式

需安裝 line-bot-sdk 才可以讀取 Line 的輸入並同時回應此輸入。

'''

from flask import Flask, request, abort
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage

app = Flask(__name__)

handler = WebhookHandler('8b2c07fb8258c98f91b2ee7296feb286')
line_bot_api = LineBotApi('hqZx62GWw3rpLToss940RJ0RV8dcferdAInkAMX3zt5q3WRaNVrIfMtLzv1ulj8NYX/j5Hs71ZH7lgVwERCQyUuRLIyqUfWdYkQCCzHMjQ+17hiKxml4koR/4PjgfOy9h9owIlj6EVWP64xFPIjVHQdB04t89/1O/w1cDnyilFU=')

# 收Line的訊息
@app.route('/callback', methods=['POST'])
def callback():
    signature = request.headers['X-Line-Signature']
    body = request.get_data(as_text=True)
    try:
        print(body, signature)
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    return 'ok'

# Echo 回應, 相當於學你說話
@handler.add(MessageEvent, message=TextMessage)
def echo_message(event):
    line_bot_api.reply_message(event.reply_token, TextSendMessage(text=event.message.text))

if __name__ == "__main__":
    app.run()
    