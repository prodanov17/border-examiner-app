import threading
from time import sleep
from tkinter import messagebox

from dotenv import load_dotenv
from src.BorderService import BorderService
import tkinter as tk
from src.Data import CSVStore
from src.GUI import BorderServiceApp


def center_window(window):
    window.update_idletasks()
    width = window.winfo_width()
    height = window.winfo_height()
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x_coordinate = (screen_width / 2) - (width / 2)
    y_coordinate = (screen_height / 2) - (height / 2)
    window.geometry("+%d+%d" % (x_coordinate, y_coordinate))


if __name__ == "__main__":
    load_dotenv()
    root = tk.Tk()

    try:
        app = BorderServiceApp(root)
        center_window(root)
        root.mainloop()
    except Exception as e:
        messagebox.showerror("Error", str(e))
