from typing import Dict, Union
import pprint

key = Union[int,str]
value = Union[str,int,list,dict,tuple,set]

data1 : Dict [key,value] = {
                          "name" : "Lubna",
                          "fname": "Adnan Ansari",
                          "class": "perp one",
                          "age": "5 years",
                          } 
    
#  key and value comprehensive style   
pprint.pprint({k:v for k,v in data1.items()})

# Shuffling  key with value comprehensive style
pprint.pprint({v:k for k,v in data1.items()})

# To understand what is shuffling

a = 5
b = 4
# and we want to changing values a = 4 and b = 5
a,b = b,a  # Shuffle process

print(f"a = {a} , b = {b}")