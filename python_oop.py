class employee:
	rate = 1.05
	num = 0

	def __init__(self,first,last,email,pay):
		self.first = first
		self.last = last
		self.email = email
		self.pay = pay
		employee.num+=1 # the front must be employee , but not self!!!

	@property 
	def get_name(self):
		return '{} {}' .format(self.first, self.last)

	@get_name.setter
	def get_name(self, name):
		first, last = name.split()
		self.first = first
		self.last = last

	@get_name.deleter
	def get_name(self):
		print("Delete name!")
		self.first = None
		self.last = None

	def pay_raise(self):
		self.pay = int(self.pay * employee.rate)

	### special method repr = representation for compiler
	def __repr__(self):
		return "employee('{}' , '{}', '{}')" . format(self.first, self.last, self.pay)
	### special method str is more readable for human
	def __str__(self):
		return '{}  {}' .format(self.get_name(), self.pay)

	### operator overloading
	def __add__(self, other):
		return self.pay + other.pay

	### dunder length of class
	def __len__(self):
		name = self.get_name()
		return len(''.join(name.split()))



	# to set all the variable of class as the same
	@classmethod 
	def set_rate(cls, rt):
		cls.rate = rt
	# used to be a constructor
	@classmethod
	def to_construct(cls, str):
		first , last , email, pay = str.split('-')
		return cls(first, last, email,pay)
	# no "self" or "cls" in the bracket
	@staticmethod
	def is_workday(day):
		if day.weekday()== 5 or day.weekday()== 6:
			return True
		else:
			return False

### inherent from employee
class developer(employee):
	rate = 1.1
	def __init__(self, first, last, email, pay, language):
		super().__init__(first,last,email,pay)
		#employee.__init__(self,first,last,email,pay) add 'self'
		self.language = language

class manager(developer):
	rate = 1.2
	def __init__(self, first, last, email, pay, language,  employees=None):
		super().__init__(first, last, email, pay, language)
		if employees is None:
			employees = []
		else:
			self.employees = employees
	def add_emp(self, emp):
		if emp not in self.employees:
			self.employees.append(emp)

	def remove_emp(self, emp):
		if emp in self.employees:
			self.employees.remove(emp)

	def print_emp(self):
		for emp in self.employees:
			print(emp.get_name())


test1 = employee('aaaa', 'bbbb', '@@@@', 50)
test2 = developer('apple', 'banana' , '@@@',100,'c++')
test3 = developer('cable', 'durable', '@@',200,'python')
test4 = manager('dddd','eeee','@',400,'java',[test1])


### the basic of python oop
# test2.set_rate(1.06)
# print(test2.rate)
# print(test3.rate)
# print(test2.get_name())
# test3.rate  = 1.06
# print(test3.rate)
# print(test2.rate)

### constructor of class method
# emp_str = 'hi-yo-EE-500'
# test4 = employee.to_construct(emp_str)
# print(test4.get_name())

### use the static method in the employee as the function
# import datetime
# date = datetime.date(2019,8,21)
# print(employee.is_workday(date))

### the inherentence 
# test4.add_emp(test2)
# test4.remove_emp(test2)
# test4.print_emp()
# print(isinstance(test4,manager))
# print(isinstance(test3,manager))
# print(issubclass(manager,developer))
# print(issubclass(developer,manager))

### display how 1+2 and 'a'+'b' ('+'' equals __add__)
# print(int.__add__(1,2))
# print(str.__add__('a','b'))

### display len is also a dunder function
# print(len('test'))
# print('test'.__len__())

### the special method
# print(test1.__str__())
# print(test1.__repr__())
# print(str(test1))
# print(repr(test1))

###operator overloading
# print(test1.__add__(test2))
# print(test1+test2)
# print(len(test1))

### add the property on get_name, we don't have to add brackets after it
# print(test1.get_name)

### if we want to set the name of the employee, the first and last will not change
### if we don't use setter
# test1.get_name = 'hey you'
# print(test1.get_name)
# print(test1.first)
# print(test1.last)

### delete the name
# del test1.get_name
# print(test1.first)
# print(test1.last)