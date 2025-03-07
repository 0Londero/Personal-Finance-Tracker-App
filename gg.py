ef edit_transaction(sampledata):
    # Load the file
    df = pd.read_csv("sampledata.csv")

    # Show existing transactions with index
    print("Existing Transactions:")
    print(df.reset_index().to_string(index = False))

    # Ask the user for the index of the transaction to edit
    index_transaction = input("Enter the index of the transaction to edit: ")

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
    df.at[index, "Date"] = new_date
    df.at[index, "Category"] = new_category
    df.at[index, "Description"] = new_description
    df.at[index, "Amount"] = new_amount
    df.at[index, "Type"] = new_type


# To ensure that the correct file is uploaded and the processing works without errors
sampledata = "sampledata.csv"

edit_transaction(sampledata)