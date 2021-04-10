from pyvirtualdisplay import Display
from qtgallery.qtscraper import reset_qapp

disp = None


def start_display(app, config):
    global disp
    disp = Display(backend="xvfb", size=(800, 600))
    disp.start()


def stop_display(app, exception):
    # seems to be necessary to avoid "fatal IO error on X server..."
    reset_qapp(None, None)

    if disp is not None:
        disp.stop()


def setup(app):
    app.connect("config-inited", start_display)
    app.connect("build-finished", stop_display)

    return {"version": "0.1"}
