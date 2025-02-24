from Crypto.Util.number import *
import base64

"""
Commutative: A ⊕ B = B ⊕ A
Associative: A ⊕ (B ⊕ C) = (A ⊕ B) ⊕ C
Identity: A ⊕ 0 = A
Self-Inverse: A ⊕ A = 0 

KEY1 = a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313
KEY2 ^ KEY1 = 37dcb292030faa90d07eec17e3b1c6d8daf94c35d4c9191a5e1e
KEY2 ^ KEY3 = c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1
FLAG ^ KEY1 ^ KEY3 ^ KEY2 = 04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf
"""


def bd(text):
    return base64.b64decode(text)
def bl(data):
    return bytes_to_long(data)


k1 = bytes.fromhex("a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313")
k2 = bytes.fromhex("37dcb292030faa90d07eec17e3b1c6d8daf94c35d4c9191a5e1e")
k3 = bytes.fromhex("c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1")
fg = bytes.fromhex("04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf")

key1 = bl(k1)
key2 = key1 ^ bl(k2)
key3 = key2 ^ bl(k3)
flag = key1 ^ key2 ^ key3 ^ bl(fg)

print(long_to_bytes(flag))

# s1 = bl(k2) ^ bl(k1)
# s2 = s1 ^ bl(k3)
# s3 = bl(k1) ^ s1 ^ s2 ^ bl(fg)
# print(long_to_bytes(s3))




