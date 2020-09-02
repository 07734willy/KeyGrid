from PyQt5.QtGui import QPainter, QPen
from PyQt5.QtWidgets import QMainWindow, QWidget, QApplication
from PyQt5.QtCore import Qt, QEvent



class Overlay(QMainWindow, QWidget):

	def __init__(self, geometry, handler):
		super().__init__()
		self.lines = []
		self.handler = handler

		self.setFocus()
		self.installEventFilter(self)
		self.init_ui(geometry)

	def init_ui(self, geometry):
		self.setWindowFlags(Qt.FramelessWindowHint)
		self.setGeometry(geometry.x, geometry.y, geometry.width, geometry.height)
		self.setStyleSheet("background:transparent")
		self.setAttribute(Qt.WA_TranslucentBackground)
		self.show()

	def eventFilter(self, source, event):
		if event.type() == QEvent.WindowDeactivate:
			self.exit()
		return super().eventFilter(source, event)

	def keyPressEvent(self, event):
		key = event.key()
		modifiers = QApplication.keyboardModifiers()
		self.handler(key, modifiers)

	def exit(self):
		self.close()

	def paintEvent(self, e):
		qp = QPainter()
		qp.begin(self)
		self.draw_lines(qp)
		qp.end()

	def set_gridlines(self, gridlines):
		self.gridlines = list(gridlines)

	def draw_lines(self, qp):
		pen = QPen(Qt.blue, 2, Qt.SolidLine)
		qp.setPen(pen)

		for line in self.gridlines:
			pen.setStyle(line.style)
			pen.setWidth(line.width)
			pen.setColor(line.color)

			qp.setPen(pen)
			qp.drawLine(line.x1, line.y1, line.x2, line.y2)
