
# Import the necessary modules and libraries

import os
import json
import numpy as np
import pandas as pd
from pandas.io.json import json_normalize



def load_flatten_df(path, nrows=None):
    """
    Rads the CSV data and flattens the JSON fields.
    
    """ 
    json_columns = ['device', 'geoNetwork', 'totals', 'trafficSource']
    df = pd.read_csv(path, 
                     converters={column: json.loads for column in json_columns}, #Decoding JSON, loading those col as json dtype
                     dtype={'fullVisitorId': 'str'}, 
                     nrows=nrows)
    
    for column in json_columns:
        column_as_df = json_normalize(df[column]) 
        column_as_df.columns = [f"{column}.{subcolumn}" for subcolumn in column_as_df.columns]
        df = df.drop(column, axis=1).merge(column_as_df, right_index=True, left_index=True) # merge by index, don't add extra rows
    #print(f"Loaded {os.path.basename(path)}. Shape: {df.shape}")
    return df


