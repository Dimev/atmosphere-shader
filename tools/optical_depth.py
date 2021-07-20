import numpy as np
import scipy.integrate

# we want to figure out a good approximation to the optical depth integral 
# we can calculate this as the integral over beta * exp(-scale_height * (sqrt(t^2 + 2bt + c) - planet_radius), from t = 0 to infinity 
# with t as the distance from the start position, b = dot(ray direction, ray start) and c = dot(ray start, ray start) - planet radius^2
# beta can be left out
# to actually do anything with it, we first want to have this formula to make some data with it
# so set it up here
def optical_depth(b, c, scale_height, planet_radius):

	def density(t):

		np.exp(-scale_height * (np.sqrt(t * t + 2.0 * b * t + c) - planet_radius))

	# get the integral, 0 to infinity
	return scipy.integrate.quad(density, 0.0, np.inf)


print(optical_depth(0.0, 0.0, 1.0, 2.0))