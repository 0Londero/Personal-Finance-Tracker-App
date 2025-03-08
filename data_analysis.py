"""
Analyzes spending by category, calculates average spending, and identifies top spending categories.
"""

# Imports
import pandas
import pandas as pd


# 3 - SPENDING ANALYSIS
# Analyze Spending by Category: Display total spending for each category.
def spending_category(user_csv):
    return user_csv.groupby('Category')['Amount'].sum()


# Calculate Average Monthly Spending: Show average spending per month.
def average_spending_month(user_csv):
    user_csv['Date'] = pd.to_datetime(user_csv['Date']) # Convert to datetime
    user_csv['Month'] = user_csv['Date'].dt.month # Month as a new column
    return user_csv.groupby('Month')['Amount'].mean()


# Show Top Spending Category: Identify the category with the highest total spending.
def top_spending_category(user_csv):
    spending_by_category = user_csv.groupby('Category')['Amount'].sum()
    top_category = spending_by_category.idxmax()  # Get category with max spending
    top_amount = spending_by_category.max()  # Get max spending amount
    return top_category, top_amount