"""
The main script that runs the app and handles the user interface.
"""
# Imports
from data_analysis import *
from data_management import *

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


def main_menu():
    user_csv = None

    while True:
        print("\n--- Personal Finance Tracker ---")
        print("0. Import a CSV File")
        print("1. View All Transactions")
        print("2. View Transactions by Date Range")
        print("3. Add a Transaction")
        print("4. Edit a Transaction")
        print("5. Delete a Transaction")
        print("6. Analyze Spending by Category")
        print("7. Calculate Average Monthly Spending")
        print("8. Show Top Spending Category")
        print("9. (Option Missing)")
        print("10. Save Transactions to CSV")
        print("11. Exit")

        try:
            option = int(input("Choose an option (0-11): "))

            if option == 0:
                user_csv = import_csv_file()
                print("CSV file imported successfully!")

            elif option in [1, 2, 3, 4, 5, 6, 7, 8, 10]:
                if user_csv is None:
                    print("Please import a CSV file first (Option 0).")
                    continue

                if option == 1:
                    view_all_transactions(user_csv)
                elif option == 2:
                    filter_transactions_by_date(user_csv)
                elif option == 3:
                    add_transaction(user_csv)
                elif option == 4:
                    edit_transaction(user_csv)
                elif option == 5:
                    delete_transaction(user_csv)
                elif option == 6:
                    spending_category(user_csv)
                elif option == 7:
                    average_spending_month(user_csv)
                elif option == 8:
                    top_spending_category(user_csv)
                elif option == 10:
                    export_csv_file(user_csv)

            elif option == 11:
                print("Goodbye!")
                break

            else:
                print("Invalid option. Please choose a number between 0 and 11.")

        except ValueError:
            print("Invalid input. Please enter a number between 0 and 11.")

main_menu()