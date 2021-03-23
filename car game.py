helpcondition =''
started = False

while condition != 'quiet':
     condition = input("> ").lower()
     if condition == 'start' :
         if started:
             print(' car has already started. thank you')
         else:
             print('car has started. ready to go.....')
             started = True
     elif condition == 'stop' :
         if not started:
             print('car has already stopped. thank you.')
         else:
             print('car has stopped.')
             started = False
     elif condition =='help':
        print( """
        start -> to start the car
        stop -> to stop th car
        quiet -> to exit the game
        help -> for instructions""")
     else:
         print('i dont understand that. please provide valid command.')
if condition == 'quiet' :
     print('Thank you for playing our game.')