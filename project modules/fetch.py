import mysql.connector
import xlsxwriter
import win32com.client as win32

playlist = []
fullname = 'Ankit Vishnoi'

def add_to_playlist(module):
    workbook = xlsxwriter.Workbook('Modules.xlsx')
    worksheet = workbook.add_worksheet()
    row = 0
    col = 0
    for i in range(0, len(module)):
        for j in  range(0, len(module[i])):
            worksheet.write(row, col, module[i][j])
            col += 1
        col = 0
        row+=1
    workbook.close()
    excel = win32.gencache.EnsureDispatch('Excel.Application')
    wb = excel.Workbooks.Open(r'C:\Users\superuser\PycharmProjects\Infosys\Modules.xlsx')
    ws = wb.Worksheets("Sheet1")
    ws.Columns.AutoFit()
    wb.Save()
    excel.Application.Quit()
    print("List of posts links has been saved successfully in Instagram.xlsx file")


conn = mysql.connector.connect(host='localhost', user='root', password='', db='erp')
cur = conn.cursor()
cur.execute(
    'CREATE TABLE IF NOT EXISTS Faculty_Module(Faculty VARCHAR(75),Module_Name VARCHAR(150),Platform VARCHAR(120), Launch_Date VARCHAR(10),Link VARCHAR(500))')

cur.execute('SELECT * from Faculty_Module where Faculty = %s', (fullname,))
module = cur.fetchall()
add_to_playlist(module)

