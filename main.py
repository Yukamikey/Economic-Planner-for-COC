from coc_modules import  *
from ui import *
from PyQt5 import uic
from PyQt5.QtWidgets import *

class MyGui(QMainWindow):

    def __int__(self):
        super(MyGui, self).__init__()
        uic.loadUi("econ_planner_ui.ui", self)
        self.show()
def main():
    app = QApplication([])
    window = MyGui()
    app.exec()

if __name__ == "__main__":
    main()
