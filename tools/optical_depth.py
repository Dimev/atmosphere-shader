import numpy as np
import scipy.integrate
import math
import gplearn.genetic

# we want to figure out a good approximation to the optical depth integral 
# we can calculate this as the integral over beta * exp(-scale_height * (sqrt(t^2 + 2bt + c) - planet_radius)), from t = 0 to infinity 
# with t as the distance from the start position, b = dot(ray direction, ray start) and c = dot(ray start, ray start) - planet radius*planet_radius
# beta can be left out
# to actually do anything with it, we first want to have this formula to make some data with it
# so set it up here
def optical_depth(b, c, inv_scale_height, planet_radius):

	# the density function along the ray
	density = lambda t: np.exp(-inv_scale_height * (np.sqrt((t * t) + (2.0 * b * t) + c) - planet_radius))

	# get the integral, 0 to infinity
	return scipy.integrate.quad(density, 0.0, np.inf)


# now, make some data points
i = 0

data = []

print("making data")

# loop over all possible points
# b is basically -inf to inf
# c is - planet_radius^2 to inf
# scale height is can be -inf to inf, but more realistically 0 to inf
# planet radius is 0 to inf
# for inf, we'll just use 10
# big enough
# well kinda, otherwise we get to some very high values
for b in np.arange(-10, 20, 0.1):
	for c in np.arange(-10, 20, 0.1):
		#for scale_height in np.arange(0.01, 1.0, 0.1):
			#for planet_radius in np.arange(1.0, 11, 1):

		# skip when the inside of the sqrt can become smaller than 0
		# t^2 + 2bt + c, derivative is 2t + 2b, is 0 (aka min) when t = -b
		# so min is b^2 + 2b*-b + c = c - b^2
		min_val = c - b*b

		if min_val < 0.0:

			continue

		val = optical_depth(b, c, 1.0, 0.0)[0]

		if not math.isnan(val):

			data.append((b, c, val))

print(len(data))
print("training")

x_train = [(x[0], x[1]) for x in data]
y_train = [x[2] for x in data]

# and estimate
est_gp = gplearn.genetic.SymbolicRegressor(population_size=1000,
                           generations=20, stopping_criteria=0.01,
                           p_crossover=0.7, p_subtree_mutation=0.1,
                           p_hoist_mutation=0.05, p_point_mutation=0.1,
                           max_samples=0.9, verbose=1,
                           parsimony_coefficient=0.01, random_state=0)
est_gp.fit(x_train, y_train)

print(est_gp._program)




