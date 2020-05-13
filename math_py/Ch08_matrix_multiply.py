# matrix multiplication

def multimatrix(a,b):
    # return the product of matrix a and matrix b
    m = len(a)
    n = len(b[0])
    newmatrix = []
    for i in range(m):
        row = []
        # for every column in b
        for j in range(n):
            sum1 = 0
            # for every element in the column
            for k in range(len(b)):
                sum1 += a[i][k]*b[k][j]
            row.append(sum1)
        newmatrix.append(row)
    return newmatrix

a = [[1,2,-3,-1]]
b = [[4,-1],
     [-2,3],
     [6,-3],
     [1,0]]

print(multimatrix(a,b))
