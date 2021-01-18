import pandas as pd
excel_file='C:\\Users\\ADMIN\\Desktop\\harikesh_1si17is012\\part_b\\licenses.xlsx'
j=1
records = pd.read_excel(excel_file)
key=input("Enter the license key u want to search:")
for i in records.index:
	if(key==records['LicenseKey'][i]):
		j=0
		a=i
		print("Key found at index (",a,",0 )")
if(j==1):
	print("Key not found")