from flask import Flask
from flask import request, redirect
from flask import render_template

app = Flask(__name__)

@app.route('/mypage')
def mypage():
