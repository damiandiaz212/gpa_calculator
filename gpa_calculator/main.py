import control_functions as cf

# PROGRAMMER: Damian D.
# DATE CREATED: 05/22/2018                                  
# REVISED DATE: 05/22/2018 
# PURPOSE: Calculate GPA, program does not use Letter grades, grades must be translated as per university
#		   template, ex at Queens College [B+ = 3.33] whilst at NCC [B+ = 3.5]. Weight is the credits worth 
#		   not credits earned.
#

print('\n===== GPA Calculator =====')
try:
	cf.load()
except:
	print('no data loaded, did you save?')
print('enter \'help\' for commands.')

run = True

#Runtime
while(run == True):

	command = input('\nEnter Command: \n').lower()

	if command == 'x':
		cf.save()
		run = False
	elif command == 'help':
		print('\'gpa\' ~ view gpa')
		print('\'add\' class_name grade weight ~ add\'s class and grade.\n                                ex: add differential_equations 3.5 4.0')
		print('\'remove\' class_name ~ removes class from calculation')
		print('\'all\' ~ views all classes, grades and weight')
		print('\'class\' class_name ~ views class grade and weight')
		print('\'save\' ~ saves data to gpa_data.pkl')
		print('\'load\' ~ loads data from gpa_data.pkl')
		print('\'x\' ~ saves and terminates program')
	elif 'gpa' in command:
		cf.calc_gpa()
	elif 'add' in command:
		cf.add_class(command)
	elif 'remove' in command:
		cf.remove_class(command)
	elif 'class' in command:
		cf.view_class(command)
	elif 'all' in command:
		cf.all()
	elif 'save' in command:
		cf.save()
	elif 'load' in command:
		cf.load()


print('Terminating process')
