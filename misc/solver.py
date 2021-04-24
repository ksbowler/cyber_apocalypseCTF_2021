from pwn import *

host = "138.68.185.219"
port = 31305
r = remote(host, port)

# get numbers
r.sendlineafter("> ", b"1")
r.recvuntil("Here is a little help:\n\n")
numbers = r.recvline().decode()
numbers_list = numbers.split(" ")
print(numbers_list)
#print(
hel = []
num = []
for i in range(0,len(numbers_list)-1,3):
	hel.append(ord(numbers_list[i]))
	num.append(int(numbers_list[i+2]))
for i in range(len(hel)):
	print(hel[i],num[i])

# Take test!
r.sendlineafter("> ", b"2")

i=1
while(i<=500):
	print("Now :",i)
	r.recvuntil("Question " + str(i) + ":\n\n")
	question = r.recvline().decode()
	que = question.split()
	for j in range(0,len(que)):
		if que[j] == "?": print(que[j],end="")
		elif j%2 == 0: print(num[hel.index(ord(que[j]))]," ",end="")
		else: print(que[j]+" ",end="")
	print()
	ans = [0 for j in range(len(que)//2)]
	bef = "+"
	way = []
	cnt = 1
	#ansに対応する数字を格納していく。a - bの場合、[a,-b]と格納していき、最後にsum(ans)とすれば和が出る
	ans[0] = num[hel.index(ord(que[0]))]
	for ind in range(1,len(que),2):
		if que[ind] == "=":
			break
		if que[ind] == "*":
			#かけ算の場合、足し引き算より先に行わないといけない
			#先に積を導出し、掛けられる数が入ってたansのところを0に、掛ける数のとこを今求めた積を格納する
			# a + b * c * d の場合、[a,0,0,0] -> [a,b,0,0] -> [a,0,b*c,0] -> [a,0,0,b*c*d] -> sum(ans) となる
			temp = ans[cnt-1]*num[hel.index(ord(que[ind+1]))]
			ans[cnt-1] = 0
			ans[cnt] = temp
			cnt += 1
		else:
			#+ or -
			#足し引き算ならそのまま格納するだけでよい
			if que[ind] == "+":
				ans[cnt] = num[hel.index(ord(que[ind+1]))]
				cnt += 1
			elif que[ind] == "-":
				ans[cnt] = -num[hel.index(ord(que[ind+1]))]
				cnt += 1
			else:
				print("division")
	print(ans)
	ans = sum(ans)
	#print(que)
	print("Final answer :",ans)
	r.sendlineafter("Answer: ", str(ans).encode())
	i += 1
	for _ in range(3):
		test = r.recvline()
		print(test.decode())
while True:
	test = r.recvline()
	print(test.decode())
