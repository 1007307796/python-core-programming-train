#coding:gbk
from flask import Flask, request

app = Flask(__name__)


@app.route("/",)
def index():
    from flask import redirect
    return redirect("/static/login.html")


@app.route("/login",methods=['GET','POST'])
def login():
    args = request.form
    if args['account'] == 'admin' and args['password'] == '1234':
        return "��¼�ɹ���"
    else:
        return "��¼ʧ�ܣ�"


if __name__ == '__main__':
    app.run(debug=True)