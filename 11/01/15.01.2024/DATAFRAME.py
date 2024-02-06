import pandas as pd
"""CONVERTING PANDAS DATAFRAME TO NUMPY ARRAY"""
"""df = pd.DataFrame([[1, 2, 3], [4, 5, 6], [7, 8, 9]], columns=['a', 'b', 'c'])
print(df)
# convert dataframe to numpy array
arr = df.to_numpy()
print('\n NUMPY ARRAY\n________________________\n', arr) # Escape sequence for new line
#print(arr)
print(type(arr))"""
data = pd.read_csv("C:/Users/NEW USER/PycharmProjects/pythonProject6/nba.file.csv")
data.drop(inplace=True) # cleaning null values from the data
# Creating Dataframe from weight column
dff = pd.DataFrame(data['weight'].head())
# Converting the dataframe to a numpy array
app = dff.to_numpy()
print('\n Numpy Array\n______________________________\n', app)