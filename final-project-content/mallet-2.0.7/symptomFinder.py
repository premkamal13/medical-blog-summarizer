# Finding symptoms in test data

import re
import collections


#with open("results_test_data.txt") as f:
with open("result.txt") as f:
   global text
   text=f.readlines()


with open("test_new.txt") as g:
   global symptoms
   symptoms=g.readlines()

#print symptoms

n = len(symptoms)
i = 0

while i<n:
   temp_val = symptoms[i]
   #print temp_val
   temp_len = len(temp_val)
   temp_val = temp_val[0:temp_len-1]
   #print temp_val
   symptoms[i] = temp_val
   i = i+1
   
#print symptoms

flag = -1
n = len(text)
i = 0
lis_symptoms = []

while i<n:
   if text[i]=="#SB \n":
      temp_str = symptoms[i]
      j = i+1
      while j<n and text[j]=="#SC \n":
         temp_str = temp_str + " " + symptoms[j]
         j = j+1
      lis_symptoms.append(temp_str)
      temp_str = "\n"
      lis_symptoms.append(temp_str)
      i = j
   else:
      i = i+1

with open("final_results.txt","w") as f1:
   for lines in lis_symptoms:
      f1.write(lines)
	  tmp = "\n"
	  f1.write(tmp)
