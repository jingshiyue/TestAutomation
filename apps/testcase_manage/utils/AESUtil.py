import binascii

from Crypto.Cipher import AES  # pip install pycryptodome
from Crypto.Util import Padding


class AESUtil:
    """
    AES加密模式: ECB
    数据块: 128位
    填充方式: pkcs7padding
    密钥:系统注册时所分配的APPkey
    输出格式: HEX
    字符集: UTF-8
    """
    model = AES.MODE_ECB
    enc_fun = binascii.hexlify
    dec_fun = binascii.unhexlify
    # BASE64 enc_fun = base64.b64encode
    # BASE64 enc_fun = base64.b64decode
    encoding = 'utf8'

    def __init__(self, key):
        self.key = key.encode(self.encoding)
        self.cipher = AES.new(self.key, self.model)

    def encrypt(self, unencrypted_str):
        """
        加密函数
        str => byte => 填充 => 密文二进制 => hex输出 => 转换为str
        :param unencrypted_str: 明文
        :return: 密文
        """
        unencrypted_bytes = unencrypted_str.encode(self.encoding)
        padded_bytes = Padding.pad(unencrypted_bytes, AES.block_size)
        encrypted_bytes = self.cipher.encrypt(padded_bytes)
        ciphertext = self.enc_fun(encrypted_bytes).decode(self.encoding)
        return ciphertext

    def decrypt(self, encrypted_data):
        """
        解密函数
        str => hex转换为二进制 => 解密 => 去除尾部空格
        :param encrypted_data: 密文
        :return: 明文
        """
        plaintext = self.cipher.decrypt(self.dec_fun(encrypted_data)).decode(self.encoding).strip('\b')
        return plaintext


if __name__ == '__main__':
    data = '12345678'  # 待加密数据
    key = '85CCQWE456SXXSD6'  # 16,24,32位长的密钥
    util = AESUtil(key)
    enc = util.encrypt(data)
    dec = util.decrypt(enc)
    assert enc == '61bc76446f27e83368db5161d6030e44'
    assert dec == data
