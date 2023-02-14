from random import randint
answer = input("Welcome to Monty's.\n What would you like to eat or to drink? \n Print your answer, using commas")
choice = answer.split(',') 
sum = 0
for i in choice: 
    price = randint (50,100) 
    print (i + '.....UAH{}'.format(price))
    sum += price
print('Total.....UAH{}'.format(sum))
