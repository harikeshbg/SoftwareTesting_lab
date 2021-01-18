import pandas as pd
import xlsxwriter
wb=xlsxwriter.Workbook("C:\\Users\\ADMIN\\Desktop\\harikesh_1si17is012\\part_b\\failed_list.xlsx")
ws=wb.add_worksheet()
ws.write(0,0,"USN")
ws.write(0,1,"Name")
ws.write(0,0,"M1")
ws.write(0,0,"M2")
ws.write(0,0,"M3")
exfl="C:\\Users\\ADMIN\\Desktop\\harikesh_1si17is012\\part_b\\studentdetails.xlsx"

j=1
records = pd.read_excel(exfl)
for i in records.index:
    if(records['M1'][i]<20 or records['M2'][i]<20 or records['M3'][i]<20):
        ws.write(j, 0, records['USN'][i])
        ws.write(j, 1, records['Name'][i])
        ws.write(j, 2, records['M1'][i])
        ws.write(j, 3, records['M2'][i])
        ws.write(j, 4, records['M3'][i])
        j+=1


wb.close()