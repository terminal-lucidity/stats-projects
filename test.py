import pandas as pd
from scipy.stats import shapiro

def shapiro_wilk_test(csv_file, column_name):
    df = pd.read_csv(csv_file)
    df = df.dropna(subset=[column_name])
    df[column_name] = pd.to_numeric(df[column_name], errors='coerce')
    stat, p_value = shapiro(df[column_name])
    print(f"Shapiro-Wilk Test for {column_name}:")
    print(f"Statistic: {stat}")
    print(f"P-value: {p_value}")
    alpha = 0.05
    if p_value > alpha:
        print("Sample looks Gaussian (fail to reject H0)")
    else:
        print("Sample does not look Gaussian (reject H0)")

csv_file_path = '/Users/anmolmago/Downloads/archive.csv' 
column_name = 'February Average Temperature'

shapiro_wilk_test(csv_file_path, column_name)
