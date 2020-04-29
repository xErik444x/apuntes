from random import randrange
from colorama import Fore,init,Style
init()
# #
# # la función acepta un parámetro el cual contiene el estado actual del tablero
# # y lo muestra en la consola
# #
def DisplayBoard(board):
    print(Fore.YELLOW," ","+---------" * 3,"+",sep="")
    for linea in range(3):
        print(Fore.YELLOW,"|   ",end="")
        for col in range(3):
            print(Fore.GREEN,board[linea][col],Fore.YELLOW ,end="   |   ")
        print()
    print(Fore.YELLOW," ","+---------" * 3,"+",sep="")
    if(len(MakeListOfFreeFields(board))<=0):
        return(print("Empate"))
    if turno == 0:
        EnterMove(board)
    else:
        DrawMove(board)
# #
# # la función acepta el estado actual del tablero y pregunta al usuario acerca de su movimiento, 
# # verifica la entrada y actualiza el tablero acorde a la decisión del usuario
# #
def EnterMove(board):
    mov = int(input("Escoje la casilla:"))
    if mov in MakeListOfFreeFields(board):
        if mov <= 3:
            mov -=1
            board[0][mov] = "O"
        elif mov <= 6:
            mov -=1
            board[1][mov%3] = "O"
        elif mov <= 9:
            mov -=1
            board[2][mov%3] = "O"
        if (VictoryFor(board, "O")):
            quit()
        global turno
        turno = 1
        DisplayBoard(board)
    else:
        print("Movimiento no valido.")
        EnterMove(board)
# #
# # la función examina el tablero y construye una lista de todos los cuadros vacíos 
# # la lista esta compuesta por tuplas, cada tupla es un par de números que indican la fila y columna
# #
def MakeListOfFreeFields(board):
    libres=[]
    for linea in range(3):
        for col in range(3):
            if board[linea][col] != 'X' and board[linea][col] != 'O':
                libres.append((board[linea][col]))
    #print(tuple(libres))
    return(tuple(libres))

# #
# # la función analiza el estatus del tablero para verificar si
# # el jugador que utiliza las 'O's o las 'X's ha ganado el juego
# #
def VictoryFor(board, sign):
    for l in range(3):
        if (board[l][0] == sign and board[l][1] == sign and board[l][2] == sign):
            #print(board[l][0],board[l][1],board[l][2])
            print("+-------" * 3,"+",sep="")
            for linea in range(3):
                print("|   ",end="")
                for col in range(3):
                    print(board[linea][col] ,end="   |   ")
                print()
            print("+-------" * 3,"+",sep="")
            print("Ganó ",sign)
            return True

    for l in range(3):
        if (board[0][l] == sign and board[1][l] == sign and  board[2][l] == sign):
            print("+-------" * 3,"+",sep="")
            for linea in range(3):
                print("|   ",end="")
                for col in range(3):
                    print(board[linea][col] ,end="   |   ")
                print()
            print("+-------" * 3,"+",sep="")
            print("Ganó ",sign)
            return True
    
    if(board[0][0]== sign and board[1][1]==sign and board[2][2]==sign):
        print("+-------" * 3,"+",sep="")
        for linea in range(3):
            print("|   ",end="")
            for col in range(3):
                print(board[linea][col] ,end="   |   ")
            print()
        print("+-------" * 3,"+",sep="")
        print("Ganó ",sign)
        return True
    if(board[0][2]== sign and board[1][1]==sign and board[2][0]==sign):
        print("+-------" * 3,"+",sep="")
        for linea in range(3):
            print("|   ",end="")
            for col in range(3):
                print(board[linea][col] ,end="   |   ")
            print()
        print("+-------" * 3,"+",sep="")
        print("Ganó ",sign)
        return True
# #
# # la función dibuja el movimiento de la maquina y actualiza el tablero
# #
def DrawMove(board):
    mov = randrange(9)
    if len(MakeListOfFreeFields(board)) <= 1:
        mov = MakeListOfFreeFields(board)[0]
    if mov in MakeListOfFreeFields(board):
        if mov <= 3:
            mov -=1
            board[0][mov] = "X"
        elif mov <= 6:
            mov -=1
            board[1][mov%3] = "X"
        elif mov <= 9:
            mov -=1
            board[2][mov%3] = "X"
        global turno
        turno = 0
        if(VictoryFor(board, "X")):
            exit()
        DisplayBoard(board)
    else:
        DrawMove(board)

global turno
turno = 0 #0 jugador, 1 maquina
x = 1
tablero = [ [3 * j + i + 1 for i in range(3)] for j in range(3) ]
tablero[1][1] = "X"

DisplayBoard(tablero)