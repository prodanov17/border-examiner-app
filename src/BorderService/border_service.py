import requests
from bs4 import BeautifulSoup
from src.Border import BorderWaitTimes
from src.Data import CSVStore


class BorderService:
    def __init__(self, url: str, storage: CSVStore):
        if not url.endswith("/"):
            url = url + "/"
        self.url = url
        self.border_name = url.split("/")[-2]
        self.storage = storage

    def run(self):
        response = requests.get(self.url)

        if response.status_code == 200:
            # Parse the HTML content of the webpage
            soup = BeautifulSoup(response.content, 'html.parser')

            # Find all elements with class name 'date-time'
            date_time_elements = soup.find_all(class_='date-time')
            date_times = list(map(lambda x: x.text, date_time_elements))

            # Find all elements with class name 'waiting-time'
            waiting_time_elements = soup.find_all(class_='waitting-time')
            waiting_times = list(map(lambda x: x.text, waiting_time_elements))

            border = BorderWaitTimes(self.border_name)
            border.set_wait_time(self.get_average_wait_time(waiting_times))
            border.set_datetime(date_times[-2], date_times[0])
            self.save(border)

            print(f"Average waiting time for {self.border_name} is {border.get_wait_time()} for range {border.get_datetime()}")
        else:
            raise Exception("There was an error getting the average waiting time")

    def get_average_wait_time(self, wait_times: list) -> str:
        times = list(map(lambda x: int(x.split(" ")[0]), wait_times))
        return f"{sum(times) / len(wait_times)} min"

    def save(self, border: BorderWaitTimes) -> None:
        self.storage.store_data(border)

    def get_border_wait_times(self) -> list:
        return self.storage.load_data()

    def get_border_name(self) -> str:
        return self.border_name