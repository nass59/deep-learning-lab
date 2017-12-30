from sklearn.linear_model import LinearRegression
import pandas as pd
import warnings

warnings.filterwarnings(action="ignore", module="scipy", message="^internal gelsd")

bmi_life_data = pd.read_csv('./bmi.csv')

print(bmi_life_data)

bmi_life_model = LinearRegression()
bmi_life_model.fit(bmi_life_data[['BMI']], bmi_life_data[['Life expectancy']])

laos_life_exp = bmi_life_model.predict(21.07931)
print(laos_life_exp)
