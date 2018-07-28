from flask import Flask
from flask import Blueprint, render_template, json, request, Response, session, flash, jsonify
from bson import json_util
from modules import mongo 

main = Blueprint('main', __name__, url_prefix='/api')

@main.route('/', methods=['GET', 'POST'])
def index():
    return render_template('main.html')

@main.route('/api/users/login', methods=['POST'])
def doLogin():
    if request.method == 'POST':
        # request.form['username']
        session['userId'] = '1234'
        # flash('Welcome')

        return Response(
            response=json.dumps({'email':'uds214125@gmail.com', 'content':'Login successfull'}),
            status=200,
            mimetype='application/json'
        )

@main.route('/api/users/logout', methods=['POST'])
def doLogout():
    if 'userId' in session:
        user = session['userId']
        session.clear()

        return jsonify(
            data='logout successfull : ' + user,
            status=202
        )
    else:
        return " no user in session"

@main.route('/api/books/find/', methods=['GET'])
def getAllBooks():
    docs_list  = list(mongo.db.Books.find())
    return json.dumps(docs_list, default=json_util.default)

@main.route('/api/books/find/<id>', methods=['GET'])
def getBookById(id):
    docs_list  = list(mongo.db.Books.find({'_id':id}))
    return json.dumps(docs_list, default=json_util.default)

@main.route('/api/books/create', methods=['POST'])
def saveBook():
    docs_list  = mongo.db.Books.save({'name':'C','year':1972})
    return json.dumps(docs_list, default=json_util.default)

# save many books
@main.route('/api/books/create-many', methods=['POST'])
def saveBook():
    docs_list  = mongo.db.Books.insertMany([{'name':'C','year':1972},{'name':'C++','year':1972}])
    return json.dumps(docs_list, default=json_util.default)
   
@main.route('/api/books/update/<id>', methods=['PUT'])
def putBookById(id):
    docs_list  = mongo.db.Books.update({'_id':id},{'set':{'name':'Let Us C'}})
    return json.dumps(docs_list, default=json_util.default)
  
@main.route('/api/books/delete/<id>', methods=['DELETE'])
def deleteBookById(id):
    docs_list  = mongo.db.Books.remove({'_id':id})
    return json.dumps(docs_list, default=json_util.default)
  
