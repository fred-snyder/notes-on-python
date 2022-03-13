import pandas as pd

# https://www.kaggle.com/residentmario/creating-reading-and-writing
# https://www.kaggle.com/fredsnyder/exercise-creating-reading-and-writing/edit

fruits = pd.DataFrame({
    "Apples": [30],
    "Bananas": [21],
})

fruit_sales = pd.DataFrame({
    "Apples": [35, 41],
    "Bananas": [21, 34],
}, index=["2017 Sales", "2018 Sales"])

print(fruit_sales)
