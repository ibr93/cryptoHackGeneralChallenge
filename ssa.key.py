from Crypto.PublicKey import RSA
import base64
file = open('bruce_rsa.pub', 'rb').read()

#ssh_public_key = file.split(' ')[1]

print(RSA.import_key(file).n)
#print(ssh_public_key)