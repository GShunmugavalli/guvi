s=int(input())
ele=list(map(int,input().strip().split()))[:s]
ele.sort()
print(" ".join(str(a) for a in ele))
