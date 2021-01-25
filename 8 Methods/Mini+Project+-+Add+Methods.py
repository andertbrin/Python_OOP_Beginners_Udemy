class MusicSchool:

	students = {"Gino":   [15, "653-235-345", ["Piano", "Guitar"]],
                        "Talina": [28, "555-765-452", ["Chello"]],
                        "Eric":   [12, "583-356-223", ["Singing"]]}

	def __init__(self, working_hours, revenue):
		self.working_hours = working_hours
		self.revenue = revenue

	# Add your methods below this line

	def print_student_data(self):
		for student in MusicSchool.students.items():
			print(f"Student: {student[0]} who is {student[1][0]} years old is taking {student[1][2]}")
	
	def print_student(self, student):
		std = MusicSchool.students[student]
		print(f"Student: {student} who is {std[0]} years old is taking {std[2]}")

	def add_student(self, name, data):
		MusicSchool.students[name] =  data

# Create the instance
ms = MusicSchool(20, 15000)

# Call the methods
ms.print_student_data()
ms.print_student("Gino")
ms.add_student("Jack", [60, "562-234-234", ["Piano"]])

# Saving as txt
with open("MusicSchool.txt","w") as file:
	file.write(str(ms.students))


