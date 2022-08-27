from random import randint
import ai_tictac as ai

#tic_tac_field
class Field:
	def __init__(self, width, height, style="|"):
		self.width = width
		self.height = height
		self.style = style
	def show(self, filled_bounds):
		# first row of numbers
		print(" ", end="") # empty first column
		for i in range(1, self.width + 1):
			print(f" {i}", end="")
		print()
		
		# main table
		for i in range(self.height):
			print(i + 1, end="") # empty first column
			for j in range(self.width):
				print("|" + filled_bounds[i][j], end="")
			print("|")

class Game:
	def __init__(self, condition, Field):
		self.player_one = ""
		self.player_two = ""
		self.condition = condition
		self.field = Field

	def begin(self):
		print("Console TIC-TAC. Made by ArturBV")

		self.player_one = input("Name: ")
		print(f"Welcome, {self.player_one}!")
		self.player_two = bots[randint(0, len(bots) - 1)]
		print(f"Your opponent: {self.player_two}")

	def end(self, winner):
		print(f"{winner} won!")

	def pat(self):
		print("Game over! Nobody wons")

#input string must accords to template: 1 2
def is_correct_turn(string, width, height, filled_bounds):
	string = string.split()
	
	if len(string) != 2:
		return 0
	elif not string[0].isdigit() or not string[1].isdigit():
		return 0
	elif (int(string[0]) > height or int(string[0]) <= 0) or (int(string[1]) > width or int(string[1]) <= 0):
		return 0
	elif filled_bounds[int(string[0]) - 1][int(string[1]) - 1] != "_":
		return 0

	return 1

def game_analyze(Game, field, filled_bounds):
	result = ai.field_analyze(filled_bounds).split()
	field.show(filled_bounds)

	if result[0] == "pat":	
		Game.pat()
		return 0

	if result[0] != "none":
		Game.condition = 0
		if result[1] == "X":
			Game.end(Game.player_one)
			return 0
		elif result[1] == "O":
			Game.end(Game.player_two)
			return 0

	return 1

bots = ["Andrey_AI", "Henry_AI", "Bob_AI", "Eugene_AI"]
condition_start = 1
condition_stop = 0
filled_bounds = [["_", "_", "_"],
				 ["_", "_", "_"],
				 ["_", "_", "_"]]
ai_field = [[1, 1, 1],
			[1, 1, 1],
			[1, 1, 1]]

if __name__ == "__main__":
	field = Field(3, 3)

	game = Game(condition_start, field)
	game.begin()
	field.show(filled_bounds)

	while game.condition != condition_stop:
		man_turn = input("Your turn(row, column): ")
		
		while not is_correct_turn(man_turn, field.width, field.height, filled_bounds):
			man_turn = input("Incorrect turn input(example: 1 2). Try again: ")
		
		man_turn = man_turn.split()
		turn_row = (int(man_turn[0]) - 1)
		turn_col = (int(man_turn[1]) - 1)
		filled_bounds[turn_row][turn_col] = "X"

		if game_analyze(game, field, filled_bounds) == condition_stop:
			break

		ai_turn = ai.turn(filled_bounds, ai_field)
		filled_bounds[ai_turn[0]][ai_turn[1]] = "O"

		if game_analyze(game, field, filled_bounds) == condition_stop:
			break
