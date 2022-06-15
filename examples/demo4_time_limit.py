"""
Demo 3: Demonstrates runs that take a long time.
You can stop the run and then re-start it,
    and it will pick up where it left.
"""
import time

def adder(x, y):
    time.sleep(x*y/10)
    return {"sum": x+y}

import experiments_csv, logging
ex = experiments_csv.Experiment("results/", "demo4.csv", backup_folder="results/backups")
ex.logger.setLevel(logging.DEBUG)
# ex.clear_previous_results()

input_ranges = {
    "x": [1,2,3],
    "y": [4,5,6],
}
ex.run_with_time_limit(adder, input_ranges, time_limit=0.9)
