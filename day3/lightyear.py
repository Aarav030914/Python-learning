print('''@@ Buzz Lightyear (Toy Story) @@ 11/96

            _._                           _._
           ||||                           ||||
           ||||_           ___           _||||
           |  ||        .-'___`-.        ||  |
           \   /      .' .'_ _'. '.      \   /
           /~~|       | (| b d |) |       |~~\
          /'  |       |  |  '  |  |       |  `\
,        /__.-:      ,|  | `-' |  |,      :-.__\       ,
|'-------(    \-''""/.|  /\___/\  |.\""''-/    )------'|
|         \_.-'\   /   '-._____.-'   \   /'-._/        |
|.---------\   /'._| _    .---. ===  |_.'\   /--------.|
'           \ /  | |\_\ _ \=v=/  _   | |  \ /          '
             `.  | | \_\_\ ~~~  (_)  | |  .'
               `'"'|`'--.__.^.__.--'`|'"'`
                   \                 /
                    `,..---'"'---..,'
                      :--..___..--:    TO INFINITY...
                       \         /
                       |`.     .'|       AND BEYOND!
                       |  :___:  |
                       |   | |   |
                       |   | |   |
                       |.-.| |.-.|
                       |`-'| |`-'|
                       |   | |   |
                      /    | |    \
                     |_____| |_____|
                     ':---:-'-:---:'
                     /    |   |    \
                    /.---.|   |.---.\
                    `.____;   :____.' ''')
print('''Captian lightyear is in a game zone to earn some credits.
         Help him earn maximum credits''')
letter = input("Choose any of the three letters:- a, b or c:").lower()
credits = 0
if letter == 'a':
    credits +=0
elif letter =='b':
    credits += 2
    color = input("Choose any one of the color:- Blue or Yellow")
    if color.lower() == 'blue':
        credits +=10
    elif color.lower() == 'yellow':
        credits += 4
elif letter == 'c':
    credits += 5
    fruit = input("Choose any one of the fruit:- banana or orange:").lower()
    if fruit == 'banana':
        print('''Congratulations!, you have intered into our bonus round.
        If you win, you get 100 points and if you fail, you loose 3 points''')
        dog = input("What was the name of einstien's dog?:").lower()
        wife = input("What was the name of einstien's wife:").lower()
        if wife == 'milena maric einstien' and dog =="chico":
            credits += 100
            print("Yay!, you won the bonus round ")
        else:
            print("Sorry, You failed")
            credits -= 3
    elif fruit == 'orange':
        credits +=2
else:
    print("please enter a valid letter")
print(f"His total credit is {credits}$")    
print("Thanks for helping the captian")                        

