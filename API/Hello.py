from flask_restful import Resource
from flask import request
from CryptoFile.HDCrypto import encrypt, decrypt

class Hello(Resource):
    def get(self):
        return {"message": "Hello, World!"}

    def post(self):
        json_data = request.get_json(force=True)

        # 解密数据
        decrypt_dict = decrypt(json_data)

        # 加密数据
        return_json = {"error_code": 0, "error_msg": "", "data": {"message": "Hello, World!"}}
        encrypt_dict = encrypt(return_json)

        return encrypt_dict