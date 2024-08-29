import pandas as pd

def age_matcher(n):
        if n < 4:
                return "1Y"
        elif n < 7: 
                return "4Y"
        elif n < 10:
                return "7Y"
        elif n < 13:
                return "10Y"
        elif n < 16:
                return "13Y"
        elif n < 19:
                return "16Y"
        elif n < 31:
                return "19Y"
        elif n < 51:
                return "31Y"
        elif n < 71:
                return "51Y"
        else:
                return "71Y"

data = pd.read_excel(r'./dietary_reference_intakes.xlsx', header=1)
df = pd.DataFrame(data)

age = age_matcher(int(input("enter age: ")))                     #輸入年齡、轉換成相符區間
substance = input("enter nutrient: ")

a = df.where(df==age).dropna(how='all').dropna(axis=1)            #比對年齡、找row
amount = int(df.loc[a.index, substance])                             #找column
unit = df.loc[0, substance]                                          #找單位

print(amount, unit)
#print("原資料：\n", df)