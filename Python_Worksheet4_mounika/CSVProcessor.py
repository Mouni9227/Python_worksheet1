import pandas as pd

def load_csv_file(file_path):
    data=pd.read_csv(file_path)
    return data

def total_col(data):
    return data.shape[1]

def total_rows(data):
    return data.shape[0]

def fill_zeros_in_missing_value(data):
    return data.fillna(0)
