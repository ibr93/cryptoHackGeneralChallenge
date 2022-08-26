from codecs import ascii_decode, utf_8_encode
from sre_parse import FLAGS
from pwn import *
from Crypto.Util.number import long_to_bytes
'''
KEY1 = a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313
KEY2 ^ KEY1 = 37dcb292030faa90d07eec17e3b1c6d8daf94c35d4c9191a5e1e
KEY2 ^ KEY3 = c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1
FLAG ^ KEY1 ^ KEY3 ^ KEY2 = 04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf 

KEY2 =  KEY2 ^ KEY1 ^ KEY1
'''
key1_xor_key2 = int('37dcb292030faa90d07eec17e3b1c6d8daf94c35d4c9191a5e1e', base=16)
key2_xor_key3 = int('c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1', base=16)
flag_key1_xor_key2_xor_key3 = int('04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf', base=16)
KEY1 = int('a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313', base=16)
KEY2 = key1_xor_key2 ^ KEY1
KEY3 = key2_xor_key3 ^ KEY2

FLAG = flag_key1_xor_key2_xor_key3 ^ KEY1 ^ key2_xor_key3

print(long_to_bytes(FLAG).decode('utf-8'))