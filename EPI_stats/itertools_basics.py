# itertools basics

import itertools

for i in itertools.count(5, 5):
    if i == 35:
        break
    else:
        print(i, end = " ")
print()        
print(list(itertools.permutations('abc')))

mylist = [6, 7, 8, 9, 10]
print(list(itertools.islice(mylist, 2, 4))) # 2, 4, index     
