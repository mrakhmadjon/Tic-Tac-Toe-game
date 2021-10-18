import os

a = ['1', '2', '3', '4', '5', '6', '7', '8', '9']


def clear():
    os.system ("clear")


def tictac():
    print ("""Tic Tac Toe
1-o'yinchi - X   2-o'yinchi - O""")
    print (f"""
             {a[0]}  |  {a[1]}  |   {a[2]}
           _____|_____|_____
             {a[3]}  |  {a[4]}  |   {a[5]}
           _____|_____|_____
             {a[6]}  |  {a[7]}  |   {a[8]}
           _____|_____|_____
                """)


sanoq = 0
while sanoq != 9:
    tictac ()
    if sanoq % 2 == 0:
        clear ()
        tictac ()
        choice = input ("1-o'yinchi sizning yurishingiz: ")
        clear ()
        while choice not in a:
            clear ()
            tictac ()
            print ("To'gri kiriting ey")
            choice = input ("1-o'yinchi sizning yurishingiz: ")
        for i in range (len (a)):
            if choice == a[i]:
                a[i] = "X"
        sanoq += 1
        if a[0] == "X" and a[1] == "X"and a[2] == "X":
            print ("1-o'yinchi yutdi")
            exit ()
        elif a[0] == "X" and a[4] == "X" and a[8] == "X":
            print ("1-o'yinchi yutdi")
            exit ()
        elif a[0]  == "X"and a[3] == "X" and a[6] == "X":
            print ("1-o'yinchi yutdi")
            exit ()
        elif a[6] == "X" and a[7] == "X" and a[8] == "X":
            print ("1-o'yinchi yutdi")
            exit ()
        elif a[2] == "X" and a[5] == "X" and a[8] == "X":
            print ("1-o'yinchi yutdi")
            exit ()
        elif a[2] == "X" and a[4] == "X" and a[6] == "X":
            print ("1-o'yinchi yutdi")
            exit ()
        elif a[3] == "X" and a[4] == "X" and a[5] == "X":
            print("1-o'yinchi yutdi")
            exit()
        elif a[1] == "X" and a[4] == "X" and a[7] == "X":
            print("1-o'yinchi yutdi")
            exit()
    else:
        clear ()
        tictac ()
        choice = input ("2-o'yinchi sizning yurishingiz:")
        clear ()
        while choice not in a:
            clear ()
            tictac ()
            print ("To'gri kiriting ey")
            choice = input ("2-o'yinchi sizning yurishingiz: ")
        for i in range (len (a)):
            if choice == a[i]:
                a[i] = "O"
        sanoq += 1
        if a[0] == "O" and a[1] == "O" and a[2] == "O":
            print("2-o'yinchi yutdi")
            exit()
        elif a[0] == "O" and a[4] == "O" and a[8] == "O":
            print("2-o'yinchi yutdi")
            exit()
        elif a[0] == "O" and a[3] == "O" and a[6] == "O":
            print("2-o'yinchi yutdi")
            exit()
        elif a[6] == "O" and a[7] == "O" and a[8] == "O":
            print("2-o'yinchi yutdi")
            exit()
        elif a[2] == "O" and a[5] == "O" and a[8] == "O":
            print("2-o'yinchi yutdi")
            exit()
        elif a[2] == "O" and a[4] == "O" and a[6] == "O":
            print("2-o'yinchi yutdi")
            exit()
        elif a[3] == "O" and a[4] == "O" and a[5] == "O":
            print("2-o'yinchi yutdi")
            exit()
        elif a[1] == "O" and a[4] == "O" and a[7] == "O":
            print("2-o'yinchi yutdi")
            exit()

print("DURRANG", sanoq)



