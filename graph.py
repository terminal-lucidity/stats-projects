import pandas as pd
import matplotlib.pyplot as plt

def create_histogram(csv_file):
    df = pd.read_csv(csv_file)
    plt.hist(df['February Average Temperature'])
    plt.ylabel('Frequency')
    plt.xlabel('Average Temperature')
    plt.title('Average Temperature in February for 124 years')
    plt.show()
csv_file_path = '/Users/anmolmago/Downloads/archive.csv'     
create_histogram(csv_file_path)
