import numpy as np
import pandas as pd
"""CONVERTING PANDAS DATAFRAME TO NUMPY ARRAY"""
"""df = pd.DataFrame([[1, 2, 3], [4, 5, 6], [7, 8, 9]], columns=['a', 'b', 'c'])
print(df)
# convert dataframe to numpy array
arr = df.to_numpy()
print('\n NUMPY ARRAY\n________________________\n', arr) # Escape sequence for new line
#print(arr)
print(type(arr))
data = pd.read_csv("nba.file.csv")
data.dropna(inplace=True) # cleaning null values from the data
# Creating Dataframe from weight column
df = pd.DataFrame(data['Weight'].head(20))
# Converting the dataframe to a numpy array
app = df.to_numpy()
#print(df.to_numpy())
print('\n DATA FRAME TO NUMPY ARRAY\n__________________________\n', app)"""

"""PANDAS SERIES TO NUMPY ARRAY"""
"""# METHOD to be used is series.to_numpy
df = pd.Series(data['Weight']. head(20)) # to change your data to series you use the
# series method()
# Printing the data series
print(df)
# converting the pandas series to numpy array
series_to_numpy = df.to_numpy()
print(series_to_numpy"""

# HOW TO PERFORM SELECTION:
"""1. dealing with rows and columns
2. Multiple rows/column selection
3. Pyhton/Pandas extracting rows using loc[], iloc[] methods
4. indexing selection
5. Boolean indexing
6. Label and integer base slicing techinque"""
# makes dataframe
#data = pd.read_csv("nba.file.csv", index_col="Name")
#print(date)
# dropping passed columns.
#date.drop(["Team", "Weight"], axis=1, inplace= True)
#print(date.head(20))
#print(data[["Name", "Salary", "Number"]])
#da = date.loc(["Name", "Salary"], axis=1, inplace=True)
#print(da)
""" Selecting multiple columns in pandas can be done in four ways using
1. Using Basic Method
2. Using loc[]
3. using iloc[]
4. using s.ix"""
""" ASSIGNMENT
Convert from nd_array to series and how to convert from 
nd_array to dataframe. with examples 
data = pd.read_csv("nba.file.csv")
df = np.array(data[["Weight", "Salary", "Name"]].head(20))
print(df)
# TO CONVERT ND_ARRAY TO A PANDAS SERIES
#SP = pd.Series(df)
#print(SP)
 NOTE: converting from any of the method to a
  pandas series only requires a one dimensional array 
# TO CONVERT ND_ARRAY TO DATAFRAME
DF = pd.DataFrame(df)
print(DF)
print(data.columns[0:]) # this is used to know all the columns name in a data set
"""


"""USING LOC
   16/05/2024"""
# selecting multiple columns in pandas dataframe using loc function
""" Note: Loc can be used to select the number of rows to return from a dataframe, 
and also the number of columns"""
data = pd.read_csv("nba.file.csv")
df = pd.DataFrame(data)
# print(df)
"""print(df.loc[1:10,["Name", "Salary"]]) # this is to select and retrieve only name and salary
print(df.loc[0:, :]) # Loc is used to select rows and columns,
# hence this syntax produces all the rows and all the columns"""
""" Selecting multiple rows in pandas using *ILOC* 
i in iloc stand for index, as its only through index 
number that you can get the data you want"""
"""print()
print("ILOC")
print(data.iloc[1:5, 0:6])
print(data.iloc[1:10, 3:5])"""
# DATA MANIPULATION: ADDING NEW COLUMN TO EXISTING DATA FRAME IN PANDAS
# ADVANTAGE
""" 1. it makes the representation of data easy in rows and columns
2. it has an heterogenous data type, it allows you to stop different data type 
3. labeling: in pandas dataframe each rows and columns has a label(indexs and column name)
4. new table: it allows data manipulation and modification
5. power operations: dataframe in pandas provides various functions and methods for data analysis,
manipulation and exploration.
6. it is extensible: it can be customize and extended with additional functionalities through
libraries and user defined functions.
_______________________VARIOUS WAYS WE CAN NEW COLUMN TO EXISTING COLUMNS IN PANDAS___________
_______________________BELOW ARE THE VARIOUS WAYS_____________
1. By using dataframe.insert() method
2. By using dataframe.assign() method
3. By using dictionary
4. By using list
5. By using .loc()
"""
# DT = {"Name": ["Jai", "Princi", "Guarav", "Anuj"], "Height": [5.1, 6.2, 5.1, 5.2],
# "Qualification": ["MSC", "MA", "MSC", "MSC"]}
# AS = pd.DataFrame(DT)
# print(AS)
"""NOTE: dataframe.insert() method gives you the freedom to add a column 
at any position you like and not just at the end. 
it provide different options for inserting the column values"""
# print()
# print("USING DATAFRAME.ASSIGN() METHOD")
# AS.insert(2, "Age", [21, 23, 24, 21], True)
# print(AS)
""" Adding value to pandas data using assign() method, 
this will create a new dataframe entirely
_____________DATAFRAME.ASSIGN() METHOD____________"""
# print()
# print(" USING DATAFRAME.ASSIGN() METHOD")
# AS2 = AS.assign(Address= ["Delhi", "Bangalore", "Chennai", "Patna"])
# print(AS2)
# print()
# print("ADDING NEW COLUMN USING A LIST")
# Group = ["New york", " Washinton", "Texas", "Las Angelus"]
# AS2["Group"] = Group
# print(AS2)
"""CLASS-WORK
Add new column titled: course scores=[cit112:[75, 80, 50, 78] using a dictionary to the dataset"""
# print()
# print("ADDING COLUMNS USING DICTIONARY")
# Course_Score ={"Cit112":[75, 80, 50, 78]}
# AS2["Cit112"] = Course_Score["Cit112"]
# print(AS2)
"""ASSIGNMENT:
Research how to use .loc() method to add new columns"""
""" In order to to select rows and columns, we pass the desired labels.
The colon indicates that we want to select all the rows. In the column part, we specify
the labels of the columns to be selected. Since the dataframe does not have column temperament,
 pandas creates a new column"""
