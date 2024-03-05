import sys

from PySide2.QtWidgets import QApplication
from interface import TInterface



if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = TInterface()
    sys.exit(app.exec_())

