import fileinput
import pylab,sys,os
import matplotlib.pyplot as plt
from matplotlib import cm
import numpy as np
disease="CSL"
import matplotlib.ticker as ticker
#CUT = int(sys.argv[2])

rows = []

import math as mt

A1=["South_African_CSL","Khoe-San","Niger-Congo_Bantu_South","Niger_Congo_West","African-American"]
B=["Afro-Asiatic_Cushitic","Afro-Asiatic_Omotic","Afro-Asiatic_Semitic"]
C=["European_North","European_center","European_South","European_USA"]
D=["Latin_American","African-Caribbean",]
E =["East_Asian","South_Asian"]
F =["USA_Indian","UK_Indian"]

A = A1+ B+C+D+E+F; AFR = A1;EUR = C;ASN = E;IND = F;AFRO = B + D
SNP = [];LOWS = {}

for i in range(len(A)):
	rows.append([])

for line in fileinput.input("CSL.gene3.frq"):
	data=line.split()
	if fileinput.lineno()>1:
		SNP.append(data[0].strip('"').strip('"'))
		LOWS[data[0]] = [float(data[1])]+data[1:]
	else:
		B = data[1:]
pos = range(2,len(LOWS)+2);pos = np.array(pos)+2.5;pos = list(pos)

L = LOWS.values()
L = sorted(L, key = lambda x: (x[0]))	

for des in L:
	T = des[1:]
	for j in range(len(A)):
		rows[j].append(float(T[j])) #;rows[].append(float(des[3]))


B = [d.strip('"').strip('"') for d in B]
symbols =["*",".","<","+","x","d","1","4","s"] 
colors= ['k','g','r','b','m','y','k','c','b','g','r','c','m','xy','k','w','b','g','r','c','m','y','k',"b"]


fig=plt.figure(2,dpi=150)
ax = fig.add_subplot(111) #plt.subplot(111)
fig.subplots_adjust(bottom=0.2)
fig.set_size_inches(17,11)
ax.margins(x=0)
ax.set_ylabel("Log2 Gene-specific in SNPs Frequencies")
s=9.9871

xs = np.array([5.79843965218024 for i in xrange(len(pos))])
i  = 0;PHE=[]
for phe in rows:
	idx = rows.index(phe)
	p = B[idx]
	phe = np.asarray(phe)+1.0
	pos = np.asarray(pos)
	if p in AFR:
		px = AFR.index(p); col = 'g'+symbols[px]
		if p in ["South_African_CSL"]:
			col = 'r'+symbols[px]
			ax.plot(pos,phe,col,ls=('dashed'),lw=3)
		elif p in ["FB"]:
			col = 'r'+symbols[px]
			ax.plot(pos,phe,col,ls=('dashed'),lw=3)
		else:
			ax.plot(pos,phe,col,linewidth=3)
	elif p in EUR:
		px = EUR.index(p); col = 'b'+symbols[px]
		ax.plot(pos,phe,col,linewidth=3)
	elif p in ASN:
		px = ASN.index(p); col = 'r'+symbols[px]
		ax.plot(pos,phe,col,linewidth=3)
	elif p in AFRO:
		px = AFRO.index(p); col = 'm'+symbols[px]
		ax.plot(pos,phe,col,linewidth=3)
	elif p in IND:
		px = IND.index(p); col = 'k'+symbols[px]
		ax.plot(pos,phe,col,linewidth=3)
	else:
		print(p)
	i = i +1

y=rows[-1]
plt.xticks(pos,SNP,rotation='vertical') #,rotation=45)

ax.set_yscale('log', basey=2)
plt.grid(True)
plt.tick_params(labelsize=12)
plt.margins(0.01)
box = ax.get_position()
ax.set_position([box.x0, box.y0 + box.height * 0.4,box.width, box.height * 0.7])


ax.legend(("South African ACL","KhoeSan","Niger-Congo Bantu South","Niger Congo West","African-American","African-Caribbean","Latin American","Afro-Asiatic Cushitic","Afro-Asiatic Omotic","Afro-Asiatic Semitic","East Asian","South Asian","European Center","European North","European South","European USA","UK Indian","USA Indian"),loc='upper center',bbox_to_anchor=(0.5, -0.19),fancybox=True, shadow=True, ncol=6,fontsize='large',labelspacing=0.1,columnspacing=0.2)
fig.savefig("CSL_GENE.FRQ.png")
