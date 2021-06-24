''' WAP TO CREATE CLASS FOR STUDENT WHICH TAKE NAME, ENROLLMENT NO. , SEMESTER MARKS AS INPUT.
    1. CALCULATE SPI , CPI FOR EACH SEMESTER
    2. DISPLAY RESULT WITH SPI AND CPI
    3. USER SHOULD BE ALLOWED TO UPDATE MARKS
    4. USER CAN SEE RESULT (spi & cpi) ANYTIME. '''

class result:
	marks = {}
	spi ={}
	cpi = {}
	enroll = 123
	name = 'abc'
	branch = 'CE'

                                #FUNCTION TO CALCULATE SPI

	def cal_spi(self,sem):
		total = 0
		score = self.marks[sem]
		for i in score:
			total += int(i)	
		res = (total/(len(score)*10))
		self.spi[sem] = res		
		return res


                                #FUNCTION TO CALCULATE CPI

	def cal_cpi(self,sem):
		s = 0			
		if sem == 1:
			self.cpi[sem] = self.spi[sem]
		else:		
			for i in self.spi:
				if(i<=sem):					
					s += self.spi[i]
			self.cpi[sem] = s/sem

                                #CHECKING IF ANY POSSIBLE CALCULATION IS LEFT
		available_spi = self.spi.keys()
		available_cpi = self.cpi.keys()
		for flag in available_spi:
			if flag not in available_cpi:
				count = 0
				for i in range(1,flag):			
					if i in available_spi:
						count += 1
				if (count == flag-1):				
					self.cal_cpi(flag)	



student = result()
student.name = input("enter name : ")
student.enroll = input("enter enrollment number: ")
student.branch = input("enter branch: ")
print("press 1 to enter marks ")
print("press 2 to update marks in subjects form any semester")
print("press 3 to check result")
print("press 4 to exit")

choice = int(input("Enter your options(1/2/3/4): "))

while(choice != 4):
	if (choice == 1):
		sem = int(input("which semester marks you want to enter : "))
		print("enter marks obtained in each subject you studied in semester",sem,"seperated by commas: ",end='')
		in_mark=input()
		student.marks[sem] = in_mark.split(',')
		student.cal_spi(sem)
		x  = student.spi.keys()		
		count = 0
		if sem==1:
			student.cal_cpi(sem)
		else:		
			for i in range(1,sem):			
				if i in x:
					count += 1
			if (count == sem-1):				
				student.cal_cpi(sem)
			
		

	elif (choice == 2):
		sem = int(input("which semester marks you want to update : "))
		in_mark = input("re-enter all subject marks of this semester in comma seperated manner: ")
		student.marks[sem] = in_mark.split(',')		
		student.cal_spi(sem)  
		count = 0
		available_cpi = student.cpi.keys()
		for i in available_cpi:
			if i>sem:
				count += 1
		for i in range(count+1):
			student.cal_cpi(sem + i)
			
	elif (choice == 3):
		print("press 1 to check SPI of any specific semester")
		print("press 2 to CPI upto any specific semester")
		print("press 3 to check complete result.")
		
		choice = input("Enter your choice : ")
		if choice == '1':
			sem = int(input("Which semester result you want to check"))
			if sem in student.spi:
				print("SPI score for semester {} = {}".format(sem,student.spi[sem]))
			else:
				print("You first need to enter marks for this semester !")
		elif choice == '2':
			sem = int(input("Which semester result you want to check"))
			if sem in student.cpi:
				print("CPI upto semester {} = {}".format(sem,student.cpi[sem]))
			else:
				x=1
				for i in range(1,sem):
					if sem-x in student.cpi:
						print("Marks for some of previous semesters are yet to be entered.")						
						print("latest calculated CPI is of  semester {} wchich is {}".format(sem-x,student.cpi[sem-x]))
						break;								
					else:
						x += 1
				else:
					print("Not yet calculated !")
		else:		
			print("SPI for the passed semesters: ",student.spi)
			print("CPI : ",student.cpi)

	elif(choice == 4):
		pass

	choice = int(input("Enter your options(1/2/3/4): "))




