"""
QML Example
===========
"""

import os
import sys

from qtpy import QtCore, QtWidgets, QtQml

app = QtWidgets.QApplication([])

# %%
# Set up some QtQuick styling

os.environ["QT_QUICK_CONTROLS_STYLE"] = "Material"
os.environ["QT_QUICK_CONTROLS_MATERIAL_THEME"] = "Dark"

# %%
# For simplicity, we put the QML in a string rather than a file

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
# Load the application. If using a ``.qml`` file instead, you can use ``engine.load``

engine = QtQml.QQmlApplicationEngine()
engine.loadData(qml)

app.exec_()
