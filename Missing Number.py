N = int(input())

A = list(map(int,input().split()))

X = lambda index, xor : X(index+1,xor^A[index]) if index<N else xor

print(X(0,0))
