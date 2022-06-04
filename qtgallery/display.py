import os
import os.path

from pyvirtualdisplay import Display

from qtgallery.qtscraper import reset_qapp
from qtgallery.utils import logger


def xvfb_is_available():
    return any(
        os.access(os.path.join(path, "Xvfb"), os.X_OK)
        for path in os.environ["PATH"].split(os.pathsep)
    )


class XVFB:
    def __init__(self):
        self._virtual_display = None

    def start_display(self, size, color_depth, use_xauth, extra_args):
        if not xvfb_is_available():
            logger.warning("Could not find Xvfb")
            return
        logger.info(
            "xvfb parameters: size=%s, color_depth: %s, use_xauth:%s, extra_args:%s",
            size,
            color_depth,
            use_xauth,
            extra_args,
        )
        self._virtual_display = Display(
            backend="xvfb",
            size=size,
            color_depth=color_depth,
            use_xauth=use_xauth,
            extra_args=extra_args,
        )
        self._virtual_display.start()
        if self._virtual_display.is_alive():
            logger.info("Started Xvfb")
        else:
            logger.warning("Failed Xvfb")

    def stop_display(self):
        # seems to be necessary to avoid "fatal IO error on X server..."
        reset_qapp(None, None)

        if self._virtual_display is not None and self._virtual_display.is_alive():
            self._virtual_display.stop()
            logger.info("Stopped Xvfb")


xvfb = XVFB()
