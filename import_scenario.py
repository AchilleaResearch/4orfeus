import pandas as pd

if __name__ == "__main__":
    line2busname_from = pd.read_pickle('scenario_example/from_bus.pickle')
    line2busname_to = pd.read_pickle('scenario_example/to_bus.pickle')
    print('finished')