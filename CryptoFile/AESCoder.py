from Crypto.Cipher import AES
import base64, hashlib
class AESCoder():
    def __init__(self, key):
        SHA384 = hashlib.sha384()
        SHA384.update(key.encode('utf-8'))
        res = SHA384.digest()
        key = res[:32]

        self.key = key
        self.mode = AES.MODE_CBC
        self.iv = res[32:48]

    #加密函数，如果text不是16的倍数【加密文本text必须为16的倍数！】，那就补足为16的倍数
    def encrypt(self, text):
        cryptor = AES.new(self.key, self.mode, IV=self.iv)
        length = 16
        count = len(text)
        add=count % length
        if add:
            text = text + ('\0' * (length-add))
        self.ciphertext = cryptor.encrypt(text)
        #因为AES加密时候得到的字符串不一定是ascii字符集的，输出到终端或者保存时候可能存在问题
        #所以这里统一把加密后的字符串用base64转化
        return base64.b64encode(self.ciphertext)

    #解密后，去掉补足的'\0'用strip() 去掉
    def decrypt(self, text):
        decode = base64.b64decode(text)
        cryptor = AES.new(self.key, self.mode, IV=self.iv)
        plain_text = cryptor.decrypt(decode).decode()
        strip_text = plain_text.rstrip('\0')
        return strip_text