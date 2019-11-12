def merge(A,p,q,r):
    n1=q-p+1
    n2=r-q
    L=[0]*(n1+1)
    R=[0]*(n2+1)
    for i in range(n1):
        L[i]=A[p+i]
    for j in range(n2):
        R[j]=A[q+j+1]
    L[n1]=float('inf')
    R[n2]=float('inf')
    i,j=0,0
    for k in range(p,r+1):
        if L[i]<=R[j]:
            A[k]=L[i]
            i+=1
        else:
            A[k]=R[j]
            j+=1

def merge_sort(A,p,r):
    if p<r:
        q=(p+r)//2
        merge_sort(A,p,q)
        merge_sort(A,q+1,r)
        merge(A,p,q,r)

A=[1,3,5,7,2,4,6,8]
merge_sort(A,0,7)
print(A)

a='dsds'

    