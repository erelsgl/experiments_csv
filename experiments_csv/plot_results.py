import pandas
import matplotlib as plt
from experiments_csv.dict_to_row import dict_to_rows
# from typing import List

import logging
logger = logging.getLogger(__name__)

def plot_results(ax, results_csv_file:str, filter:dict, xcolumn:str, ycolumn:str, zcolumn:str, mean:bool=True):
    """
    Plot on the given axis, results from the given file.

    :param filter: a dict used to filter the rows of the results file. See dict_to_row.
    :param xcolumn: name of column for x axis.
    :param ycolumn: name of column for y axis.
    :param zcolumn: name of column for z axis (for each value of z, there will be a different plot).
    :param mean: if True, it makes a line-plot of the mean over all rows with the same xcolumn and zcolumn. If False, it makes a scatter-plot of all values.
    """
    results = pandas.read_csv(results_csv_file)
    results = dict_to_rows(results, filter)
    if len(filter)>0:
        title = "Plots results with " + ", ".join([f"{key}={value}" for key,value in filter.items()])
    else:
        title = "Plotting all results"
    logger.info(title)

    if isinstance(zcolumn, list):
        zcolumn_join = ",".join(zcolumn)
        results[zcolumn_join] = results[zcolumn].apply(lambda x: ",".join(map(str,x)), axis=1)
        zcolumn=zcolumn_join
    zvalues = results[zcolumn].unique()
    zvalues.sort()
    for zvalue in zvalues:
        label = f"{zcolumn} = {zvalue}"
        logger.info("  Plotting %s",label)
        results_for_zvalue = results[results[zcolumn]==zvalue]
        # print("results_for_zvalue", results_for_zvalue)
        if mean:
            mean_results_for_zvalue = results_for_zvalue.groupby([xcolumn]).mean()
            print("mean_results_for_zvalue", mean_results_for_zvalue)
            ax.plot(mean_results_for_zvalue.index, mean_results_for_zvalue[ycolumn], label=label)
        else:
            ax.scatter(results_for_zvalue[xcolumn], results_for_zvalue[ycolumn], label=label)
        ax.legend()

    ax.xlabel(xcolumn)
    ax.ylabel(f"mean {ycolumn}" if mean else ycolumn)
    ax.title(title)
    ax.show()

plot_results.logger = logger
logger.setLevel(logging.INFO)
logger.addHandler(logging.StreamHandler())
