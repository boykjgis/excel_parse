import pandas as pd 

excel_path = ("../../../map_stuff/madison_cemeteries.xlsx")

table = pd.read_excel(excel_path, sheet_name = 'Sheet1',
                    header = 0,
                    index_col = 0,
                    usecols = 'A, C, D')

print(table)