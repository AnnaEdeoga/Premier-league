"""We can join, merge and concatenate dataframe using different methods.
In Dataframe we use df.merge(), df.join(), and df.concatenate() method
to help in joining, merging, concatenating different dataframe
_______________________________CONCATENATING DATAFRAME___________________________________
we can concatenate a dataframe in mant different ways: They are:
1. Concatenating dataframe using .concat()
2. Concatenating Dataframe by setting logic on axes
3. Concatenating Dataframe using .append()
4. Concatenating Dataframe by joining indexes
5. Concatenating Dataframe with group keys
6. Concatenating with mixed ndims."""
import pandas as pd

Dict1 = {'Name': ['Jail', 'Anuj', 'Jai', 'Princi'],
      'Age': [27, 24, 22, 32],
      'Address': ['Nagpur', 'Kanpur', 'Allahabad', 'Kannuaj'],
      'Qualification': ['MSc', 'MA', 'MCA', 'Phd']}
Dict2 = {"Name": ['Abhi', 'Ayushi', 'Dhira', 'Hitcsh'],
         "Age": [17, 14, 12, 52],
         "Address": ['Nagpur', ' Kanpur', 'Allahabad', 'Kannuaj'],
         "Qualification": ['B.Tech', 'B.A', 'B.Com', 'B.hons']}
# Convert the dictionary into Dataframe
df = pd.DataFrame(Dict1, index= [0, 1, 2, 3])
df1 = pd.DataFrame(Dict2, index= [4, 5, 6, 7])
print(df, "\n\n", df1)
# Using Concatenate, method
frames = [df, df1]
concatenate_frames = pd.concat(frames)
print(concatenate_frames)
# applying concatenate with axes
print()
concate_by_axes = pd.concat([df, df1], axis=0, join= 'inner')
print(concate_by_axes)
concate_by_axe = pd.concat([df, df1], axis=1, join= 'outer')
print(concate_by_axe)
concate_by_ax = pd.concat([df, df1], axis=0, sort= False)
print(concate_by_ax)
print()
print('APPLYING CONCAT WITH JOIN USING IGNORING INDEX')
# applying concat with join
pdr = pd.concat([df, df1], ignore_index=True)
print(pdr)
print()
print('Applying Concatenating Dataframes using Append')
appended_df = df._append(df1, sort=True)
print(appended_df)
"""__________________MERGING DATAFRAME__________________
there are four basic ways to handle the join in python
1. inner
2. left
3. right
4. outter
depending on which rows must retain their data.
Join can only be done on two dataframe at a time.
denoted as left and right table. The key is the common column that the two dataframe
will be joined on. It is a good practice to use keys which have unique values throughout
the column to avoid unintended duplication of row values.
Pandas provide a single function merge() as the entry point for all standard database,
join operations between dataframe object.
"""
# MERGING DATA WITH ONE UNIQUE KEY COMBINATION
"""data2 = {'key': ['k0', 'k1', 'k2', 'k3'],
         'name': ['Jai', ' Princi', 'Guarav', 'Anuj'],
         'age': [27, 24, 22, 32]}
data3 = {'key': ['k0', 'k1', 'k2', 'k3'],
         'address': ['Abuja', 'Lagos', 'Bauchi', 'Benue'],
         'Qualification': ['B.Tech', 'B.A', 'B.Com', 'B.Hons']}
dx = pd.DataFrame(data2)
dx1 = pd.DataFrame(data3)
# using .merge() function.
merged_data = pd.merge(dx,dx1, on='key')
print()
print('MERGING DATA WITH ONE UNIQUE KEY COMBINATION')
print(merged_data)"""
"""______________________ASSIGNMENT________________________
Concatenating with mixed ndims: one can concatenate a mix of Series and Dataframe.
The series will be transformed to Dataframes with the column name as the name of the series.
if unnamed series are passed they will be numbered consecutively. Passing ignore_index=True
will drop all name references."""
# Creating a dictionary
da1 = pd.DataFrame({'Domestic Animals': ['Dog', 'Goat', 'Horse', 'Chicken', 'Duck'],
                    'Wild Animals': ['Wolf', 'Lion', 'Tiger', 'Bear', 'Snake'],
                    'Aquatic Animals': ['Sea Lions', 'Jelly Fish', 'Shark', 'Dolphin', 'Wale']},
                   index=[1, 2, 3, 4, 5])
da2 = pd.DataFrame({'Amphibians': ['Frogs', 'Newts', 'Salamanders', 'Toads', 'Mudpuppy'],
                    'Birds': ['Falcons', 'Flamingos', 'Ostriches', 'Owls', 'Penguins'],
                    'Mammals': ['Humans', 'Elephants', 'Hamsters', 'Rabbits', 'Rhinoceroses']},
                   index=[6, 7, 8, 9, 10])
frames_1 = [da1, da2]
result = pd.concat(frames_1)
print(frames_1)
print(result)
result_1 = pd.concat(frames_1, keys=['A', 'B'])
print(result_1)
print(result_1.loc['B'])
# CONCATENATING USING MIXED NDIMS
S1 = pd.Series(['Turtles', 'Geckos', 'Tortoise', 'Crocodile', 'Sea Turtles'], name='Reptiles')
print(pd.concat([da1, S1], axis=1))
# Unknown Series when passed are numbered consecutively
S2 = pd.Series(['Donkey', 'Hippos', 'Deer', 'Camel', 'Wild Dog'])
print(pd.concat([da2, S2], axis=1))
