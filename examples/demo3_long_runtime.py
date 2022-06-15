"""
Demo 3: Demonstrates runs that take a long time.
You can stop the run and then re-start it,
    and it will pick up where it left.
"""
import time

def algorithm_A(x, y, z):
    time.sleep(1)
    return 2*(x+y+z)

def algorithm_B(x, y, z):
    time.sleep(1)
    return 3*(x+y+z)

def adder(algorithm, x, y, z):
    time.sleep(1)
    return {"sum": algorithm(x,y,z)}


import experiments_csv, logging
ex = experiments_csv.Experiment("results/", "demo3.csv", backup_folder="results/backups")
ex.logger.setLevel(logging.DEBUG)
# ex.clear_previous_results()

input_ranges = {
    "x": [1,2,3],
    "y": [4,5],
    "z": [6],
    "algorithm": [algorithm_A, algorithm_B]
}
ex.run(adder, input_ranges)
