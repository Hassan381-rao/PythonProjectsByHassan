num=input("Enter number whose table you want to see:")
try:
  for i in range(1,11):
    print(f"{num} x {i}={num * i}")  
except Exception as e:
    print(e)