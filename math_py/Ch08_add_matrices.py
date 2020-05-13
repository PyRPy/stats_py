# add matrix

A = [[2,3], [5,8]]
B = [[1,-4],[8,-6]]

def addMatrices(a,b):
    '''add two 2 x 2 matrices together'''
    C = [[a[0][0] + b[0][0], a[0][1] + b[0][1]],
         [a[1][0]+b[1][0], a[1][1] + b[1][1]]]
    return C
C = addMatrices(A,B)
print(C)
