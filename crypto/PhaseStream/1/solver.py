from Crypto.Util.number import *
enc = "2e313f2702184c5a0b1e321205550e03261b094d5c171f56011904"
mes = b"CHTB{"
#flagの先頭が分かるので先頭5bytesのkeyを特定する
key = []
for i in range(5):
	c = mes[i]^int(enc[i*2:(i+1)*2],16)
	key.append(c)

#求めたkeyで復号
cnt = 0
for i in range(0,len(enc),2):
	print(chr(key[cnt%5]^int(enc[i:i+2],16)),end="")
	cnt += 1

