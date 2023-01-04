#FILES
#a file stores data on your file system
#"on disk"

#Goal: read the content of data.csv into our python program memory. Eventually, store the content in a 2D list

#3-part file processing format template
#1. open the file
#2. process the file (e.g. read or write or sth else)
#3. close the file

#let use the function for practice


def load_line_from_file(filename):
    #filename is a string representing a path to file we want to work on
    #1. abosolute path: start with a drive in general
    #example: /Users/tony/Documents/Python Coding/CPSC222/FileFun
    #2. relative path: don't start with a drive, relative to the current working directory
    #use "pwd" with terminal
    infile = open(filename, "r") #r is the file read mode
    lines = infile.readlines()
    infile.close()
    return lines

def clean_lines(lines):
    for i in range(len(lines)):
        #lines[i] is a string
        lines[i] = lines[i].strip()

file_lines = load_line_from_file("data.csv") #relative path: in the same directory
print(file_lines)
clean_lines(file_lines)
print(file_lines)

#restructuring them into 2D list format
def restructure_data_into_model(lines):
    #lines is 1D
    table = []
    for line in lines:
        #line is a string in the CSV format
        #we're gonna split lines by the comma
        values = line.split(",")
        print(values)
        table.append(values)
    return table

table = restructure_data_into_model(file_lines)

def convert_column_into_numerical(table, col_index):
    for row in table:
        row[col_index] = int(row[col_index])

def printTable(table):
    for i in range(3):
        for j in range(3):
            print(table[i][j], end = "\t")
        print()

#convert numeric columns into numeric types
#store the header seperately from the data
header = table.pop(0)
print(header)
print(table)
convert_column_into_numerical(table, 1)
convert_column_into_numerical(table, 2)
print(table)
table.insert(0, header)
print(table)

#look into tabulate model
printTable(table)