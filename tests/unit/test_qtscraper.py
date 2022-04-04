from qtpy.QtWidgets import QApplication

from qtgallery.qtscraper import reset_qapp


def test_reset_qapp():
    app = QApplication([])
    reset_qapp(None, None)
    assert QApplication.instance() is None

    app = QApplication([])
    assert app.exec_() is None
