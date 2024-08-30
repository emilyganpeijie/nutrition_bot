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

def dri_matcher(age, substance, kind):
        data = pd.read_excel(r'./dietary_reference_intakes.xlsx', header=1) 
        df = pd.DataFrame(data)
        
        if kind:
                a = df.where(df==age).dropna(how='all').dropna(axis=1)            #比對年齡、找row
                amount = int(df.loc[a.index, substance])                             #找column
                print("a.index", a.index)
                unit = df.loc[0, substance]                                          #找單位
                return amount, unit
        else:
                return "全部印"


kind = True                                                    # kind: [True = specific, False = all nutrients]
age = age_matcher(int(input("enter age: ")))                     # age in
substance = input("enter nutrient: ")                            # nutrient in

if kind:
        print(dri_matcher(age, substance, kind)[0], dri_matcher(age, substance, kind)[1])
else:
        print(dri_matcher(age, substance, kind))

print(age)
data = pd.read_excel(r'./dietary_reference_intakes.xlsx', header=1) 
df = pd.DataFrame(data)
print("原資料：\n", df)
print("test: ", df.loc[5, substance])