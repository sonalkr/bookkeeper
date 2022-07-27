import os
import sys

from PySide6.QtGui import QGuiApplication
from PySide6.QtQml import QQmlApplicationEngine


def view(root_location: str, file_name: str):
    app = QGuiApplication(sys.argv)
    engine = QQmlApplicationEngine()
    engine.load(os.path.join(  # type: ignore
        root_location, file_name))

    if not engine.rootObjects():
        sys.exit(-1)
    sys.exit(app.exec())
