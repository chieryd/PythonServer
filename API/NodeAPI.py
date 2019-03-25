from flask_restful import Resource
from flask import request
from CryptoFile.HDCrypto import encrypt, decrypt
from Models.NodeModel import NodeModel, db
import json

class NodeAPI(Resource):
    def get(self):
        # 获取用户数据
        nodes = db.query
        return {"message": "Hello, World!"}

    def post(self):
        json_data = request.get_json(force=True)

        if not json_data:
            return_json = {'message': 'No input data provided'}
            return encrypt(return_json), 400

        # 解密数据
        decrypt_dict = decrypt(json_data)
        if not decrypt_dict:
            return_json = {'message': 'No input data provided'}
            return encrypt(return_json), 400

        trasform_json = {"transform": decrypt_dict["transform"]}
        trasform_json_string = json.dumps(trasform_json)
        # 数据库存储相关, 数据解析成功了
        node = NodeModel(
            title=decrypt_dict['title'],
            subtitle=decrypt_dict['subtitle'],
            image=decrypt_dict['image'],
            nodetype=decrypt_dict['type'],
            transform=trasform_json_string,
        )
        db.session.add(node)
        db.session.commit()

        # 加密数据
        return_json = {"error_code": 0, "error_msg": "", "data": "success"}
        encrypt_dict = encrypt(return_json)

        return encrypt_dict