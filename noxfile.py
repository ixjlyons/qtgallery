import nox
import sys

nox.options.sessions = ["test"]


@nox.session(reuse_venv=True)
@nox.parametrize("qt_api", ["pyside2", "pyside6", "pyqt5", "pyqt6"])
def test(session, qt_api):
    py_version = sys.version_info[:2]
    # https://bugreports.qt.io/browse/PYSIDE-1797
    if qt_api == "pyside2" and py_version == (3, 11):
        session.skip()
    # https://forum.qt.io/topic/144843/pyside2-shiboken2-support-for-python-3-11
    if qt_api == "pyside6" and py_version == (3, 7):
        session.skip()

    session.install(".[docs]", "pytest", "pytest-xvfb", qt_api)

    env = {"QT_API": qt_api}
    session.run("pytest", "tests/functional", "--no-xvfb", *session.posargs, env=env)
    session.run("pytest", "tests/unit", *session.posargs, env=env)
