# Tony Nguyen
# CPSC 222 01
# Data Assignment #5
# 11/08/2022
# I attempted half of the bonus question
# Description: This file contains functions and implementations as required by DA5

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

def data_loading(filename):
    # This function loads a .csv file to a Pandas DataFrame and set "ID" as its index
    # Parameter: filename - name of file
    # Return: a DataFrame

    data = pd.read_csv(filename)
    data.set_index("ID", inplace=True)
    return data

def string_check(string1, string2):
    # This function checks if string1 has its character matche at least 80% of string2
    # Parameter: string1 and string2 - two strings
    # Return: boolean

    count = 0
    check = False
    for i in range(len(string1)):
        if string1[i] in string2:
            count += 1
    if count > (len(string2) * 80 / 100): # 80% Exploratory CI
        check = True
    return check

def marital_status_cleaning(data):
    # This function performs data cleaning for "Marital Status" column
    # Parameter: data - a DataFrame
    # Return: void

    # Make sure fields are not case sensitive by remove the trailing white spaces in front of, behind, and between characters.
    # All characters are in lowercases
    for row in range(len(data["Marital Status"])):
        data.iloc[row, 2] = data.iloc[row, 2].lower()
        data.iloc[row, 2] = data.iloc[row, 2].strip()
        data.iloc[row, 2] = data.iloc[row, 2].replace(" ", "")
    
    # Search for absolute match and assign overwrite with pretty-print marital status
    for row in range(len(data["Marital Status"])):
        if "widow" in data.iloc[row, 2]:
            data.iloc[row, 2] = "Widowed"
        if "divorce" in data.iloc[row, 2]:
            data.iloc[row, 2] = "Divorced"
        if "separated" in data.iloc[row, 2]:
            data.iloc[row, 2] = "Separated"
        if "nevermarried" in data.iloc[row, 2]:
            data.iloc[row, 2] = "Never married"
        if "single" in data.iloc[row, 2]:
            data.iloc[row, 2] = "Never married"
        elif "married" in data.iloc[row, 2]:
            data.iloc[row, 2] = "Married"
    
    # Search for instances that have at least 80% match and assign the corresponding marital status
    for row in range(len(data["Marital Status"])):
        if data.iloc[row, 2] != "Widowed" and data.iloc[row, 2] != "Divorced" and data.iloc[row, 2] != "Separated" and data.iloc[row, 2] != "Never married" and data.iloc[row, 2] != "Married":
            if string_check(data.iloc[row, 2], "widowed") == True:
                data.iloc[row, 2] = "Widowed"
            if string_check(data.iloc[row, 2], "divorced") == True:
                data.iloc[row, 2] = "Divorced"
            if string_check(data.iloc[row, 2], "separated") == True:
                data.iloc[row, 2] = "Separated"
            if string_check(data.iloc[row, 2], "single") == True:
                data.iloc[row, 2] = "Never married"
            if string_check(data.iloc[row, 2], "married") == True:
                data.iloc[row, 2] = "Married"
            if string_check(data.iloc[row, 2], "engaged") == True:
                data.iloc[row, 2] = "Married"
    
    # Assign the remaining cases with np.NaN
    for row in range(len(data["Marital Status"])):
        if data.iloc[row, 2] != "Widowed" and data.iloc[row, 2] != "Divorced" and data.iloc[row, 2] != "Separated" and data.iloc[row, 2] != "Never married" and data.iloc[row, 2] != "Married":
            data.iloc[row, 2] = np.NaN
    
    # Manually assign with their respective status, as explained in PatientEDA.ipynb
    data.iloc[1899, 2] = "Divorced"
    data.iloc[3468, 2] = "Married"

def ric_cleaning(data):
    # This function replaces the numerical value in RIC column with text label
    # Parameter: string1 and string2 - two strings
    # Return: void

    ric_decoder = {1: "Stroke", 2: "TBI", 3: "NTBI", 4: "TSCI", 5: "NTSCI", 6: "Neuro",
                   7: "FracLE", 8: "ReplLE", 9: "Ortho", 10: "AMPLE", 11: "AMP-NLE",
                   12: "OsteoA", 13: "RheumA", 14: "Cardiac", 15: "Pulmonary", 16: "Pain",
                   17: "MMT-NBSCI", 18: "MMT-BSCI", 19: "GB", 20: "Misc", 21: "Burns"}
    
    for row in range(len(data["RIC"])):
        for key in ric_decoder:
            if data.iloc[row, 3] == key:
                data.iloc[row, 3] = ric_decoder[key]

def data_cleaning(data):
    # This function calls two cleaning methods
    # Parameter: data - a DataFrame
    # Return: a DataFrame

    marital_status_cleaning(data)
    ric_cleaning(data)
    data.to_csv("patient_data_cleaned.csv")
    return data

