from coc_modules.coc_econ_module import *

coal = Good("coal", 5.25, 2)
wool = Good("wool", 7.25, 5)

my_cycle_manager = CycleManager([])
my_cycle_manager.start_cycle()
my_cycle_manager.add_good(coal)
my_cycle_manager.end_cycle()

my_cycle_manager.start_cycle()
my_cycle_manager.add_good(wool)
my_cycle_manager.end_cycle()