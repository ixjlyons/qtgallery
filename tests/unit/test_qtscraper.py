import time

from qtpy.QtCore import Qt, QTimer
from qtpy.QtWidgets import QApplication

from qtgallery.qtscraper import reset_qapp


def test_reset_qapp():
    app = QApplication([])

    t0 = time.perf_counter()
    timer = QTimer(
        interval=1000, timerType=Qt.TimerType.PreciseTimer, timeout=QApplication.quit
    )
    timer.start()
    ret = app.exec_()
    assert ret == 0
    assert (time.perf_counter() - t0) > 0.9

    reset_qapp(None, None)
    assert QApplication.instance() is None

    t0 = time.perf_counter()
    ret = app.exec_()
    assert (time.perf_counter() - t0) < 0.001
    ret is None
