import pdftables_api


print('Put your files n input folder')
key = input("Enter API Key (Get from 'https://pdftables.com/pdf-to-excel-api') :")


while(True):
	try:
		name = input('Enter file name :')
		c = pdftables_api.Client(key)
		c.xlsx('input/'+name,'output/'+name[:-4])
		print('Sucess')
		print('Files are saved in output')
	except:
		print('Error')
		print('May be file dose not exist or Wrong path')
	opt = input('Do you want to Continu(y/n) :')
	if opt == 'n':
		print('Thankyou')
		exit(0)
	else:
		pass 