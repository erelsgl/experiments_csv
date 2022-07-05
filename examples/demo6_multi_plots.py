"""
Demo 6: plotting experiment results; multiple subplots.
"""

from experiments_csv import *
from matplotlib import pyplot as plt

multi_plot_results("../examples/results/demo1.csv", filter={}, subplot_field="z", subplot_rows=2, subplot_cols=2,
    x_field="x", y_field="sum", z_field="y", mean=True)
plt.show()
    # Should show two-by-two subplots.

multi_plot_results("../examples/results/demo1.csv", filter={}, subplot_field="z", subplot_rows=2, subplot_cols=2,
    x_field="x", y_field="sum", z_field="y", sharex=True, sharey=True, mean=True)
plt.show()
    # Should show two-by-two subplots.
