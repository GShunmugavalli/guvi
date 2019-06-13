a=int(input())
x= [int(n) for n in input().split()]

def median(x):
    x.sort()
    mid = len(x) // 2
    return (x[mid] + x[~mid]) // 2
s1=median(x)
print(s1)
