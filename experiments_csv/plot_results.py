import pandas
from matplotlib import pyplot as plt
from experiments_csv.dict_to_row import dict_to_rows
# from typing import List

import logging
logger = logging.getLogger(__name__)

def plot_dataframe(ax, results: pandas.DataFrame,
    x_field:str, y_field:str, z_field:str, mean:bool=True, 
    legend_properties={'size':8}):
    """
    Plot on the given axis, results from the given pandas dataframe.

    :param ax      a matplotlib axis to plot on.
    :param results  a DataFrame containing the results to show.

    :param x_field: name of column for x axis.
    :param y_field: name of column for y axis.
    :param z_field: name of column for different lines in the same plot (for each value of this column, there will be a different line).
    :param mean: if True, it makes a line-plot of the mean over all rows with the same xcolumn and zcolumn. If False, it makes a scatter-plot of all values.

    :param legend_properties: delegated to the legend-drawing function.
    """
    if isinstance(z_field, list):
        z_field_join = ",".join(z_field)
        results[z_field_join] = results[z_field].apply(lambda x: ",".join(map(str,x)), axis=1)
        z_field=z_field_join
    
    z_values = results[z_field].unique()
    z_values.sort()
    for z_value in z_values:
        logger.info("    Line: %s=%s",z_field, z_value)
        results_for_z_value = results[results[z_field]==z_value]
        # label = z_value
        label = f"{z_field}={z_value}"
        if mean:
            mean_results_for_z_value = results_for_z_value.groupby([x_field]).mean()
            ax.plot(mean_results_for_z_value.index, mean_results_for_z_value[y_field], label=label)
        else:
            ax.scatter(results_for_z_value[x_field], results_for_z_value[y_field], label=label)
        ax.legend(prop=legend_properties)


def single_plot_results(results_csv_file:str, filter:dict, 
    x_field:str, y_field:str, z_field:str, mean:bool=True, 
    save_to_file:bool=False,
    **kwargs):
    """
    Make a single plot of results from the given file.

    :param results_csv_file  path to the CSV file containing the results.
    :param filter: a dict used to filter the rows of the results file. See dict_to_row.

    :param x_field: name of column for x axis.
    :param y_field: name of column for y axis.
    :param z_field: name of column for different lines in the same plot (for each value of this column, there will be a different line).
    :param mean: if True, it makes a line-plot of the mean over all rows with the same xcolumn and zcolumn. If False, it makes a scatter-plot of all values.
    :param save_to_file: if True, it saves the plot to a PNG file with the same name as the results_csv_file. If False, it just shows the plot.

    :param kwargs: arguments to delegate to plot_dataframe.
    """
    results = pandas.read_csv(results_csv_file)
    results = dict_to_rows(results, filter)
    if len(filter)>0:
        title = ", ".join([f"{key}={value}" for key,value in filter.items()])
    else:
        title = "All results"
    logger.info("Plot: %s", title)
    plot_dataframe(plt, results, 
        x_field, y_field, z_field, mean, 
        **kwargs)

    plt.xlabel(x_field)
    ylabel = f"mean {y_field}" if mean else y_field
    plt.ylabel(ylabel)
    plt.title(title)

    if save_to_file:
        output_file = results_csv_file.replace(".csv",".png")
        plt.savefig(output_file)
    else:
        plt.show()




def multi_plot_results(results_csv_file:str, filter:dict,
    x_field:str, y_field:str, z_field:str, mean:bool, 
    subplot_field:str, subplot_rows:int, subplot_cols:int, 
    sharex: bool=False, sharey: bool=False,
    save_to_file:bool=False,
    **kwargs):
    """
    Make multiple plots (on subplots of the same figure), each time with a different value of the subplot_field column.

    :param results_csv_file  path to the CSV file containing the results.
    :param filter: a dict used to filter the rows of the results file. See dict_to_row.

    :param x_field: name of column for x axis.
    :param y_field: name of column for y axis.
    :param z_field: name of column for different lines in the same plot (for each value of this column, there will be a different line).
    :param mean: if True, it makes a line-plot of the mean over all rows with the same xcolumn and zcolumn. If False, it makes a scatter-plot of all values.

    :param subplot_field: name of column for different subplots (for each value of this column, there will be a different subplot).
    :param subplot_rows: num of rows in the subplots grid
    :param subplot_cols: num of cols in the subplots grid
    :param sharex: whether to share the x axis between subplots.
    :param sharey: whether to share the y axis between subplots.
    :param save_to_file: if True, it saves the plot to a PNG file with the same name as the results_csv_file. If False, it just shows the plot.

    :param kwargs: arguments to delegate to plot_dataframe.
    """
    results = pandas.read_csv(results_csv_file)
    results = dict_to_rows(results, filter)
    if len(filter)>0:
        suptitle = ", ".join([f"{key}={value}" for key,value in filter.items()])
    else:
        suptitle = "All results"
    logger.info("Plot: %s", suptitle)

    if isinstance(subplot_field, list):
        subplot_field_join = ",".join(subplot_field)
        results[subplot_field_join] = results[subplot_field].apply(lambda x: ",".join(map(str,x)), axis=1)
        subplot_field=subplot_field_join
    subplot_values = results[subplot_field].unique()
    subplot_values.sort()

    num_of_subpltos = subplot_rows * subplot_cols
    if num_of_subpltos < len(subplot_values):
        raise ValueError(f"Not enough subplots! {subplot_rows}*{subplot_cols} < len({subplot_values})")

    fig, axs = plt.subplots(subplot_rows, subplot_cols, sharex=sharex, sharey=sharey)
    axs = axs.flatten()
    axs_index = 0
    for subplot_value in subplot_values:
        subtitle = f"{subplot_field}={subplot_value}"
        logger.info("  Subplot: %s",subtitle)
        results_for_subplot_value = results[results[subplot_field]==subplot_value]
        plot_dataframe(axs[axs_index], results_for_subplot_value, 
            x_field, y_field, z_field, mean, 
            **kwargs)
        axs[axs_index].set_title(subtitle)
        axs_index += 1

    fig.supxlabel(x_field)
    ylabel = f"mean {y_field}" if mean else y_field
    fig.supylabel(ylabel)
    fig.suptitle(suptitle)

    if save_to_file:
        output_file = results_csv_file.replace(".csv",".png")
        fig.savefig(output_file)
    else:
        plt.show()


plot_dataframe.logger = single_plot_results.logger = multi_plot_results.logger = logger
logger.setLevel(logging.INFO)
logger.addHandler(logging.StreamHandler())
