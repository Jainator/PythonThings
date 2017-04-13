import random

def yesOrNo(question):
    reply = str(input(question + ' [Y/N]')).upper().strip('.')
    if reply == 'Y':
        return True
    elif reply == 'YES':
        return True
    elif reply == 'N':
        return False
    elif reply == 'NO':
        return False
    else:
        return yesOrNo('Please enter Y or N...')
        
theAlmightyAnswer = yesOrNo('Enter \"yes\" to roll dice, or \"no\" to close program...')

while theAlmightyAnswer == True:
    print(random.randint(1,6))
    theAlmightyAnswer = yesOrNo('Enter \"yes\" to roll dice, or \"no\" to close program...')
print('Have a nice day. Thank you for using SeaWare.')
