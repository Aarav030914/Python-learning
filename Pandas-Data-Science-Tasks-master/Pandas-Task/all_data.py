import pandas
import os

data = pandas.read_csv("./Sales_Data/Sales_April_2019.csv")
sales_files = [file for file in os.listdir("./Sales_Data")]

# Merging all the sales data into one file
all_month_data = pandas.DataFrame()
for file in sales_files:
    df = pandas.read_csv("./Sales_Data/"+file)
    all_month_data = pandas.concat([all_month_data, df])
# Adding a month column to the dataframe.

# all_month_data.to_csv("all_month_sales_data.csv")
print(all_month_data.head())


