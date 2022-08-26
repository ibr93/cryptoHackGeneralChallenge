from binascii import unhexlify
from codecs import utf_8_decode
from pwn import *
from Crypto.Util.number import long_to_bytes, bytes_to_long
cypher_flag = '73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d'

cypher_flag_bin = unhexlify(cypher_flag)

for i in range(255):
    
    message = xor(cypher_flag_bin , i)
    decrypted_message= message.decode('utf-8')
    if(decrypted_message.startswith('crypto')):
        print(decrypted_message)
   # print(bytes_to_long(message))