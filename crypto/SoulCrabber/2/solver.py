f = open("test1.txt") #こちらは過去一週間のUNIX TIMEをseedとした結果
a = f.readlines()

pt = "A"*41
for ct in a:
	ct = ct.strip()
	assert len(ct) == 82
	key = []
	#得られた結果からkeyを特定
	for i in range(0,len(ct),2):
		key.append(int(ct[i:i+2],16)^ord("A"))
	enc = "418a5175c38caf8c1cafa92cde06539d512871605d06b2d01bbc1696f4ff487e9d46ba0b5aaf659807"
	flag = ""
	for i in range(0,len(enc),2):
		flag += chr(key[i//2]^int(enc[i:i+2],16))
	if "CHTB" in flag: print(flag) #問題作成時と同じUNIX TIMEだったらflagが復元される
