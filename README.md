# KeyGrid
Use your keyboard as your mouse by selecting grid cells that contain the item you wish to click


Execute the main.py file to run the program-  it will create a 9x9 grid of cells over the current active window. You can then use the keys on your keyboard to select the cell you wish to click in. Q->R and Y->P (top row minus 'T') select along the vertical axis, while the keys below them (on a QWERTY keyboard) select along the horizonal axis. The grid will recurse into the selected cell, until you feel the the center of the middle-most cell is over the area you wish to click. You can then press [enter] to left click, or [shift]+[enter] to right click. The program will exit immediately.

This program mainly serves to eliminate the need for a mouse in those circumstances where you must interact with some GUI application for a short period of time. With practice, the key->cell mapping can become muscle memory, and it can take just a few keystrokes to pinpoint the element you wish to click on.

### Requirements

This project relies on the Xlib and PyQt5 modules, in addition to Python 3.x.
