# Cleaning the code

import re
import collections

def replacement1(word):
   alphabet="abcdefghijklmnopqrstuvwxyz"
   splits = [(word[:i], word[i:]) for i in range(len(word) + 1)]
   #print splits
   posChange1 = [a + b[1:] for a, b in splits if b] # making deletions
   #print posChange1
   posChange2 = [a + b[1] + b[0] + b[2:] for a, b in splits if len(b)>1] # making transposes
   #print posChange2
   posChange3 = [a + c + b[1:] for a, b in splits for c in alphabet if b] # making replacements
   #print posChange3
   posChange4 = [a + c + b     for a, b in splits for c in alphabet] # making insertions
   #print posChange4
   return set(posChange1 + posChange2 + posChange3 + posChange4) 

def replacement2(word):
    return set(e2 for e1 in replacement1(word) for e2 in replacement1(e1) if e2 in myDict)

def known(words):
    return set(w for w in words if w in myDict)

def present(word):
    if word in myDict:
        return 1
    else :
        return 0

def correct(word):
    word=word.lower()
    if(present(word)):
        return word
    else:
        candidates = known([word]) or known(replacement1(word)) or replacement2(word) or [word]
        return max(candidates, key=myDict.get)

def words(text):
    return re.findall('[a-z]+', text.lower()) 

def formDictionary(features):
    tempDict = collections.defaultdict(lambda: 0)
    for f in features:
        tempDict[f] += 1
    return tempDict

myDict = formDictionary(words(file('Words.txt').read()))
def run():
    text=""
    with open("Step1Input1.txt") as f:
        text=f.read()
        #print text
    cleanCode=""
    temp=""
    for x in text:
        if x==' ' or x=='\n' or x==',' or x=='.':
            if( len(temp)>0):
                var=correct(temp)
                cleanCode+=var
                #print temp,var
            cleanCode+=x
            temp=""
        else:
            temp+=x
    if(len(temp)>0):
        cleanCode+=correct(temp)
    #print cleanCode
    with open("Step2Input.txt","w") as f1:
        f1.write(cleanCode)

run()
