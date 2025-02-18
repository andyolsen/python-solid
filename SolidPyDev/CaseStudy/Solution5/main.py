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


def if_time_permits_exercise():

	emps = [
		Employee("Andy", 10_000),
		Employee("Jayne", 20_000),
		Employee("Emily", 30_000),
		Employee("Tom", 40_000),
		Employee("Andrew", 50_000),
	]

	emps[0].promote()
	emps[0].promote()

	emps[1].promote()
	emps[1].promote()
	emps[1].promote()

	print("\nInitial details...")
	for e in emps:
		print(e)

	junior_emp = next((e for e in emps if e.is_junior_role()), None)
	if junior_emp:
		junior_emp.promote()
		print(f"\nPromoted junior employee, new details: {junior_emp}")


if __name__ == "__main__":
	core_exercises()
	if_time_permits_exercise()