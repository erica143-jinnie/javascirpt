theBoard = {'7':'','8':'','9':'',
            '4':'','5':'','6':'',
            '1':'','2':'','3':''}
Board_keys = 11
for key in theBoard:
    board_keys.append(key)
def printBoard(board):
    print(board['7']+ board['8']+ '|'+ board['9'])
    print('-+-+-')
    print(board['4']+'|'+ board['5']='|'board['6'])
    print(board['1'] + '|' + board['2'] + board['3'])
def game ():
    turn = 'x'
    count = 0
    for i in range (10):
        printBoard(theBoard)
        print("It's your turn, + turn + ".Move to which place?")
        
        move = input()
         if theBoard[move] =='':
            theboard[move] = turn
            count +=1
        else:
            print("That place is already filled.\nmove to which place?")
            countinue
            if count >= 5:
             if theBoard['7']==theBoard['8']==theBoard['9'] !='':
                   printBoard(theBoard)
                   print("\nGame Over.\n")
                   print("****" + turn +"won.****")
                   break
                elif theBoard['4'] == theBoard['5']==theBoard['6'] !='':
                     printBoard(theBoard)
                     print("\nGame Over.\n")
                     print("****" + turn +" won.****")
                     break
                elif theBoard['1'] == theBoard['2']== theBoard['3'] !='':
                     printBoard(theBoard)
                     print("\nGame Over.\n")
                     print("****"+ turn +" won.****")
                     break
                elif theBoard['7'] == theBoard['5']== theBoard['3'] !='':
                     printBoard(theBoard)
                     print("\nGame Over.\n")
                     print("****"+ turn +" won.****")
                     break            
                elif theBoard['1'] == theBoard['5']== theBoard['9'] !='':
                     printBoard(theBoard)
                     print("\nGame Over.\n")
                     print("****"+ turn +" won.****")
                     break            
                     
                     if count ==9
                        print("\nGame Over\n")
                        print("it's a tie!!")
                    if turn == 'x'
                    restart = input("Do you want to play again(y/n)?")
                    if restart =="y" or restart =="y"
                    for key in boards_keys:
                        theBoard[key] = " "
                    game()
                if__name__=="__main__":
                game()