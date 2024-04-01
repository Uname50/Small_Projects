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
print(multiple_columns)