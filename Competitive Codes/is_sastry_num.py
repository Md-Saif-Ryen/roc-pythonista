import math
#183 is a sastry number as 183184 is a #perfect square number of 432

def sastry_num(n):
	"""returns True if a number n is sastry number,False otherwise"""
	num = str(n) + str(n+1)
	sqt = math.sqrt(int(num))
	if int(sqt) - sqt == 0:
		return True
	return False
