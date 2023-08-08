from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
# from flask_pymongo import PyMongo

app = Flask (__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://*:*@localhost/cosmetics' # database_user_name:database_user_password@database_domain_or_host_address/database_name_not_the_name_of_table
# app.config['MONGO_URI'] = 'mongodb://*:*@localhost/cosmetics' # database_user_name:database_user_password@database_domain_or_host_address/database_name

db = SQLAlchemy(app)
# db = PyMongo(app)

# app.app_context().push()

class Cosmetics(db.Model):
    __tablename__ = "cosmetics"
    id = db.Column(db.Integer, primary_key=True) # equivalent to posgresql arguments: id SERIAL PRIMARY KEY
    brand = db.Column(db.String(80), unique=True, nullable=False)
    product_line_name = db.Column(db.String(120))
    product_line_category = db.Column(db.String(120))

    def __repr__(self):
        return f"{self.brand} - {self.product_line_name} - {self.product_line_category}"


@app.route('/')
def index():
    return 'Hello!'

@app.route('/cosmetics/')
def get_cosmetics():
    print(request.args.get('A'), request.args.get('B'), request.args.get('C')) # request.args.get is used to fetch the values of url params if present e.g. cosmetics?A=my&B=name&C=is
    cosmetic_get_query = Cosmetics.query.all()
    output = []
    for item in cosmetic_get_query:
        cosmetic_data = {"Brand": item.brand, "Product Line Name": item.product_line_name,
                         "Product Line Category": item.product_line_category}
        output.append(cosmetic_data)
    return {"results":output}

@app.route('/cosmetics/<id>/')
def get_cosmetic_by_id(id):
    cosmetic_id_get_query = Cosmetics.query.get_or_404(id)
    return {"Brand": cosmetic_id_get_query.brand, "Product Line Name": cosmetic_id_get_query.product_line_name,
                         "Product Line Category": cosmetic_id_get_query.product_line_category}

@app.route('/cosmetics/add_item/', methods=['POST']) # make sure that Content-Type header is application/json otherwise a 400 error response would be returned
def add_cosmetic():
    cosmetic = Cosmetics(brand=request.json["brand"], product_line_name=request.json["product_line_name"], product_line_category=request.json["product_line_category"])
    db.session.add(cosmetic)
    db.session.commit()
    return {"result": "success - item is added", "added_item": {"Brand": cosmetic.brand, "Product Line Name": cosmetic.product_line_name,
                         "Product Line Category": cosmetic.product_line_category}}


@app.route('/cosmetics/<id>/', methods=['DELETE'])
def delete_cosmetic_by_id(id):
    cosmetic_id_get_query = Cosmetics.query.get(id)
    if cosmetic_id_get_query is None:
        return {"result": "error - item can't be found"}
    db.session.delete(cosmetic_id_get_query)
    db.session.commit()
    return {"result": "success - item is deleted"}
