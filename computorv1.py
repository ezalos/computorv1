import sys
from parse import parse_equation
from polynomial_class import Polynomial
from graph import PolGraph
from colors import *

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

def test_sol(pol):
	a, b, c, = pol.coefs()
	mine = pol.sol.sort()
	them = PolGraph(a, b, c).root.tolist().sort()
	err = False
	if mine == None or them == None:
		if mine != None or them != None:
			err = True
	elif len(mine) != len(them):
		err = True
	for me, np in zip(mine, them):
		if me != np:
			err = True
			print("me: ", me)
			print("np: ", np)
	if err:
		print("mine: ", mine)
		print("them: ", them)
		print(RED   + "FAILURE" + RESET)
	else:
		print(GREEN + "SUCCESS" + RESET)


class ComputorV1():
	def __init__(self, equation_str="", visual=False, debug=False):
		equation = parse_equation(equation_str)
		if equation:
			pol = Polynomial(equation)
			print("Reduced form: ", pol)
			pol.solve()
			if visual:
				a, b, c, = pol.coefs()
				PolGraph(a, b, c).plot()
			if debug:
				test_sol(pol)
		else:
			print("Invalid equation: ", equation_str)
			usage()

if __name__ == "__main__":
	equation, visual = arg_pase(sys.argv[1:])
	ComputorV1(equation, visual)
