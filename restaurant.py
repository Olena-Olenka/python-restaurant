from random import randint
answer = input("Welcome to Monty's.\n What would you like to eat or to drink? \n Print your answer, using commas")
choice = answer.split(',') 
print("Thank you for visiting Monty's!")
for i in choice:
  
   print (i + '.....UAH{}'.format(randint (50,100)))
 
print('Total.....UAH{}'.format(randint (100,500)))
