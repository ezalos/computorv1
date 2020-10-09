import sys
import re

PURPLE = '\033[95m'
BLUE = '\033[94m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
RED = '\033[91m'
RESET = '\033[0m'
BOLD = '\033[1m'
UNDERLINE = '\033[4m'

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

def get_col(degree):
	term = ""
	if degree == 0:
		term += GREEN
	elif degree == 1:
		term += BLUE
	elif degree == 2:
		term += PURPLE
	else:
		term += RED
	return term

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
		term += get_col(self.n)
		if int(self.a) == float(self.a):
			term += "{:d}".format(int(self.a))
		else:
			temp = "{1:{0}f}".format(self.a_len, self.a)
			ind = len(temp)
			if '.' in temp:
				for i in range(-1, -len(temp) -1, -1):
					if temp[i] != '0':
						break
					ind = i
			term += temp[:ind]
		term += " * X^{:d}".format(self.n)
		term += RESET
		return term

class polynomial():
	def __init__(self, equation):
		cleaned = [e for e in equation if e.a != 0]
		if len(cleaned) == 0:
			cleaned.append(polynomial_term(0, 0, 0))
		self.eq = cleaned
		self.deg = equation[-1].n

	def solve(self):
		print("Polynomial degree: " + get_col(self.deg) + "{}".format(self.deg) + RESET)
		eq = self.eq
		if eq[-1].n > 2:
			print("The polynomial degree is stricly greater than 2, I can't solve.")
		elif eq[-1].n == 0:
			self.solve_degree_0()
		elif eq[-1].n == 1:
			self.solve_degree_1()
		elif eq[-1].n == 2:
			self.solve_degree_2()

	def solve_degree_0(self):
		print("X^0 is always equal to 1:")
		print(YELLOW, end="")
		if self.eq[-1].a == 0:
			print("\tAny X is a solution")
		else:
			print("\tThere is no X which can be a solution")
		print(RESET, end="")

	def solve_degree_1(self):
		a = self.eq[-1].a
		if a == 0:
			self.solve_degree_0()
			return
		if len(self.eq) > 1:
			b = self.eq[0].a
		else:
			b = 0
		print("The solution is:")
		print(YELLOW, end="")
		print("\t{:f}".format(-b/a))
		print(RESET, end="")

	def solve_degree_2(self):
		a , b, c = (0, 0, 0)
		for v in self.eq:
			if v.n == 0:
				c = v.a
			elif v.n == 1:
				b = v.a
			elif v.n == 2:
				a = v.a
		if a == 0:
			self.solve_degree_1()
		delta = b ** 2 - 4 * a * c
		print('Delta = ', delta)
		if delta < 0:
			print("Discriminant is strictly negative, the two complex solutions are:")
			sol_i = ((-delta) ** 0.5) / (2 * a)
			sol_ = (-b) / (2 * a)
			print(YELLOW, end="")
			print("\t", sol_, "+", sol_i, "i")
			print("\t", sol_, "-", sol_i, "i")
			print(RESET, end="")
		elif delta > 0:
			print("Discriminant is strictly positive, the two solutions are:")
			sol_1 = (-b + delta ** 0.5) / (2 * a)
			print(YELLOW, end="")
			print("\t", sol_1)
			sol_2 = (-b - delta ** 0.5) / (2 * a)
			print("\t", sol_2)
			print(RESET, end="")
		else:
			print("Discriminant is equal to zero, the solution is:")
			sol = -b / (2 * a)
			print(YELLOW, end="")
			print("\t", sol)
			print(RESET, end="")

	def __str__(self):
		red = ""
		for val in self.eq:
			if len(red):
				red += "+ "
			red += val.__str__() + ' '
		red += '= 0'
		red = red.replace("+ -", "-")
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
	# eq_dic[0] = polynomial_term(0, 0, 0)
	# eq_dic[1] = polynomial_term(0, 0, 0)
	# eq_dic[2] = polynomial_term(0, 0, 0)
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
		"1 * X^0 + 1 * X^1 + 1 * X^2 = 0 * X^0",
		"1 * X^0 + 2 * X^1 + 1 * X^2 = 0 * X^0",
		"1 * X^0 = 0 * X^0",
		"0 * X^0 = 0 * X^0",
		"0 * X^1 = 0 * X^0",
		"0 * X^1 = 0",
		"1 * X^1 = 10",
		"42 * X0 = 42 * X0",
		"21 * X0 = -21 * X0",
		"0 * X^2 = 0 * X^0",
		"0 * X^3 = 0 * X^2",
		"5 * X^0 + 4 * X^1 = 4 * X^0"]
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
