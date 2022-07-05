"""
Demo 5: plotting experiment results.
"""

from experiments_csv import *
from matplotlib import pyplot as plt

single_plot_results("../examples/results/demo1.csv", filter={"z": 6}, x_field="x", y_field="sum", z_field="y")
plt.show()
    # Should show two parallel straight lines.

single_plot_results("../examples/results/demo1.csv", filter={"z": 6}, x_field="x", y_field="sum", z_field="y", mean=False)
plt.show()
    # Should show a scatter-plot with six points.

single_plot_results("../examples/results/demo1.csv", filter={}, x_field="x", y_field="sum", z_field=["y","z"])
plt.show()
    # Should show four parallel straight lines.

single_plot_results("../examples/results/demo4.csv", filter={}, x_field="x", y_field="runtime", z_field="y")
plt.show()
    # Should show two straight lines.
