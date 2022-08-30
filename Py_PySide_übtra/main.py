# File: main.py
import sys
from PySide6.QtUiTools import QUiLoader
from PySide6.QtWidgets import QApplication, QWidget
from PySide6.QtCore import QFile, QIODevice

class Example(QWidget):
    def __init__(self):
        super(Example, self).__init__()
      #  ui_file.
      #  self.button = ui_file.QPushButton(u"Drück mich.", self)
      #  self.button.clicked.connect(foobar)
        self.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)

    ui_file_name = "mainwindow.ui"
    ui_file = QFile(ui_file_name)
    if not ui_file.open(QIODevice.ReadOnly):
        print(f"Cannot open {ui_file_name}: {ui_file.errorString()}")
        sys.exit(-1)
    loader = QUiLoader()
    window = loader.load(ui_file)
    ui_file.close()
    if not window:
        print(loader.errorString())
        sys.exit(-1)
    window.show()
    #PySide6.QtWidgets.QPushButton("Download", self)

    sys.exit(app.exec())
