from flask import Flask
from flask import render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('hi.html')


@app.route('/aaa',methods=['GET'])
def aaa():
    data = request.args['account']
    pwd = request.args['password']
    return data+'<br>'+pwd

if __name__ == '__main__':
    app.debug = True
    app.run() 