# print()
"""print(" USING .LOC() METHOD TO ADD NEW DATA")
Temperament = ["Sanguine", "Choleric", "Melancholic", "Phlegmatic"]
AS2.loc[:, "Temperament"] = Temperament
print(AS2)
AS2.loc[:, "Temperament"] = list("Sanguine,Choleric,Melancholic,Phlegmatic"
print(AS2)
fees = [607.9, 798.9, 709.8, 456.5]
state = ["NCT", "Karnataka", "Tamil Nadu", "Bihari"]
# Add multiple columns using dictionary assignment
new_data = {"Fees": fees, "State": state}
AS2 = AS2.assign(**new_data)
print(AS2)
da = AS2.drop(["Cit112", "Address"], axis= 1)
print(da)"""
"""________________________17.01.2024___________________________
HOW TO USE THE TRUNCATE() METHOD
PANDAS DATAFRAME.TRUNCATE() METHOD
It is used to truncate a series or dataframe before and after some index value.
this is an useful shorthand for boolean indexing base on index values above or below
certain treasholds.
 # _______________SYNTAX: DataFrame.Truncate(before = None, after= None, Axis = None, Copy= True)
 before means to truncate all rows before this index value.
 after means to truncate all rows after this index value.
 axis means Axis to truncate when you want specify either 0 or 1 but if not, it will
 truncate the index(rows) by default.
 copy means to return a copy of the truncated section."""
