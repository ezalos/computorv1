import sys
from parse import parse_equation
from polynomial_class import Polynomial
from graph import PolGraph

def usage():
	usage_message = ""
	usage_message += "usage: " + "python3 " + sys.argv[0] + " "
	usage_message += " [-v or --visual] "
	usage_message += "\"5 * X^0 + 4 * X^1 - 9.3 * X^2 = 1 * X^0\""
	print(usage_message)
	sys.exit()

def debug():
	eq = ["5 * X^0 + 4 * X^1 - 9.3 * X^2 = 1 * X^0",
		"8 * X^0 - 6 * X^1 + 0 * X^2 - 5.6 * X^3 = 3 * X^0",
		"1 * X^0 + 1 * X^1 + 1 * X^2 = 0 * X^0",
		"1 * X^0 + 10 * X^2 + 1 * X^1 - 1 * X^2 = 0 * X^0 - 5 * X^2 ",
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
		"5 * X^0 + 4 * X^1 = 4 * X^0"
	]

	bad = ["shit",
		"sh=it",
		"1 * x^1 = 0",
		"1 * x^1 +- 1 * x^1 = 0",
		"1 * X^a = 0",
		"e * X^a = 0",
	]
	for i in eq:
		ComputorV1(i)

class ComputorV1():
	def __init__(self, equation="", visual=False):
		print(sys.argv[0] + " \"" + equation + "\"")
		equation = parse_equation(equation)
		if equation:
			pol = Polynomial(equation)
			print("Reduced form: ", pol)
			pol.solve()
			print()
			if visual:
				a, b, c, = pol.coefs()
				PolGraph(a, b, c).plot()

if __name__ == "__main__":
	if 3 < len(sys.argv) < 2:
		usage()
	visual = False
	if len(sys.argv) == 3:
		if sys.argv[1] == "-v" or sys.argv[1] == "--visual":
			visual = True
			equation = sys.argv[2]
		else:
			usage()
	else:
		equation = sys.argv[1]

	if False:
		debug()

	ComputorV1(equation, visual)
