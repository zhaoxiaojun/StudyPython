#coding=utf8
from Crypto.Cipher import AES
import base64
import os
import binascii
import hashlib
import md5

def get_MD5(data):
    '''
    md5加密
    '''
    m = md5.new()
    m.update(data)
    #return m.digest()  #摘要
    return m.hexdigest()  #16进制的摘要

def get_md5(data):
    '''
    md5加密
    '''
    m = hashlib.md5()
    m.update(data)
    return m.hexdigest()

def get_sha1(data):
    '''
    sha1加密
    '''
    s = hashlib.sha1()
    s.update(data)
    return s.hexdigest()

def get_base64(data):
    '''
    base64加密
    '''
    b64 = base64.b64encode(data)
    return b64

def getde_base64(encrypted):
    '''
    base64解密
    '''
    data = base64.b64decode(encrypted)
    return data


def aes_encrypt(data, key, iv, pkcs):
    '''
    用aes CBC加密,加密后的字符串转化为16进制字符串
    '''
    BS = AES.block_size
    if pkcs == 0:
        #PKCS7Padding方式补码
        pad_PKCS7 = lambda s: s + (BS - len(s) % BS) * '0'
        data = pad_PKCS7(data)
    else:
        #PKCS5Padding方式补码
        pad_PKCS5 = lambda s: s + (BS - len(s) % BS) * chr(BS - len(s) % BS)
        data = pad_PKCS5(data)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    encrypted = cipher.encrypt(data)  #aes加密
    result = binascii.b2a_hex(encrypted)
    return result

def aes_decode(encrypted, datalen, key, iv, pkcs):
    '''
    把加密的数据解密
    '''
    cipher = AES.new(key, AES.MODE_CBC, iv)
    decrypted = cipher.decrypt(binascii.a2b_hex(encrypted))
    if pkcs == 0:
        decrypted =  decrypted[:datalen]
    else:
        unpad = lambda s: s[0:-ord(s[-1])]
        decrypted = unpad(decrypted)
    return decrypted

def aespks7b64_encrypt(data, key, iv):
    '''
    用aes CBC加密，再用base64  encode
    '''
    BS = AES.block_size
    #PKCS7Padding方式补码
    pad_PKCS7 = lambda s: s + (BS - len(s) % BS) * '0'
    cipher = AES.new(key, AES.MODE_CBC, iv)
    encrypted = cipher.encrypt(pad_PKCS7(data))  #aes加密
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
    用aes CBC加密，再用base64  encode
    '''
    BS = AES.block_size
    #PKCS5Padding方式补码
    pad_PKCS5 = lambda s: s + (BS - len(s) % BS) * chr(BS - len(s) % BS)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    encrypted = cipher.encrypt(pad_PKCS5(data))  #aes加密
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
    encrypted = aespks7b64_encrypt(data, key, iv)
    #encrypted = get_sha1(data)
    print 'encrypted: ',encrypted

    print '解密----------'
    decrypted = aespks7b64_decode(encrypted, datalen, key, iv)
    print 'decrypted: ',decrypted


