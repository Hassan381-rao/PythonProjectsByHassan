import os
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
clear_screen()
amount=int(input("------------\nEnter your amount of Agriculture Lands in canalss:"))
son=int(input("------------\nHow many son:"))
daughter=int(input("------------\nHow many daughters:"))
myvidow=int(input("------------\nHow many vidows:"))
total_heirs=son+daughter
vidow=amount / 8
vidow=vidow / myvidow
amount=amount - vidow
print(f"------------\nvidow part={vidow}")
result=amount / total_heirs
son_part=result * 2
s=son_part / son
print(f"-------------\nEvery son part={s}")
z=result / daughter
print(f"------------\nEvery daughter part={z}")




    
