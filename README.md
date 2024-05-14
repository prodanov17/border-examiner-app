# Border Service Application

The Border Service Application is a tool designed to help users monitor border wait times at specific checkpoints. It periodically fetches data from a provided URL, extracts relevant information about wait times, and stores it for analysis. Additionally, it allows users to generate reports in Excel format and Matplotlib graphs for further analysis.

## Features

- **Monitoring Border Wait Times**: Users can input the URL of a website containing border wait time information. The application fetches this data periodically and updates the user interface with the latest wait times.
- Example URL - `https://borderalarm.com/bottlenecks/horgos-roszke/`

- **Saving Data**: Border wait time data is stored in a CSV file for future reference. The CSV file includes information such as the border name, wait time, and date.

- **Generating Reports**: Users can generate reports in Excel and Matplotlib format summarizing the border wait time data. These reports provide insights into trends and patterns in border wait times over time.

## Usage

1. **Enter URL**: Input the URL of the website containing border wait time information in the provided text field.

2. **Start Service**: Click the "Start Service" button to begin monitoring border wait times. The application will fetch data periodically and display the latest wait times.

3. **Stop Service**: Click the "Stop Service" button to stop monitoring border wait times.

4. **Generate Report**: Click the "Save as Excel" button to generate a report summarizing the border wait time data. The report will be saved in Excel format for further analysis.

## Requirements

- Python 3.x
- Tkinter (for the GUI)
- Requests library (for making HTTP requests)
- BeautifulSoup library (for web scraping)
- Pandas library (for data manipulation and Excel report generation)

## Installation

1. Clone the repository:

`git clone https://github.com/prodanov17/border-examiner-app.git`

2. Install the required Python libraries:

`pip install -r requirements.txt`

3. Run the application:

`python main.py`

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

