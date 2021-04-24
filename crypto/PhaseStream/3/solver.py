from Crypto.Util.number import *

test_enc = "464851522838603926f4422a4ca6d81b02f351b454e6f968a324fcc77da30cf979eec57c8675de3bb92f6c21730607066226780a8d4539fcf67f9f5589d150a6c7867140b5a63de2971dc209f480c270882194f288167ed910b64cf627ea6392456fa1b648afd0b239b59652baedc595d4f87634cf7ec4262f8c9581d7f56dc6f836cfe696518ce434ef4616431d4d1b361c"
flag_enc = "4b6f25623a2d3b3833a8405557e7e83257d360a054c2ea"

test = b"No right of private conversation was enumerated in the Constitution. I don't suppose it occurred to anyone at the time that it could be prevented."
#test=平文と、test_enc=暗号文の組み合わせが分かるのでenc(key) xor test = test_encからenc(key)を求める
enc_key = long_to_bytes(bytes_to_long(test)^int(test_enc,16))
#flag長が46//2 = 23ということが分かる。enc(key)の上位23bytesとxorさせればOK
print(long_to_bytes(bytes_to_long(enc_key[:23])^int(flag_enc,16)))

