from flask import Flask
from flask_restful import Api
from item import Item, Itemlist


app = Flask(__name__)
api = Api(app)

api.add_resource(Item, '/item/<string:name>') #http://127.0.0.1:5000/student/siri
api.add_resource(Itemlist, '/items')

if __name__ == '__main__':
    app.run(port=5000, debug=True)