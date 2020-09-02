from itertools import count
from PyQt5.QtCore import Qt

from lines import MinorLine, MajorLine
from overlay import Overlay

KEY_MAP = {
	Qt.Key_Q: (None, -4), Qt.Key_W: (None, -3), Qt.Key_E: (None, -2), Qt.Key_R: (None, -1), 
	Qt.Key_Y: (None,  0), Qt.Key_U: (None,  1), Qt.Key_I: (None,  2), Qt.Key_O: (None,  3), Qt.Key_P: (None,  4), 

	Qt.Key_A: (-4, None), Qt.Key_B: (-3, None), Qt.Key_C: (-2, None), Qt.Key_D: (-1, None), 
	Qt.Key_H: ( 0, None), Qt.Key_J: ( 1, None), Qt.Key_K: ( 2, None), Qt.Key_L: ( 3, None), Qt.Key_Semicolon: ( 4, None), 
}

class Grid(object):
	
	def __init__(self, geometry):
		self.x1 = 0
		self.y1 = 0

		self.x2 = geometry.width - 1
		self.y2 = geometry.height - 1

		
		self.click_type = 0
		
		self.overlay = Overlay(geometry, handler=self.key_event)
		self.update_overlay()

	def key_event(self, key, modifiers):
		if key == Qt.Key_Escape:
			self.exit()

		elif key == Qt.Key_Return:
			if Qt.ShiftModifier & modifiers:
				self.click_type = 3
			else:
				self.click_type = 1
			self.exit()

		elif key in KEY_MAP:
			self.resize(*KEY_MAP[key])
			self.update_overlay()

	def exit(self):
		self.overlay.exit()

	def update_overlay(self):
		gridlines = self.make_gridlines()
		self.overlay.set_gridlines(gridlines)
		self.overlay.update()

	def click_pos(self):
		xpos = int(round((self.x1 + self.x2) / 2))
		ypos = int(round((self.y1 + self.y2) / 2))

		return xpos, ypos
		
	def resize(self, xl, yl):
		dx = (self.x2 - self.x1) / 9
		dy = (self.y2 - self.y1) / 9
		
		xs = [int(round(self.x1 + i*dx)) for i in range(10)]
		ys = [int(round(self.y1 + i*dy)) for i in range(10)]
		
		if xl is not None:
			self.x1 = xs[xl+4]
			self.x2 = xs[xl+5]
		if yl is not None:
			self.y1 = ys[yl+4]
			self.y2 = ys[yl+5]

	def make_gridlines(self):
		dx = (self.x2 - self.x1) / 9
		dy = (self.y2 - self.y1) / 9

		for i in range(8):
			x = int(round(self.x1 + i*dx + dx/2))
			y = int(round(self.y1 + i*dy + dy/2))

			if i in (2, 5):
				yield MajorLine(x, self.y1, x, self.y2)
				yield MajorLine(self.x1, y, self.x2, y)
			else:
				yield MinorLine(x, self.y1, x, self.y2)
				yield MinorLine(self.x1, y, self.x2, y)
		
