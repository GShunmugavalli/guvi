s=int(input())
temp=s
sum=0
while temp>0:
  r=temp%10
  sum+=r**3
  temp//=10
if(s==sum):
  print("yes")
else:
  print("no")
