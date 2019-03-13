from M2Crypto import RSA
import base64
from pathlib import Path

class RSACoder():
    def __init__(self):
        # 找到绝对路径
        script_location = Path(__file__).absolute().parent
        file_location = script_location / 'rsa_private_key.pem'
        self.rsa = RSA.load_key(file_location)

    #加密函数, 返回string,这里是base64  还是utf-8还不是很清楚
    def encrypt(self, text):
        encrypt_string = self.rsa.private_encrypt(text.encode(), 1)
        return base64.b64encode(encrypt_string).decode()

    #解密函数,返回utf-8
    def decrypt(self, text):
        decrypt_string = self.rsa.private_decrypt(base64.b64decode(text), 1)
        return decrypt_string.decode()