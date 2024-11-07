"""Useful reused code"""

import pandas as pd

def load_vehicle_data(url="https://github.com/mattharrison/datasets/raw/master/data/vehicles.csv.zip"):
    """
    Loads the vehicle dataset from the provided URL, and returns the DataFrame.
    
    Returns:
        pd.DataFrame: DataFrame with vehicle data.
    """
    df = pd.read_csv(url, dtype_backend="pyarrow", engine="pyarrow", compression="zip")
    return df