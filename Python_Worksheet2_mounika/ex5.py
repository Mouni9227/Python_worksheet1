#5 program to subtract two matrices, m1 and m2, using a list of lists.

m1=[[2,3,4],[3,5,8],[4,6,7]]
m2=[[5,7,3],[5,6,9],[3,6,9]]

for i,j in list(zip(m1,m2)):
    mat_sub=[]
    for x,y in list(zip(i,j)):
        mat_sub.append(x-y)
    print(mat_sub)