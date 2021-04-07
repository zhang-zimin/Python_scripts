import openpyxl

filenames=os.listdir(r'D:\python\root\Scripts\4-6')
for file in filenames:
    if '.xlsm' in file:
        workbook = openpyxl.load_workbook(f'{file}',keep_vba=False)
        file = file.strip('.xlsm')
        workbook.save(fr"{file}.xlsx")
