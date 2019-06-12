x1=input().split()
num1=float(x1[0])
num2=float(x1[1])
num3=float(x1[2])
if(num1>num2 and num1>num3):
  print(int(num1))
elif(num2>num1 and num2>num3):
  print(int(num2))
else:
  print(int(num3))
