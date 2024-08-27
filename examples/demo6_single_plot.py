"""
Demo 6: plotting experiment results.

To use, install as:

   pip install experiments_csv[plotting]
"""

from experiments_csv import *
from matplotlib import pyplot as plt

# single_plot_results("../examples/results/demo1.csv", filter={"z": 6}, x_field="x", y_field="sum", z_field="y")
#     # Should show two parallel straight lines.

# single_plot_results("../examples/results/demo1.csv", filter={"z": 6}, x_field="x", y_field="sum", z_field="y", mean=False)
#     # Should show a scatter-plot with six points.

# single_plot_results("../examples/results/demo1.csv", filter={}, x_field="x", y_field="sum", z_field=["y","z"])
#     # Should show four parallel straight lines.

# single_plot_results("../examples/results/demo4.csv", filter={}, x_field="x", y_field="runtime", z_field="y")
#     # Should show two straight lines.

# single_plot_results("../examples/results/demo4.csv", filter={}, x_field="x", y_field="runtime", z_field="y", save_to_file="../examples/results/demo4.png")
#     # Should save the last plot to file "results/demo4.png"

single_plot_results("../examples/results/demo5.csv", filter={"y": [5,10,15]}, x_field="x", y_field="sum", z_field="y", save_to_file="../examples/results/demo5a.png", mean=True)
    
single_plot_results("../examples/results/demo5.csv", filter={"y": [5,10,15]}, x_field="x", y_field="sum", z_field="y", save_to_file="../examples/results/demo5b.png", mean=False)
