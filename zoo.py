#-1
from collections import Counter                   
name = input() 
l = [*name] 
ct = Counter(l) 
z = ct['z'] 
o = ct['o'] 
if (z*2)==o:     
    print('Yes') 
else:     
    print('No')

