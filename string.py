str='Shoaib Akhtar'
a=str.lower().strip()
for i in range(0,5):  
  guess=input("Guess any fastest boller of pakistan in the histry of cricket =")
  if a == guess:
    print('You win!')
    #break
  else:
    print('Try again!')

#print("python".lower().strip() == input("Guess the word: ").lower().strip() and "You win!" or "Try again!")
