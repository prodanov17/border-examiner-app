import os
import pandas as pd

def get_border_names():
    # Read the CSV file
    data = pd.read_csv(os.getenv("CSV_FILE"))

    # Get the unique border names
    border_names = data['border'].unique().tolist()

    return border_names
