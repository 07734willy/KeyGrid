from abc import ABC, abstractmethod
from PyQt5.QtGui import QColor
from PyQt5.QtCore import Qt

class Line(ABC):

	color = None
	width = None
	style = None
	
	def __init__(self, x1, y1, x2, y2):
		self.x1 = x1
		self.y1 = y1
		
		self.x2 = x2
		self.y2 = y2


class MinorLine(Line):
	color = QColor(70, 30, 30)
	width = 2
	style = Qt.DotLine


class MajorLine(Line):
	color = QColor(150, 30, 30)
	width = 3
	style = Qt.DashLine
