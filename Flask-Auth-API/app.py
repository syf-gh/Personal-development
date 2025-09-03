import json
from flask import Flask,jsonify,request
from flask_cors import CORS
app = Flask(__name__)   #创建falsk对象
#解决跨越问题
CORS(app)
#处理token
def Get_token_data():
    info_data = {}
    with open('db.txt','r',encoding='utf-8')as f:
        for line in f:
            line = line.strip()
            token , name = line.split(',')
            info_data[token] = name
    return info_data
@app.route("/index",methods=['POST'])#定义路由
def index():
    '''
    鉴权要求携带数据token{token=？} get
    携带json数据order_sting{}
    :return: json
    '''
    token = request.args.get('token')
    if not token:
        return jsonify({'status': False,'error':'token缺失'})
    user_data = Get_token_data()
    if token not in user_data:
        return jsonify({'status': False, 'error': 'token错误'})
    order_sting = request.json.get('order_sting')
    if not order_sting:
        return jsonify({'status': False, 'error': 'order_sting缺失'})
    sign = {
        'result':'pythonAPI鉴权成功'
    }
    return jsonify({'status': True, 'data': sign})
if __name__ =='__main__':
    app.run(host="127.0.0.1",port = 5000)
