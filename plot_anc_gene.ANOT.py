import fileinput
import pylab,sys,os
import matplotlib.pyplot as plt
from matplotlib import cm
import numpy as np

import matplotlib.ticker as ticker

rows = []

import math as mt

A1 =['Khoe-San','Niger-Congo_Bantu_South','Niger_Congo_West']
B =['African-American','African-Caribbean','Latin_American']
C = ['Afro-Asiatic_Cushitic','Afro-Asiatic_Omotic','Afro-Asiatic_Semitic']
D = ['European_center','European_North','European_South','European_USA']
E = ['East_Asian','South_Asian','UK_Indian','USA_Indian']

PHENO=['Khoe-San','Niger-Congo_Bantu_South','Niger_Congo_West','African-American','African-Caribbean','Latin_American','Afro-Asiatic_Cushitic','Afro-Asiatic_Omotic','Afro-Asiatic_Semitic','East_Asian','South_Asian','European_center','European_North','European_South','European_USA','UK_Indian','USA_Indian']

A = A1 + B+C+D+E

AFR = ['Khoe-San','Niger-Congo_Bantu_South','Niger_Congo_West', 'African-American']
EUR = ['European_center','European_North','European_South','European_USA']
ASN = ['East_Asian','South_Asian'] 
IND = ["UK_Indian","USA_Indian"]
AFRO = ['African-Caribbean','Latin_American',['Afro-Asiatic_Cushitic','Afro-Asiatic_Omotic','Afro-Asiatic_Semitic']

SNP = []
LOWS = {}

for i in range(len(PHENO)):
	rows.append([])


for line in fileinput.input("CSL_PATH.sorted.txt"):
	data=line.split()
	if fileinput.lineno()>1:
		SNP.append(data[0].strip('"').strip('"'))

		if disease in ["HIV","TB","ACG"]:
			if np.max([ float(k) for k in data[1:]]) < 5.5:
				pass
			else:
				LOWS[data[0]] = [float(data[1])]+data[1:]
		else:
			LOWS[data[0]] = [float(data[1])]+data[1:]
	else:
		B = data[1:]
pos = range(2,len(LOWS)+2)
pos = np.array(pos)+2.5
pos = list(pos)

L = LOWS.values()
L = sorted(L, key = lambda x: (x[0]))	

for des in L:
	T = des[1:]
	for j in range(len(A)):
		rows[j].append(float(T[j])) #;rows[].append(float(des[3]))


B = [d.strip('"').strip('"') for d in B]
B = [ d[len(disease)+1:] for d in B]
symbols =["*",".","<","+","x","d","1","4","s"] 

#['p','H','D','o','^','v','<','>','s','+','x','D','d','1','2','3','4','h','H','p','o','^','v','<','>','s','1']#'-','--','-.',':','.',',',
#lps = [k+'-' for k in [',','.','o','^','v','<','>','s','+','x','D','d','1','2','3','4','h','H','p']]

colors= ['k','g','r','b','m','y','k','c','b','g','r','c','m','xy','k','w','b','g','r','c','m','y','k',"b"]

fig=plt.figure(2,dpi=150)
ax = fig.add_subplot(111) #plt.subplot(111)
fig.subplots_adjust(bottom=0.2)
fig.set_size_inches(17,11)
ax.margins(x=0)
ax.set_ylabel("% Pathogenic SNPs within Gene")
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
		ax.plot(pos,phe,col,linewidth=2)
	elif p in EUR:
		px = EUR.index(p); col = 'b'+symbols[px]
		ax.plot(pos,phe,col,linewidth=2)
	elif p in ASN:
		px = ASN.index(p); col = 'r'+symbols[px]
		ax.plot(pos,phe,col,linewidth=2)
	elif p in AFRO:
		px = AFRO.index(p); col = 'm'+symbols[px]
		ax.plot(pos,phe,col,linewidth=2)
	elif p in IND:
		px = IND.index(p); col = 'k'+symbols[px]
		ax.plot(pos,phe,col,linewidth=2)
	else:
		print(p)
	i = i +1

y=rows[-1]
plt.xticks(pos,SNP,rotation='vertical') #,rotation=45)

plt.grid(True)
plt.tick_params(labelsize=10)
plt.margins(0.01)

box = ax.get_position()
ax.set_position([box.x0, box.y0 + box.height * 0.4,box.width, box.height * 0.7])
ax.legend(('Khoe San','African American','Niger Congo Bantu South','Niger Congo Bantu','Niger Congo Volta Niger','Niger Congo West','European North','European South','European USA','European center','South Asian','East Asian','UK Indian','USA Indian','African Caribbean','Afro Asiatic','Afro Asiatic Cushitic','Afro Asiatic Omotic','Afro Asiatic Semitic','Latin American'),loc='upper center',bbox_to_anchor=(0.5, -0.19),fancybox=True, shadow=True, ncol=6,fontsize='large',labelspacing=0.1,columnspacing=0.2)
fig.savefig(disease+"_PATH.png")
