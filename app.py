from flask import Flask,request,render_template
import requests
import json

app = Flask(__name__)

# default route 
@app.route('/')
def index():
    return render_template('hello.html')



if __name__ == "__main__":
    app.run(host="0.0.0.0",port=80)