import numpy as np
import scipy.integrate
import math

# we want to figure out a good approximation to the optical depth integral 
# we can calculate this as the integral over beta * exp(-scale_height * (sqrt(t^2 + 2bt + c) - planet_radius)), from t = 0 to infinity 
# with t as the distance from the start position, b = dot(ray direction, ray start) and c = dot(ray start, ray start) - planet radius*planet_radius
# beta can be left out
# to actually do anything with it, we first want to have this formula to make some data with it
# so set it up here
def optical_depth(b, c, scale_height, planet_radius):

	# the density function along the ray
	density = lambda t: np.exp(-scale_height * (np.sqrt(t * t + 2.0 * b * t + c) - planet_radius))

	# get the integral, 0 to infinity
	return scipy.integrate.quad(density, 0.0, np.inf)


# now, make some data points
i = 0

data = []

# loop over all possible points
# b is basically -inf to inf
# c is - planet_radius^2 to inf
# scale height is can be -inf to inf, but more realistically 0 to inf
# planet radius is 0 to inf
# for inf, we'll just use 1e6
# big enough
for b in np.arange(-10, 10, 1):
	for c in np.arange(-10, 10, 1):
		for scale_height in np.arange(0.0, 10, 1):
			for planet_radius in np.arange(0.0, 10, 1):

				# TODO: skip when the inside of the sqrt can become smaller than 0

				val = optical_depth(b, c, scale_height, planet_radius)[0]

				if not math.isnan(val):

					data.append((b, c, scale_height, planet_radius, val))

print(len(data))




