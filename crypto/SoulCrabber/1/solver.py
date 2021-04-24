test = "19500187e1ba0b5bf3e27914c83f1ffd67123543ffc3ae4a4d22a9d54f"
#print(len(test))
test_flag = "A"*29
key = []
for i in range(0,len(test),2):
	key.append(int(test[i:i+2],16)^ord("A"))

enc = "1b591484db962f7782d1410afa4a388f7930067bcef6df546a57d9f873"
for i in range(len(key)):
	print(chr(key[i]^int(enc[i*2:(i+1)*2],16)),end="")
print()
