import time

from qtpy.QtWidgets import QApplication

from qtgallery.qtscraper import reset_qapp


def test_reset_qapp():
    app = QApplication([])
    reset_qapp(None, None)
    assert QApplication.instance() is None

    t0 = time.perf_counter_ns()
    ret = app.exec_()
    assert (time.perf_counter_ns() - t0) < 30000
    ret is None
