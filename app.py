import json
from flask import *
# from flask import Flask
# from flasgger import Swagger
# from flasgger.utils import swag_from

# app = Flask(__name__)
# app.config["SWAGGER"] = {"title": "Swagger-UI","uiversion":2}

# swagger_config = {
#     "headers": [],
#     "specs": [
#         {
#             "endpoint": "apispec_1",
#             "route": "/apispec_1.json",
#             "rule_filter": lambda rule: True,
#             "model_filter": lambda tag: True,
#         }
#     ],
#     "static_url_path": "/flasgger_static",
#     "swagger_ui": True,
#     "specs_route": "/swagger/",
# }

# swagger = Swagger(app, config=swagger_config)

# def add_2_numbers(num1,num2):
#     output = {"sum_of_numbers": 0}
#     sum = num1 + num2
#     output["sum_of_numbers"] = sum
#     return sum


# @app.route("/")
# def index():
#     return "Add 2 numbers"


# @app.route("/add",methods=["POST"])
# @swag_from("swagger_config.yml")
# def add_numbers():
#     input_json = request.get_json()
#     try:
#         num1 = int(input_json["x1"])
#         num2 = int(input_json["x2"])
#         res = add_2_numbers(num1,num2)
#     except:
#         res = {"success":False,"message":"Error adding numbers"}

#     return json.dumps(res)

# if __name__ == "__main__":
#     app.run(debug=True)



# :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
from flask import Flask
from flasgger import Swagger

app = Flask(__name__)
swagger = Swagger(app)

@app.route('/helloWorld', methods=['GET'])
def hello():
    """
    A simple GET endpoint that returns a hello message.
    ---
    responses:
      200:
        description: A hello message
    """
    return 'Hello, World!'

@app.route('/greet', methods=['POST'])
def greet():
    """
    A simple POST endpoint that takes a name parameter and returns a greeting.
    ---
    parameters:
      - in: body
        name: name
        schema:
          type: object
          properties:
            name:
              type: string
        required: true
    responses:
      200:
        description: A greeting message
    """
    name = request.json['name']
    return f'Hello, {name}!'


@app.route('/', methods=['GET', 'POST'])
def home(): 
    try:  
        return "Homies"
    except Exception as e:
        print(e)

if __name__ == '__main__':
    app.run(debug=True)
