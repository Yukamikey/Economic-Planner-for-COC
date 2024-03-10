from coc_modules import  *
from ui import *
from PyQt5 import uic
from PyQt5.QtWidgets import *
import os

ui = os.path.abspath("ui")
display = os.path.join(ui, "econ_plannner_ui.ui")
class MyGui(QMainWindow):

    def __init__(self):
        super(MyGui, self).__init__()
        uic.loadUi(display, self)
        self.show()
def main():
    app = QApplication([])
    window = MyGui()
    app.exec()

if __name__ == "__main__":
    main()
