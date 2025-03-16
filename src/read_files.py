import pandas as pd



excel_data = pd.read_excel("../data/transactions_excel.xlsx")
print(excel_data.shape)
print(excel_data.head())


wine_reviews = pd.read_csv("../data/transactions.csv")
print(wine_reviews.shape)
print(wine_reviews.head())


