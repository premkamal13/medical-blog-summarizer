# Converting symptoms scraper to the corresponding root word ( Precalculation )

import re
file = open('symptoms.txt')
data=file.read()

arr=data.split('\n');
#print arr
lls=list()
for line in arr:
	ls = list()
	ls.extend(re.findall(r"[\w']+", line))
	lls.append((list(ls[:])))

from nltk.stem.wordnet import WordNetLemmatizer
lmtzr = WordNetLemmatizer()
nlls=list()
for il in lls:
    nls = list()
    for tmp in il:
        word = tmp.lower()
        temp_n=lmtzr.lemmatize(word)
        temp_v=lmtzr.lemmatize(word,'v')
        if(temp_n!=word) and (temp_v!=word):
            nls.append(str(temp_v))
        elif(temp_n==word):
            nls.append(str(temp_v))
        else:
            nls.append(str(temp_n))
    nlls.append((list(nls[:])))
    #print nls
file.close()
#print nlls

st = ''
with open("symptomsRootWords.txt","w") as f1:
        for lis in nlls:
                for x in lis:
                        st=st+x
                        st=st+' '
                st = st + "\n"
                f1.write(st)
                st=''
