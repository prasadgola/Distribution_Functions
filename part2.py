import math, sys
import random


def randomvar(r, n):
	randomvarlist = []
	for i in range(n):
		randomvarlist.append(random.random()*r)
	return randomvarlist





def factorial(n):
	nfact = 1
	for i in range(1,n+1):
		nfact *= i
	return nfact






def combination(n,r):
	return factorial(n)/(factorial(n-r)*factorial(r))


def bernoulli(n , p):
	randamvariable = randomvar(1, n)
	result = []
	for i in randamvariable:
		if i <= p:
			result.append(1)
		else:
			result.append(0)
	return result


def binomial( n, p):
	result = []
	for i in range(n):
		x = random.randint(0,1)
		result.append(combination(n , x) * p**x * (1-p)**(n-x))
	return result


def geometric(n, p):
	result = []
	for i in range(n):
		x = random.randint(0,1)
		result.append((1-p)**(x-1)*p)
	return result

def neg_binomial(n, k, p):
	result = []
	for i in range(n):
		x = random.randint(0,1)
		result.append(combination(x-1,k-1) * (1-p)**x-k * p**k)

	return result

def poisson(n,f):
	result = []
	for i in range(n):
		x = random.randint(0,1)
		result.append(math.exp(-f)*((f**x)/factorial(x)))
	return result

def uniform(n, a, b):
	result = []
	for i in range(n):
		result.append(random.uniform(0,1)/(b-a))
	return result

def exponential(n, f):
	result = []
	for i in range(n):
		x = random.uniform(0,100)
		result.append(f*math.exp(-f*x))
	return result


def normal(n, u, std):
	result = []
	for i in range(n):
		x = random.randint(0,10)
		t = (-((x-u)**2))/(2*std**2)
		result.append(1/(std*math.sqrt(2*3.14)) * math.exp(t))
	return result




def simulateDist(t,n , distribution, p1 = None, p2 = None):
	tempmean = 0
	if distribution == "uniform" and t == 1:
		sample = uniform(n, 0, 1)
		for i in sample:
			tempmean += i
		mean = tempmean/n

		tempvar = 0
		for i in sample:
			tempvar += i**2
		var = (tempvar - n*mean**2)/(n-1)

		std = math.sqrt(var)
		print('mean = ', mean,'std = ', std)

	if distribution == 'exponential' and t == 2:
		sample = exponential(n, 20)
		for i in sample:
			tempmean += i
		mean = tempmean/n

		tempvar = 0
		for i in sample:
			tempvar += i**2
		var = (tempvar - n*mean**2)/(n-1)

		std = math.sqrt(var)
		print('mean = ', mean,'std = ', std)

	if distribution == 'poisson' and t == 3:
		sample = poisson(n, p1)
		for i in sample:
			tempmean += i
		mean = tempmean/n

		tempvar = 0
		for i in sample:
			tempvar += i**2
		var = (tempvar - n*mean**2)/(n-1)

		std = math.sqrt(var)
		print('mean = ', mean,'std = ', std)


simulateDist(3, 10, 'poisson', 3)