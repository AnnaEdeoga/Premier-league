import pandas as pd
import xlsxwriter

import numpy

df= pd.read_excel("C:/Users/NEW USER/OneDrive/Documents/Premier League Table.xlsx")
print(df)
aver = lambda x:(x-x.mean())/x.std()*10
print(df["Goals Scored"].transform(aver))
#spt = lambda x: (x*2)-5
#print(df["Goal Scored"].transform(spt))
dc = pd.read_excel("C:/Users/NEW USER/OneDrive/Documents/Players Stat.xlsx")

df = pd.DataFrame({'Data': ['Books', 'Pencil', 'Shoes', 'Shirts', 'Trousers', 'Caps', 'Tv Set']})
writer = pd.ExcelWriter('pandasExcel.xlsx', engine='xlsxwriter')
# write a dataframe to the worksheet
df.to_excel(writer, sheet_name='Sheet1')
writer.close()
data1 = ['Math', 'Physics', 'Computer', 'Hindi', 'English', 'Chemistry']
data2 = [95, 78, 80, 80, 60, 95]
data3 = [90, 67, 78, 70, 65, 90]
# To create a pandas dataframe
dataframe = pd.DataFrame({'Subject': data1, 'Mid Term Exams': data2,
                         'End Term Exams': data3})
#dataframe
write_object = pd.ExcelWriter('Faith_Anna.xlsx', engine= 'xlsxwriter')
dataframe.to_excel(write_object, sheet_name = 'sheet1', startrow=1, header= False)
#write_object.close()
# create xlsxwriter worksheet object.
workbook_object = write_object.book
# create xlsxwriter worksheet object.
worksheet_object = write_object.sheets['sheet1']
# create a new format object to format cells.
# in the worksheet
head_format = workbook_object.add_format({'bold': True,
                                          'italic': True,
                                          'text_wrap': True,
                                          'valign': 'top',
                                          'font_color': 'red'})
#write_object.close()
for col_number, value in enumerate(dataframe.columns.values):
    worksheet_object.write(0, col_number +1, value, head_format)
write_object.close()


