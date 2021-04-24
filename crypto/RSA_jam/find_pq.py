import gmpy2
import random
import math
e = 65537
pl =[2,2,3,3,5,5,7,11,11,13,191,199,1489]
phi = 2954001204170914691805741860654963857940004074429377692284091070811401369951320958401069220899257193610366982095760499087321176610501426227559528834963391573119792751626794365037601107813476160364027477073371928090485550540475603624680000569693639581200408072914193394481017798545653296930496371873
d = 25279851828946689969935508637891642190361805428614897956944707979466882691402752252273969173866247553416847240691284721506378725185547104028957495800217551084649108905497165090047528206605038035320469604378521860671903204212263641356781239235920533291802966072966655090757438950541684952893977777198807710573
N = 123630001441211791699101815506417771377489862127836323215005247880779127747665261872791516882894729192469212567210262427681780651629370984012072785781572863755222453735206569087396934214192134882937330171191632058382828512367532999211413054935111652810223730835723518262117916443844727685713391668125094593189


for i in range(1<<len(pl)): #iのbitが立っている場合、phiに含まれるとするbit全探査
	temp = phi
	s = str(bin(i))[2:]
	s = "0"*(len(pl)-len(s)) + s
	for j in range(len(pl)):
		if s[j] == "1": temp *= pl[j]
	M = N-temp+1 #N-phi(N) = p+q-1
	rot, ch = gmpy2.iroot(M*M-4*N,2) #解の公式のルート内
	if ch:
		print("find!")
		p = (M-int(rot))//2
		q = (M+int(rot))//2
		phi = (p-1)*(q-1)
		lc = (p-1) * (q-1) // math.gcd((p-1), (q-1))
		print(d+lc)
		m = random.randrange(N)
		c = pow(m,e,N)
		m1 = pow(c,d+lc,N)
		print(m == m1) #d2 = d+lcでも復元できているか