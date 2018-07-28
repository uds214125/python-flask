from flask import Flask, render_template
# from flask_cors import CORS
from flask_pymongo import PyMongo
from modules.admin.controllers import admin
# from flask import g 

app = Flask(__name__)
# CORS(app)

# Configurations
# app.config = config
 
app.secret_key = 'dddd' 

app.config["MONGO_URI"] = "mongodb://localhost:27017/uds"
mongo = PyMongo(app)


# Sample HTTP error handling
@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404

from modules.main.controllers import main
# from tms.db import *

# Register blueprint(s)

app.register_blueprint(main, url_prefix='/')
app.register_blueprint(admin, url_prefix='/admin')

if __name__ == '__main__':
    app.run(debug=True)   