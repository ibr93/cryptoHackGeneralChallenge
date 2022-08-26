from pwn import * # pip install pwntools
import json
from Crypto.Util.number import bytes_to_long
import base64
import codecs
from binascii import unhexlify

FLAG = "crypto{????????????????????}"
ENCODINGS = [
    "base64",
    "hex",
    "rot13",
    "bigint",
    "utf-8",
]

r = remote('socket.cryptohack.org', 13377, level = 'debug')

def list_to_string(s):
    output = ""
    return(output.join(s))

def json_recv():
    line = r.recvline()
    return json.loads(line.decode())

def json_send(hsh):
    request = json.dumps(hsh).encode()
    r.sendline(request)

def decode(type, challenge_words):
    if type == "base64":
        decoded = base64.b64decode(challenge_words).decode('utf8').replace("'", '"')
    elif type == "hex":
        decoded = (unhexlify(challenge_words)).decode('utf8').replace("'", '"')
    elif type == "rot13":
         decoded = codecs.decode(challenge_words, 'rot_13')
    elif type == "bigint":
        decoded = unhexlify(challenge_words.replace("0x", "")).decode('utf8').replace("'", '"')
    elif type == "utf-8":
        decoded = list_to_string([chr(b) for b in challenge_words])
    return {"decoded": decoded}

for i in range(0, 101):
    received = json_recv()
    if "flag" in received:
        print("\n[*] FLAG: {}".format(received["flag"]))
        break

    rersponse = decode(received["type"],received["encoded"])
    json_send(rersponse)



