import base64
f = open("output.txt")
enc = ""
a = f.readlines()
#空白を削除
for i in a:
	temp = i.strip()
	temp = temp.split()
	for t in temp: enc += t
print(len(enc))
print(enc)
msg = enc.encode()
#flag formatが出るまでdecode
while True:
	msg = base64.b64decode(msg)
	if b"CHTB" in msg:
		print(msg)
		break
