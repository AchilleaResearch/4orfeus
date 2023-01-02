import pandas as pd

if __name__ == "__main__":
    # read in the dictionaries from pickle files
    line2busname_from = pd.read_pickle('Princeton/scenario_example/from_bus.pickle')
    line2busname_to = pd.read_pickle('Princeton/scenario_example/to_bus.pickle')
    
    # Create a dataframe to consolidate line information
    lineids = []
    from_bus_name = []
    to_bus_names = []
    for k in line2busname_from.keys():
        if k in line2busname_to.keys():
            lineids.append(k)
            from_bus_name.append(line2busname_from[k])
            to_bus_names.append(line2busname_to[k])
        else:
            print('Line %s from bus: %s, not found in the `to_bus.pickle` file')
    df1 = pd.DataFrame(index=lineids, data={'from': from_bus_name, 'to': to_bus_names})
    df1.to_csv('output/scenario_lines.csv', index_label='line')
