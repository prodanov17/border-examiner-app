from . import GraphReport
import matplotlib.pyplot as plt


class AverageWaitReport(GraphReport):
    def __init__(self, border_name):
        super().__init__(border_name)
        self.data['hour_of_day'] = self.data['datetime_from'].dt.hour

    def generate_report(self):
        hourly_groups = self.data.groupby('hour_of_day')
        avg_wait_times = hourly_groups['wait_time'].mean()

        plt.figure(figsize=(10, 6))
        avg_wait_times.plot(kind='bar', color='skyblue')
        plt.title(f'Average Wait Time by Hour of Day for {self.border_name}')
        plt.xlabel('Hour of Day')
        plt.ylabel('Average Wait Time (minutes)')
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()
