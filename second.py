class myclass:
	def __init__(self,name,age):
		self.name=name
		self.age=age
	
	def mydata(self):
		newage = str(self.age)
		print("my name is" + self.name +"my age is" + newage)


myobj=myclass("rashmi",25)
myobj.mydata()

