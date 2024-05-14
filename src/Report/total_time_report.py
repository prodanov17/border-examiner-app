from . import GraphReport
import matplotlib.pyplot as plt


class TotalTimeReport(GraphReport):
    def __init__(self, border_name):
        super().__init__(border_name)

    def generate_report(self):
        date_range_groups = self.data.groupby('date_range')
        avg_wait_times = date_range_groups['wait_time'].mean()

        plt.figure(figsize=(10, 6))
        avg_wait_times.plot(kind='area', color='skyblue')
        plt.title(f'Average Wait Time by Date Range for {self.border_name}')
        plt.xlabel('Date Range')
        plt.ylabel('Average Wait Time (minutes)')
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()
