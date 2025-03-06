"""
Manages loading, adding, editing, and deleting transactions.
"""
import pandas as pd

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

# To ensure that the correct file is uploaded and the processing works without errors
sampledata = "sampledata.csv"
filter_transactions_by_date(sampledata)
add_transaction(sampledata)