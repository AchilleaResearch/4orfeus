import numpy as np
import pandas as pd
import os

dataroot = 'X:\\4orfeus-gitignored-file-exchange\\TAMU\\'

val = ['Bus']

if 'Line' in val:

    f1 = 'Texas7k_2021_Line.csv'
    f2 = 'Texas7k_2030_Line.csv'

    df1 = pd.read_csv(dataroot+f1, skiprows=1, index_col=['From Number', 'To Number', 'Circuit'])
    df2 = pd.read_csv(dataroot+f2, skiprows=1, index_col=['From Number', 'To Number', 'Circuit'])

    df3 = df1.join(df2, how='outer', lsuffix='1', rsuffix='2')
    df3a = df3[df3['R1'] != df3['R2']]
    df3a.to_csv(os.path.join(dataroot, 'Texas7k_LineDifferences.csv'))

if 'Bus' in val:
    
    f1 = 'Texas7k_2021_Buses.csv'
    f2 = 'Texas7k_2030_Buses.csv'

    df1 = pd.read_csv(dataroot+f1, skiprows=1, index_col=['Number', 'Name'])
    df2 = pd.read_csv(dataroot+f2, skiprows=1,index_col=['Number', 'Name'])

    df3 = df1.join(df2, how='outer', lsuffix='1', rsuffix='2')
    df3a = df3[df3['Nom kV1'] != df3['Nom kV2']]
    df3a.to_csv(os.path.join(dataroot, 'Texas7k_BusDifferences.csv'))