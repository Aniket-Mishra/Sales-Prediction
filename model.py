import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt
import pickle # dump model into a pkl file
from sklearn.linear_model import LinearRegression

df = pd.read_csv('custom_sales_data.csv')

df['rating'].fillna(0, inplace = True) # Replacing all missing values with 0

X = df.iloc[:, :3] # Up to column Month 2 

def to_int(name):
    names_dict = {'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9, 0: 0}
    return names_dict[name]

X['rating'] = X['rating'].apply(lambda x: to_int(x))

y = df.loc[:, 'sales_in_month_3']
print(y)

linear_regressor = LinearRegression()

linear_regressor.fit(X, y)

pickle.dump(linear_regressor, open('model.pkl', 'wb'))

model = pickle.load(open('model.pkl', 'rb'))

print(model.predict([[4,500,600]]))