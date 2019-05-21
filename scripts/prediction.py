import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression

dataset = pd.read_csv('../scripts/mtcars.csv', header=0)
y = dataset.loc[:, dataset.columns == 'mpg']
x = dataset.loc[:, ['hp', 'cyl', 'disp']]
print(x.head())
print(y.head())

model_lr = LinearRegression()
model_lr.fit(x, y)


def predict(dict_values, col_imp=x.columns, model=model_lr):
    x = np.array([float(dict_values[col]) for col in col_imp])
    x = x.reshape(1,-1)
    y_pred = float(model.predict(x)[0])
    return y_pred


# print(predict({"hp": "160", "cyl": "4", "disp": "160"}))
