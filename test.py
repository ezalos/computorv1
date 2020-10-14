import sys
from computorv1 import ComputorV1
from graph import PolGraph
from colors import *

deg_0 = [
	"5 * X^0 = 5 * X^0",
	"4 * X^0 = 8 * X^0",
	"1 * X^0 = 0 * X^0",
	"0 * X^0 = 0 * X^0",
	"0 * X^1 = 0 * X^0",
	"0 * X^1 = 0",
	"0 * X^2 = 0 * X^0",
	"0 * X^3 = 0 * X^2",
	"42 * X0 = 42 * X0",
	"21 * X0 = -21 * X0",
]

deg_1 = [
	"5 * X^0 = 4 * X^0 + 7 * X^1",
	"1 * X^1 = 10",
	"5 * X^0 + 4 * X^1 = 4 * X^0"
]

deg_2_neg = [
	"5 * X^0 + 3 * X^1 + 3 * X^2 = 1 * X^0 + 0 * X^1",
	"1 * X^0 + 1 * X^1 + 1 * X^2 = 0 * X^0",
	"1 * X^0 + 10 * X^2 + 1 * X^1 - 1 * X^2 = 0 * X^0 - 5 * X^2",
]

deg_2_nul = [
	"6 * X^0 + 11 * X^1 + 5 * X^2 = 1 * X^0 + 1 * X^1",
	"1 * X^0 + 2 * X^1 + 1 * X^2 = 0 * X^0",
]

deg_2_pos = [
	"5 * X^0 + 13 * X^1 + 3 * X^2 = 1 * X^0 + 1 * X^1",
	"5 * X^0 + 4 * X^1 - 9.3 * X^2 = 1 * X^0",
]

deg_3 = [
	"8 * X^0 - 6 * X^1 + 0 * X^2 - 5.6 * X^3 = 3 * X^0"
]

bad = ["shit",
	"sh=it",
	"1 * x^1 = 0",
	"1 * x^1 +- 1 * x^1 = 0",
	"1 * X^a = 0",
	"e * X^a = 0",
]

def test_sol(pol):
	a, b, c, = pol.coefs()
	mine = pol.sol
	them = PolGraph(a, b, c).root.tolist()
	err = False
	if mine == None or them == None:
		if mine != None or them != None:
			err = True
	else:
		if len(mine) != len(them):
			err = True
		precision = 5
		for me, np in zip(mine, them):
			if np.imag != None:
				if round(me.real, precision) != round(np.real, precision):
					err = True
					print("me: ", me.real)
					print("np: ", np.real)
				if round(me.imag, precision) != round(np.imag, precision):
					err = True
					print("me: ", me.imag)
					print("np: ", np.imag)

			elif round(me, precision) != round(np, precision):
				err = True
				print("me: ", me)
				print("np: ", np)
	if err:
		print("mine: ", mine)
		print("them: ", them)
		print(RED   + "FAILURE" + RESET)
	else:
		print(GREEN + "SUCCESS" + RESET)

def debug(exemples, cmp=False):
	for ex in exemples:
		print("python3 ", sys.argv[0] + " \"" + ex + "\"")
		pol = ComputorV1(ex).pol
		if pol and cmp:
			test_sol(pol)
		print()

if __name__ == "__main__":
	eqs = [deg_0, deg_1, deg_2_neg, deg_2_nul, deg_2_pos, deg_3]
	for eq in eqs:
		debug(eq, cmp=True)
	debug(bad)
