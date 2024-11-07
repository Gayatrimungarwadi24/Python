import pandas as pd

df=pd.read_csv("d:\\downloads\\diabetes.csv")
ser=pd.Series(df['BloodPressure'])
print(ser)
ser=pd.DataFrame(df['BloodPressure','Insulin','BMI','Age','Outcome'])
print(ser)