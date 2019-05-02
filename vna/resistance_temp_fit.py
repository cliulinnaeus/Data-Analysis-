print('hi')
# import xlrd
# import numpy as np
# import matplotlib.pyplot
# print('hi')
# path = './log_201903060933_600ms.xls'
# workbook = xlrd.open_workbook(path)
# sheet = workbook.sheet_by_index(0)
# resistances, temps = [], []
# x_tag  = 'Input 1'
# y_tag = 'Input 3'
# print('hi')



# """ Returns (R, C) as the row number of first entry and column"""
# def find_x_tag():
#     for i in range(sheet.nrows):
#         for j in  range(sheet.ncols):
#             if sheet.cell_value(i, j) == x_tag:
#                 return i + 1, j
#     print('x_tag is not found!')        

# def find_y_tag():
#     for i in range(sheet.nrows):
#         for j in  range(sheet.ncols):
#             if sheet.cell_value(i, j) == y_tag:
#                 return i + 1, j
#     print('y_tag is not found!')  

# def count_rows(start_row, col):
#     for i in range(start_row, sheet.nrows):
#         if sheet.cell_type(i, col) == xlrd.XL_CELL_EMPTY:
#             return i
#     return sheet.nrows


# """ Populate an array with data starting at index (row, col) """        
# def populate(start_row, col, array):
#     end_row = count_rows(start_row, col)
#     for i in range(start_row, end_row):
#         print(sheet.cell_value(i, col))
#         array.append(sheet.cell_value(i, col))


# x_row, x_col = find_x_tag()
# y_row, y_col = find_y_tag()

# populate(x_row, x_col, resistances)
# populate(y_row, y_col, temps)

# for i in resistances:
#     print(i)

