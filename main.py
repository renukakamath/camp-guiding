from flask import Flask
from admin import admin
from public import public
from expert import expert
from photo import photo

from api import api
app=Flask(__name__)
app.secret_key="asdfg"
app.register_blueprint(admin,url_prefix='/admin')
app.register_blueprint(expert,url_prefix='/expert')
app.register_blueprint(photo,url_prefix='/photo')

app.register_blueprint(api,url_prefix='/api')
app.register_blueprint(public)
app.run(debug=True,port=5435,host="0.0.0.0")