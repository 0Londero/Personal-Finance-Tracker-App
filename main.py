"""
The main script that runs the app and handles the user interface.
"""
# Imports
from data_analysis import *
from budget_management import *
from data_management import *
from visualization import *

# Using tkinter (standard GUI library for Python) to import and export file.
from tkinter import filedialog
from tkinter import messagebox


# File import functionality
def import_csv_file():
    file_path = filedialog.askopenfilename(title="Select a File", filetypes=(("CSV Files", "*.csv"),))
    required_columns = {"Date", "Category", "Description", "Amount", "Type"}
    # if user don't select
    if not file_path:
        messagebox.showerror("Error", "No file selected")
        return None

    # check if the csv is valid for the application
    try:
        csv_file = pandas.read_csv(file_path)
        # The issubset() method returns True if all items in the set exists in the specified set, otherwise it returns False.
        missing_columns = required_columns - set(csv_file.columns)
        if not required_columns.issubset(csv_file.columns): # If not Error
            messagebox.showerror("Error", f"Invalid file! Missing columns: {','.join(missing_columns)}")
            return None

        # Valid
        messagebox.showinfo("Success", "File successfully imported.")
        return csv_file
    # If something went wrong (default exception)
    except Exception as bug:
        messagebox.showerror("Error", message= f"Something went wrong. Contact the developers.\n{bug}")
        return None


# File export functionality
def export_csv_file(csv_file):
    file_path = filedialog.asksaveasfilename(title="Select the path to save the file", defaultextension=".csv")

    # if user quit the save file window
    if not file_path:
        messagebox.showerror("Cancelled", "File save cancelled.")
        return

    try:
        csv_file.to_csv(file_path, index=False)
        messagebox.showinfo("Success", f"File successfully saved at: {file_path}.")
        print(f"\nFile successfully saved at: {file_path}.") # show on console
    except Exception as bug:
        messagebox.showerror("Error", f"Something went wrong. Contact the developers.\n{bug}")
        print(f"\nError saving file: {bug}.")