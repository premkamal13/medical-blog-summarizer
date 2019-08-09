# Matching specific patterns

import re
import collections

with open("test_new.txt") as f:
   global text
   text=f.readlines()

with open("test_new.txt","w") as f1:
   for lines in text:
      lines=re.sub(' ','\n',lines)
      f1.write(lines)
      
