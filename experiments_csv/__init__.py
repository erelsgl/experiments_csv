import pathlib
HERE = pathlib.Path(__file__).parent
__version__ = (HERE / "VERSION").read_text().strip()

from experiments_csv.Experiment import Experiment, logger
from experiments_csv.plot_results import plot_results
