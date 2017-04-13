from sys import exit
from random import randint

while True:
    try:
        print(randint(1,6))
        input('Press ENTER to roll again or Ctrl-C to close')
    except KeyboardInterrupt:
        print('Have a nice day. Thank you for using SeaWare.')
        exit()