def data_aggregation(data):
    # This function performs statistical data aggregation 
    # Parameter: data - a DataFrame
    # Return: a Series contains the required information

    data_agg = pd.Series(dtype=float)

    data_agg["patients_total"] = data.shape[0]
    data_agg["males_total"] = data["Gender"].value_counts()["M"]
    data_agg["females_total"] = data["Gender"].value_counts()["F"]
    data_agg["married_total"] = data["Marital Status"].value_counts()["Married"]
    
    # Find the most common RIC
    grouped_by_RIC_size = data.groupby("RIC").size()
    grouped_by_RIC_size.sort_values(inplace=True)
    data_agg["most_common_RIC"] = grouped_by_RIC_size.index[-1]
    data_agg["most_common_RIC_total"] = grouped_by_RIC_size[-1]

    # Filter patients with Stroke
    stroke_patients_data = data[data.RIC == "Stroke"]
    data_agg["stroke_age_avg"] = stroke_patients_data["Age"].mean()
    data_agg["stroke_age_std"] = stroke_patients_data["Age"].std(ddof=1)

    # Filter male stroke patients
    data_agg["stroke_age_male_avg"] = stroke_patients_data[stroke_patients_data.Gender == "M"]["Age"].mean()
    data_agg["stroke_age_male_std"] = stroke_patients_data[stroke_patients_data.Gender == "M"]["Age"].std(ddof=1)

    # Filter female stroke patients
    data_agg["stroke_age_female_avg"] = stroke_patients_data[stroke_patients_data.Gender == "F"]["Age"].mean()
    data_agg["stroke_age_female_std"] = stroke_patients_data[stroke_patients_data.Gender == "F"]["Age"].std(ddof=1)
    return data_agg

def draw_histogram(data, RIC_type):
    # This function plots and shows a histogram graph based on given information
    # Parameter: data - a DataFrame, RIC_type - name of RIC categories
    # Return: void

    # Filter the "Age" column by RIC_type 
    x1 = data[data.RIC == RIC_type]["Age"]

    # Plot the graph
    plt.figure()
    ax = plt.subplot()
    n, bins, patches = ax.hist(x1, bins=30, density=True, color="green")
    plt.plot(bins, norm.pdf(bins, x1.mean(), x1.std(ddof=1)))
    plt.xlabel("Age (years)")
    plt.ylabel("Frequency")

    # Construct the title
    title = RIC_type + " Age (N=" + str(data[data.RIC == RIC_type]["Age"].count()) + "): " + r'$\mu$' + " = " + str(round(x1.mean(), 2)) + ", " + r'$\sigma$' +" = " + str(round(x1.std(ddof=1), 2))
    plt.title(title)

    plt.show()

def draw_scatter(data, RIC_type):
    # This function plots and shows a scatterplot graph based on given information
    # Parameter: data - a DataFrame, RIC_type - name of RIC categories
    # Return: void

    # Filter the dataset based on gender and admission or discharge FIM score
    male_a = data[(data.RIC == RIC_type) & (data.Gender == "M")]["Admission Total FIM Score"]
    male_d = data[(data.RIC == RIC_type) & (data.Gender == "M")]["Discharge Total FIM Score"]
    female_a = data[(data.RIC == RIC_type) & (data.Gender == "F")]["Admission Total FIM Score"]
    female_d = data[(data.RIC == RIC_type) & (data.Gender == "F")]["Discharge Total FIM Score"]

    # Construct the legend
    label_m = "Male (N=" + str(male_a.count()) + ")"
    label_f = "Female (N=" + str(female_a.count()) + ")"

    # Plot the graph
    plt.figure()
    ax = plt.subplot()
    ax.plot([0, 140], [0, 140], color="black", linestyle='--', linewidth=3, label="No Change")
    ax.scatter(female_a, female_d, s=100, color="red", marker="+", label=label_f)
    ax.scatter(male_a, male_d, s=100, color="blue", marker=".", label=label_m)

    # Set axes limits and labels
    ax.set_xlim(0, 140)
    ax.set_ylim(0, 140)
    plt.xlabel("Admission Total FIM Score")
    plt.ylabel("Discharge Total FIM Score")

    # Construct the title
    title = RIC_type + " (N=" + str(male_a.count() + female_a.count()) + ")"
    plt.title(title)

    plt.legend(loc=4)
    plt.show()

def check_instances(data):
    # This function check and plots two graphs if there is at least 60 instances per each RIC types, 
    # and in each RIC type, at least 80% instances must not be np.NaN
    # Parameter: data - a DataFrame, RIC_type - name of RIC categories
    # Return: void

    ric_decoder = {1: "Stroke", 2: "TBI", 3: "NTBI", 4: "TSCI", 5: "NTSCI", 6: "Neuro",
                   7: "FracLE", 8: "ReplLE", 9: "Ortho", 10: "AMPLE", 11: "AMP-NLE",
                   12: "OsteoA", 13: "RheumA", 14: "Cardiac", 15: "Pulmonary", 16: "Pain",
                   17: "MMT-NBSCI", 18: "MMT-BSCI", 19: "GB", 20: "Misc", 21: "Burns"}

    for item in ric_decoder:
        x1 = data[data.RIC == ric_decoder[item]]["Age"].notna().value_counts()
        for elem in x1:
            if elem >= 60 and elem >= (data[data.RIC == ric_decoder[item]]["Age"].count() * 80 / 100):
                draw_histogram(data, ric_decoder[item])
                draw_scatter(data, ric_decoder[item])