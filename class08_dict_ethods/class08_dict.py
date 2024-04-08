import pprint
from turtle import clear
from typing import Dict, Union

Key = Union[str,int]
Value = Union [int,str,list,dict,tuple,set]

data : Dict [Key,Value] = {
                           "name":"M. Adnan Ansari",
                           "fname":"M.Shaifque Ansari",
                           "Profession":"TypeScript, Modren Python(pydentic), NextJs, Backend, App Programming ",
                           "Intersted In": "Web 3.0 , Advance App Programming, GenAi, BlockChain,"
                          }


dict_method : list[str] = [m for m in dir(data) if "__" not in m]
print(dict_method)

# Method 1 clear 
# First we print data and see it result
pprint.pprint(f"before apply method  : {data}")


# After apply clear method print data and see it result
# .get search for key Pakistan which is not available it will give error 
#                       Key            Custom Error
copydata = data.popitem()
pprint.pprint(data)
