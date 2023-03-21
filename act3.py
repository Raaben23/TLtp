def symetric_browse(L):
    L2=[]
    if len(L)%2==0:
        N = int(len(L)/2)
    else:N=int(len(L)/2+1)

    for i in range (N):
        L2.append(L[i])
        if i!=N-1:
           L2.append(L[len(L)-1-i])
    return L2
list=symetric_browse([2,4,6,5,8,11,3])
print(list)