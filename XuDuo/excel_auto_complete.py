#!/usr/bin/python
# -*- coding:utf-8 -*-
from xlrd import open_workbook
from xlwt import Workbook
from xlutils.copy import copy

rb = open_workbook('data.xls', 'utf-8')
wb = copy(rb)

sh = wb.get_sheet(0)
s = rb.sheet_by_index(0)
cols = s.ncols
rows = s.nrows

temp = 0
for cx in range(cols):
	for rx in range(rows):
		if s.cell_value(rowx = rx, colx = cx).encode('utf-8') != "":
			temp = s.cell_value(rowx = rx, colx = cx).encode('utf-8')
			print(temp)
		else:
			sh.write(rx, cx, unicode(temp, 'utf-8'))

wb.save('data.xls')