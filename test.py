import sys
from computorv1 import ComputorV1

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

def debug(exemples):
	for ex in exemples:
		print("python3 ", sys.argv[0] + " \"" + ex + "\"")
		ComputorV1(ex)
		print()

if __name__ == "__main__":
	eqs = [deg_0, deg_1, deg_2_neg, deg_2_nul, deg_2_pos, deg_3]
	for eq in eqs:
		debug(eq)
	debug(bad)
