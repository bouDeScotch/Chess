class Color:
	
	def __init__(self, light: (int, int, int) or str, dark: (int, int, int) or str):
		self.light = light
		self.dark = dark
	
	def __str__(self):
		return f"Light: {self.light}, Dark: {self.dark}"
	
	def __repr__(self):
		return self.__str__()
	
	def textual_repr(self):
		light_code = f"\033[38;2;{self.light[0]};{self.light[1]};{self.light[2]}m"
		dark_code = f"\033[38;2;{self.dark[0]};{self.dark[1]};{self.dark[2]}m"
		reset_code = "\033[0m"
		
		return f"{light_code}\u2588{dark_code}\u2588{reset_code}"


c = Color((255, 0, 255), (0, 255, 0))
print(c.textual_repr() * 10)
