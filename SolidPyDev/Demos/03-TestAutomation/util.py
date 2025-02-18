def get_grade(mark):
	if mark >= 75:
		return "A*"
	elif mark >= 70:
		return "A"
	elif mark >= 60:
		return "B"
	elif mark >= 50:
		return "C"
	elif mark >= 40:
		return "D"
	elif mark >= 30:
		return "E"
	else:
		return "U"