# create the index
"""index_ = pd.date_range('2010-10-09 08:45', periods= 4, freq= 'h')
AS2.index = index_ # set the index
print(AS2)
# Lets truncate entires before "2010-10-09 09:45:00"
# and after '2010-10-09 10:45:00' in the given data
result = AS2.truncate(before= '2010-10-09 09:45:00', after= '2010-10-09 10:45:00')
print(result)"""
"""_______________HOW TO USE THE TRUNCATE METHOD TO TRUNCATE SOME ENTRIES 
BEFORE AND AFTER THE PASS LABELS OF A GIVEN DATAFRAME """
# Creating the DataFrame
"""AS3 = pd.DataFrame({'A': [12, 4, 5, None, 1], 'B': [7, 2, 54, 3, None],
                    'C': [20, 16, 11, 3, 8], 'D': [14, 3, None, 2, 6]})
# Create the index
index_1 = ['Row_1', 'Row_2', 'Row_3', 'Row_4', 'Row_5']
AS3.index = index_1
print(AS3)
result_1 = AS3.truncate(before= 'Row_3', after= 'Row_4')
print(result_1)"""
""" __________________________ ASSIGNMENT ___________________________
Learn how to truncate data series with an example

Pandas series is a one dimensional ndarray with axis labels. The labels need not be unique but must be
a hashable type. The object supports both integer and label-based indexing and provides a host
of methods for performing operations involving the index.
  Hence, Pandas series() function is used to truncate a series or dataframe before
and after some index values 
# Use Series.truncate() function to truncate some data from series prior
# to given index label and after a given index label.
# Creating the series
sr = 2.7, 7.8, 17.0, 19.0000, 23.98888, 45.7, 78.1, 5.7, 4.5
si = pd.Series(sr)
# print the series
print(si)
# truncate data outside the given range
print(si.truncate(before= 2, after= 5))
___________________INTERATING OVER ROWS AND COLUMNS IN PANDAS DATAFRAME
we interact over dataframe like you interact python dictionary
we interact over the keys of the object
in pandas dataframe we can interact in two ways
1. Interacting over rows
2. Interacting over columns
 ___________________ INTERACTING OVER ROWS IN PANDAS_____________________
 In other t interact over rows in panda we canuse three functions
 a. iteritems()
 b. iterrows()
 c. itertuples()
 ______________________ITERROWS_________________
 This function returns each index values along with a series containing data for each row 
dict_01 = {'Name': ["Aparna", "Pankaj", "Sudhir", "Geeks"], "Degree": ["MBA", "BCA", "M.TECH", "MBA"],
           "Score": [90, 40, 80, 98]}
dx = pd.DataFrame(dict_01)
print(dx)
# interacting over rows using iteracting function for i, j in df.interrows():
for i, j in dx.iterrows():
    print(i,j)
    print()
read = pd.read_csv("nba.file.csv")
for column, row  in read.iterrows():
    print(column, row)
    print()
_____________USAGE OF ITERITEMS() METHOD # no longer in used or deprecated________________
for i in read._iter_column_arrays():
    print(i)
    print()
for row in read.itertuples(): # it takes the data and iterate through it then return each rows as a tuple
    print(row)
    print()"""
""" ______________________INTERACTING OVER COLUMNS___________________
pandas column interating: in other to interact over columns we need to create a list of dataframe column
and interact through the list to pull out the data list column
# Creating a list of dataframe columns.
columns = list(dict_01)
print(columns)
for i in columns:
    # print the third element of the column
    print(dict_01[i])
    print(dict_01[i][2])"""
""" ASSIGNMENT
Sorting dataframe with examples
Grouping data with examples """
# HOW TO SORT PANDAS DATAFRAME.
# importing pandas as pd
# creating and initializing a nested list
age_list = [['Ms. Anna', 1952, 8425333, 'Enugu'], ['Ms. Marleen', 1957, 9712569, 'Imo'],
            ['Ms. Faith', 1962, 6039390, 'Maiduguri'], ['Mr Charles', 1957, 8425333, 'Enugu'],
            ['Mr Jackson', 1957, 4310863, 'Delta'], ['Mr Francis', 1952, 9712569, 'Imo'],
            ['Mr David', 1957, 1984000, 'Adamawa']]
# creating a pandas dataframe
dy = pd.DataFrame(age_list, columns=['Name', 'Year', 'Population', 'Nigeria State'])
print(dy)
"""______In order to sort the data frame in pandas, the function 'sort value()'
is used. its can  sort the dataframe in ascending of descending order."""
# sorting by column 'Country'
"""print(dy.sort_values(by=['Nigeria State']))
# Sorting dataframe base of descending order in pandas
# sorting by column "Population"
print(dy.sort_values(by=['Population'], ascending= False))
an = pd.read_csv("employee_info.csv")
print(an.head(10))
# Creating a pandas Dataframe
print(an.sort_values(by=['name']).head(20))"""
"""___________SYNTAX FOR SORTING DATAFRAME__________________
Dataframe.sort_value(by): single/list of column names
axis = 0: o or index for rows and 1 or column for columns, 
ascending= True: Boolean value which sort Dataframe in ascending order if true 
and descending order if false, 
inplace= False: Boolean value makes changes in the passed dataframe itself if true, 
kind= 'quicksort': string which can have three inputs('quicksort',
'mergesort', 'heapsort') of algorithm used to sort dataframe,
na_position = 'last': this takes two string input 'last' or 'first' to 
set position of null values.)
"""
data = pd.read_csv("nba.file.csv")
dx = pd.DataFrame(data).tail(100)
#print(dx)
sorted = dx.sort_values("Name", axis=0, ascending= True, inplace=False, na_position='first')
print(sorted.tail(20))
sit = dx.sort_values("Salary", axis=0, ascending=True, inplace=False, na_position='first')
print(sit.head(20))

