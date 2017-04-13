import time,random

try:
    while True:
        print(random.randint(1,6))
        input('Press ENTER to roll again or Ctrl-C to close')
except KeyboardInterrupt:
    print('\nHave a nice day. Thank you for choosing SeaWare.')
    time.sleep(3)
