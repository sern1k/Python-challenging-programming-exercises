class InputOutput():
	def __init__(self):
		self.init = ""


	def getString(self):
		self.init = input()


	def printString(self):
		print(self.init.upper())

text = InputOutput()
text.getString()
text.printString()