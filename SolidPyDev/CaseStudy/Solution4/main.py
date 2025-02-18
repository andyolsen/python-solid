from employee import Employee

def core_exercises():

	emp1 = Employee ("Kari Nordmann", 10000.0)

	print(f"Initial details are: {emp1}")

	emp1.promote()
	print(f"After 1st promotion: {emp1}")

	emp1.promote()
	print(f"After 2nd promotion: {emp1}")

	emp1.promote()
	print(f"After 3rd promotion: {emp1}")

	emp1.promote()
	print(f"After 4th promotion: {emp1}")

	emp1.promote()
	print(f"After 5th promotion: {emp1}")


if __name__ == "__main__":
	core_exercises()