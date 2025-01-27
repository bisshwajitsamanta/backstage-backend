from flask import Flask,request,jsonify
import base64
import requests

app = Flask(__name__)
GITHUB_TOKEN = ""
GITHUB_REPO = ""
GITHUB_PATH = ""


@app.route('/api/create-dashboard',methods=['POST'])
def create_dashboard():
    return "Hello, Everyone ! This is Work in Progress."

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)