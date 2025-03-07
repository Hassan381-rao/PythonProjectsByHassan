print('\n<<<<<<<<<<Choose the correct opption>>>>>>>>>>')
str='Shoaib Akhtar'
str1='Python'
str2='Burj Khalifa'
str3='H++'
str4='Would'
a=str.lower().strip()
b=str1.lower().strip()
c=str2.lower().strip()
d=str3.lower().strip()
e=str4.lower().strip()
for i in range(0,1):  
  guess=input("\n1.Guess the fastest boller of pakistani cricket team? \nA.Imran khan\tB.Babar Azam \nC.Shoaib Akhtar\tD.Rizwan\n")
  if a == guess:
    az=5
    print(f'<<<<<Congrats!You got {az} points.>>>>>')
    break
  else:
    az=0
    print(f'<<<<<You got {az} point.>>>>>')
for i in range(0,1):  
  lan=input('\n2.What is most Famous programming Language?\nA.C#\tB.CSS\nC.Java\tD.Python\n ') 
  if b == lan:
    ax=5
    print(f'<<<<<Congrats!You got {ax} points.>>>>>')
    break
  else:
    ax=0
    print(f'<<<<<You got {ax} point.>>>>>')
for i in range(0,1): 
  bul=input("\n3.which is the highest building in the world?\nA.Heydar Aliyev Center\tB.Bilbao Guggenheim Museum\nC.Burj Khalifa\t\tD.Hagia Sophia\n")
  if c== bul:
    ac=5
    print(f'<<<<<Congrats!You got {ac} points.>>>>>')
    break
  else:
    ac=0
    print(f'<<<<<You got {ac} point.>>>>>')
for i in range(0,1): 
  nt=input("\n4.which one is not the programming language?\nA.C#\t\tB.Java\nC.Python\tD.H++\n")
  if c== nt:
    av=5
    print(f'<<<<<Congrats!You got {av} points.>>>>>')
    break
  else:
    av=0
    print(f'<<<<<You got {av} point.>>>>>')
for i in range(0,1): 
  nh=input("\n5.If you had let me know earlier, I ___ have been able to come.\nA) should\tB) would\nC) could\tD) might\n ")
  if d== nh:
    au=5
    print(f'<<<<<Congrats!You got {au} points.>>>>>')
    break
  else:
    au=0
    print(f'<<<<<You got {au} point.>>>>>')
  total=az+ax+ac+av+au
  print(f'\n|||||Your total points is {total}.|||||')










#print("python".lower().strip() == input("Guess the word: ").lower().strip() and "You win!" or "Try again!")
  