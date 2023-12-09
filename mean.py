import pandas as pd

def calculate_sample_mean(csv_file, column_name):
    df = pd.read_csv(csv_file)
    data = df[column_name]
    sample_mean = data.mean()
    return sample_mean

csv_file_path = '/Users/anmolmago/Downloads/archive.csv' 
column_name = 'February Average Temperature'
result = calculate_sample_mean(csv_file_path, column_name)
print(f"Sample Mean for {column_name}: {result}")
