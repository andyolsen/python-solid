from singleton import singleton
from role import Role

@singleton
class RolePolicy:

	def __init__(self):
		self.__roles = [
			Role("Developer"),
			Role("Senior Developer", 1.2, 2_000),
			Role("Manager", 1.2, 2_000),
			Role("Partner", 2.0, 100_000),
			Role("CEO", 10.0, 200_000)
		]

	def promote(self, currentRole: Role) -> Role:
		for i in range(len(self.__roles) - 1):
			if currentRole is self.__roles[i]:
				return self.__roles[i + 1]
		return currentRole
	
	def get_initial_role(self) -> Role:
		return self.__roles[0]