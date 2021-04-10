from sphinx_gallery import scrapers
from qtpy.QtWidgets import QApplication

__all__ = ['qtscraper', 'reset_qapp']


def qtscraper(block, block_vars, gallery_conf):
    """Basic implementation of a Qt window scraper.

    Looks for any non-hidden windows in the current application instance and
    uses ``grab`` to render an image of the window. The window is closed
    afterward, so you have to call ``show()`` again to render it in a
    subsequent cell.

    ``processEvents`` is called once in case events still need to propagate.
    """
    imgpath_iter = block_vars['image_path_iterator']

    app = QApplication.instance()
    if app is None:
        app = QApplication([])
    app.processEvents()

    # get top-level widgets that aren't hidden
    widgets = [w for w in app.topLevelWidgets() if not w.isHidden()]

    rendered_imgs = []
    for widg, imgpath in zip(widgets, imgpath_iter):
        pixmap = widg.grab()
        pixmap.save(imgpath)
        rendered_imgs.append(imgpath)
        widg.close()

    return scrapers.figure_rst(rendered_imgs, gallery_conf['src_dir'])


def reset_qapp(gallery_conf, fname):
    """Shutdown an existing QApplication and disable exec_.

    Disabling ``QApplication.exec_`` means your example scripts can call the
    exec_ (so the scripts work when run normally) without blocking example
    execution by sphinx-gallery.

    With PySide2, it seems to be necessary to destroy the QApplication instance
    between example runs.
    """
    try:
        # pyside-specific
        if qApp:
            qApp.shutdown()
    except NameError:
        pass
    QApplication.exec_ = lambda _: None
