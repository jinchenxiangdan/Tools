import xlrd
#
# Author: Shawn Jin
#



def read_sheet(sheet):

    for row_index in range(sheet.nrows):
        print(sheet.row_values(row_index))











#
# Global variables 
#
EXCEL_PATH = "~/Desktop/ee9a88b6b79e9e2b.xlsx"

def main():
    # open excel
    excel = xlrd.open_workbook(EXCEL_PATH, encoding_override='utf-8')
    # get sheets
    sheets = excel.sheets()
    # print(sheets)
    print("This file has {0} sheets".format(len(sheets)))

    # loop each sheets
    for sheet in sheets:
        print("Current sheet is {:<10s}\n\tit has {:2} rows and {:2} colums."
            .format(sheet.name, sheet.nrows, sheet.ncols))
    read_sheet(sheets[1])
if __name__ == "__main__":
    main()