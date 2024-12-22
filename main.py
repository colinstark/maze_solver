from tkinter import Tk, BOTH, Canvas
from window import Window
from geometries import Line, Point, Cell

def main():
	win = Window(800, 600)

	win.draw_line(Line((20, 100), (75, 300)))
	win.draw_line(Line((600, 200), (400, 64)))
	win.draw_line(Line((400, 80), (700, 200)))
	win.draw_line(Line((400, 80), (700, 200)))

	cell1 = Cell(200, 200, 40)
	cell2 = Cell(300, 200, 40, left_wall=False)
	win.draw_cell(cell1)
	win.draw_cell(cell2)
	win.draw_cell(Cell(400, 200, 40, right_wall=False))
	win.draw_cell(Cell(500, 200, 40, bottom_wall=False))

	win.draw_move(cell1, cell2)

	win.wait_for_close()

main()
