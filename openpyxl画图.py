import os
import pandas as pd
from openpyxl.drawing.text import CharacterProperties
from openpyxl import Workbook
from openpyxl.utils.dataframe import dataframe_to_rows
from openpyxl.chart import (
    ScatterChart,
    Reference,
    Series,
)

def getfiles():
    files = []
    filenames=os.listdir(r'D:\python\root\Scripts\4-6')
    for file in filenames:
        if '.xlsx' in file:
            files.append(file)
    return files

for path in getfiles():
    wb = Workbook()
    ws = wb.active

    data = pd.read_excel(path,sheet_name='Sheet1',header=None)
    for row in dataframe_to_rows(data[[0,1]],index=False,header=False):
        ws.append(row)

    chart = ScatterChart()
    chart.x_axis.title = '时间/s'
    chart.y_axis.title = '水位/m'

    xvalues = Reference(ws, min_col=1, min_row=1, max_row=len(data))
    values = Reference(ws, min_col=2, min_row=1, max_row=len(data))
    series = Series(values, xvalues,title_from_data=False)
    series.marker.symbol = "circle"
    series.marker.size = 2
    series.graphicalProperties.line.noFill=True
    chart.series.append(series)
    chart.legend = None
    cp = CharacterProperties(sz=100)  # Where size goes from 100 till 40000
    ws.add_chart(chart, "A10")

    wb.save(fr"D:\python\root\Scripts\4-6\图表\{path}")
