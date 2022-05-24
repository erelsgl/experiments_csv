from experiments import Experiment
import logging

Experiment.logger.setLevel(logging.DEBUG)
Experiment.logger.addHandler(logging.StreamHandler())

ex = Experiment("results/", "results.csv", "results/backup")

def add_three_numbers(x, y, z):
    return {"sum": (x+y+z)}

input_ranges = {
    "x": [1,2,3],
    "y": [4,5,6,7],
    "z": [6,7,8]
}
ex.run(add_three_numbers, input_ranges)
