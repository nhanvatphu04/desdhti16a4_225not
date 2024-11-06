# main.py
import tkinter as tk
from app.des_gui import DesApp

if __name__ == "__main__":
    root = tk.Tk()
    app = DesApp(root)
    root.mainloop()
