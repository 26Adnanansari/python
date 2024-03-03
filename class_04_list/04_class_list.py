
# ## List 
# * Dynamic Length
# * Hetrogenous Data Type (Multiple Data Type)
# * Index Feature 
#     * Positive : 0 to n-1
#     * Nagitive : -1 to length


#  ->       0       1              2          3          POSITIVE INDEXING  
names = ['Sabir', 'Rizwan','Sir Zia Khan','RatanLal']
#  <-      -4      -3              -2         -1         NAGITIVE INDEXING
# Let we try to access it by both method

# By Positive Indexing

print(names[0])    #  POSITIVE INDEXING answer should be Sabir
print(names[1])    #  POSITIVE INDEXING answer should be Rizwan
print(names[3])    #  POSITIVE INDEXING answer should be RatanLal

# By Nagitive Indexing

print(names[-3])    #  POSITIVE INDEXING answer should be Rizwan
print(names[-2])    #  POSITIVE INDEXING answer should be Sir Zia Khan
print(names[-4])    #  POSITIVE INDEXING answer should be Sabir


# Now if we want to use any method on particular value of list we can apply as our perivious class
print(f'The founder of PIAIC {names[-2].upper()}')
# we use here upper case function
