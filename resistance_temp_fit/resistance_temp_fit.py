import xlrd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import chi_squared


# File to open:
path = './log_201903060933_600ms.xls'
# Column titles; start the column with title
# end the column with an empty cell at the bottom
# the program will find the column with the title.
x_tag = 'Input 1'
y_tag = 'Input 3'


resistances, temps = [], []
workbook = xlrd.open_workbook(path)
sheet = workbook.sheet_by_index(0)


""" Returns tuple (R, C) as the row and column number of first entry """
def find_x_tag():
    for i in range(sheet.nrows):
        for j in  range(sheet.ncols):
            if sheet.cell_value(i, j) == x_tag:
                return i + 1, j
    print('x_tag is not found!')        

def find_y_tag():
    for i in range(sheet.nrows):
        for j in  range(sheet.ncols):
            if sheet.cell_value(i, j) == y_tag:
                return i + 1, j
    print('y_tag is not found!')        

""" Not important to user. Helper function to find count rows in a column. """
def count_rows(start_row, col):
    for i in range(start_row, sheet.nrows):
        if sheet.cell_type(i, col) == xlrd.XL_CELL_EMPTY:
            return i
    return sheet.nrows

""" Not important to user. Populate an array with data starting at index (row, col). """        
def populate(start_row, col, array):
    end_row = count_rows(start_row, col)
    for i in range(start_row, end_row):
        array.append(sheet.cell_value(i, col))

""" Returns a function that takes in an array x and outputs its result.
    Param is the coeff array computed from np.polyfit """ 
def make_func(coeffs):
    if len(coeffs) == 0:
        return lambda x : 0
    else:
        return lambda x : coeffs[0] * np.power(x, len(coeffs) - 1) + make_func(coeffs[1:])(x)
        

def chi_squared(actual, expected):
    return chi_squared(actual, expected)


# Find row and column number of the x and y entries:
x_row, x_col = find_x_tag()
y_row, y_col = find_y_tag()

# Populate arrays:
populate(x_row, x_col, resistances)
populate(y_row, y_col, temps)

# Logarithm scale:
log_resistances = np.log(resistances)
log_temps = np.log(temps)

# Find coefficient array. Degree can be changed:
coeffs = np.polyfit(log_resistances, log_temps, 1)
# Make a polynomial function based on the coefficient array:
func = make_func(coeffs)

# Show coefficients in terminal:
print(coeffs)

# Graphing
fig = plt.figure()
plt.xlabel('log(resistance)')
plt.ylabel('log(temperature)')
plt.scatter(log_resistances, log_temps, s=0.5, color='red')
predicted = func(log_resistances)

plt.plot(log_resistances, predicted)
plt.show()

