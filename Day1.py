import pandas as pd 
import matplotlib as md
data = pd.read_csv(r'C:\Users\USER\Desktop\SMAIMX\SMDB.csv')


# bool_series = data.isna().any(axis=1)
# filtered_data = data[bool_series]
filtered_data=data.dropna()
Total=data['Max_pulse'].mean()
Total1=data['Max_pulse'].mode()
Total2=data['Max_pulse'].median()

print("mean: "+str(Total))
print("mode: \n")
print(Total1)
print("median: "+str(Total2))
# print(filtered_data)
histo=data['Max_pulse'].hist()
