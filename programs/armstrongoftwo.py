x,y=input().split()
num1=int(x)
num2=int(y)

for i in range(num1,num2):
  orders=len(str(i))
  temp=i
  sum=0
  while temp>0:
     r=temp%10
     sum+=r**orders
     temp//=10
  if(i==sum):
    print(i,end=" ")
  
