class Role:
    
	def __init__(self, role_name: str, salary_multiplier: float = 1.0, flat_bonus: float = 0.0):
		self.__role_name = role_name
		self.__salary_multiplier = salary_multiplier
		self.__flat_bonus = flat_bonus

	def get_effective_salary(self, base_salary: float) -> float:
		return (base_salary * self.__salary_multiplier) + self.__flat_bonus

	def get_role_name(self) -> str:
		return self.__role_name