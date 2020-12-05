import os
import win32com.client as win32

def save_as_xlsx(fname):
    excel = win32.DispatchEx('Excel.Application')
    wb = excel.Workbooks.Open(fname)

    wb.SaveAs(fname+"x", FileFormat = 51)    #FileFormat = 51 is for .xlsx extension
    wb.Close()                               #FileFormat = 56 is for .xls extension
    excel.Application.Quit()


if __name__ == "__main__":
    package = "D:\\Data\\重合段单孔柱状图源文件\\"
    files = os.listdir(package)
    for fname in files:
        if fname.endswith(".xls"):
            save_as_xlsx(package + fname)