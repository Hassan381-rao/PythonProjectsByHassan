for i in range(10,81):
   print(f"{i}")

for num in range(80, 0, -1):
    print(f"{num}")

for  a in range(20,41):
    if a % 2 == 0:
        print(a)
    else:
        print("\t")

for s in range(30,51):
    if s % 2 != 0:
        print(s)
    else:
        print("\n")

for num in range(10,41):
    if num>1:
        for i in range(2,num):
            if num % i ==0:
                break
        else:
            print(f"{num} your number is prime.")


