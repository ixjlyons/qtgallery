"""
Basic Example
=============

Basic Qt tutorial.
"""

import sys
from qtpy import QtWidgets

app = QtWidgets.QApplication([])

# %%
# Create a widget, populate it with a layout, then add a label with some text:

w = QtWidgets.QWidget()
w.setFixedSize(300, 200)

layout = QtWidgets.QVBoxLayout(w)
label = QtWidgets.QLabel("Hey there!")
layout.addWidget(label)

# %%
# Show the widget so it's rendered before the next code cell:

w.show()

# %%
# If you have a ``QApplication.exec_()`` call at the end of your example
# scripts (so they can be run as-is from the command line), qtgallery can
# disable execution, preventing an indefinite loop.

app.exec_()
