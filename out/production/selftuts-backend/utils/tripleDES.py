from pyDes import *
import binascii

bytes = [0x61, 0x6c, 0x65, 0x70, 0x6f, 0x31, 0x32, 0x33]
key = "".join(map(chr, bytes)).encode('utf-8')
key1 = key + key + key
desc3key = binascii.hexlify(key1)
t1 = triple_des(binascii.unhexlify(desc3key),padmode=PAD_PKCS5)

def decrypt(encrypted_password):

    password = encrypted_password

    try:
        td2 = t1.decrypt(binascii.a2b_hex(password))
        return str(td2, 'utf-8')
    except  Exception as e:
        raise e

def encrypt(plainpassword):

    password = plainpassword

    try:
        td1 = binascii.b2a_hex(t1.encrypt(password))
        return str(td1, 'utf-8')
    except  Exception as e:
        raise e

