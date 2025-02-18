from rolePolicy import RolePolicy

class Employee:
    
	def __init__(self, name: str, salary: float):
		self.__name = name
		self.__base_salary = salary
		self.__role = RolePolicy().get_initial_role()

	def get_effective_salary(self) -> float:
		return self.__role.get_effective_salary(self.__base_salary)

	def promote(self):
		self.__role = RolePolicy().promote(self.__role)

	def is_junior_role(self) -> bool:
		return self.__role == RolePolicy().get_initial_role()
	
	def __str__(self):
		return f"{self.__name}" \
		       f"[{self.__role.get_role_name()}], " \
		       f"effective salary {self.__role.get_effective_salary(self.__base_salary)}"