from colors import *

def get_color(degree):
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

class PolynomialTerm():
	def __init__(self, a, n, a_len):
		self.a = a
		self.n = n
		self.a_len = a_len

	def __add__(self, other):
		if other == None:
			return self
		elif self.n == other.n:
			a = self.a + other.a
			return PolynomialTerm(a, self.n, a_len=len(str(a)))
		return None

	def __str__(self):
		term = ""
		term += get_color(self.n)
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

class Polynomial():
	def __init__(self, equation):
		cleaned = [e for e in equation if e.a != 0]
		if len(cleaned) == 0:
			cleaned.append(PolynomialTerm(0, 0, 0))
		self.eq = cleaned
		self.deg = cleaned[-1].n
		self.sol = []

	def coefs(self):
		a , b, c = (0, 0, 0)
		for v in self.eq:
			if v.n == 0:
				c = v.a
			elif v.n == 1:
				b = v.a
			elif v.n == 2:
				a = v.a
		return a, b, c

	def solve(self):
		print("Polynomial degree: " + get_color(self.deg) + str(self.deg) + RESET)
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
		self.sol.append(-b/a)

	def solve_degree_2(self):
		a , b, c = self.coefs()
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
			self.sol.append(sol_ + (1j * sol_i))
			self.sol.append(sol_ - (1j * sol_i))
			print(RESET, end="")
		elif delta > 0:
			print("Discriminant is strictly positive, the two solutions are:")
			sol_1 = (-b + delta ** 0.5) / (2 * a)
			print(YELLOW, end="")
			print("\t", sol_1)
			sol_2 = (-b - delta ** 0.5) / (2 * a)
			print("\t", sol_2)
			self.sol.append(sol_2)
			self.sol.append(sol_1)
			print(RESET, end="")
		else:
			print("Discriminant is equal to zero, the solution is:")
			sol = -b / (2 * a)
			self.sol.append(sol)
			self.sol.append(sol)
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
