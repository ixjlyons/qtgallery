# -*- coding: utf-8 -*-
"""
PyQtGraph ImageItem
===================

Simple ImageItem example.

This example demonstrates use of ImageItem to display image data inside a ViewBox. The
image is dynamically updated via a timer and callback function.
"""

from qtpy import QtCore
import numpy as np
import pyqtgraph as pg

app = pg.mkQApp("ImageItem Example")

# %%
# Create a window via GraphicsLayoutWidget. This is a convenient way to create a window
# and add GraphicsItem objects in a grid layout.

win = pg.GraphicsLayoutWidget()
win.setWindowTitle("pyqtgraph example: ImageItem")

# %%
# Add a ViewBox to which we'll add the ImageItem. We'll also lock the aspect ratio of
# the ViewBox so that the image's pixels are always square.

vb = win.addViewBox()
vb.setAspectLocked(True)

# %%
# Create the ImageItem and add it to the ViewBox

img = pg.ImageItem(border="w")
vb.addItem(img)

# %%
# Create a stack of images from random samples.

data = np.random.normal(size=(15, 600, 600), loc=1024, scale=64).astype(np.uint16)


# %%
# Initialize a QTimer to call our callback function (below).

i = 0
timer = QtCore.QTimer()
timer.setSingleShot(True)

# %%
# Here is our callback function called by the timer. It cycles through the stack of
# images, updates the ImageItem data, and restarts the timer.


def updateData():
    global img, data, i

    img.setImage(data[i])

    i = (i + 1) % data.shape[0]
    timer.start(1)


# %%
# Connect the timer to the callback and call the callback manually once to initialize.

timer.timeout.connect(updateData)
updateData()

# %%
# Finally, show the window and run the application.

win.show()

# %%

if __name__ == "__main__":
    pg.mkQApp().exec_()
