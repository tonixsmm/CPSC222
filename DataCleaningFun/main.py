import numpy as np
import pandas as pd

# LOAD THE DATA
df = pd.read_csv("pd_hoa_activities.csv", header=0) # we can ommit the header since the function will infer from it
print(df.shape) # print out the shape of the dataframe

# EXPLORE THE DATA
print(df.head(5)) # 5 rows at the start
print(df.tail(5)) # 5 rows at the end
print("Number of participants:", df.shape[0] // 9) # 9 is the number of tasks per pid
print(df.iloc[660:670, :])

# MISSING DATA
print(df["duration"].value_counts()["?"]) # count the number of ?
# Ways to handle missing value
# 1. Discard them. Never want to throw away data, depending on the size of the data
# 2. Fill them with the most frequent label or central tendency measure
# Replace the ? with np.NaN
# 3. Do nothing, and handel thru a case-by-case basis later
df.replace("?", np.NaN, inplace=True) #inplace is used to overwrite the original ? with np.NaN
print(df.isnull().sum())
df.dropna(inplace=True)
print(df.isnull().sum())
print(df.shape)
df.reset_index(inplace=True, drop=True) # set indexes again after dropping rows. drop=True to drop the old indexes
print(df.head(2))

# DECODE TASK
# Replace 1-8 and dot with more human readable/meaningful labels
task_decoder = {"1": "Water Plants", "2": "Fill Medication Dispenser", "3": "Wash Countertop", "4": "Sweep and Dust", "5": "Cook", "6": "Wash Hands", "7": "Perform TUG", "8": "Perform TUG w/Questions", "dot": "Day Out Task"}
def decode_task(df):
    ser = df["task"]
    for key in task_decoder:
        ser.replace(key, task_decoder[key], inplace=True)
decode_task(df)
print(df.head(10))

# CLEAN CLASS
def clean_class(df):
    ser = df["class"].copy()
    for i in range(len(ser)):
        currrent_class = str(ser.iloc[i])
        currrent_class = currrent_class.lower()
        if "hoa" in currrent_class or "healthy" in currrent_class:
            ser.iloc[i] = "HOA"
        elif "pd" in currrent_class or "parkinson" in currrent_class:
            ser.iloc[i] = "PD"
        else:
            print("Unrecognized status: %d, %s" %(i, currrent_class)) # %d: index and %s: class status
    df["class"] = ser

clean_class(df)
print(df.head(25))
print(df["class"].value_counts())

# CHECK COLUMN TYPES
for column in df.columns:
    print(column, df[column].dtype)

print(df["duration"].mean()) # logic error. duration vals are stored as strings
df["duration"] = df["duration"].astype(np.int32)
for column in df.columns:
    print(column, df[column].dtype)
print(type(df["duration"].sum()))
print(df["duration"].sum(), df["duration"].mean(), df["duration"].std())

# WRITE OUT THE CLEANED DATA
df.to_csv("pd_hoa_activities_cleaned.csv", index=False)