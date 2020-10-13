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


class ComputorV1():
	def __init__(self, equation="", visual=False):
		equation = parse_equation(equation)
		if equation:
			pol = Polynomial(equation)
			print("Reduced form: ", pol)
			pol.solve()
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

	ComputorV1(equation, visual)
