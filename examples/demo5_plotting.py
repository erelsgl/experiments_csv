"""
Demo 5: plotting experiment results.
"""

import logging
from experiments_csv import plot_results

plot_results.logger.setLevel(logging.INFO)
plot_results.logger.addHandler(logging.StreamHandler())
from matplotlib import pyplot as plt

plot_results(plt, "../examples/results/demo1.csv", filter={"z": 6}, xcolumn="x", ycolumn="sum", zcolumn="y")
    # Should show two parallel straight lines.
plot_results(plt, "../examples/results/demo1.csv", filter={"z": 6}, xcolumn="x", ycolumn="sum", zcolumn="y", mean=False)
    # Should show a scatter-plot with six points.
plot_results(plt, "../examples/results/demo1.csv", filter={}, xcolumn="x", ycolumn="sum", zcolumn=["y","z"])
    # Should show four parallel straight lines.
plot_results(plt, "../examples/results/demo4.csv", filter={}, xcolumn="x", ycolumn="runtime", zcolumn="y")
    # Should show two straight lines.
