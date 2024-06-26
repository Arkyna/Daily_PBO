import tkinter as tk
from tkinter import filedialog

def open_file():
    # Open a file document
    filepath = filedialog.askopenfilename(
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
    )
    if not filepath:
        return
    txt_edit.delete(1.0, tk.END)
    with open(filepath, "r") as input_file:
        text = input_file.read()
        txt_edit.insert(tk.END, text)
    window.title(f"Text Editor - {filepath}")

def save_file():
    # Save the currently opened file
    filepath = filedialog.asksaveasfilename(
        defaultextension="txt",
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")],
    )
    if not filepath:
        return
    with open(filepath, "w") as output_file:
        text = txt_edit.get(1.0, tk.END)
        output_file.write(text)
    window.title(f"Text Editor - {filepath}")

def close_file():
    # Close the currently opened file
    txt_edit.delete(1.0, tk.END)
    window.title("Text Editor")

# Creating the main window
window = tk.Tk()
window.title("Text Editor")

window.rowconfigure(0, minsize=800, weight= 1)
window.columnconfigure(1, minsize=800, weight=1)

# Widgets
txt_edit = tk.Text(window)
fr_buttons = tk.Frame(window)
btn_open = tk.Button(fr_buttons, text="Open", command=open_file)
btn_save = tk.Button(fr_buttons, text="Save As...", command=save_file)
btn_close = tk.Button(fr_buttons, text="Close", command=close_file)

# Widgets placements
btn_open.grid(row=0, column=0, sticky="ew", padx=5, pady=5)
btn_save.grid(row=1, column=0, sticky="ew", padx=5)
btn_close.grid(row=2, column=0, sticky="ew", padx=5)

fr_buttons.grid(row=0, column=0, sticky="ns")
txt_edit.grid(row=0, column=1, sticky="nsew")

#Event loop to keep the window open
window.mainloop()
