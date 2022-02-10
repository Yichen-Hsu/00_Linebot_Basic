'''Flask基本架構'''
'''
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

from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello Flask'

if __name__ == "__main__":
    app.run()
    