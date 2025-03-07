num=input("Enter 1 or 2 :")
if(num=='1'):
 def hsn(a,b):
    c=a+b
    return c
else:
 def hsn(a,b):
     c=a-b
     return c
a=int(input("Enter n1:"))
b=int(input("Enter n2:"))
result=hsn(a,b)
print(f"Your result is={result}")