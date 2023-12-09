import pandas as pd
import numpy as np
import scipy.stats as stats

def calculate_confidence_interval(data, confidence_level=0.95):
    sample_mean = np.mean(data)
    sample_std = data.std(ddof=1)
    print(f"Sample Standard Deviation: {sample_std}")
    n = 124
    df = n - 1
    standard_error = sample_std / (n**0.5)
    alpha = 0.05
    critical_t = stats.t.ppf(1 - alpha/2, df)  
    margin_of_error = critical_t * standard_error
    confidence_interval = (sample_mean - margin_of_error, sample_mean + margin_of_error)
    return confidence_interval

csv_file_path = '/Users/anmolmago/Downloads/archive.csv' 
column_name = 'February Average Temperature'
df = pd.read_csv(csv_file_path)
df = df.dropna(subset=[column_name])
data = df[column_name]
confidence_interval = calculate_confidence_interval(data)
if confidence_interval is not None:
    print(f"Confidence Interval (95%): {confidence_interval}")

