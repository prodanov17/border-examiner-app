import os
from abc import ABC, abstractmethod

import pandas as pd


class GraphReport(ABC):
    def __init__(self, border_name):
        self.border_name = border_name
        self.data = pd.read_csv(os.getenv("CSV_FILE"))
        self.data['wait_time'] = self.data['wait_time'].str.replace(' min', '').astype(float)
        self.data['datetime_from'] = pd.to_datetime(self.data['datetime_from'], format='%d.%m.%Y %H:%M')
        self.data['datetime_to'] = pd.to_datetime(self.data['datetime_to'], format='%d.%m.%Y %H:%M')
        self.data['date_range'] = self.data.apply(lambda
                                                      row: f"{row['datetime_from'].strftime('%d.%m.%Y %H:%M')} - {row['datetime_to'].strftime('%d.%m.%Y %H:%M')}",
                                                  axis=1)
        self.data = self.data[self.data['border'] == border_name]

    @abstractmethod
    def generate_report(self):
        pass
