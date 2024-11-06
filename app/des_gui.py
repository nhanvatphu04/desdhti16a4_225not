# app/des_gui.py
import tkinter as tk
from tkinter import Button, Entry, Label, Text
import webbrowser
from screeninfo import get_monitors
from app import des_controller

monitors = get_monitors()
monitor = monitors[0] if monitors else None

SCREENWIDTH = 600
SCREENHEIGHT = 400

COLOR = {
    'Black'    : '#000000',
    'White'    : '#FFFFFF',
    'Grey'     : '#808080',
    'Red'      : '#FF0000',
    'Green'    : '#008000',
    'Blue'     : '#0000FF',
    'Yellow'   : '#FFFF00',
    'Cyan'     : '#00FFFF',
    'Magenta'  : '#FF00FF',
    'Orange'   : '#FFA500',
    'Purple'   : '#800080',
    'Brown'    : '#A52A2A',
    'Pink'     : '#FFC0CB',
    'LightGrey': '#D3D3D3',
    'DarkGrey' : '#A9A9A9'
}

WINDOWWIDTH = monitor.width if monitor else SCREENWIDTH
WINDOWHEIGHT = monitor.height if monitor else SCREENHEIGHT

x = (WINDOWWIDTH // 2) - (SCREENWIDTH // 2)
y = (WINDOWHEIGHT // 2) - (SCREENHEIGHT // 2)

intro_text = "Hello, Welcome to my tkinter GUI window! If you want to try some mini DES tools, please check the options above."

def centerWidgetHorizontally(widget, root):
    root.update_idletasks()
    window_width = root.winfo_width()
    widget_width = widget.winfo_reqwidth()
    x = (window_width - widget_width) // 2
    widget.place(x=x, y=widget.winfo_y())

class DesApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Mini DES Tool")
        self.root.config(background=COLOR['White'])
        self.root.geometry(f'{SCREENWIDTH}x{SCREENHEIGHT}+{x}+{y}')
        self.root.resizable(False, False)

        self.label1 = Label(self.root, text="DATA ENCRYPTION STANDARD MINI TOOL", font=("Arial", 16, "bold"), bg=COLOR['White'], fg=COLOR['Blue'])
        self.label1.place(x=10, y=10)

        self.label2 = Label(self.root, text=intro_text, justify="left", anchor="w", wraplength=(SCREENWIDTH - 10), font=("Arial", 12, "bold"), bg=COLOR['White'])
        self.label2.place(x=10, y=70)

        self.label3 = Label(self.root, text="There is nothing here!", justify="center", anchor="center", font=("Arial", 12), bg=COLOR['White'])
        self.label3.place(x=200, y=250)

        self.text_box = Text(root, height=10, width=80, wrap="word", font=("Arial", 10))
        self.text_box.config(state="disabled")

        self.menu_bar = tk.Menu(root)
        function_menu = tk.Menu(self.menu_bar, tearoff=0)
        function_menu.add_command(label="IP (Initial Permutation)", command=self.showIPScreen)
        function_menu.add_command(label="FP (Final Permutation)", command=self.showFPScreen)
        function_menu.add_command(label="Expansion", command=self.showExpansionScreen)
        function_menu.add_command(label="Key Generator", command=self.showKeyGeneratorScreen)
        function_menu.add_command(label="Permutation", command=self.showPermutationScreen)
        function_menu.add_command(label="Substitution", command=self.showSubstitutionScreen)
        function_menu.add_command(label="Encryption & Decryption", command=self.showEDScreen)
        about_menu = tk.Menu(self.menu_bar, tearoff=0)
        about_menu.add_command(label="About", command=self.showAbout)

        self.menu_bar.add_cascade(label="Options", menu=function_menu)
        self.menu_bar.add_cascade(label="About", menu=about_menu)
        root.config(menu=self.menu_bar)

        self.title_label = Label(root, font=("Arial", 14, "bold"))
        self.title_label.place()

        self.input_label = Label(root, font=("Arial", 10))
        self.output_label = Label(root, font=("Arial", 10))
        self.input_entry = Entry(root, width=80)
        self.execute_button = Button(root, text="Run", command=self.executeFunction)

        self.current_function = None

    def clearDataFields(self):
        self.input_entry.delete(0, tk.END)
        self.text_box.config(state="normal")
        self.text_box.delete("1.0", tk.END)
        self.text_box.config(state="disabled")

    def showIPScreen(self):
        self.clearDataFields()
        self.label2.place_forget()
        self.label3.place_forget()
        self.current_function = "IP"
        self.title_label.config(text="IP")
        self.input_label.config(text="Insert block for IP:")
        self.output_label.config(text="Output:")
        self.showInputWidgets()
        self.showTextBox()

    def showFPScreen(self):
        self.clearDataFields()
        self.label2.place_forget()
        self.label3.place_forget()
        self.current_function = "FP"
        self.title_label.config(text="FP")
        self.input_label.config(text="Insert block for FP:")
        self.output_label.config(text="Output:")
        self.showInputWidgets()
        self.showTextBox()

    def showExpansionScreen(self):
        self.clearDataFields()
        self.label2.place_forget()
        self.label3.place_forget()
        self.current_function = "Expansion"
        self.title_label.config(text="Expansion")
        self.input_label.config(text="Insert block for Expansion:")
        self.output_label.config(text="Output:")
        self.showInputWidgets()
        self.showTextBox()

    def showKeyGeneratorScreen(self):
        self.clearDataFields()
        self.label2.place_forget()
        self.label3.place_forget()
        self.current_function = "Key Generator"
        self.title_label.config(text="Key Generator")
        self.input_label.config(text="Insert key for Key Generator:")
        self.output_label.config(text="Output:")
        self.showInputWidgets()
        self.showTextBox()

    def showPermutationScreen(self):
        self.clearDataFields()
        self.label2.place_forget()
        self.label3.place_forget()
        self.current_function = "Permutation"
        self.title_label.config(text="Permutation")
        self.input_label.config(text="Insert block for Permutation:")
        self.output_label.config(text="Output:")
        self.showInputWidgets()
        self.showTextBox()

    def showSubstitutionScreen(self):
        self.clearDataFields()
        self.label2.place_forget()
        self.label3.place_forget()
        self.current_function = "Substitution"
        self.title_label.config(text="Substitution")
        self.input_label.config(text="Insert block for Substitution:")
        self.output_label.config(text="Output:")
        self.showInputWidgets()
        self.showTextBox()

    def showEDScreen(self):
        self.clearDataFields()
        self.label2.place_forget()
        self.label3.place_forget()
        self.current_function = "ED"

    def showInputWidgets(self):
        centerWidgetHorizontally(self.title_label, self.root)
        centerWidgetHorizontally(self.input_label, self.root)
        centerWidgetHorizontally(self.input_entry, self.root)
        centerWidgetHorizontally(self.output_label, self.root)
        centerWidgetHorizontally(self.execute_button, self.root)

        self.title_label.place(y=40)
        self.input_label.place(y=70)
        self.input_entry.place(y=100)
        self.execute_button.place(y=130)
        self.output_label.place(y=170)

    def showTextBox(self):
        centerWidgetHorizontally(self.text_box, self.root)
        self.text_box.place(y=200)

    def executeFunction(self):
        block_data = self.input_entry.get()
        self.text_box.config(state="normal")
        self.text_box.delete("1.0", tk.END)
        try:
            if self.current_function == "IP":
                result = des_controller.executeIP(block_data)
                self.text_box.insert(tk.END, f"{result}")
            elif self.current_function == "FP":
                result = des_controller.executeFP(block_data)
                self.text_box.insert(tk.END, f"{result}")
            elif self.current_function == "Expansion":
                result = des_controller.executeExpansion(block_data)
                self.text_box.insert(tk.END, f"{result}")
            elif self.current_function == "Key Generator":
                result = des_controller.executeGenKey(block_data)
                detailed_keys = [f"Key {i+1}: {round_key}" for i, round_key in enumerate(result)]
                self.text_box.insert(tk.END, "\n".join(detailed_keys))
            elif self.current_function == "Substitution":
                result = des_controller.executeSubstitution(block_data)
                self.text_box.insert(tk.END, f"{result}")
            elif self.current_function == "Permutation":
                result = des_controller.executePermutation(block_data)
                self.text_box.insert(tk.END, f"{result}")
            elif self.current_function == "ED":
                pass

            else:
                self.text_box.insert(tk.END, "Please select a function first")
        except ValueError as ve:
            self.text_box.insert(tk.END, f"Error: {ve}")
        except Exception as e:
            self.text_box.insert(tk.END, f"An unexpected error occurred: {e}")

        self.text_box.config(state="disabled")

    def showAbout(self):
        about_window = tk.Toplevel(self.root)
        about_window.title("About")
        width, height = 400, 400
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        x = (screen_width // 2) - (width // 2)
        y = (screen_height // 2) - (height // 2)
        about_window.geometry(f"{width}x{height}+{x}+{y}")
        about_window.resizable(False, False)
        about_window.configure(bg="lightgray")
        about_label1 = Label(about_window, text="Mini DES Tool", font=("Arial", 12), bg="lightgray")
        about_label2 = Label(
            about_window,
            text="""This tool is designed to help users understand and experiment with the DES encryption algorithm. The GUI allows users to apply steps like Initial Permutation (IP), Final Permutation (FP), Expansion, Key Generator, Substitution, and other features on input data blocks.""",
            justify="left",
            anchor="w",
            wraplength=350,
            padx=10,
            font=("Arial", 12),
            bg="lightgray"
        )
        about_label3 = Label(
            about_window,
            text='This is my first project (maybe) so if there is any errors or/and exceptions please inform me. (or just ignore them :D). And I\'m no longer continue to update this project.',
            justify="left",
            anchor="w",
            wraplength=350,
            padx=10,
            font=("Arial", 12),
            bg="lightgray"
        )
        
        about_label1.pack(pady=10)
        about_label2.pack(pady=10)
        about_label3.pack(pady=10)
        link_label = Label(about_window, text="Visit my GitHub", fg="blue", cursor="hand2", font=("Arial", 10, "underline"), bg="lightgray")
        link_label.pack(pady=5)
        link_label.bind("<Button-1>", lambda e: webbrowser.open("https://github.com/nhanvatphu04/desdhti16a4_225not"))
