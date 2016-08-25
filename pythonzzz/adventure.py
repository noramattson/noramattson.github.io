print("Start Game")
print("It is 8:00 and you are trying to get to your Girls Who Code program from Staten Island.")
bus_or_ferry = input(" Do you take the ferry or do you take the bus? ")
while bus_or_ferry.upper() != "FERRY" and bus_or_ferry.upper() != "BUS":
    bus_or_ferry = input(" Do you take the ferry or do you take the bus? ")
if bus_or_ferry.upper() == "FERRY":
    print('''

                   ,:',:`,:'
                __||_||_||_||__
           ____["""""""""""""""]____
           \ " '''''''''''''''''''' |
    ~~^~^~^~^^~^~^~^~^~^~^~^~~^~^~^^~~^~^
    There is turbulence.''')
    boat_or_lifeboat = input ("Do you take a lifeboat or do you stay on the ferry? ")
    while boat_or_lifeboat.upper() != "LIFEBOAT" and boat_or_lifeboat.upper() != "BOAT":
        boat_or_lifeboat = input("Do you take a lifeboat or do you stay on the ferry? ")
    if boat_or_lifeboat.upper() == "LIFEBOAT":
        print ("Lifeboat reaches the shore! Congratulations! You walk to a bus stop.")
        stop1_or_stop2 = input('''
        .---------------------------.
       /,--..---..---..---..---..--. `.
      //___||___||___||___||___||___\_|
      [j__ ######################## [_|
         \============================|
      .==|  |"""||"""||"""||"""| |"""||
     /======"---""---""---""---"=|  =||
     |____    []*          ____  | ==||
     //  \\               //  \\ |===||
     "\__/"---------------"\__/"-+---+'

        The bus is packed. Do you get off at stop one or stop two?''')
        while stop1_or_stop2.upper() != "STOP ONE" and stop1_or_stop2.upper() != "STOP TWO":
                stop1_or_stop2 = input('''
                .---------------------------.
               /,--..---..---..---..---..--. `.
              //___||___||___||___||___||___\_|
              [j__ ######################## [_|
                 \============================|
              .==|  |"""||"""||"""||"""| |"""||
             /======"---""---""---""---"=|  =||
             |____    []*          ____  | ==||
             //  \\               //  \\ |===||
             "\__/"---------------"\__/"-+---+'

                The bus is packed. Do you get off at stop one or stop two?''')
        if stop1_or_stop2.upper() == "STOP ONE":
            walk_or_wait = input ("You got off too early. Do you take a walk or wait for the next bus? ")
            while walk_or_wait.upper() != "WALK" and walk_or_wait.upper() != "WAIT":
                walk_or_wait = input ("You got off too early. Do you take a walk or wait for the next bus? ")
            if walk_or_wait.upper() == "WALK":
                print("You meet a nice taxi driver who drives you the rest of the way! Congrats!! You are on time!!")
            else:
                print("You wait for seven hours and die of starvation because you didn't eat a healthy breakfast. You lose. Make better choices. Cmon.")
        else:
            print ("Your get off at the right stop! It looks like you are actually going to make it on time! Unfortunately, you get trampled by an elephant on the walk from the bus stop. Oops. Accidents happen. You lose.")
    else:
        print("The boat sinks, and there is no room on the door. You die :(")
else:
    stop1_or_stop2 = input('''
    .---------------------------.
   /,--..---..---..---..---..--. `.
  //___||___||___||___||___||___\_|
  [j__ ######################## [_|
     \============================|
  .==|  |"""||"""||"""||"""| |"""||
 /======"---""---""---""---"=|  =||
 |____    []*          ____  | ==||
 //  \\               //  \\ |===||
 "\__/"---------------"\__/"-+---+'

    The bus is packed. Do you get off at stop one or stop two?''')
    while stop1_or_stop2.upper() != "STOP ONE" and stop1_or_stop2.upper() != "STOP TWO":
            stop1_or_stop2 = input('''
            .---------------------------.
           /,--..---..---..---..---..--. `.
          //___||___||___||___||___||___\_|
          [j__ ######################## [_|
             \============================|
          .==|  |"""||"""||"""||"""| |"""||
         /======"---""---""---""---"=|  =||
         |____    []*          ____  | ==||
         //  \\               //  \\ |===||
         "\__/"---------------"\__/"-+---+'

            The bus is packed. Do you get off at stop one or stop two?''')
    if stop1_or_stop2.upper() == "STOP ONE":
        walk_or_wait = input ("You got off too early. Do you take a walk or wait for the next bus? ")
        while walk_or_wait.upper() != "WALK" and walk_or_wait.upper() != "WAIT":
            walk_or_wait = input ("You got off too early. Do you take a walk or wait for the next bus? ")
        if walk_or_wait.upper() == "WALK":
            print("You meet a nice taxi driver who drives you the rest of the way! Congrats!! You are on time!!")
        else:
            print("You wait for seven hours and die of starvation because you didn't eat a healthy breakfast. You lose. Make better choices. Cmon.")
    else:
        print ("Your get off at the right stop! It looks like you are actually going to make it on time! Unfortunately, you get trampled by an elephant on the walk from the bus stop. Oops. Accidents happen. You lose.")

print("End game")
