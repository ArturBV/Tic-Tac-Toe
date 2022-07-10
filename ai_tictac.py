# from ai_tests import test_dict
from random import randint

def turn(filled_bounds, ai_field):
	ai_field = fill_ai_field(filled_bounds, ai_field)
	best = get_best_bound(ai_field)

	return (best[0], best[1])

# returns:
# 	f"<type> _" if no winner yet
# 	f"<type> X" if man wins(triple "X")
# 	f"<type> O" if ai wins(triple "O")
# types: none, col, row, main_d, sub_d, pat
def field_analyze(filled_bounds):
	# symbols = ["_", "X", }"O"]
	rows_number = len(filled_bounds)
	columns_number = len(filled_bounds[0])
	field_is_full = 1

	# check all rows and columns
	for i in range(rows_number):
		row_symbol = filled_bounds[i][0]
		col_symbol = filled_bounds[0][i]
		full_row = full_col = 1

		for j in range(columns_number):
			if row_symbol == "_" or filled_bounds[i][j] != row_symbol:
				full_row = 0
			if col_symbol == "_" or filled_bounds[j][i] != col_symbol:
				full_col = 0

			if filled_bounds[i][j] == "_" or filled_bounds[j][i] == "_":
				field_is_full = 0

		if full_row: # row_symbol triple in a row
			return f"row {row_symbol}"
		elif full_col: # col_symbol triple in a column
			return f"col {col_symbol}"

	# check all diagonales
	main_diag_symbol = filled_bounds[0][0]
	sub_diag_symbol = filled_bounds[0][columns_number - 1]
	full_main_diag = full_sub_diag = 1

	for i in range(3):
		if main_diag_symbol == "_" or filled_bounds[i][i] != main_diag_symbol:
			full_main_diag = 0
		if sub_diag_symbol == "_" or filled_bounds[i][columns_number - 1 - i] != sub_diag_symbol:
			full_sub_diag = 0
	
	if full_main_diag:
		return f"main_d {main_diag_symbol}" # main_diag_symbol triple in main diagonale
	elif full_sub_diag:
		return f"sub_d {sub_diag_symbol}" # sub_diag_symbol triple in sub diagonale

	# if field is full and nobody wons
	if field_is_full:
		return f"pat _"
	return f"none _"

def get_best_bound(ai_field):
	rows_number = len(ai_field)
	columns_number = len(ai_field[0])

	best_bound = (0, 0, 0)
	ones = []
	for i in range(rows_number):
		for j in range(columns_number):
			if ai_field[i][j] == 1:
				ones.append((i, j))
			if best_bound[2] < ai_field[i][j]:
				best_bound = (i, j, ai_field[i][j])

	if best_bound[2] == 1:
		# there is no best turn
		best_bound = ones[randint(0, len(ones) - 1)]
	return best_bound

def fill_ai_field(filled_bounds, ai_field):
	rows_number = len(filled_bounds)
	columns_number = len(filled_bounds[0])
	symbols_score = {"_": 1, "X": 0, "O": 0}

	# enumerate empty and filled bounds
	for i in range(rows_number):
		for j in range(columns_number):
			ai_field[i][j] = symbols_score[filled_bounds[i][j]]

	# rows analyze
	row_counter = 0
	for row in filled_bounds:
		if row.count("X") == 2 and "_" in row:
			ai_field[row_counter][filled_bounds[row_counter].index("_")] += 3
		if row.count("O") == 2 and "_" in row:
			ai_field[row_counter][filled_bounds[row_counter].index("_")] += 5
		
		row_counter += 1

	# columns analyze
	column = []
	col_counter = 0
	for i in range(columns_number):
		# create column
		for j in range(rows_number):
			column.append(filled_bounds[j][i])

		if column.count("X") == 2 and "_" in column:
			ai_field[column.index("_")][col_counter] += 3
		if column.count("O") == 2 and "_" in column:
			ai_field[column.index("_")][col_counter] += 5

		col_counter += 1
		column = []

	# diagonales analyze
	main_diag = []
	sub_diag = []
	for i in range(rows_number):
		main_diag.append(filled_bounds[i][i])
		sub_diag.append(filled_bounds[i][columns_number - 1 - i])

	if main_diag.count("X") == 2 and "_" in main_diag:
		ai_field[main_diag.index("_")][main_diag.index("_")] += 3
	if main_diag.count("O") == 2 and "_" in main_diag:
		ai_field[main_diag.index("_")][main_diag.index("_")] += 5
	
	if sub_diag.count("X") == 2 and "_" in sub_diag:
		ai_field[sub_diag.index("_")][columns_number - 1 - sub_diag.index("_")] += 3
	if sub_diag.count("O") == 2 and "_" in sub_diag:
		ai_field[sub_diag.index("_")][columns_number - 1 - sub_diag.index("_")] += 5	
	# show_field(ai_field)
	return ai_field

# function for tests
def show_field(field):
	for i in range(len(field)):
		for j in range(len(field[0])):
			print(field[i][j], end=" ")
		print()
	print()

if __name__ == "__main__":
	filled_bounds = [["O", "O", "O"],
					 ["_", "_", "_"],
					 ["X", "X", "X"]]
	ai_field = [[1, 1, 1],
				[1, 1, 1],
				[1, 1, 1]]
	fill_ai_field(filled_bounds, ai_field)
	print(get_best_bound(ai_field))

	# for test_name in test_dict.keys():
		# fill_ai_field(test_dict[test_name], ai_field)
		# print(test_name, field_analyze(test_dict[test_name]))
