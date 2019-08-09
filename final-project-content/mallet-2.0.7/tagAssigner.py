# Matching specific patterns

import re
import collections

with open("assignedTagsInput.txt") as f:
   text=f.readlines()
   
with open("taggedSentences.txt","w") as f1:
   for lines in text:
      temp=lines[:-1]
      if temp != "":
         f1.write(temp+" #NA\n")
      
