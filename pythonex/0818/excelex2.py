'''
Created on 2020. 8. 18.

@author: GDJ24
excelex2.py : xlsx의 모든 sheet 읽기
'''

import openpyxl
filename = "sales_2015.xlsx"
book = openpyxl.load_workbook(filename)
for sheet in book.worksheets :
    data = []
    for row in sheet.rows :
        line = []
        for i,c in enumerate(row) :
            line.append(c.value)
        print(line)
        data.append(line)