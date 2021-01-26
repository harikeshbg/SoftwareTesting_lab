import pandas as pd
excel_file='/home/harikesh/Documents/Lab_programs/SoftwareTesting_lab/software_testing/part_b/licenses.xlsx'
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