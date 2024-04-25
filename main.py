import medical_data_visualizer
from unittest import main

# Testeo de las funciones
medical_data_visualizer.draw_cat_plot()
medical_data_visualizer.draw_heat_map()

# Correr los test unitarios
main(module='test_module', exit=False)