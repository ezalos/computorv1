import sys
from parse import parse_equation
from polynomial_class import Polynomial
from graph import PolGraph

def usage():
	usage_message = ""
	usage_message += "usage: " + "python3 " + sys.argv[0] + " "
	usage_message += " [-v or --visual] "
	usage_message += " [-h or --help] "
	usage_message += "\"5 * X^0 + 4 * X^1 - 9.3 * X^2 = 1 * X^0\""
	print(usage_message)

def arg_pase(av):
	help = False
	visual = False
	equation = None
	for arg in av:
		if arg == "-v" or arg == "--visual":
			visual = True
		elif arg == "-h" or arg == "--help":
			help = True
		else:
			equation = arg
	if help:
		usage()
		sys.exit()
	elif equation == None:
		equation = input("Please input your equation: ")
	return equation, visual



class ComputorV1():
	def __init__(self, equation_str="", visual=False):
		equation = parse_equation(equation_str)
		if equation:
			pol = Polynomial(equation)
			print("Reduced form: ", pol)
			pol.solve()
			if visual:
				a, b, c, = pol.coefs()
				PolGraph(a, b, c).plot()
		else:
			print("Invalid equation: ", equation_str)
			usage()

if __name__ == "__main__":
	equation, visual = arg_pase(sys.argv[1:])
	ComputorV1(equation, visual)
