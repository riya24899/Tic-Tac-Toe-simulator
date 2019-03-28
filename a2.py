#Assignment-2, Game Tic-tac-toe

#State: Tiles are numbered 1 to 9

"""
Tick-Tac-Toe game state is defined as follows: 

tile1 |  tile2  | tile3
______|_________|______
tile4 |  tile5  | tile6
______|_________|______
tile7 |  tile8  | tile9
______|_________|______

A player can belong to one of the following two categories:
1. Naive: Player checks a tile randomly.
2. Intelligent: Player follows some strategy to win a game. You shall define a strategy that an intelligent player can take.

We will estimate probability of winning for a player for different scenarios.
 
Game1: A number of games are played between two naive players. Estimate probability of winning for player1. Assume player1 starts the game.

Game2: A number of games are played between a naive and intelligent player. Estimate probability of winning for player1. Assume player1 is naive and starts the game.

Game3: A number of games are played between two intelligent players. Estimate probability of winning for player1. Assume player1 starts the game.  
"""

import random 

tile1= 0    
tile2= 0
tile3= 0
tile4= 0
tile5= 0
tile6= 0
tile7= 0
tile8= 0
tile9= 0
#counts the number of moves played by player1
move1=0 
#counts the number of moves played by player2
move2=0 
# turn variable defines whose turn is now
turn ="Player1"

# There are 9 tiles numbered tile0 to tile9
# 0 value of a tile indicates that tile has not been ticked
# 1 value indicates that the tile is ticked by player-1
# 2 value indicates that the tile is ticked by player-2


def updateMove(move):
	
	global turn, tile1, tile2, tile3, tile4, tile5, tile6, tile7, tile8, tile9
	
	if turn=="Player1":
		if move==1:
			tile1+=1
		elif move==2:
			tile2+=1
		elif move==3:
			tile3+=1
		elif move==4:
			tile4+=1
		elif move==5:
			tile5+=1
		elif move==6:
			tile6+=1
		elif move==7:
			tile7+=1
		elif move==8:
			tile8+=1
		elif move==9:
			tile9+=1		

	elif turn=="Player2":
		if move==1:
			tile1+=2
		elif move==2:
			tile2+=2
		elif move==3:
			tile3+=2
		elif move==4:
			tile4+=2
		elif move==5:
			tile5+=2
		elif move==6:
			tile6+=2
		elif move==7:
			tile7+=2
		elif move==8:
			tile8+=2
		elif move==9:
			tile9+=2 	

def winningMove():
	""" Checks whether there is a winning move, if yes then returns the winning tile number
		In case there are two winning moves then returns the tile with the minimum tile number
	    Otherwise returns False
	"""
	global turn, tile1, tile2, tile3, tile4, tile5, tile6, tile7, tile8, tile9

	noWin=True
	move=False
	if turn=="Player1":
		if validMove(1):
			tile1+=1
			if win():
				noWin=False
				move=1	
			tile1+=-1
			if move:
				return move	
		if validMove(2):
			tile2+=1
			if win():
				noWin=False
				move= 2
			tile2+=-1
			if move:
				return move	
		if validMove(3):
			tile3+=1
			if win():
				noWin=False
				move= 3
			tile3+=-1
			if move:
				return move				
		if validMove(4):
			tile4+=1
			if win():
				noWin=False
				move= 4	
			tile4+=-1	
			if move:
				return move			
		if validMove(5):
			tile5+=1
			if win():
				noWin=False
				move= 5		
			tile5+=-1		
			if move:
				return move		
		if validMove(6):
			tile6+=1
			if win():
				noWin=False
				move= 6	
			tile6+=-1		
			if move:
				return move		
		if validMove(7):
			tile7+=1
			if win():
				noWin=False
				move= 7	
			tile7+=-1		
			if move:
				return move		
		if validMove(8):
			tile8+=1
			if win():
				noWin=False
				move= 8	
			tile8+=-1		
			if move:
				return move		
		if validMove(9):
			tile9+=1
			if win():
				noWin=False
				move= 9		
			tile9+=-1		
			if move:
				return move	

	elif turn=="Player2":
		if validMove(1):
			tile1+=2
			if win():
				noWin=False
				move= 1				
			tile1+=-2
			if move:
				return move	
		if validMove(2):
			tile2+=2
			if win():
				noWin=False
				move= 2
			tile2+=-2
			if move:
				return move	
		if validMove(3):
			tile3+=2
			if win():
				noWin=False
				move= 3
			tile3+=-2		
			if move:
				return move		
		if validMove(4):
			tile4+=2
			if win():
				noWin=False
				move= 4	
			tile4+=-2		
			if move:
				return move		
		if validMove(5):
			tile5+=2
			if win():
				noWin=False
				move= 5	
			tile5+=-2		
			if move:
				return move		
		if validMove(6):
			tile6+=2
			if win():
				noWin=False
				move= 6	
			tile6+=-2		
			if move:
				return move		
		if validMove(7):
			tile7+=2
			if win():
				noWin=False
				move= 7	
			tile7+=-2		
			if move:
				return move		
		if validMove(8):
			tile8+=2
			if win():
				noWin=False
				move= 8	
			tile8+=-2		
			if move:
				return move		
		if validMove(9):
			tile9+=2
			if win():
				noWin=False
				move= 9
			tile9+=-2		
			if move:
				return move	
	if noWin:
		return False

