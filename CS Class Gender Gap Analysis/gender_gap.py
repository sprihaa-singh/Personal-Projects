import pandas as pd
import matplotlib.pyplot as plt

df1 = pd.read_csv (r"20-21.csv")
df2 = pd.read_csv (r"21-22.csv")
df1_final=pd.read_csv (r"20-21_final.csv")

df2 = df2[["Description", "Male","Female"]]

df1 = df1[["Description", "Gender"]]

# design with code = intro, design w/ physical computing = intermediate

# Calculates the total number of students who fit in each category, making it easier to
# build a dataset in the format I want
print(df1[(df1["Gender"]==1) & (df1["Description"] == "Algorithms and Data Structure")].count())
print(df1[(df1["Gender"]==2) & (df1["Description"] == "Algorithms and Data Structure")].count())

print(df1[(df1["Gender"]==1) & (df1["Description"] == "Intermediate Programming")].count())
print(df1[(df1["Gender"]==2) & (df1["Description"] == "Intermediate Programming")].count())

print(df1[(df1["Gender"]==1) & (df1["Description"] == "Intro to Programming")].count())
print(df1[(df1["Gender"]==2) & (df1["Description"] == "Intro to Programming")].count())


print(df1[(df1["Gender"]==1) & (df1["Description"] == "AP Computer Science A")].count())
print(df1[(df1["Gender"]==2) & (df1["Description"] == "AP Computer Science A")].count())

print(df1[(df1["Gender"]==1) & (df1["Description"] == "Design & Fabrication Lab")].count())
print(df1[(df1["Gender"]==2) & (df1["Description"] == "Design & Fabrication Lab")].count())

print(df1[(df1["Gender"]==1) & (df1["Description"] == "Data Science")].count())
print(df1[(df1["Gender"]==2) & (df1["Description"] == "Data Science")].count())

print(df1[(df1["Gender"]==1) & (df1["Description"] == "Design Studio")].count())
print(df1[(df1["Gender"]==2) & (df1["Description"] == "Design Studio")].count())

for(i in range(len(df)))
    row = df.iloc[i]
df_gender = df1_final.groupby("male").sum()

df_gender.plot.pie(y="female", labels=df_gender.index)

plt.show()