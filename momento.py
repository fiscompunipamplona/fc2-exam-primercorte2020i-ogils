from numpy import*
from math import*

class mdistribucion:
	def __init__(self,datos):

		self.data=datos
		self.media= 0.
		self.varianza=0
		self.desestandar=0
		self.skew=0
		self.kurtosis=0

	def medial(self):
		self.media= sum(self.data)/len(self.data)
		return(self.media)

	def varianz(self):
		x = (self.data - self.media)
		c = x*x
		self.var =sum(c)/(len(self.data) - 1 )
		return(self.var)

	def destandar(self):
		self.q=sqrt(self.var)
		return(self.q)

	def skev(self):
		self.s=(self.data - self.media)/self.q
		self.r=list(map(lambda x: x**3, self.s))
		self.skew= (sum(self.r)/len(self.data))
		return(self.skew)

	def curtosis(self):
		self.t=list(map(lambda x: x**4, self.s))
		self.kurtosis = (sum(self.t)/len(self.data)) - 3
		return(self.kurtosis)
	def cova(self):
                self.x=self.data[:,0]
                self.y=self.data[:,1]
                self.xy=self.x*self.y
                self.covarianza=(sum(self.xy)/len(self.xy))-((sum(self.x)/len(self.x)) * (sum(self.y)/len(self.y)))
                return(self.covarianza)	

	def cor(self):
                self.a=sum(self.x)/len(self.x)
                self.b=sum(self.y)/len(self.y)
                self.aa=sum ( (self.x-self.a)*(self.x-self.a) )/(len(self.x)-1)
                self.bb=sum ( (self.y-self.b)*(self.y-self.b) )/(len(self.y)-1)
                return(self.covarianza/(sqrt(self.aa)*sqrt(self.bb)))