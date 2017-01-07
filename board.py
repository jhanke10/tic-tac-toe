#Creates the tic-tac-toe board
class Board:
	grid = []

	#Initializes board
	def __init__(self):
		self.grid = []
		for i in range(3):
			row = []
			for j in range(3):
				row.append('_')
			self.grid.append(row)
			row = []

	#String format of Board object
	def __str__(self):
		board = ''
		for i in range(len(self.grid)):
			for j in range(len(self.grid)):
				board += self.grid[i][j] + ' '
			board += '\n'
		return board

	#Checks horizontal
	def checkHoriz(self, row, player):
		for i in range(len(self.grid[row])):
			if self.grid[row][i] != player:
				return False
		return True

	#Checks vertical
	def checkVert(self, col, player):
		for i in range(len(self.grid)):
			if self.grid[i][col] != player:
				return False
		return True

	#Checks Diagonals
	def checkDiag(self, player):
		same = False
		if self.grid[0][0] == self.grid[1][1] and self.grid[2][2] == self.grid[1][1]:
			same = True
		if self.grid[2][0] == self.grid[1][1] and self.grid[0][2] == self.grid[1][1]:
			same = True
		return same and self.grid[1][1] == player

	#Checks if player has won
	def hasWon(self, player, position):
		row, col = position
		return self.checkHoriz(row, player) or self.checkVert(col, player) or self.checkDiag(player)

	#Check if tie and game is over
	def gameOver(self):
		for i in range(len(self.grid)):
			for j in range(len(self.grid)):
				if self.grid[i][j] == '_':
					return False
		return True

	#Adds piece to board and returns position
	def placePiece(self, player, row, col):
		if self.grid[row][col] == '_':
			self.grid[row][col] = player
			return (row, col)
		else:
			return None