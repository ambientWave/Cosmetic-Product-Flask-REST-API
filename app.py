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

'''POST requests can be done using:
1- CURL on Unix

CURL is awesome to do what you want! It's a simple, but effective, command line tool.

REST implementation test commands:

curl -i -X GET http://rest-api.io/items
curl -i -X GET http://rest-api.io/items/5069b47aa892630aae059584
curl -i -X DELETE http://rest-api.io/items/5069b47aa892630aae059584
curl -i -X POST -H 'Content-Type: application/json' -d '{"name": "New item", "year": "2009"}' http://rest-api.io/items
curl -i -X PUT -H 'Content-Type: application/json' -d '{"name": "Updated item", "year": "2010"}' http://rest-api.io/items/5069b47aa892630aae059584

2- javascript
async function postData(url = "", data = {}) {
  // Default options are marked with *
  const response = await fetch(url, {
    method: "POST", // *GET, POST, PUT, DELETE, etc.
    cache: "no-cache", // *default, no-cache, reload, force-cache, only-if-cached
		mode: "cors",
    headers: {
            "Content-Security-Policy": "script-src 'self'; connect-src 'self';",
      "Content-Type": "application/json",
      // 'Content-Type': 'application/x-www-form-urlencoded',
    },
    redirect: "follow", // manual, *follow, error
    referrerPolicy: "no-referrer", // no-referrer, *no-referrer-when-downgrade, origin, origin-when-cross-origin, same-origin, strict-origin, strict-origin-when-cross-origin, unsafe-url
    body: JSON.stringify(data), // body data type must match "Content-Type" header
  });
  return response.json(); // parses JSON response into native JavaScript objects
}

postData("http://127.0.0.1:5000/cosmetics/add_item", {
"brand": "Oz Naturals",
"product_line_name": "Serum",
"product_line_category": "skin/moisturizers"
}).then((data) => {
  console.log(data); // JSON data parsed by `data.json()` call
});
'''

@app.route('/cosmetics/<id>/', methods=['DELETE'])
def delete_cosmetic_by_id(id):
    cosmetic_id_get_query = Cosmetics.query.get(id)
    if cosmetic_id_get_query is None:
        return {"result": "error - item can't be found"}
    db.session.delete(cosmetic_id_get_query)
    db.session.commit()
    return {"result": "success - item is deleted"}