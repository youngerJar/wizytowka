from flask import Flask
from flask import request, redirect
from flask import render_template

app = Flask(__name__)

@app.route("/mypage/me", methods=['GET'])
def me():
    return render_template("strona1.html")

@app.route("/mypage/contact", methods=['GET', "POST"])
def kontakt():
    if request.method == 'GET':
       print("We received GET")
       return render_template("strona2.html")
    elif request.method == 'POST':
       print("We received POST")
       print(request.form)
       return(request.form)