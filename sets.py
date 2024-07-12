# SETS
# sets are like tuples but are updateable , also like dictionary but have no key value pairs
# they are like mathematical sets 
# a set ignores same items 

set1={1,2,3,4}
set2={3,4,5,6}
set3={1}

intersection=set1 & set2  
print(intersection)

union=set1 | set2
print(union)

diff= set1 -set2
print(diff) 

print(set1>set3)  #subset check

list1=list(set2)  # creates list of set
print(list1)

set34={1,1,2,3,4,5,5}
 #NOTe: repeated pair of data gets ignored
print(set34)
print(len(set34))

#to find number of items in a list

list2=list(set34)
print(len(list2))
