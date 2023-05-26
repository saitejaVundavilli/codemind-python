def printBoundary(a, m, n):
    s = 0
    for i in range(m):
        for j in range(n):
            if (i == 0):
                s += a[i][j]
            elif (i == m-1):
                s += a[i][j]
            elif (j == 0):
                s += a[i][j]
            elif (j == n-1):
                s += a[i][j]
    return s
r,c=map(int,input().split())
mat=[list(map(int,input().split())) for i in range(r)]
print(printBoundary(mat,r,c))
 