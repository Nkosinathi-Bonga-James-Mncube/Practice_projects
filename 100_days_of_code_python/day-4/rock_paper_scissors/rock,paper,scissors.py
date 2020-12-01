import random

def fist(input_value):
    fist_value = ''
    if (input_value == 0):
        fist_value = 'Throws Rock'
    elif (input_value == 1):
        fist_value = 'Throws Paper'
    elif (input_value == 2):
        fist_value = 'Throws Scissors'
    return fist_value
    
def rock_paper_scissor_game():
    user=int(input('What do you choose? Type 0 for rock,1 for Paper or 2 for Scissors : '))
    value = random.randrange(0,3)
    print('User value : '+fist(user) + ' '+str(user))
    print('Compute value :'+fist(value)+' '+str(value))
    if (value == 0 and user == 2):
        print('You lose')
    elif (value == 1 and user== 0):
        print('You lose')
    elif (value ==2 and user == 1):
        print('You lose')
    else:
        if (value == user):
            print('Draw')
        else:
            print('You win')
rock_paper_scissor_game()