"""
Manages loading, adding, editing, and deleting transactions.
"""
from operator import index
from random import choice

import pandas as pd

# View all Transactions
def view_all_transactions(sampledata):
    # Load the file
    df = pd.read_csv("sampledata.csv")
    print(df)

# View Transactions by Date Range
def filter_transactions_by_date(sampledata):
    # Load the file
    df = pd.read_csv("sampledata.csv")

    # Convert the date to datetime format
    df["Date"] = pd.to_datetime(df["Date"])

    # Enable the option for the user to enter the start and end dates
    start_date = input("Enter the start date (YYYY-MM-DD): ")
    end_date = input("Enter the end date (YYYY-MM-DD): ")

    # Filter by dates
    filtered = df[(df["Date"] >= start_date) & (df["Date"] <= end_date)]

    # Print
    print(f"--- Transactions from {start_date} to {end_date} ---")

    if filtered.empty:
        print("The transaction was not found within this range.")

    # To print the results
    else:
        print(filtered.to_string(index=False))


# Add a Transaction

def add_transaction(sampledata):
    # Load the file
    df = pd.read_csv("sampledata.csv")

    # Ask the user for the data they want to add
    date = input("Enter the transaction date (YYYY-MM-DD): ")
    category = input("Enter the category: ")
    description = input("Enter the description: ")
    amount = input("Enter the amount: ")
    trans_type = input("Enter te type (Expense/Income): ")

    # Create new DataFrame with the new transaction
    new_transaction = pd.DataFrame({
        "Date": [date],
        "Category": [category],
        "Description": [description],
        "Amount": [amount],
        "Type": [trans_type]
    })

    # Add the new transaction to the existing DataFrame
    df = pd.concat([df, new_transaction], ignore_index = True)


# Edit a Transaction

def edit_transaction(sampledata):
    # Load the file
    df = pd.read_csv("sampledata.csv")

    # Show existing transactions with index
    print("Existing Transactions:")
    print(df.reset_index().to_string(index = False))

    # Ask the user for the index of the transaction to edit
    index_transaction = int(input("Enter the index of the transaction to edit: "))

    # If the user enters an index that doesn't exist
    if index_transaction < 0 or index_transaction >= len(df):
        print("Invalid transaction")
        return

    # Show the current transactions
    print("Current transactions:")
    print(df.iloc[index_transaction])

    # Ask for the new information
    new_date = input("Enter new date (YYYY-MM-DD) or press Enter to keep current: ") or df.at[index_transaction, "Date"]
    new_category = input("Enter new category or press Enter to keep current: ") or df.at[index_transaction, "Category"]
    new_description = input("Enter new description or press Enter to keep current: ") or df.at[index_transaction, "Description"]
    new_amount = input("Enter new amount or press Enter to keep current: ") or df.at[index_transaction, "Amount"]
    new_type = input("Enter new type (Expense/Income) or press Enter to keep current: ") or df.at[index_transaction, "Type"]

    # Apply changes
    df.at[index_transaction, "Date"] = new_date
    df.at[index_transaction, "Category"] = new_category
    df.at[index_transaction, "Description"] = new_description
    df.at[index_transaction, "Amount"] = float(new_amount)
    df.at[index_transaction, "Type"] = new_type

    # Show the new DataFrame with the new information
    print("Updated Transactions:")
    print(df.reset_index().to_string(index=False))


# Delete a Transaction

def delete_transaction(sampledata):
    # Load the file
    df = pd.read_csv("sampledata.csv")

    # Show existing transactions with index
    print("Existing Transactions:")
    print(df.reset_index().to_string(index=False))

    # Ask the user for the index of the transaction to delete
    index_transaction = int(input("Enter the index of the transaction to delete: "))

    # If the user enters an index that doesn't exist
    if index_transaction < 0 or index_transaction >= len(df):
        print("Invalid transaction")
        return

    # Delete the transaction
    df = df.drop(index_transaction).reset_index(drop = True)

    # Show the new DataFrame with the new information
    print("Updated Transactions:")
    print(df.reset_index().to_string(index=False))


# Initial menu display
def main_menu():
    while True:
        print("--- Personal Finance Tracker ---")
        print("0. Import a CSV File")
        print("1. View All Transactions")
        print("2. View Transactions by Date Range")
        print("3. Add a Transaction")
        print("4. Edit a Transaction")
        print("5. Delete a Transaction")
        print("6. Analyze Spending by Category")
        print("7. Calculate Average Monthly Spending")
        print("8. Show Top Spending Category")
        print("9. Visualize Monthly Spending Trend")
        print("10. Save Transactions to CSV")
        print("11. Exit")

        try:
            option = int(input("Choose an option (0-11): "))
            if option == 0:
                import_csv_file()
            elif option == 1:
                view_all_transactions()
            elif option == 2:
                filter_transactions_by_date()
            elif option == 3:
                add_transaction()
            elif option == 4:
                edit_transaction()
            elif option == 5:
                delete_transaction()
            elif option == 6:
                spending_category()
            elif option == 7:
                average_spending_month()
            elif option == 8:
                top_spending_category()
            elif option == 9:

            elif option == 10:
                export_csv_file()
            elif option == 11:
                print("Goodbye!")
                break
            else:
                print("Invalid option. Please choose a number between 0 and 11")

# To ensure that the correct file is uploaded and the processing works without errors
sampledata = "sampledata.csv"
main_menu()
view_all_transactions(sampledata)
filter_transactions_by_date(sampledata)
add_transaction(sampledata)
edit_transaction(sampledata)
delete_transaction(sampledata)