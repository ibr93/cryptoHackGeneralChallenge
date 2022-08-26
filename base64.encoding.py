import base64

base64_message = '72bca9b68fc16ac7beeb8f849dca1d8a783e8acf9679bf9269f7bf'
hex_message = bytearray.fromhex(base64_message)

print(base64.b64encode(hex_message).decode('utf-8'))

