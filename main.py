from PyQt5.QtWidgets import QApplication
from Xlib.ext.xtest import fake_input
import Xlib.display
import Xlib.X
import sys

from grid import Grid

display = Xlib.display.Display()
root = display.screen().root

def get_active_window():
	windowID = root.get_full_property(display.intern_atom('_NET_ACTIVE_WINDOW'), Xlib.X.AnyPropertyType).value[0]
	window = display.create_resource_object('window', windowID)

	parent = window
	while window.id != root.id:
		window, parent = window.query_tree().parent, window
	return parent

def mouse_move(xpos, ypos):
	root.warp_pointer(xpos, ypos)

def mouse_click(window, mouse_button):
	old_focus = display.get_input_focus()

	#display.set_input_focus(window, Xlib.X.RevertToPointerRoot, Xlib.X.CurrentTime)
	#display.sync()

	fake_input(display, Xlib.X.ButtonPress, mouse_button)
	display.sync()
	fake_input(display, Xlib.X.ButtonRelease, mouse_button)
	display.sync()

	#display.set_input_focus(old_focus.focus, Xlib.X.RevertToPointerRoot, Xlib.X.CurrentTime)
	#display.sync()


def main():
	window = get_active_window()
	geometry = window.get_geometry()

	app = QApplication(sys.argv)
	grid = Grid(geometry)
	exit_code = app.exec_()

	if grid.click_type:
		dx, dy = grid.click_pos()
		mouse_move(geometry.x + dx, geometry.y + dy)
		mouse_click(window, grid.click_type)

	sys.exit(exit_code)

if __name__ == '__main__':
	main()
