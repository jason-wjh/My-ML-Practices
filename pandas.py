# import pandas as pd
import pandas as pd
 
# list of strings
lst = ['a', 'b', 'v', 'd', 'e', 'f', 'g']
 
# Calling DataFrame constructor on list
df = pd.DataFrame(lst)
print(df)

###
# intialise data of lists.
data = {'Name':['a', 'aa', 'aaa', 'aaaa'],
        'Age':[20, 21, 22, 23]}
 
# Create DataFrame
df = pd.DataFrame(data)
 
# Print the output.
print(df)

###
# Define a dictionary containing employee data
data = {'Name':['a', 'aa', 'aaa', 'aaaa'],
        'Age':[20, 21, 22, 23]}
        'Address':['bb', 'cc', 'dd', 'ee'],
        'Qualification':['ff', 'gg', 'hh', 'oo']}
 
# Convert the dictionary into DataFrame 
df = pd.DataFrame(data)
 
# select two columns
print(df[['Name', 'Age']])


###

# making data frame from csv file
data = pd.read_csv("test.csv", index_col ="Name")
 
# retrieving row by loc method
first = data.loc["aa"]
second = data.loc["bb"]
 
 
print(first, "\n\n\n", second)

###
# making data frame from csv file
data = pd.read_csv("test.csv", index_col ="Name")
 
# retrieving columns by indexing operator
first = data["Age"]
 
print(first)

# retrieving rows by iloc method 
row2 = data.iloc[3] 

print(row2)

###
# dictionary of lists
dict = {'First':[100, 90, np.nan, 95],
        'Second': [30, 45, 56, np.nan],
        'Third':[np.nan, 40, 80, 98]}
 
# creating a dataframe from list
df = pd.DataFrame(dict)
 
# using isnull() function  
df.isnull()


###
# dictionary of lists
dict = {'First':[100, 90, np.nan, 95],
        'Second': [30, 45, 56, np.nan],
        'Third:[np.nan, 40, 80, 98]}
 
# creating a dataframe from dictionary
df = pd.DataFrame(dict)
 
# filling missing value using fillna()  
df.fillna(0)

###
# dictionary of lists
dict = {'First':[100, 90, np.nan, 95],
        'Second': [30, np.nan, 45, 56],
        'Third':[52, 40, 80, 98],
        'Fourth':[np.nan, np.nan, np.nan, 65]}
 
# creating a dataframe from dictionary
df = pd.DataFrame(dict)
 
# using dropna() function  
df.dropna()
