import os
from src.Border import BorderWaitTimes
import csv


class CSVStore:
    def __init__(self):
        self.file_path = os.getenv('CSV_FILE')

        # Create the CSV file if it doesn't exist
        if not os.path.exists(self.file_path):
            self.create_csv_file()

        # Check if the CSV file is empty
        if os.path.getsize(self.file_path) == 0:
            self.add_csv_header()

        self.csv_file = open(self.file_path, 'a+', newline='\n')

    def create_csv_file(self):
        # Create an empty CSV file
        with open(self.file_path, 'w', newline='\n') as file:
            file.close()
            pass

    def add_csv_header(self):
        # Add the header with the necessary columns
        header = ['border', 'wait_time', 'datetime_from', 'datetime_to']
        with open(self.file_path, 'w', newline='\n') as file:
            writer = csv.writer(file)
            writer.writerow(header)
            file.close()

    def store_data(self, border: BorderWaitTimes):
        if not border.validate():
            raise Exception("Invalid border")
        self.csv_file.write(os.linesep + self.parse_data(border))

    def parse_data(self, border: BorderWaitTimes):
        return str(border)

    def load_data(self) -> list:
        borders = []
        with open(self.csv_file, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                border = BorderWaitTimes(row['border'], row['wait_time'], row['datetime_from'], row['datetime_to'])
                borders.append(border)
        return borders

    def __del__(self):
        self.csv_file.close()
