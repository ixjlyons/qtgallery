import qtpy
from qtpy.QtWidgets import QApplication
from sphinx_gallery import scrapers

from qtgallery.utils import logger


logger.info("Qt api: %s", qtpy.API_NAME)


def qtscraper(block, block_vars, gallery_conf):
    """Basic implementation of a Qt window scraper.

    Looks for any non-hidden windows in the current application instance and
    uses ``grab`` to render an image of the window. The window is closed
    afterward, so you have to call ``show()`` again to render it in a
    subsequent cell.

    ``processEvents`` is called twice with a delay between in case events still need to
    propagate.

    Intended for use in ``image_scrappers`` in the sphinx-gallery configuration.
    """
    imgpath_iter = block_vars["image_path_iterator"]

    app = QApplication.instance() or QApplication([])

    app.processEvents()

    windows = (
        window for window in QApplication.topLevelWindows() if window.isVisible()
    )

    rendered_imgs = []
    for window, imgpath in zip(windows, imgpath_iter):
        logger.info(
            "QWindow information: objectName='%s', className='%s'",
            window.objectName(),
            window.metaObject().className(),
        )
        wid = window.winId()
        screen = window.screen()
        pixmap = screen.grabWindow(wid)
        if not pixmap.save(imgpath):
            logger.warning("Failed to save image: %s", imgpath)
        window.close()
        rendered_imgs.append(imgpath)

    return scrapers.figure_rst(rendered_imgs, gallery_conf["src_dir"])


def reset_qapp(gallery_conf, fname):
    """Shutdown an existing QApplication and disable ``exec_``.

    Disabling ``QApplication.exec_`` means your example scripts can run the Qt event
    loop (so the scripts work when run normally) without blocking example execution by
    sphinx-gallery.

    Intended for use in ``reset_modules`` in the sphinx-gallery configuration.
    """
    app = QApplication.instance()

    if app is not None:
        if qtpy.API_NAME in ("PySide2", "PySide6"):
            app.shutdown()
        elif qtpy.API_NAME in ("PyQt5", "PyQt6"):
            from qtpy import sip

            sip.delete(app)

    QApplication.exec = QApplication.exec_ = lambda _: None
