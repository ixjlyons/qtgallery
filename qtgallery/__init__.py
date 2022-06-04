from qtgallery.qtscraper import qtscraper, reset_qapp
from qtgallery.display import xvfb
from qtgallery._version import __version__


DEFAULT_QTGALLERY_CONF = {
    "xvfb_size": (640, 480),
    "xvfb_color_depth": 24,
    "xfvb_use_xauth": False,
    "xfvb_extra_args": [],
}


def handle_config_inited(app, config):
    conf = app.config.qtgallery_conf.copy()
    for key, value in DEFAULT_QTGALLERY_CONF.items():
        conf.setdefault(key, value)
    xvfb.start_display(
        conf["xvfb_size"],
        conf["xvfb_color_depth"],
        conf["xfvb_use_xauth"],
        conf["xfvb_extra_args"],
    )


def handle_build_finished(app, exception):
    xvfb.stop_display()


def setup(app):
    app.add_config_value("qtgallery_conf", DEFAULT_QTGALLERY_CONF, "html")
    app.connect("config-inited", handle_config_inited)
    app.connect("build-finished", handle_build_finished)

    return {"version": __version__}


__all__ = ["qtscraper", "reset_qapp", "setup"]
