from flask import Flask
from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with
from flask_sqlalchemy import SQLAlchemy
import requests
import json

app = Flask(__name__)
api = Api(app)

bill_put_args = reqparse.RequestParser()
bill_put_args.add_argument("model", type=str, help="Model of the bom, string")
bill_put_args.add_argument("pk", type=int, help="Item number, integer")
bill_put_args.add_argument("uuid", type=str, help="Unique ID in form of string")
bill_put_args.add_argument("created_at", type=str, help="String representation of date created")
bill_put_args.add_argument("updated_at", type=str, help="String representation of date last updated")
bill_put_args.add_argument("is_active", type=str, help="Boolean in string format, bom is still active")
bill_put_args.add_argument("bom", type=int, help="Bom ID number, integer")
bill_put_args.add_argument("quantity", type=int, help="Quantity of boms of similar kind, integer")
bill_put_args.add_argument("specific_part", type=int, help="ID number representing specific part")
bill_put_args.add_argument("item_unit_cost", type=str, help="Cost per unit, in string format")

class BOM(Resource):
	def get(self, bom_id):
		
		# Open mock bom json file
		json_file = open('mock_bom_data.json','r')
		json_data = json_file.read()
		json_object = json.loads(json_data)
		bill_materials = str(json_object["data"])

		# Use library requests to get (or download) the json file
		#bill_materials = requests.get('https://www.mobiusmaterials.com/api/v1/bom/<int:bom_id>/')
		
		return bill_materials

	def put(self, bom_id):
		bill_materials = bill_put_args.parse_args()
		return bill_materials

api.add_resource(BOM, "/bom/<int:bom_id>")

#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
#db = SQLAlchemy(app)


if __name__ == "__main__":
	app.run(debug=True)