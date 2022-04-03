"""
QML Basic Example
=================
Basic Qt tutorial.
"""
import os
import sys

from qtpy import QtCore
from qtpy import QtWidgets
from qtpy import QtQml

app = QtWidgets.QApplication([])

os.environ["QT_QUICK_CONTROLS_STYLE"] = "Material"
os.environ["QT_QUICK_CONTROLS_MATERIAL_THEME"] = "Dark"
# %%
# Create a widget, populate it with a layout, then add a label with some text:
qml = b"""
import QtQuick 2.15
import QtQuick.Controls 2.15

ApplicationWindow {
    id: root
    visible: true
    width: 640
    height: 480
    title: qsTr("QtGallery")

    Button {
        text: qsTr("Qt is awesome!!!")
        anchors.centerIn: parent
    }
}
"""

# %%
# Show the widget so it'll render right after this text:
engine = QtQml.QQmlApplicationEngine()
engine.loadData(qml)
# %%
# If you have a ``QApplication.exec_()`` call at the end of your example script
# (so it can be run as-is from the command line), ``qtgallery`` disables
# the Qt event loop execution to prevent an indefinite loop.

if __name__ == "__main__":
    app.exec_()
