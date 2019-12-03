# calculating mode
simplelist = [4, 2, 1, 3, 4]
from collections import Counter
c = Counter(simplelist)
print(c.most_common())

print(c.most_common(1)) # first one

# another way to do it
mode = c.most_common(1)
print(mode)

print(mode[0])
print(mode[0][0]) # retrieve first element of first tuple

