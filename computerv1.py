import sys
import re

polynomial_elem_pattern = r"(?#\
)(?P<Polynomial_Elem>(?#\
	)(?P<sign>[+\-])?(?#\
	)\s*(?#\
	)(?P<a_coef>\d+(?:.\d+)?)(?#\
		)(?:(?#\
		)\s*\*\s*(?#\
		)(?P<x_n>(?#\
			)X\^(?#\
			)(?P<n_coef>\d+)(?#\
		))(?#\
	))?(?#\
))(?#\
)"

class polynomial_term():
	def __init__(self, a, n, a_len):
		self.a = a
		self.n = n
		self.a_len = a_len

	def __add__(self, other):
		if other == None:
			return self
		elif self.n == other.n:
			a = self.a + other.a
			return polynomial_term(a, self.n, a_len=len(str(a)))
		return None
	def __str__(self):
		term = ""
		if int(self.a) == float(self.a):
			term += "{:d}".format(int(self.a))
		else:
			term += "{1:{0}f}".format(self.a_len, self.a)
		term += " * X^{:d}".format(self.n)
		term = term.replace("+ -", "-")
		return term

class polynomial():
	def __init__(self, equation):
		self.eq = equation
		self.deg = equation[-1].n

	def solve(self):
		print("Polynomial degree: {}".format(self.deg))
		eq = self.eq
		if eq[-1].n > 2:
			print("The polynomial degree is stricly greater than 2, I can't solve.")
		elif eq[-1].n == 0:
			print("X^0 is always equal to 1:")
			if eq[-1].a == 0:
				print("\tAny X is a solution")
			else:
				print("\tThere is no X which can be a solution")
		elif eq[-1].n == 1:
			a = eq[-1].a
			if len(eq) > 1:
				b = eq[0].a
			else:
				b = 0
			print("The solution is:")
			print("\t{:f}".format(-b/a))
		elif eq[-1].n == 2:
			self.solve_degree_2()

	def solve_degree_2(self):
		a , b, c = (0, 0, 0)
		for v in self.eq:
			if v.n == 0:
				c = v.a
			elif v.n == 1:
				b = v.a
			elif v.n == 2:
				a = v.a
		delta = b ** 2 - 4 * a * c
		print('Delta = ', delta)
		if delta < 0:
			print("Complex Sol!")
			#Complex solution
			pass
		elif delta > 0:
			print("Discriminant is strictly positive, the two solutions are:")
			sol_1 = (-b + delta ** 0.5) / (2 * a)
			print("\t", sol_1)
			sol_2 = (-b - delta ** 0.5) / (2 * a)
			print("\t", sol_2)
		else:
			print("Double root!")




	def __str__(self):
		red = ""
		for val in self.eq:
			if len(red):
				red += "+ "
			red += val.__str__() + ' '
		red += '= 0'
		return red

def fill_pol_class(eq_dic, pol_dic, right=False):
		a = float(pol_dic['a_coef'])
		a_len = len(pol_dic['a_coef'])
		if right == True:
			a *= -1
		if pol_dic['sign'] == '-':
			a *= -1
		if pol_dic['x_n'] != None:
			n = int(pol_dic['n_coef'])
		else:
			n = 0
		elem = polynomial_term(a, n, a_len)
		# print(elem)
		if n in eq_dic:
			eq_dic[n] = eq_dic[n] + elem
		else:
			eq_dic[n] = elem
		return eq_dic


def cut_around_equal(str):
	eq_dic = {}
	if '=' in str:
		str = str.split('=')
		regex = re.compile(polynomial_elem_pattern)
		# print("Left side")
		for pol_el in regex.finditer(str[0]):
			pol_dic = pol_el.groupdict()
			eq_dic = fill_pol_class(eq_dic, pol_dic, right=False)
		# print("Right side")
		for pol_el in regex.finditer(str[1]):
			pol_dic = pol_el.groupdict()
			eq_dic = fill_pol_class(eq_dic, pol_dic, right=True)
		# print("Dic")

		equation = list(eq_dic.values())
		equation.sort(key=lambda x: x.n)
		# for val in equation:
		# 	print(val.__str__())
		return equation

class ComputorV1():
	def __init__(self, equation=""):
		print(sys.argv[0] + " \"" + equation + "\"")
		equation = cut_around_equal(equation)
		pol = polynomial(equation)
		print("Reduced form: ", pol)
		pol.solve()
		print()

if __name__ == "__main__":

	eq = ["5 * X^0 + 4 * X^1 - 9.3 * X^2 = 1 * X^0",
		"8 * X^0 - 6 * X^1 + 0 * X^2 - 5.6 * X^3 = 3 * X^0",
		"5 * X^0 + 4 * X^1 = 4 * X^0"]
	# eq = "1 * X^0 = 0"
	for i in eq:
		ComputorV1(i)

	# $>./computor
	# Reduced form: 4 * X^0 + 4 * X^1 - 9.3 * X^2 = 0
	# Polynomial degree: 2
	# Discriminant is strictly positive, the two solutions are:
	# 0.905239
	# -0.475131
	# $>./computor "5 * X^0 + 4 * X^1 = 4 * X^0"
	# Reduced form: 1 * X^0 + 4 * X^1 = 0
	# Polynomial degree: 1
	# The solution is:
	# -0.25
	# ./computor "8 * X^0 - 6 * X^1 + 0 * X^2 - 5.6 * X^3 = 3 * X^0"
	# Reduced form: 5 * X^0 - 6 * X^1 + 0 * X^2 - 5.6 * X^3 = 0
	# Polynomial degree: 3
	# The polynomial degree is stricly greater than 2, I can't solve.
