from tkinter import Tk, BOTH, Canvas

class Window:
	def __init__(self, width, height):
		self.width = width
		self.height = height
		self.root = Tk(screenName="Yolo")
		self.root.geometry(f"{self.width}x{self.height}")
		self.canvas = Canvas(self.root, bg="white", width=width, height=height)
		self.running = False

	def redraw(self):
		self.root.update_idletasks()
		self.canvas.pack()
		self.root.update()

	def wait_for_close(self):
		self.running = True
		while self.running:
			self.redraw()

	def close(self):
		self.running = False
		self.root.protocol("WM_DELETE_WINDOW", self.close)

	def draw_line(self, line, fill="black"):
		line.draw(self.canvas, fill)

	def draw_cell(self, cell, fill="black"):
		cell.draw(self.canvas, fill)

	def draw_move(self, cell, cell2, undo=False):
		cell.draw_move(self.canvas, cell2, undo)
