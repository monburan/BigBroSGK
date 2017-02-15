# -*- coding: utf-8 -*-
from flask import Flask, jsonify, abort

app = Flask(__name__)

tasks = [
    {
        'num':1,
        'qq':123456789,
        'tel':13800000000,
        'email':'test@gmail.com'
    },
    {
        'num':2,
        'qq':111111,
        'tel':13800001234,
        'email':'test2@gmail.com'
    },
    {
        'num':3,
        'qq':124356789,
        'tel':13899990000,
        'email':'test3@gmail.com'
    }
]

from flask import make_response
@app.errorhandler(404)
def select_not_find(error):
    return make_response(jsonify({'error': 'Not Find'}), 404)

@app.route('/api/select_qq/<int:qq>',methods=['GET'])
def select_qq(qq):
    """
    select qq api
    """
    task = filter(lambda data: data['qq'] == qq, tasks)
    task = list(task)
    if len(task) == 0:
        abort(404)
    return jsonify({'tasks':task})
if __name__ == '__main__':
    app.run()