def blockingMove():
	""" Checks whether there is a blocking move, if yes then returns the winning tile number
		In case there are two winning moves then the tile with minimum tile number
	    Otherwise returns False

	    A move is a blocking move when it prevents the opponent from winning.
	"""

	global turn

	noBlock=True
	move=False
	if turn=="Player1":
		turn="Player2"
		if winningMove():
			noBlock=False
			move=winningMove()
		turn="Player1"	
		if move:
			return move			
	elif turn=="Player2":
		turn="Player1"
		if winningMove():
			noBlock=False
			move=winningMove()
		turn="Player2"
		if move:
			return move

	if noBlock:
		return False

				
def validMove(move):
	""" Checks whether a move played by a player is valid or invalid.
		Return True if move is valid. 
		
		A move is valid if the corresponding tile for the move is not ticked.
	"""

	global tile1, tile2, tile3, tile4, tile5, tile6, tile7, tile8, tile9

	a=eval("tile"+str(move)+"==0")
	return a

def win():
	""" Returns True if the board state specifies a winning state for some player.
		
		A player wins if ticks made by the player are present either
		i) in a row
		ii) in a cloumn
		iii) in a diagonal
	"""

	global turn, tile1, tile2, tile3, tile4, tile5, tile6, tile7, tile8, tile9, move1, move2, player1, player2

	win1 = tile1==tile2==tile3==1 or tile1==tile2==tile3==2
	win2 = tile4==tile5==tile6==1 or tile4==tile5==tile6==2
	win3 = tile7==tile8==tile9==1 or tile7==tile8==tile9==2
	win4 = tile1==tile4==tile7==1 or tile1==tile4==tile7==2
	win5 = tile2==tile5==tile8==1 or tile2==tile5==tile8==2
	win6 = tile3==tile6==tile9==1 or tile3==tile6==tile9==2
	win7 = tile1==tile5==tile9==1 or tile1==tile5==tile9==2
	win8 = tile3==tile5==tile7==1 or tile3==tile5==tile7==2

	win = win1 or win2 or win3 or win4 or win5 or win6 or win7 or win8
	return win

def takeNaiveMove():
	""" Returns a tile number randomly from the set of unchecked tiles with uniform probability distribution.    
	"""
	notFound=True
	while notFound:
		move=random.randint(1,9)
		if validMove(move):
			notFound=False
	return move

def takeStrategicMove():
	""" Returns a tile number from the set of unchecked tiles
	using some rules.
	
	"""
	global move1, move2

	if move1==0 or move2==0:
		if validMove(1):
			return 1
		elif validMove(5):
			return 5
	elif winningMove():
		return winningMove()		
	elif blockingMove():
		return blockingMove()
	else:
		return takeNaiveMove()	
	
def validBoard():
	""" Return True if board state is valid.
		
		A board state is valid if number of ticks by player1 is always either equal to or one more than the ticks by player2.
	"""

	global move1, move2

	if move1==move2 or move1-move2==1:
		return True
	else:
		return False					

def game(gametype=1):
	""" Returns 1 if player1 wins and 2 if player2 wins
		and 0 if it is a draw.
	
		gametype defines three types of games discussed above.
		i.e., game1, game2, game3
	"""

	global turn, tile1, tile2, tile3, tile4, tile5, tile6, tile7, tile8, tile9, move1, move2

	tile1= 0    
	tile2= 0
	tile3= 0
	tile4= 0
	tile5= 0
	tile6= 0
	tile7= 0
	tile8= 0
	tile9= 0

	move1= 0 
	move2= 0 
	turn="Player1"

	winner=0
	if gametype==1:
		while (not(win()) and validBoard()):
			turn="Player1"
			move=takeNaiveMove()
			updateMove(move)
			move1+=1
			if win():
				winner=1
				break
			if move1+move2==9:
					break	
			turn="Player2"
			move=takeNaiveMove()
			updateMove(move)
			move2+=1
			if win():
				winner=2
		if validBoard():			
			return winner
		else:
			return "Error in board"	
		 
	elif gametype==2:
		while(not(win()) and validBoard()):
			turn="Player1"
			move=takeNaiveMove()
			updateMove(move)
			move1+=1
			if win():
				winner=1
				break
			if move1+move2==9:
				break	
			turn="Player2"
			move=takeStrategicMove()
			updateMove(move)
			move2+=1
			if win():
				winner=2
		if validBoard():
			return winner			
		else:
			return "Error in board"			
	else:
		while(not(win()) and validBoard()):
			turn="Player1"
			move=takeStrategicMove()
			updateMove(move)
			move1+=1
			if win():
				winner=1
				break
			if move1+move2==9:
				break		
			turn="Player2"
			move=takeStrategicMove()
			updateMove(move)
			move2+=1
			if win():
				winner=2
		if validBoard():
			return winner			
		else:
			return "Error in board"

