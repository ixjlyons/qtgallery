"""
Iterative Example
=================

Example that tests out showing a wiget more than once in an iterative tutorial
style.
"""

from qtpy import QtWidgets

app = QtWidgets.QApplication([])

# %%
# We start by constructing the View and Scene.

scene = QtWidgets.QGraphicsScene()
view = QtWidgets.QGraphicsView(scene)
view.setFixedSize(300, 200)

# %%
# Add an item to the scene. Default position is centered.

text = scene.addText("hey there!")
view.show()

# %%
# Move the text.

text.moveBy(0, 80)
view.show()

# %%

app.exec_()
