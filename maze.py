import time
import random
from tkinter import Tk, BOTH, Canvas

from geometries import Cell

class Maze:
	def __init__(
			self,
			x1,
			y1,
			num_rows,
			num_cols,
			cell_size,
			win=None,
			seed=None
		):
		self.x1 = x1
		self.y1 = y1
		self.num_rows = num_rows
		self.num_cols = num_cols
		self.cell_size = cell_size
		self.win = win

		if seed:
			random.seed(seed)

		self.create_cells()
		self.break_entrance_and_exit()
		self.break_walls_r()
		self.reset_visited()

	def create_cells(self):
		self.cells = []
		for i in range(0, self.num_rows):
			self.cells.append([])
			for j in range(0, self.num_cols):
				self.cells[i].append(Cell(0, 0, self.cell_size))
				self.draw_cell(i, j)


	def draw_cell(self, row, col):
		cell = self.cells[row][col]
		cell.x1 = self.x1 + (self.cell_size * col)
		cell.y1 = self.y1 + (self.cell_size * row)
		cell.x2 = self.x1 + (self.cell_size * (col + 1))
		cell.y2 = self.y1 + (self.cell_size * (row + 1))
		cell.center = ((cell.x1 + cell.x2) / 2, (cell.y1 + cell.y2) / 2)
		print(f"rendering... row:{row}, col:{col}, x: {cell.x1}, y:{cell.y1}, width:{cell.x2}, height:{cell.y2}")
		if self.win is None:
			return

		self.win.draw_cell(cell)

	def draw_move(self, row, col, row2, col2):
		cell1 = self.cells[row][col]
		cell2 = self.cells[row2][col2]
		print(f"rendering... move from:{row},{col} to:{col}, {row2},{col2}")
		if self.win is None:
			return

		self.win.draw_move(cell1, cell2)

	def break_entrance_and_exit(self):
		self.cells[0][0].top_wall = False
		self.cells[self.num_rows - 1][self.num_cols - 1].bottom_wall = False
		self.draw_cell(0, 0)
		self.draw_cell(self.num_rows - 1, self.num_cols - 1)

	def break_walls_r(self, row=0, col=0):
		self.cells[row][col].visited = True
		while True:
			next_index_list = []

			# // determine which cell(s) to visit next
			# left
			if col > 0 and not self.cells[row][col - 1].visited:
				next_index_list.append((row, col - 1))
			# right
			if col < self.num_cols - 1 and not self.cells[row][col + 1].visited:
				next_index_list.append((row, col + 1))
			# up
			if row > 0 and not self.cells[row - 1][col].visited:
				next_index_list.append((row - 1, col))
			# down
			if row < self.num_rows - 1 and not self.cells[row + 1][col].visited:
				next_index_list.append((row + 1, col))

			# if there is nowhere to go from here
			# just break out
			if len(next_index_list) == 0:
				self.draw_cell(row, col)
				return

			# randomly choose the next direction to go
			direction_index = random.randrange(len(next_index_list))
			next_index = next_index_list[direction_index]

			# knock out walls between this cell and the next cell(s)
			# right
			if next_index[1] == col + 1:
				self.cells[row][col].right_wall = False
				self.cells[row][col + 1].left_wall = False
			# left
			if next_index[1] == col - 1:
				self.cells[row][col].left_wall = False
				self.cells[row][col - 1].right_wall = False
			# down
			if next_index[0] == row + 1:
				self.cells[row][col].bottom_wall = False
				self.cells[row + 1][col].top_wall = False
			# up
			if next_index[0] == row - 1:
				self.cells[row][col].top_wall = False
				self.cells[row - 1][col].bottom_wall = False

			# recursively visit the next cell
			self.break_walls_r(next_index[0], next_index[1])

	def reset_visited(self):
		for row in range(self.num_rows):
			for col in range(self.num_cols):
				self.cells[row][col].visited = False

	def solve(self):
		return self.solve_r(0,0)

	def solve_r(self, row, col):
		self.animate()
		self.cells[row][col].visited = True

		# If at exit
		if row == self.num_rows and col == self.num_cols:
			return True

		target = False
		# left
		if col != 0 and not self.cells[row][col - 1].visited:
			if not self.cells[row][col].left_wall and not self.cells[row][col - 1].right_wall:
				target = (row, col - 1)
		# right
		if col < self.num_cols - 1 and not self.cells[row][col + 1].visited:
			if not self.cells[row][col].right_wall and not self.cells[row][col + 1].left_wall:
				target = (row, col + 1)
		# up
		if row != 0 and not self.cells[row - 1][col].visited:
			if not self.cells[row][col].top_wall and not self.cells[row - 1][col].bottom_wall:
				target = (row - 1, col)
		# down
		if row < self.num_rows - 1 and not self.cells[row + 1][col].visited:
			if not self.cells[row][col].bottom_wall and not self.cells[row + 1][col].top_wall:
				target = (row + 1, col)

		if target:
			if self.win is None:
				return

			self.win.draw_move(self.cells[row][col], self.cells[target[0]][target[1]])

			if self.solve_r(target[0], target[1]):
				return True
			else:
				self.animate()
		else:
			return False


	def animate(self):
		if self.win is None:
			return
		self.win.redraw()
		time.sleep(0.05)
