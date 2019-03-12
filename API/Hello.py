from flask_restful import Resource
from flask import request

class Hello(Resource):
    def get(self):
        return {"message": "Hello, World!"}

    def post(self):
        json_data = request.get_json(force=True)
        print(json_data)
        aesPrivateKey = json_data["secretKey"]
        dataContent = json_data["data"]
        return {"message": "Hello, World!"}