#!/bin/python3
#clean_drops.py
#We're going to clean up our oildrops and export em as .csvs

import os
import pandas as pd

px_over_meters = 167/(.04) # pixel to cm

def cleaner(filename):
    df = pd.read_csv(filename, sep='\t', encoding='latin1')
    df = df.drop(df.columns[[0,1,3,5,6,7]], axis=1) # Columns 3 and 5 are necessary
    df.columns = ['frame','y']  # label the new headings
    df['y'] = 800 - df['y'] #count pixels from the bottom
    df['y'] = df['y']/px_over_meters # pixels -> cm
    df.to_csv (filename[:-4] + '.csv', index = False, header=True)


# This can get tricky - use the absolute path of the filename
# for linux:

#folder = "/path/to/drops"
folder = "/home/guest/fall_20/lab/oildrops/raw/"


for f in os.listdir(folder):
    cleaner(folder + f)

