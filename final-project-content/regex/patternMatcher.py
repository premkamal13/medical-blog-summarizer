# Matching specific patterns

import re
import collections

text=""
with open("PatternData.txt") as f:
   text=f.readlines()
arr=[]

def matchAndSave(data):
   global ans
   for lines in text:
      #print lines
      #print data
      lines=re.sub('\n','',lines)
      matched = re.findall(lines,data)
      for everyMatch in matched:
         if ans:
            ans+="\n"
         ans+=everyMatch

def run():
   global ans
   ans=""
   with open("input5.txt") as f:
      data=f.read().lower()
   matchAndSave(data)
   print ans
   with open("MatchedOutput5.txt","w") as f1:
      f1.write(ans)

run()
