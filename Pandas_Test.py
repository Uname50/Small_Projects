import pandas as pd

# define a dictionary to work with
test_dict = {
    'Name': ['Jane', 'John', 'Mary', 'Mark'],
    'ID': [1, 2, 3, 4], 
    'Department': ['Architect Group', 'Software Group', 'Design Team', 'Infrastructure'],
    'Salary': [100000, 80000, 50000, 60000]
}

# cast the dictionary to a pandas dataframe
test_dataframe = pd.DataFrame(test_dict)

# display the dataframe
# print(test_dataframe)

# select a column from the data frame and assign it to a variable
selected_column = test_dataframe[['Name']]
# print(selected_column)

# display the type of the selected_column variable 
# print(type(selected_column))

# access multiple columns of a dataframe 
multiple_columns = test_dataframe[['Name', 'ID', 'Department']]
# print(multiple_columns)


# Problem 1: Create a dataframe to display the result 
practice_dictionary = {
    'Student': ['David', 'Samuel', 'Terry', 'Evan'],
    'Age': [27, 24, 22, 32],
    'Country': ['UK', 'Canada', 'Spain', 'USA'],
    'Course': ['Python', 'Data Structures', 'Machine Learning', 'Web Development'],
    'Marks': [85, 72, 89, 76]
} 

practice_dataframe = pd.DataFrame(practice_dictionary)

# Problem 2: Retrieve the Marks column and assign it to a variable b
b = practice_dataframe[['Marks']]

# Problem 3: Retrieve the Country and Course columns and assign it to a variable c
c = practice_dataframe[['Country', 'Course']]


# To view the column as a series, just use one bracket
x = practice_dataframe['Student']
# print(x, type(x))

"""
loc() is a label-based data selecting method. Syntax: loc[row_label, column_label]
iloc() is an index-based selecting method. Syntax: iloc[row_index, column_index]
"""

# access the value on the first row and the first column
practice_dataframe.iloc[0, 0]

# access the value on the first row and the third column
practice_dataframe.iloc[0, 2]

# access the column using name
practice_dataframe.loc[0, 'Marks']

df2 = practice_dataframe
df2 = df2.set_index("Student")

# access first 5 rows of a dataframe
df2.head()

# access the column using name
print(df2.loc['David', 'Marks'])