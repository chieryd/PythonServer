from flask_restful import Resource
from flask import request
from CryptoFile.AESCoder import AESCoder
from CryptoFile.RSACoder import RSACoder
import json

class Hello(Resource):
    def get(self):
        return {"message": "Hello, World!"}

    def post(self):
        json_data = request.get_json(force=True)
        print(json_data)
        aesPrivateKey = json_data["secretKey"]
        dataContent = json_data["data"]

        rsa_coder = RSACoder()

        # 解密aes秘钥
        aes_encrypt_key = rsa_coder.decrypt(aesPrivateKey)

        # 解密数据
        aes_coder = AESCoder(aes_encrypt_key)
        decrypt_data = aes_coder.decrypt(dataContent)

        # string to json
        json_data_content = json.load(decrypt_data)
        print(json_data_content)

        return {"message": "Hello, World!"}