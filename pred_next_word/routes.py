import json
from flask import request, jsonify, g
from pred_next_word import app
# import datetime
# from datetime import timedelta
from src.user import main

@app.route('/', methods=["GET", "POST"])
def catch():
    return app.send_static_file('index.html')

@app.route('/api/getWord', methods=["POST", "GET"])
def upload_file():
    content = request.get_json()
    # print(f"Content : {content}")
    order=content["order"]
    text=content["text"]
    result=main(order,text)
    # print(f"Result : {result}")
    # print(f"Order : {order}")
    # print(f"Text : {text}")
    res={}
    # print(result)
    res={'resp':result}
    li=[]
    li.append(res)
    return json.dumps(li)