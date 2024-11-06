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

intro_text = 'Hello, Welcome to my tkinter GUI window! If you want to try some mini DES tools, please check the options above.'
about_text1 = 'This tool is designed to help users understand and experiment with the DES encryption algorithm. The GUI allows users to apply steps like Initial Permutation (IP), Final Permutation (FP), Expansion(E), Key Generator, Permutation(P), Substitution(P), and other features.'
about_text2 = 'This is my first project (maybe) so if there is any errors or/and exceptions please inform me. (or just ignore them :D). And I\'m no longer continue to update this project.'

def centerWidgetHorizontally(widget, root):
    root.update_idletasks()
    window_width = root.winfo_width()
    widget_width = widget.winfo_reqwidth()
    x = (window_width - widget_width) // 2
    widget.place(x=x, y=widget.winfo_y())

class DesApp:
    def __init__(self, root):
        self.root = root
        self.root.title('Mini DES Tool')
        self.root.config(background=COLOR['White'])
        self.root.geometry(f'{SCREENWIDTH}x{SCREENHEIGHT}+{x}+{y}')
        self.root.resizable(False, False)
        # Main screen
        self.label1 = Label(self.root, text='DATA ENCRYPTION STANDARD MINI TOOL', font=('Arial', 16, 'bold'), bg=COLOR['White'], fg=COLOR['Blue'])
        self.label2 = Label(self.root, text=intro_text, justify='left', anchor='w', wraplength=(SCREENWIDTH - 10), font=('Arial', 12, 'bold'), bg=COLOR['White'])
        self.label3 = Label(self.root, text='There is nothing here!', justify='center', anchor='center', font=('Arial', 40), bg=COLOR['White'])
        self.version = Label(self.root, text='Last update: Nov 6 2024', font=('Arial', 8), bg=COLOR['White'])
        self.label1.place(x=10, y=10)
        self.label3.place(x=40, y=220)
        self.label2.place(x=10, y=70)
        self.version.place(x=470, y=380)
        # Tool attributes <IP, FP,...>
        self.tool_output_text = Text(root, height=10, width=80, wrap='word', font=('Arial', 10))
        self.tool_title_label = Label(root, font=('Arial', 14, 'bold'))
        self.tool_input_label = Label(root, font=('Arial', 10))
        self.tool_output_label = Label(root, font=('Arial', 10))
        self.tool_input_text = Entry(root, width=80)
        self.tool_run_btn = Button(root, text='Run', command=self.toolFunction)
        # E & D attributes
        self.EDTextbox = Text(self.root, height=3, width=80, wrap='word', font=('Arial', 10))
        self.EDmode = tk.StringVar(value='encrypt')
        self.EDLabel = Label(self.root, text='Select Mode:', bg=COLOR['White'], font=('Arial', 16, 'bold'))
        self.encrypt = tk.Radiobutton(self.root, text='Encrypt', font=('Arial', 12), variable=self.EDmode, value='encrypt', bg=COLOR['White'])
        self.decrypt = tk.Radiobutton(self.root, text='Decrypt', font=('Arial', 12) ,variable=self.EDmode, value='decrypt', bg=COLOR['White'])
        self.EDInput_label = Label(self.root, text='Input Text (64-bit):', bg=COLOR['White'])
        self.EDInput_text = Entry(self.root, width=80)
        self.EDKey_label = Label(self.root, text='Key (64-bit)', bg=COLOR['White'])
        self.EDKey_text = Entry(self.root, width=80)
        self.ED_run_btn = Button(self.root, text='Execute', command=self.EDFunction)
        self.ED_refresh_btn = Button(self.root, text='Refreh', command=self.clearEDDataFields)
        self.EDOutput_label = Label(self.root, text='Cipher text:', font=('Arial', 10))
        # Conversion
        self.con_label = Label(self.root, text='Select Mode:', bg=COLOR['White'], font=('Arial', 16, 'bold'))
        self.con_mode = tk.StringVar(value='bin2hex')
        self.bin2hex = tk.Radiobutton(self.root, text='Bin to Hex', font=('Arial', 12) ,variable=self.con_mode, value='bin2hex', bg=COLOR['White'])
        self.hex2bin = tk.Radiobutton(self.root, text='Hex to Bin', font=('Arial', 12) ,variable=self.con_mode, value='hex2bin', bg=COLOR['White'])
        self.con_input_label = Label(self.root, text='Input:', bg=COLOR['White'])
        self.con_input_text = Entry(self.root, width=80)
        self.con_run_btn = Button(self.root, text='Convert', command=self.convertFunction)
        self.con_refresh_btn = Button(self.root, text='Refresh', command=self.clearConDataFields)
        self.con_output_label = Label(self.root, text='Output:', bg=COLOR['White'])
        self.con_textbox = Text(root, height=3, width=80, wrap='word', font=('Arial', 10))
        # Menu
        self.menu_bar = tk.Menu(root)
        function_menu = tk.Menu(self.menu_bar, tearoff=0)
        function_menu.add_command(label='Initial Permutation (IP)', command=self.showIPScreen)
        function_menu.add_command(label='Final Permutation (FP)', command=self.showFPScreen)
        function_menu.add_command(label='Expansion (E)', command=self.showExpansionScreen)
        function_menu.add_command(label='Key Generator', command=self.showKeyGeneratorScreen)
        function_menu.add_command(label='Permutation (P)', command=self.showPermutationScreen)
        function_menu.add_command(label='Substitution (S)', command=self.showSubstitutionScreen)
        function_menu.add_command(label='Encrypt & Decrypt', command=self.showEDScreen)
        function_menu.add_command(label='Conversion', command=self.showConversionScreen)
        about_menu = tk.Menu(self.menu_bar, tearoff=0)
        about_menu.add_command(label='About', command=self.showAbout)
        self.menu_bar.add_cascade(label='Options', menu=function_menu)
        self.menu_bar.add_cascade(label='About', menu=about_menu)
        root.config(menu=self.menu_bar)

        self.current_function = None

    def clearToolDataFields(self):
        self.tool_input_text.delete(0, tk.END)
        self.tool_output_text.config(state='normal')
        self.tool_output_text.delete('1.0', tk.END)
        self.tool_output_text.config(state='disabled')

    def clearEDDataFields(self):
        self.EDInput_text.delete(0, tk.END)
        self.EDKey_text.delete(0, tk.END)
        self.EDTextbox.config(state='normal')
        self.EDTextbox.delete('1.0', tk.END)

    def clearConDataFields(self):
        self.con_input_text.delete(0, tk.END)
        self.con_textbox.config(state='normal')
        self.con_textbox.delete('1.0', tk.END)
        self.con_textbox.config(state='disabled')

    def clearConWidget(self):
        self.con_label.place_forget()
        self.bin2hex.place_forget()
        self.hex2bin.place_forget()
        self.con_input_label.place_forget()
        self.con_input_text.place_forget()
        self.con_run_btn.place_forget()
        self.con_refresh_btn.place_forget()
        self.con_output_label.place_forget()
        self.con_textbox.place_forget()

    def clearEDWidget(self):
        self.label2.place_forget()
        self.label3.place_forget()
        self.EDLabel.pack_forget()
        self.encrypt.place_forget()
        self.decrypt.place_forget()
        self.EDInput_label.place_forget()
        self.EDInput_text.place_forget()
        self.EDKey_label.place_forget()
        self.EDKey_text.place_forget()
        self.ED_run_btn.place_forget()
        self.ED_refresh_btn.place_forget()
        self.EDOutput_label.place_forget()
        self.EDTextbox.place_forget()

    def clearOtherWidget(self):
        self.label2.place_forget()
        self.label3.place_forget()
        self.tool_title_label.place_forget()
        self.tool_input_label.place_forget()
        self.tool_input_text.place_forget()
        self.tool_run_btn.place_forget()
        self.tool_output_label.place_forget()
        self.tool_output_text.place_forget()

    def showIPScreen(self):
        self.clearToolDataFields()
        self.clearEDWidget()
        self.clearConWidget()
        self.current_function = 'IP'
        self.tool_title_label.config(text='Initial Permutation')
        self.tool_input_label.config(text='Input data:')
        self.tool_output_label.config(text='Output:')
        self.showInputWidgets()
        self.showTextBox()

    def showFPScreen(self):
        self.clearToolDataFields()
        self.clearEDWidget()
        self.clearConWidget()
        self.current_function = 'FP'
        self.tool_title_label.config(text='Final Permutation')
        self.tool_input_label.config(text='Input data:')
        self.tool_output_label.config(text='Output:')
        self.showInputWidgets()
        self.showTextBox()

    def showExpansionScreen(self):
        self.clearToolDataFields()
        self.clearEDWidget()
        self.clearConWidget()
        self.current_function = 'E'
        self.tool_title_label.config(text='Expansion')
        self.tool_input_label.config(text='Input data:')
        self.tool_output_label.config(text='Output:')
        self.showInputWidgets()
        self.showTextBox()

    def showKeyGeneratorScreen(self):
        self.clearToolDataFields()
        self.clearEDWidget()
        self.clearConWidget()
        self.current_function = 'KG'
        self.tool_title_label.config(text='Key Generator')
        self.tool_input_label.config(text='Input key:')
        self.tool_output_label.config(text='Subkey:')
        self.showInputWidgets()
        self.showTextBox()

    def showPermutationScreen(self):
        self.clearToolDataFields()
        self.clearEDWidget()
        self.clearConWidget()
        self.current_function = 'P'
        self.tool_title_label.config(text='Permutation')
        self.tool_input_label.config(text='Input data:')
        self.tool_output_label.config(text='Output:')
        self.showInputWidgets()
        self.showTextBox()

    def showSubstitutionScreen(self):
        self.clearToolDataFields()
        self.clearEDWidget()
        self.clearConWidget()
        self.current_function = 'S'
        self.tool_title_label.config(text='Substitution')
        self.tool_input_label.config(text='Input data:')
        self.tool_output_label.config(text='Output:')
        self.showInputWidgets()
        self.showTextBox()

    def showEDScreen(self):
        self.clearOtherWidget()
        self.clearEDDataFields()
        self.clearConWidget()
        self.current_function = 'ED'
        self.EDmode.trace_add('write', lambda *args: self.updateEDOuputLabel())
        self.createMode()

    def updateEDOuputLabel(self):
        self.EDOutput_label.config(text='Cipher Text:' if self.EDmode.get() == 'encrypt' else 'Plain Text:')

    def showConversionScreen(self):
        self.clearOtherWidget()
        self.clearEDWidget()
        centerWidgetHorizontally(self.con_label, self.root)
        centerWidgetHorizontally(self.con_input_label, self.root)
        centerWidgetHorizontally(self.con_input_text, self.root)
        centerWidgetHorizontally(self.con_output_label, self.root)
        centerWidgetHorizontally(self.con_textbox, self.root)
        self.con_label.place(y=40)
        self.bin2hex.place(x=20, y=80)
        self.hex2bin.place(x=20, y=110)
        self.con_input_label.place(y=150)
        self.con_input_text.place(y=180)
        self.con_run_btn.place(x=240, y=220)
        self.con_refresh_btn.place(x=300, y=220)
        self.con_output_label.place(y=250)
        self.con_textbox.place(y=280)

    def showInputWidgets(self):
        centerWidgetHorizontally(self.tool_title_label, self.root)
        centerWidgetHorizontally(self.tool_input_label, self.root)
        centerWidgetHorizontally(self.tool_input_text, self.root)
        centerWidgetHorizontally(self.tool_output_label, self.root)
        centerWidgetHorizontally(self.tool_run_btn, self.root)
        self.tool_title_label.place(y=40)
        self.tool_input_label.place(y=70)
        self.tool_input_text.place(y=100)
        self.tool_run_btn.place(y=130)
        self.tool_output_label.place(y=170)

    def showTextBox(self):
        centerWidgetHorizontally(self.tool_output_text, self.root)
        self.tool_output_text.place(y=200)

    def createMode(self):
        centerWidgetHorizontally(self.EDLabel, self.root)
        centerWidgetHorizontally(self.EDInput_label, self.root)
        centerWidgetHorizontally(self.EDInput_text, self.root)
        centerWidgetHorizontally(self.EDKey_label, self.root)
        centerWidgetHorizontally(self.EDKey_text, self.root)
        centerWidgetHorizontally(self.EDOutput_label, self.root)
        centerWidgetHorizontally(self.EDTextbox, self.root)
        self.EDLabel.pack(pady=40)
        self.encrypt.place(x=20, y=80)
        self.decrypt.place(x=20, y=110)
        self.EDInput_label.place(y=150)
        self.EDInput_text.place(y=180)
        self.EDKey_label.place(y=210)
        self.EDKey_text.place(y=240)
        self.ED_run_btn.place(x=240, y=270)
        self.ED_refresh_btn.place(x=300, y=270)
        self.EDOutput_label.place(y=300)
        self.EDTextbox.place(y=330)

    def EDFunction(self):
        data = self.EDInput_text.get()
        key = self.EDKey_text.get()
        mode = self.EDmode.get()
        result = ''
        try:
            if mode == 'encrypt':
                result = des_controller.executeEncryption(data, key)
            else:
                result = des_controller.executeDecryption(data, key)
            self.EDTextbox.insert(tk.END, f'{result}')
        except ValueError as ve:
            self.EDTextbox.insert(tk.END, f'Error: {ve}')
        except Exception as e:
            self.EDTextbox.insert(tk.END, f'An unexpected error occurred: {e}')
        self.EDTextbox.config(state='disabled')

    def convertFunction(self):
        data = self.con_input_text.get()
        self.con_textbox.config(state='normal')
        mode = self.con_mode.get()
        try:
            if mode == 'bin2hex':
                result = des_controller.executeBin2Hex(data)
            else:
                result = des_controller.executeHex2Bin(data)
            self.con_textbox.insert(tk.END, f'{result}')
        except ValueError as ve:
            self.con_textbox.insert(tk.END, f'Error: {ve}')
        except Exception as e:
            self.con_textbox.insert(tk.END, f'An unexpected error occurred: {e}')
        self.con_textbox.config(state='disabled')

    def toolFunction(self):
        block_data = self.tool_input_text.get()
        self.tool_output_text.config(state='normal')
        self.tool_output_text.delete('1.0', tk.END)
        try:
            if self.current_function == 'IP':
                result = des_controller.executeIP(block_data)
                self.tool_output_text.insert(tk.END, f'{result}')
            elif self.current_function == 'FP':
                result = des_controller.executeFP(block_data)
                self.tool_output_text.insert(tk.END, f'{result}')
            elif self.current_function == 'E':
                result = des_controller.executeExpansion(block_data)
                self.tool_output_text.insert(tk.END, f'{result}')
            elif self.current_function == 'KG':
                result = des_controller.executeGenKey(block_data)
                detailed_keys = [f'Key {i+1}: {round_key}' for i, round_key in enumerate(result)]
                self.tool_output_text.insert(tk.END, '\n'.join(detailed_keys))
            elif self.current_function == 'S':
                result = des_controller.executeSubstitution(block_data)
                self.tool_output_text.insert(tk.END, f'{result}')
            elif self.current_function == 'P':
                result = des_controller.executePermutation(block_data)
                self.tool_output_text.insert(tk.END, f'{result}')
            else:
                self.tool_output_text.insert(tk.END, 'Please select a function first')
        except ValueError as ve:
            self.tool_output_text.insert(tk.END, f'Error: {ve}')
        except Exception as e:
            self.tool_output_text.insert(tk.END, f'An unexpected error occurred: {e}')
        self.tool_output_text.config(state='disabled')

    def showAbout(self):
        about_window = tk.Toplevel(self.root)
        about_window.title('About')
        width, height = 400, 400
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        x = (screen_width // 2) - (width // 2)
        y = (screen_height // 2) - (height // 2)
        about_window.geometry(f'{width}x{height}+{x}+{y}')
        about_window.resizable(False, False)
        about_window.configure(bg=COLOR['LightGrey'])
        about_label1 = Label(about_window, text='Mini DES Tool', font=('Arial', 12), bg=COLOR['LightGrey'])
        about_label2 = Label(about_window, text=about_text1, justify='left', anchor='w', wraplength=350, padx=10, font=('Arial', 12), bg=COLOR['LightGrey'])
        about_label3 = Label(about_window, text=about_text2, justify='left', anchor='w', wraplength=350, padx=10, font=('Arial', 12), bg=COLOR['LightGrey'])
        about_label1.pack(pady=10)
        about_label2.pack(pady=10)
        about_label3.pack(pady=10)
        link_label = Label(about_window, text='Visit my GitHub', fg=COLOR['Blue'], cursor='hand2', font=('Arial', 10, 'underline'), bg=COLOR['LightGrey'])
        link_label.pack(pady=5)
        link_label.bind('<Button-1>', lambda e: webbrowser.open('https://github.com/nhanvatphu04/desdhti16a4_225not'))
