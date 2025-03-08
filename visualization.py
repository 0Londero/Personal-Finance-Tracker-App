"""
Generates line, bar, and pie charts for data visualization.
"""

import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("sampledata.csv")
print(df)

df_expenses = df[df["Type"] == "Expense"]
df_grouped = df_expenses.groupby("Date")["Amount"].sum().reset_index()
plt.plot(df_grouped["Date"], df_grouped["Amount"], marker='o', linestyle='-', color='b')

plt.xlabel("Date")
plt.ylabel("Spending Amount ($)")
plt.title("Monthly Spending Trend")
plt.grid(True)

plt.xticks(rotation=45)
plt.show()

import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("sampledata.csv")
df_expenses = df[df["Type"] == "Expense"]
df_category = df_expenses.groupby("Category")["Amount"].sum().reset_index()
df_category = df_category.sort_values(by="Amount", ascending=False)
plt.bar(df_category["Category"], df_category["Amount"], color="r")
plt.xlabel("Category")
plt.ylabel("Total Spending ($)")
plt.title("Total Spending by Category")

plt.xticks(rotation=45)
plt.show()

import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("sampledata.csv")
df_expenses = df[df["Type"] == "Expense"]
df_category = df_expenses.groupby("Category")["Amount"].sum()
colors = ["#ff9999", "#66b3ff", "#99ff99", "#ffcc99", "#c2c2f0", "#ffb3e6"]
plt.pie(
    df_category,
    labels=df_category.index,
    autopct='%1.1f%%',
    startangle=140,
    colors=colors,
    wedgeprops={'edgecolor': 'black'}
)
plt.title("Percentage Distribution")
plt.show()