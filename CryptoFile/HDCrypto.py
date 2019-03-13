import json
from CryptoFile.RSACoder import RSACoder
from CryptoFile.AESCoder import AESCoder
from CryptoFile.RandomGenerate import generate_random_str

def encrypt(dict):
    return_json_string = json.dumps(dict)

    # 生成随机数
    random_string = generate_random_str()
    print(random_string)

    # 数据加密
    aes_encrypt = AESCoder(random_string)
    aes_encrypt_string = aes_encrypt.encrypt(return_json_string)

    # 加密对称加密的秘钥
    rsa_encrypt = RSACoder()
    rsa_encrypt_string = rsa_encrypt.encrypt(random_string)

    join_data = {"dafefsadfefeasd": rsa_encrypt_string, "jijaijiheawfndu": aes_encrypt_string}
    return join_data

def decrypt(dict):
    aesPrivateKey = dict["dafefsadfefeasd"]
    dataContent = dict["jijaijiheawfndu"]

    rsa_coder = RSACoder()

    # 解密aes秘钥
    aes_encrypt_key = rsa_coder.decrypt(aesPrivateKey)

    # 解密数据
    aes_coder = AESCoder(aes_encrypt_key)
    decrypt_data = aes_coder.decrypt(dataContent)

    # string to json
    json_data_content = json.loads(decrypt_data)
    return json_data_content