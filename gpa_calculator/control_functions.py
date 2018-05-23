import pickle

grades = dict()

#add_class: adds class_name as a key and grade and weight as list to grades
def add_class(arg):
	arg_list = arg.split(" ")
	class_name = arg_list[1].lower()
	class_grade = float(arg_list[2])
	class_weight = float(arg_list[3])

	values_list = [class_grade, class_weight]
	grades[class_name] = values_list
	print('%s sucessfully added.' % class_name)

#remove_class: removes by class_name from grades
def remove_class(arg):
	arg_list = arg.split(" ")
	class_name = arg_list[1].lower()
	if class_name in grades:
		grades.pop(class_name, None)
		print('%s sucessfully removed.' % class_name)
	else:
		print('class does not exist..')

#view_class: views grades and weight by class name
def view_class(arg):
	arg_list = arg.split(" ")
	class_name = arg_list[1].lower()
	print_info(class_name)

#all: views all classes and grades
def all():
	if len(grades) == 0:
		print('No classes exist..')
	else:
		for key in grades:
			print_info(key)

#print_info: print formatted class info
def print_info(arg):
	if arg in grades:
		print('\nClass Name: %s' % arg)
		print('Class Grade: %2f' % grades[arg][0])
		print('Class Weight: %2f' % grades[arg][1])
	else:
		print('class does not exist..')

#calc_gpa: calculates gpa
def calc_gpa():
	total_weight = 0
	wightbygrade = 0
	gpa = 0

	if len(grades) == 0:
		print('No classes, add classes to view GPA')
	else:
		for key in grades:
			total_weight += grades[key][1]
			wightbygrade += grades[key][0] * grades[key][1]
			gpa = wightbygrade / total_weight

		print('Total GPA: %2f' % gpa)

#save: saves data externally
def save():
    with open('gpa_data.pkl', 'wb') as f:
        pickle.dump(grades, f, pickle.HIGHEST_PROTOCOL)

#load: loads data 
def load():
    with open('gpa_data.pkl', 'rb') as f:
        grades = pickle.load(f)

