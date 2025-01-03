from tkinter import Tk, BOTH, Canvas

class Point:
	def __init__(self, x=0, y=0):
		self.x = x
		self.y = y

class Line:
	def __init__(self, p1, p2):
		self.p1 = p1
		self.p2 = p2

	def draw(self, canvas, fill_color):
		canvas.create_line (
			self.p1[0], self.p1[1], self.p2[0], self.p2[1], fill=fill_color, width=2
		)

class Cell:
	def __init__(self, x1, y1, size, top_wall=True, right_wall=True, bottom_wall=True, left_wall=True):
		self.x1 = x1
		self.x2 = self.x1 + size
		self.y1 = y1
		self.y2 = self.y1 + size
		self.center = (x1 + (size/2), y1 + (size/2))
		self.top_wall = top_wall
		self.right_wall = right_wall
		self.bottom_wall = bottom_wall
		self.left_wall = left_wall
		self.visited = False

	def __repr__(self) -> str:
		return f"Cell: (x1: {self.x1}, x2: {self.x2}, y1: {self.y1}, y2: {self.y2}), top:{self.top_wall}, right:{self.right_wall}, bottom:{self.bottom_wall}, left:{self.left_wall}\n"

	def draw(self, canvas, fill_color):
		canvas.create_line (self.x1, self.y1, self.x2, self.y1, fill="white", width=2)
		canvas.create_line (self.x2, self.y1, self.x2, self.y2, fill="white", width=2)
		canvas.create_line (self.x1, self.y2, self.x2, self.y2, fill="white", width=2)
		canvas.create_line (self.x1, self.y1, self.x1, self.y2, fill="white", width=2)
		
		if self.visited:
			canvas.create_rectangle (
				self.x1, self.y1, self.x2, self.y1, fill="grey"
			)

		if self.top_wall:
			canvas.create_line (
				self.x1, self.y1, self.x2, self.y1, fill=fill_color, width=2
			)
		if self.right_wall:
			canvas.create_line (
				self.x2, self.y1, self.x2, self.y2, fill=fill_color, width=2
			)
		if self.bottom_wall:
			canvas.create_line (
				self.x1, self.y2, self.x2, self.y2, fill=fill_color, width=2
			)
		if self.left_wall:
			canvas.create_line (
				self.x1, self.y1, self.x1, self.y2, fill=fill_color, width=2
			)

	def draw_move(self, canvas, to_cell, undo=False):
		fill_color = "red"
		if(undo):
			color = "grey"
		canvas.create_line (
			self.center[0], self.center[1], to_cell.center[0], to_cell.center[1], fill=fill_color, width=2
		)
