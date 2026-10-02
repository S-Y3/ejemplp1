def burbuja(A):
    for i in range(1,len(A)):
        for j in range(0,len(A)-i):
            if (A[j+1] < A[j]) :
                aux = A[j]
                A[j] = A[j+1]
                A[j+1] = aux


    print(A)

def ordenin (A):
    pos=0
    i=0
    aux=0
    for i in range(1,len(A)):
        pos=i
        aux=A[i]
        while (pos>0 and A[pos-1]>aux):
            A[pos]=A[pos-1]
            pos=pos-1
        A[pos]=aux
        i=i+1
    print(A);
#Programa Principal
A=[6,5,3,1,8,7,2,4]
print (A)
burbuja(A)
