import  numpy as np
import csv
from coc_modules.coc_stats_module import *
from coc_modules.coc_goods_module import *
from dictionaries import cycles_dictionary

class GDP:
    def __init__(self, value: float):
        self.value = value

class Cycle:
    """The measurement of an economic period. Similar to a quarter in real life."""
    def __init__(self, goods_produced: list[Good]):
        """Initialises a cycle with a list of goods that were produced during that cycle.

        Instance Variables:
        self.goods_produced is an instance variable made from the parameter goods_produced.
        self.name is simply the name of the cycle.
        self.gdp is the Gross Domestic of a cycle. It's initialised to 0, but can be calculated at a later time"""
        self.goods_produced = goods_produced
        self.name = ""
        self.gdp = GDP(0)

class CycleManager:
    """Manages what happens during a cycle (adding goods, removing goods, etc.)"""
    def __init__(self, cycles:list[Cycle]):
        """Initialises a cycle manager and list of cycles

        Instance Variables:
        self. cycles is the list of cycles parameter as an instance variable.
        self.current_cycle is the cycle the manager is currently managing.
        self.cycle_num is the number of cycles that have occurred with that cycle manager.
        """
        self.cycles = cycles
        self.current_cycle = None
        self.cycle_num = 0


    def start_cycle(self):
        """Instantiates a cycle and appends it to the cycles list. It also sets what the current cycle is and increases the cycle_num by 1. The cycle_name is also declared."""
        my_cycle = Cycle([])
        self.cycles.append(my_cycle)
        my_cycle.name = f"cycle_{self.cycles.index(my_cycle) + 1}"
        if self.current_cycle is None:
            self.current_cycle = my_cycle

        self.cycle_num += 1


    def end_cycle(self):
        self.get_gdp()

        with open(f"{self.current_cycle.name}.csv", "w") as production_sheet:
            writer = csv.writer(production_sheet)
            for goods in self.current_cycle.goods_produced:
                writer.writerow([f"{goods.name}", f"${goods.price}", f"{goods.num_produced}"])
            writer.writerow([f"{self.current_cycle.name} GDP", f"${self.current_cycle.gdp.value}"])

        with open(f"gdp_logs.csv", "a") as gdp_sheet:
            writer = csv.writer(gdp_sheet)
            writer.writerow([f"{self.current_cycle.name} GDP", f"${self.current_cycle.gdp.value}"])

            cycles_dictionary.cycles.update({self.current_cycle.name: self.current_cycle.gdp})
            if self.cycle_num > 1:
                gdp_growth = calc_gdp_growth(cycles_dictionary.cycles[f"{self.current_cycle.name}"],
                                             cycles_dictionary.cycles[f"cycle_{self.cycles.index(self.current_cycle)}"])
                writer.writerow([f"GDP Growth", gdp_growth])


        self.current_cycle = None

    def add_good(self, good_to_add: Good):
        self.current_cycle.goods_produced.append(good_to_add)

    def get_gdp(self):
        calculated_val = calc_gdp(self.current_cycle.goods_produced)
        self.current_cycle.gdp.value = calculated_val

def calc_gdp(goods_produced: list[Good]):
    total = 0
    for goods in goods_produced:
        total += (goods.price * goods.num_produced)

    return total

def calc_gdp_growth(a: GDP, b: GDP):
    gdp_growth = ((a.value/b.value) - 1) * 100
    return gdp_growth

