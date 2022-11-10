import numpy as np 
import openpyxl as pyxl

excel_path = ("../../../map_stuff/madison_cemeteries.xlsx")

# Load the worksheet
wb = pyxl.load_workbook(excel_path)

# Grab the active worksheet
sheet = wb.active
count = 0

# Iterate through columns and print each value
for row in sheet.iter_cols(min_row=1, min_col=1, max_col=3, values_only=True):
    #for cell in row:
    count += 1
    print(row)
    print()
    print("Iteration:", count)