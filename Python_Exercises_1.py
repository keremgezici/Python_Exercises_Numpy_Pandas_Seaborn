#############################################
# Python Exercises
#############################################

#############################################
# TASK 1: Examine the types of data structures.
#############################################
x=8
y=3.2
z=8j+18
a="Hello World"
b=True
c=23<22
l=[1,2,3,4]
d={"Name":"Jake",
   "Age": 27,
   "Adress":"Downtown"}
t=("Machine Learning","Data Science")
s={"Python","Machine Learning","Data Science "}

list=[x,y,z,a,b,c,l,d,t,s]

for k in list:
    print(k,type(k))

#############################################
# TASK 2: Convert all letters of the given string expression to uppercase. Put space instead of commas and periods, separate them word by word.
#############################################
text="The goal is to turn data into information ,and information into insight."
k=[text]
k[0].upper()
k[0]=k[0].upper()
k[0]
k[0].split()
new_text=text.upper()
new_text
new_text.split()

#############################################
# TASK 3: Do the following tasks for the given list.
#############################################
lst = ["D","A","T","A","S","C","I","E","N","C","E"]

# Step 1: Look at the number of elements of the given list.
len(lst)

# Step 2: Call the elements at index zero and ten.
lst[0]
lst[10]

# Step 3: Create a list ["D","A","T","A"] from the given list.

data_list = lst[0:4]
data_list

# Step 4: Delete the element in the eighth index.

lst.pop(8)
lst

# Step 5: Add a new element.

lst.append(101)
lst


# Step 6: Re-add element "N" to the eighth index.

lst.insert(8, "N")
lst



#############################################
# TASK 4: Apply the following steps to the given dictionary structure.
#############################################

dict = {'Christian': ["America",18],
        'Daisy':["England",12],
        'Antonio':["Spain",22],
        'Dante':["Italy",25]}


# Step 1: Access the key values.

dict.keys()

# Step 2: Access the values.

dict.values()

# Step 3: Update the value 12 of the Daisy key to 13.
dict.update({"Daisy": ["England",13]})
dict

dict["Daisy"][1] = 14
dict


# Step 4: Add a new value whose key value is Ahmet value [Turkey,24].

dict.update({"Ahmet": ["Turkey", 24]})
dict

# Step 5: Delete Antonio from dictionary.

dict.pop("Antonio")
dict

#############################################
# TASK 5: Write a function that takes a list as an argument, assigns the odd and even numbers in the list to separate lists, and returns these lists.
#############################################
l=[2,13,18,93,22]
odd_list=[]
even_list=[]
def func(x):
    if x%2==0:
        even_list.append(x)
    else:
        odd_list.append(x)
    return odd_list,even_list
range(len(l))
for i in range(len(l)):
    func(l[i])

#############################################
# TASK 6: Using the List Comprehension structure, capitalize the names of the numeric variables in the car_crashes data and add NUM to the beginning.
#############################################

import seaborn as sns
import pandas as pd
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 500)

df = sns.load_dataset("car_crashes")
df.head()
df.columns
df.info()

[col for col in df.columns]

["NUM_" + col.upper() for col in df.columns if df[col].dtype != "O"]

# df["total"].dtype

["NUM_" + col.upper() if df[col].dtype != "O" else col.upper() for col in df.columns]


df.columns

# list comp. kullanmadan
l = []
for col in df.columns:
    if df[col].dtype != "O":
        l.append("NUM_" + col.upper())
    else:
        l.append(col.upper())

l

#############################################
# TASK 7: Using the List Comprehension structure, write "FLAG" after the names of the variables in the car_crashes data that do not contain "number" in their names.
#############################################
[col.upper() + "_FLAG" for col in df.columns if "no" not in col ]

[col.upper() + "_FLAG" if "no" not in col  else col.upper() for col in df.columns]

#############################################
# Task 8: Using the List Comprehension structure, select the names of the variables that are DIFFERENT from the variable names given below and create a new dataframe.
#############################################
og_list = ["abbrev", "no_previous"]
new_cols = [col for col in df.columns if col not in og_list]
new_df = df[new_cols]
# df[['total', 'speeding', 'alcohol', 'not_distracted', 'ins_premium', 'ins_losses']]
new_df.head()

df.head()
type(df[["total"]])
type(df["total"])

df[["total","speeding","ins_losses"]]
