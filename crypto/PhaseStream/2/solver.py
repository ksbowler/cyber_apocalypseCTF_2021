f = open("output.txt")
a = f.readlines()


for key in range(256):
	print(key) #keyのbrute force
	for t in a:
		#10000行の中からflag formatに適したものがあるかチェック
		temp = t.strip()
		enc = ""
		for j in range(0,len(temp),2):
			enc += chr(key^int(temp[j:j+2],16))

		if "CHTB{" in enc:
			print(enc)
