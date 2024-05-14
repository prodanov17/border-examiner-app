import os
from datetime import datetime

import pandas as pd
from tkinter import filedialog, messagebox


class ExcelReport:
    def __init__(self):
        self.file_name = os.getenv("CSV_FILE")

    def generate_report(self, border_name=None):
        if border_name is None:
            border_name = os.getenv("DEFAULT_BORDER_NAME")

        df = pd.read_csv(os.getenv('CSV_FILE'))

        default_filename = datetime.now().strftime(f"{border_name}-%Y_%m_%d_%H_%M_%S")

        # Ask user for the location to save the Excel file
        file_path = filedialog.asksaveasfilename(
            initialfile=default_filename,
            defaultextension=".xlsx",
            filetypes=[("Excel files", "*.xlsx")]
        )

        if file_path:
            df.to_excel(file_path, index=False)
            messagebox.showinfo("File saved!", "Report generated and saved successfully.")
        else:
            messagebox.showerror("No file selected!", "Exiting without saving.")
            # print("No file selected. Exiting without saving.")