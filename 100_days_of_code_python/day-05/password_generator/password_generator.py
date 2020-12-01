import random
def letter():
    return chr(random.randrange(1,27)+96)
def rand_uppercase(value):
    rand_upper=random.randrange(0,2)
    if (rand_upper == 1):
        value = value.upper()
    return value
def symbol():
    return chr(random.randrange(33,48))
def number():
    return chr(random.randrange(48,58))
def choice_function(letter_loop,symbol_loop,number_loop):
    temp=''
    while (letter_loop !=0 or symbol_loop!=0 or number_loop!=0):
        value=random.randrange(1,4)
        if (value == 1 and letter_loop != 0):
            temp = temp+rand_uppercase(letter())
            letter_loop = letter_loop-1
        if (value == 2 and symbol_loop != 0):
            temp = temp+symbol()
            symbol_loop = symbol_loop-1
        if (value == 3 and number_loop != 0):
            temp = temp+number()
            number_loop = number_loop-1

    return temp
    
print('Welcome to PyPassword Generator!')
letter_loop=int(input('How many letters would you like in password?'))
symbol_loop= int(input('How many symbol would you like in password?'))
number_loop= int(input('How many number would you like in password?'))
print('New password :',choice_function(letter_loop,symbol_loop,number_loop))

