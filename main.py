from tkinter import Tk, BOTH, Canvas
from window import Window
from geometries import Line, Point, Cell
from maze import Maze
import time

def main():
	win = Window(800, 600)
	maze = Maze(20, 20, 5, 8, 60, win)
	maze.solve()

	win.wait_for_close()

main()
