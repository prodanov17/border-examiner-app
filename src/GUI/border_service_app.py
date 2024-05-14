import time
import tkinter as tk
from src.Report import ExcelReport
from src.Report import TotalTimeReport
from tkinter import messagebox
from tkinter import ttk
from tkinter import simpledialog as sd
from threading import Thread
from src.BorderService import BorderService
from src.Data import CSVStore
from src.Utils import get_border_names
import re
import os

from src.Report.average_wait_report import AverageWaitReport

URL_REGEX = r"[(http(s)?):\/\/(www\.)?a-zA-Z0-9@:%._\+~#=]{2,256}\.[a-z]{2,6}\b([-a-zA-Z0-9@:%_\+.~#?&//=]*)"

class BorderServiceApp:
    def __init__(self, master):
        self.master = master
        master.title("Border Service Application")
        img = tk.PhotoImage(file=self.get_icon_path("flyicon.png"))
        master.iconphoto(False, img)

        self.create_widgets()
        self.create_menu()

        self.is_running = False
        self.border_name = None
        self.border_thread = None
        self.run_count = 0
        self.start_time = None

    def get_icon_path(self, filename):
        # Get the directory path of the current script
        script_dir = os.path.dirname(os.path.abspath(__file__))
        # Go one directory up from the script directory
        parent_dir = os.path.dirname(script_dir)
        # Construct the path to the icon file relative to the parent directory
        icon_path = os.path.join(parent_dir, f"assets/{filename}")
        return icon_path

    def create_menu(self):
        menubar = tk.Menu(self.master)

        # Create File menu
        file_menu = tk.Menu(menubar, tearoff=0)
        file_menu.add_command(label="Save as Excel", command=lambda: self.generate_report("Excel"))

        # Submenu for different types of graphs
        graph_submenu = tk.Menu(file_menu, tearoff=0)
        graph_submenu.add_command(label="Total Wait Times", command=lambda: self.generate_report_prompt("totalgraph"))
        graph_submenu.add_command(label="Wait Times By Hour", command=lambda: self.generate_report_prompt("averagegraph"))

        file_menu.add_command(label="Status", command=self.get_status)

        # Add the graph submenu to "Generate Graph"
        file_menu.add_cascade(label="Generate Graph", menu=graph_submenu)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.master.quit)
        menubar.add_cascade(label="File", menu=file_menu)

        # Create Edit menu (you can add commands here if needed)
        edit_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Edit", menu=edit_menu)

        # Create View menu (you can add commands here if needed)
        view_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="View", menu=view_menu)


        self.master.config(menu=menubar)

    def create_widgets(self):
        self.url_label = tk.Label(self.master, text="Enter URL:")
        self.url_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")

        self.url_entry = tk.Entry(self.master)
        self.url_entry.grid(row=0, column=1, padx=5, pady=5, sticky="we")

        self.start_button = tk.Button(self.master, text="Start Service", command=self.toggle_service)
        self.start_button.grid(row=1, column=0, columnspan=2, padx=5, pady=5, sticky="ew")


    def toggle_service(self):
        if not self.is_running:
            url = self.url_entry.get()
            if url:
                self.start_time = time.time()
                self.border_thread = Thread(target=self.run_border_service, args=(url,))
                self.is_running = True
                self.border_thread.start()
                self.start_button.config(text="Stop Service")
            else:
                messagebox.showerror("Error", "Please enter a URL.")
        else:
            self.is_running = False
            self.start_button.config(text="Start Service")
            # You can also interrupt the thread if needed

    def run_border_service(self, url):
        while self.is_running:
            if not re.match(URL_REGEX, url):
                messagebox.showerror("Error", "Please enter a valid URL.")
                self.is_running = False
                self.start_button.config(text="Start Service")
                return

            storage = CSVStore()
            border_service = BorderService(url, storage)
            border_service.run()

            self.run_count += 1

            if self.border_name is None:
                self.border_name = border_service.get_border_name()

            # Sleep for a specific duration or perform any other action
            time.sleep(3 * 60 * 60)

    def get_status(self):
        if self.is_running:
            running_time = time.time() - self.start_time
            hours = int(running_time // 3600)
            minutes = int((running_time % 3600) // 60)
            seconds = int(running_time % 60)

            messagebox.showinfo("Service Status", f"Service has run {self.run_count} times.\n"
                                                  f"Running time: {hours} hours, {minutes} minutes, {seconds} seconds.")
        else:
            messagebox.showinfo("Service Status", "Service is not running.")

    def generate_report(self, type):
        print("HERE")
        border_name = self.border_combobox.get()  # Get the selected border name from the Combobox
        if border_name:
            # Close the report generation prompt window
            self.report_prompt_window.destroy()

            if type.lower() == "excel":
                ExcelReport().generate_report(border_name)
            elif type.lower() == "totalgraph":
                TotalTimeReport(border_name).generate_report()
            elif type.lower() == "averagegraph":
                AverageWaitReport(border_name).generate_report()
        else:
            messagebox.showerror("Error", "Please select a border.")

    def get_border_name(self):
        border_name = sd.askstring("Border Name", "Enter the border name (example: horgos-roszke")
        return border_name.strip() if border_name else None

    def generate_report_prompt(self, type):
        # Create a Toplevel window for the report generation prompt
        self.report_prompt_window = tk.Toplevel(self.master)
        self.report_prompt_window.title("Generate Report")

        # Create a label for the dropdown menu
        border_label = tk.Label(self.report_prompt_window, text="Select Border:")
        border_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")

        # Create a Combobox for selecting the border name
        self.border_combobox = ttk.Combobox(self.report_prompt_window, state="readonly")
        self.border_combobox.grid(row=0, column=1, padx=5, pady=5, sticky="we")

        # Add some default options to the Combobox (you can update this dynamically if needed)
        self.border_combobox['values'] = get_border_names()

        # Create a button to confirm the report generation
        generate_button = tk.Button(self.report_prompt_window, text="Generate", command=lambda: self.generate_report(type))
        generate_button.grid(row=1, column=0, columnspan=2, padx=5, pady=5, sticky="ew")

