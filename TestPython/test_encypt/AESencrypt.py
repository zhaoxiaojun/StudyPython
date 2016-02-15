#coding=utf8
import crypto
import sys
sys.modules['Crypto'] = crypto
from Crypto.Cipher import AES
import hashlib
import base64
from binascii import b2a_hex, a2b_hex


def get_sha1(data):
    '''
    sha1加密
    '''
    s = hashlib.sha1()
    s.update(data)
    return s.hexdigest()
    #return s.digest()

def aespks7b64_encrypt(data, key, iv):
    '''
    用aes CBC加密，再用base64  encode，补码方式：pks7
    '''
    BS = AES.block_size
    #PKCS7Padding方式补码
    pad_PKCS7 = lambda s: s + (BS - len(s) % BS) * '0'
    cipher = AES.new(key, AES.MODE_CBC, iv)
    encrypted = cipher.encrypt(pad_PKCS7(data))  #aes加密
    #print 'encrypted: %s' % b2a_hex(encrypted)
    result = base64.b64encode(encrypted)  #base64 encode
    return result

def aespks7b64_decode(encrypted, datalen, key, iv):
    '''
    把加密的数据，用base64  decode，再用aes解密
    '''
    cipher = AES.new(key, AES.MODE_CBC, iv)
    result = base64.b64decode(encrypted)
    decrypted = cipher.decrypt(result)
    return  decrypted[:datalen]

def aespks5b64_encrypt(data, key, iv):
    '''
    用aes CBC加密，再用base64  encode，补码方式：pks5
    '''
    BS = AES.block_size
    #PKCS5Padding方式补码
    pad_PKCS5 = lambda s: s + (BS - len(s) % BS) * chr(BS - len(s) % BS)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    encrypted = cipher.encrypt(pad_PKCS5(data))  #aes加密
    #print 'encrypted: %s' % b2a_hex(encrypted)
    result = base64.b64encode(encrypted)  #base64 encode
    return result

def aespks5b64_decode(data, key, iv):
    '''
    把加密的数据，用base64  decode，再用aes解密
    '''
    unpad = lambda s: s[0:-ord(s[-1])]
    cipher = AES.new(key, AES.MODE_CBC, iv)
    result = base64.b64decode(data)
    decrypted = cipher.decrypt(result)
    return  unpad(decrypted)


if __name__ == '__main__':
    #待加密串
    data = '{"UserTypeId":"1"}'
    datalen = len(data)

    #秘钥
    key = 'A0B5C2D4E7F90301' # the length can be (16, 24, 32)

    #初始向量
    iv = key

    print '加密----------'
    encrypted = aespks5b64_encrypt(data, key, iv)
    encrypted = get_sha1(encrypted)
    print 'encrypted: ',encrypted

    # print '解密----------'
    # decrypted = aespks5b64_decode(encrypted, key, iv)
    # print 'decrypted: ',decrypted

