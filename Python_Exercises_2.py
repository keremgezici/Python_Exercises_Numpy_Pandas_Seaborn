##################################################
# Python Exercises-2
##################################################
import numpy as np
import seaborn as sns
import pandas as pd
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 1000)

#########################################
# Task 1: Identify the Titanic dataset from the Seaborn library.
#########################################
df = sns.load_dataset("titanic")
df.head()
df.info()

#########################################
# Task 2: Find the number of male and female passengers in the Titanic dataset described above.
#########################################
df["sex"].value_counts()

#########################################
# Task 3: Find the number of unique values for each column
#########################################
for col in df.columns:
    print(col ,"nunique değer :",  df[col].nunique())

#########################################
# Task 4: Find the number of unique values of the variable pclass.
#########################################
df["pclass"].nunique()

#########################################
# Task 5: Find the number of unique values of pclass and parch variables
#########################################
k=["pclass", "parch"]

for col in k :
    print(col , "nunique değer :", df[k].nunique())

#########################################
# Task 6: Check the type of the embarked variable. Change its type to category. Check the repetition type.
#########################################
df["embarked"].dtype
df["embarked"] = df["embarked"].astype("category")
df["embarked"].dtype

#########################################
# Task 7: Show all the sages of those with embarked value C.
#########################################
df[df["embarked"]=="C"]

#########################################
# Task 8: Show all the sages of those whose embarked value is not S.
#########################################
df[df["embarked"]!="S"]
df[df["embarked"]!="S"]["embarked"].unique()

#########################################
# Task9: Show all information for female passengers younger than 30 years old
#########################################
df.loc[(df["age"]<30) & (df["sex"]=="female"),:]

#########################################
# Task10: Show the information of passengers over 500 or 70 years of age.
#########################################
df.loc[(df["mouse"]>500) | (df["age"]>70) , :]

#########################################
# Task 11: Find the sum of the null values in each variable.
#########################################
df.isnull().sum()
df["sex"].isnull().sum()

for col in df.columns:
    print(col , "sum of nulls in variable : " , df[col].isnull().sum())

#########################################
# Task 12: remove the who variable from the dataframe.
#########################################
df.drop("who", axis=1, inplace=True)

#########################################
# Task 13: Fill the empty values in the deck variable with the most repeated value (mode) of the deck variable.
#########################################
df["deck"].isnull().sum()
df["deck"].mode()
df["deck"].mode()[0]
df["deck"].fillna(df["deck"].mode()[0], inplace=True)

#########################################
# Task 14: Fill the empty values in the age variable with the median of the age variable.
#########################################
df["age"].isnull().sum()
df["age"].fillna(df["age"].median(), inplace=True)

#########################################
# Task 15: Find the sum, count, mean values of the survived variable in the breakdown of Pclass and Gender variables.
#########################################
df.groupby(["pclass", "sex"]).agg({"survived": ["mean","sum","count"]})

#########################################
# Task 16: Task16: Write a function that will give a0 for those under 301, those equal to 30 and above. Create a variable named age_flag in the dataset using the function you wrote. (use the apply velambda constructs
#########################################
def age_30(age):
    if age<30:
        return 1
    else:
        return 0

df["age_flag"]=df["age"].apply(lambda x :age_30(x))

#########################################
# Task17: Define Tips dataset from Seaborn library
#########################################
df = sns.load_dataset("tips")
df.head()
df.shape

#########################################
# Task18: Find the sum, min, max and mean values of the total_bill value according to the categories (Dinner, Lunch) of the Time variable
#########################################
df.groupby(["time"]).agg({"total_bill": ["sum","min","max","mean"]})

#########################################
# Task19: Find the sum, min, max andmean values of the total_bill values according to the day and time.
#########################################
df.groupby(["day","time"]).agg({"total_bill": ["min","max","mean"]})

#########################################
# Task 20: Find the sum, min, max and average of the total_bill and type values of the female customers, according to the day of the lunch time.
#########################################
df[(df["time"]=="Lunch") & (df["sex"]=="Female")].groupby("day").agg({"total_bill": ["sum","mean","max","min","std"],
                                                                      "tip":  ["sum","mean","max","min"]})

#########################################
# Task 21:What is the average of orders with size less than i3 and total_bill greater than 10? (use loc)
#########################################
k=df.loc[(df["size"]<3) & (df["total_bill"]>10), : ]["total_bill"].mean()
k["total_bill"].mean()

#########################################
# Task22: Create a new variable called total_bill_tip_sum. Return the total of the total bill and tip paid by each customer
#########################################
df["total_bill_tip_sum"]=df["total_bill"]+df["tip"]

#########################################
# Task 23: Find the average of the total_bill variable for men and women separately.
# Create a new total_bill_flag variable that gives 0 for those below the averages you found, and one for those above and equal.
# Attention !! For females, the average for females will be taken into account, and for male, the average for males will be taken into account.
# start by writing a function that takes a gender and total_bill as a parameter. (will include if-else conditions)
#########################################
df = sns.load_dataset("Tips")
df.head()
f=df.loc[df["sex"]=="Female",:]
female_total_bill_mean=f["total_bill"].mean()
for i in f["total_bill"].index:
    if f["total_bill"][i]<female_total_bill_mean:
        f["total_bill"][i]=0
    else:
        f["total_bill"][i]=1
f.head()
m=df.loc[df["sex"]=="Male",:]
male_total_bill_mean=m["total_bill"].mean()
for i in m["total_bill"].index:
    if m["total_bill"][i]<male_total_bill_mean:
        m["total_bill"][i]=0
    else:
        m["total_bill"][i]=1
m.head()

total_bill_flag=pd.concat([f,m])
df["total_bill_flag"]=total_bill_flag.sort_index()
df

#########################################
# Task 24: Observe the number of below and above average by gender using the total_bill_flag variable.
#########################################
df.groupby(["sex","total_bill_flag"]).agg({"total_bill_flag":"count"})

#########################################
# Task 25: Sort according to the total_bill_tip_sum variable from largest to smallest and assign the first 30 people to a new dataframe.
#########################################
temp_df = df.sort_values("total_bill_tip_sum", ascending=False)[:30]
temp_df.head()
temp_df.shape
