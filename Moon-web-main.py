from flask import Flask
#利用Flask对象建造app对象

app = Flask(__name__)
#路由声明器app.route('/'),

@app.route('/')
def hello_world():
    return 'Hello world!'

if __name__ == '__main__':
    app.run()
