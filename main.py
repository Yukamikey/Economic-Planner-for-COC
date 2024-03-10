from coc_modules import  coc_econ_module as econ
from coc_modules.coc_goods_module import Good
from ui import *
from PyQt5 import uic
from PyQt5.QtWidgets import *
import os

ui_path = os.path.abspath("ui/econ_planner_ui.ui")
print(ui_path)
my_cycle_manager = econ.CycleManager([])

class MyGui(QMainWindow):

    def __init__(self):
        super(MyGui, self).__init__()
        uic.loadUi(os.path.abspath("ui/econ_planner_ui.ui"), self)
        self.show()

        self.StartCycleButton.clicked.connect(self.ui_start_cycle)
        self.EndCycleButton.clicked.connect(self.ui_end_cycle)
        self.AddGoodButton.clicked.connect(self.ui_add_good)
        self.ProduceGoodButton.clicked.connect(self.ui_produce_good)
        self.CalculateGDP_Button.clicked.connect(self.ui_calc_gdp)

    def ui_start_cycle(self):
        my_cycle_manager.start_cycle()
        self.EndCycleButton.setEnabled(True)
        self.AddGoodButton.setEnabled(True)
        self.ProduceGoodButton.setEnabled(True)
        self.CalculateGDP_Button.setEnabled(True)
        self.GoodNameInput.setEnabled(True)
        self.GoodPriceInput.setEnabled(True)
        self.NumToProduceSpin.setEnabled(True)
        #self.GoodsProducedTable.setEnabled(True)
        #self.CopyToTableButton.setEnabled(True)
        self.StartCycleButton.setEnabled(False)

    def ui_end_cycle(self):
        my_cycle_manager.end_cycle()
        self.EndCycleButton.setEnabled(False)
        self.AddGoodButton.setEnabled(False)
        self.ProduceGoodButton.setEnabled(False)
        self.CalculateGDP_Button.setEnabled(False)
        self.GoodNameInput.setEnabled(False)
        self.GoodPriceInput.setEnabled(False)
        self.NumToProduceSpin.setEnabled(False)
        #self.GoodsProducedTable.setEnabled(False)
        #self.CopyToTableButton.setEnabled(False)
        self.StartCycleButton.setEnabled(True)

    def ui_add_good(self):
        my_good = Good(self.GoodNameInput.text(), float(self.GoodPriceInput.text()), 1)
        my_cycle_manager.add_good(my_good)

    def ui_produce_good(self):
        good_to_produce = self.GoodNameInput.text()
        stacks = self.NumToProduceSpin.value()

        my_cycle_manager.produce_good(good_to_produce, stacks)

    def ui_calc_gdp(self):
        my_cycle_manager.get_gdp()
        self.GDP.setText(str(my_cycle_manager.current_cycle.gdp.value))

    #def copy_to_table(self):
        #for goods in my_cycle_manager.current_cycle.goods_produced:



def main():
    app = QApplication([])
    window = MyGui()
    app.exec()

if __name__ == "__main__":
    main()