def game1(n):
	""" Returns the winning probability for player1. 

	n games are played between two naive players. Estimate probability of winning for player1. Assume player1 starts the game.
	"""
	win=0
	for i in range(n):
		if game(1)==1:
			win+=1
	prob1=win/n
	return prob1	

def game2(n):
	"""Returns the winning probability for player1.
	
	n games are played between a naive and intelligent move. Estimate probability of winning for player1. Assume player1 is naive and starts the game.
	"""
	win=0
	for i in range(n):
		if game(2)==1:
			win+=1
	prob2=win/n
	return prob2	

def game3(n):
	"""Returns the winning probability for player1. 
	
	n games are played between two intelligent players. Estimate probability of winning for player1. Assume player1 starts the game.
	"""
	win=0
	for i in range(n):
		if game(3)==1:
			win+=1	
	prob3=win/n
	return prob3	

#test cases

def case0():
	global tile1, tile2, tile3, tile4, tile5, tile6, tile7, tile8, tile9, turn, move1, move2

	tile1= 0    
	tile2= 0
	tile3= 0
	tile4= 0
	tile5= 0
	tile6= 0
	tile7= 0
	tile8= 0
	tile9= 0
	move1= 0
	move2= 0	
	turn="Player1"

def case1():
	global tile1, tile2, tile3, tile4, tile5, tile6, tile7, tile8, tile9, turn, move1, move2

	tile1= 1    
	tile2= 1
	tile3= 0
	tile4= 2
	tile5= 2
	tile6= 0
	tile7= 0
	tile8= 0
	tile9= 0
	move1= 2
	move2= 2
	turn="Player1"

def case2():
	global tile1, tile2, tile3, tile4, tile5, tile6, tile7, tile8, tile9, turn, move1, move2

	tile1= 0    
	tile2= 0
	tile3= 0
	tile4= 0
	tile5= 0
	tile6= 0
	tile7= 0
	tile8= 0
	tile9= 0
	move1= 0
	move2= 0	
	turn="Player1"

def case3():
	global tile1, tile2, tile3, tile4, tile5, tile6, tile7, tile8, tile9, turn, move1, move2

	tile1= 1    
	tile2= 1
	tile3= 0
	tile4= 1
	tile5= 2
	tile6= 2
	tile7= 0
	tile8= 2
	tile9= 0
	move1= 3
	move2= 3
	turn="Player1"

def case4():
	global tile1, tile2, tile3, tile4, tile5, tile6, tile7, tile8, tile9, turn, move1, move2

	tile1= 1    
	tile2= 1
	tile3= 0
	tile4= 2
	tile5= 0
	tile6= 0
	tile7= 0
	tile8= 0
	tile9= 0
	move1= 2
	move2= 1
	turn="Player2"

def case5():
	global tile1, tile2, tile3, tile4, tile5, tile6, tile7, tile8, tile9, turn, move1, move2

	tile1= 1    
	tile2= 1
	tile3= 0
	tile4= 1
	tile5= 2
	tile6= 2
	tile7= 0
	tile8= 0
	tile9= 0
	move1= 3
	move2= 2
	turn="Player2"

def case6():
	global tile1, tile2, tile3, tile4, tile5, tile6, tile7, tile8, tile9, turn, move1, move2

	tile1= 1    
	tile2= 1
	tile3= 1
	tile4= 2
	tile5= 0
	tile6= 0
	tile7= 0
	tile8= 0
	tile9= 2
	move1= 3
	move2= 2
	turn="Player2"	

def case7():
	global tile1, tile2, tile3, tile4, tile5, tile6, tile7, tile8, tile9, turn, move1, move2

	tile1= 1    
	tile2= 1
	tile3= 1
	tile4= 2
	tile5= 0
	tile6= 0
	tile7= 2
	tile8= 2
	tile9= 2
	move1= 3
	move2= 4
	turn="Player2"	

def case8():
	global tile1, tile2, tile3, tile4, tile5, tile6, tile7, tile8, tile9, turn, move1, move2

	tile1= 1    
	tile2= 0
	tile3= 0
	tile4= 0
	tile5= 0
	tile6= 0
	tile7= 0
	tile8= 0
	tile9= 0
	move1= 1
	move2= 0
	turn="Player2"

def case9():
	global tile1, tile2, tile3, tile4, tile5, tile6, tile7, tile8, tile9, turn, move1, move2

	tile1= 1    
	tile2= 0
	tile3= 0
	tile4= 0
	tile5= 2
	tile6= 0
	tile7= 0
	tile8= 0
	tile9= 0
	move1= 1
	move2= 1
	turn="Player1"		