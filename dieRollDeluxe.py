import time,random

while True:
    try:
        while True:
            try:
                timesToRoll = input('How many die would you like to roll today? [Default=2]')
                if timesToRoll == '':
                    timesToRoll = 2
                elif int(timesToRoll) < 1:
                    timesToRoll = 2
                else:
                    int(timesToRoll)
                break
            except ValueError:
                print('Hold up. I don\'t think that is a number. Try again...')
        
        rollResults = [random.randint(1,6) for _ in range(int(timesToRoll))]
        print(str(sum(rollResults)) + ' You rolled the following:' + str(rollResults))
        input('Press ENTER to roll again or Ctrl-C to close.')
    except KeyboardInterrupt:
        print('Thank you for using SeaWare.')
        time.sleep(3)
        break
