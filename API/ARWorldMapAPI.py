from flask_restful import Resource
from flask import request
from CryptoFile.HDCrypto import encrypt, decrypt

class ARWorldMapAPI(Resource):
    def get(self):
        # 获取用户数据, 这里需要更具arworldMap的id获取对应的nodes
        return {"message": "Hello, World!"}

    def post(self):
        json_data = request.get_json(force=True)

        if not json_data:
            return_json = {'message': 'No input data provided'}
            return encrypt(return_json), 400

        # 解密数据
        decrypt_dict = decrypt(json_data)
        if not decrypt_dict:
            print(decrypt_dict)

        # 加密数据
        return_json = {"error_code": 0, "error_msg": "", "data": "上传数据成功"}
        encrypt_dict = encrypt(return_json)

        return encrypt_dict