import math

def polySum(n, s):

	'''
	Function takes 2 parameters:
	n = number of sides of a regular polygon
	s = length of sides
	Returns (area + perimeter^2), rounded to 4 decimal places
	'''
	
	poly_area = (0.25 * n * s**2) / (math.tan(math.pi / n))
	poly_perim = (n * s)
	
	return round((poly_area + poly_perim**2), 4)