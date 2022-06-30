import pandas
import matplotlib as plt
from experiments_csv.dict_to_row import dict_to_rows

import logging
logger = logging.getLogger(__name__)

def plot_results(ax, results_csv_file:str, filter:dict, xcolumn:str, ycolumn:str, zcolumn:str):
    """
    Plot on the given axis, results from the given file.

    :param filter: a dict used to filter the rows of the results file. See dict_to_row.
    :param xcolumn: name of column for x axis.
    :param ycolumn: name of column for y axis.
    :param zcolumn: name of column for z axis (for each value of z, there will be a different plot).
    """
    results = pandas.read_csv(results_csv_file)
    results = dict_to_rows(results, filter)
    if len(filter)>0:
        title = ", ".join([f"Plots results with {key}={value}" for key,value in filter.items()])
    else:
        title = "Plotting all results"
    logger.info(title)
    zvalues = results[zcolumn].unique()
    zvalues.sort()
    for zvalue in zvalues:
        label = f"{zcolumn}={zvalue}"
        logger.info("  Plotting %s",label)
        results_for_zvalue = results[results[zcolumn]==zvalue]
        ax.plot(results_for_zvalue[xcolumn], results_for_zvalue[ycolumn], label=label)
        ax.legend()

    ax.xlabel(xcolumn)
    ax.ylabel(ycolumn)
    ax.title(title)
    ax.show()

plot_results.logger = logger

if __name__ == "__main__":
    logger.setLevel(logging.INFO)
    logger.addHandler(logging.StreamHandler())
    from matplotlib import pyplot as plt
    plot_results(plt, "../examples/results/demo1.csv", filter={"z": 6}, xcolumn="x", ycolumn="sum", zcolumn="y")
        # Should show two parallel straight lines.
    plot_results(plt, "../examples/results/demo4.csv", filter={}, xcolumn="x", ycolumn="runtime", zcolumn="y")
        # Should show two straight lines.

