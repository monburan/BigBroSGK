# -*- coding: utf-8 -*-
# __author__: monburan

from flask import Flask
from flask import jsonify, abort, make_response


app = Flask(__name__)

from pymongo import MongoClient
from bson.objectid import ObjectId

def connect_db():
    client = MongoClient('127.0.0.1',32768)
    db = client.test
    collection = db.daxiongdi
    return collection

@app.errorhandler(404)
def not_find(error):

    return make_response(jsonify({'error':'Not Find'}), 404)

@app.errorhandler(500)
def server_error(error):

    return make_response(jsonify({'error':'Server Error'}), 500)

@app.route('/api/datasize', methods=['GET'])
def datasize():
    datasize = connect_db().find().count()
    
    return make_response(jsonify({'data_size':datasize}))
@app.route('/api/select/all', methods=['GET'])
def select_all():
    """
    select all data from MongoDB
    """
    datas = list(connect_db().find({},projection={'_id':False}))
    # datas = [{'name':data['name'],'qq':data['qq']} for data in datas]
    return make_response(jsonify({'data':datas}))

@app.route('/api/select/qq/<int:qq>', methods=['GET'])
def select_qq(qq):
    """
    select all qq from MongoDB
    """
    print(type(qq))
    datas = list(connect_db().find({"qq",123456789}))
    print(datas)
    return make_response(jsonify({'qq':datas}))

@app.route('/')
def index():

    return 'index'

if __name__ == '__main__':

    app.run()
