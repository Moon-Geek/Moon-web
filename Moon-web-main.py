from flask import Flask
#利用Flask对象建造app对象

app = Flask(__name__)
#路由声明器app.route('/'),
# ip域网：http://192.168.112.1:5000(凤台移动域网)
@app.route('/')
def hello_world():
    return 'Hello world!'

if __name__ == '__main__':
    app.run()
