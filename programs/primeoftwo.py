x1,y1=input().split()
num1=int(x1)
num2=int(y1)
for num in range(num1+1,num2):
  if num>1:
    for i in range(2,num):
      if(num%i==0):
        break
    else:
      print(num,end=" ")
