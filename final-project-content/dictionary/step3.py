# Extracting symptoms from the given input file

import re
file = open('Step3Input.txt')
data1=file.read()
arr1=data1.split('.')
#print arr
lls1=list()
for line in arr1:
	ls = list()
	ls.extend(re.findall(r"[\w']+", line))
	lls1.append((list(ls[:])))
lls1.remove(lls1[-1])
#print lls
file.close()
file = open('SymptomsRootWords.txt')
data2=file.read()
arr2=data2.split('\n')
#print arr2
lls2=list()
for line in arr2:
	ls = list()
	ls.extend(re.findall(r"[\w']+", line))
	lls2.append((list(ls[:])))
lls2.remove(lls2[-1])
#print lls2
file.close()
line_num = list()
for lis2 in lls2:
    for lis1 in lls1:
        ctr=0
        for x in lis2:
            for y in lis1:
                if x==y:
                    #print x,y
                    ctr=ctr+1
                    break
        if ctr==len(lis2):
            ind = lls2.index(lis2)
            print ind
            line_num.append(ind)
file = open('symptoms.txt')
data3=file.read()
arr3=data3.split('\n')
file.close()
#print arr3
dic = {}
for ind in line_num:
        #print arr3[ind]
        dic[ind] = arr3[ind]
#print dic
st=''
with open("resultSymptoms.txt","w") as f1:
        for key in dic:
                st=st+dic[key]
                st = st + "\n"
                f1.write(st)
                st=''


        
