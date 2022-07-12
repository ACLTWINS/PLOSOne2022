import fileinput
import sys,os
import matplotlib.pyplot as plt
from matplotlib import cm

file1=sys.argv[1]
rows = {}
A =['Khoe-San','Niger-Congo_Bantu_South','Niger_Congo_West','South_African_ACL']
B =['African-American','African-Caribbean','Latin_American']
C = ['Afro-Asiatic_Cushitic','Afro-Asiatic_Omotic','Afro-Asiatic_Semitic']
D = ['European_center','European_North','European_South','European_USA']
E = ['East_Asian','South_Asian','UK_Indian','USA_Indian']

PHENO=['Khoe-San','Niger-Congo_Bantu_South','Niger_Congo_West','South_African_ACL','African-American','African-Caribbean','Latin_American','Afro-Asiatic_Cushitic','Afro-Asiatic_Omotic','Afro-Asiatic_Semitic','East_Asian','South_Asian','European_center','European_North','European_South','European_USA','UK_Indian','USA_Indian']


Z = A +B + C+D+E

for line in fileinput.input(file1):
	data=line.split()
	if fileinput.lineno()>1:
		if data[0] in Z:
			rows[data[0]] = [float(j) for j in data[1:]]
	else:
		anc_av=[]
		header=data[1:]

print("\nNumber of Phenotype:",len(rows.keys()),len(A))

pos=[0.005, 0.1,0.25,0.50,0.75,1.0]

symbols =["*",".","<","+","x","d","1","4","s"]
colors = ["k","r","b","m","g","c"]
fig=plt.figure(2,dpi=150)

ax = fig.add_subplot(111) #plt.subplot(111)
ax.set_xlabel("Minor Allele Frequency Bin")
ax.set_ylabel("log2 Proportion of MAF")
i  = 0;PHE=[]
a=0;b=0;c=0;d=0;e=0
for p in PHENO:
	PHE.append(p)
	phe = rows[p]
	print"\n",p
	if p in A:
		px = A.index(p); col = 'k'+symbols[px]
		ax.plot(pos,phe,colors[px],ls=('dashed'),lw=2,marker='*',ms=8)
	elif p in B:
		px = B.index(p); col = 'b'+symbols[px]
		ax.plot(pos,phe,colors[px],marker='^',ms=6)
	elif p in C:
		px = C.index(p); col = 'r'+symbols[px]
		ax.plot(pos,phe,colors[px],marker='+',ms=6)
	elif p in D:
		px = D.index(p); col = 'g'+symbols[px]
		ax.plot(pos,phe,colors[px],marker='o',ms=8)
	elif p in E:
		px = E.index(p); col = 'c'+symbols[px]
		ax.plot(pos,phe,col,ls=('dashed'),lw=2)

plt.xticks([0.005, 0.1,0.25,0.50,0.75,1.0],['0-0.05', '>0.05-0.1', '>0.1-0.2', '>0.2-0.3', '>0.3-0.4', '>0.4-0.5'])
plt.yscale('log',basey=2)
plt.grid(True)
plt.tick_params(labelsize=8)


box = ax.get_position()
ax.set_position([box.x0, box.y0 + box.height * 0.4,box.width, box.height * 0.7])

ax.legend(('KhoeSan','Niger-Congo Bantu South','Niger-Congo West','South African ACL','African-American','African-Caribbean','Latin American','Afro-Asiatic Cushitic','Afro-Asiatic Omotic','Afro-Asiatic Semitic','East Asian','South Asian','European Center','European North','European South','European USA','UK Indian','USA Indian'),loc='upper center', bbox_to_anchor=(0.5, -0.09),fancybox=True, shadow=True, ncol=4,fontsize='x-small',labelspacing=0.1,columnspacing=0.2)

fig.savefig("ACL.log2..MAF.bins.png")
