import sys
from computorv1 import ComputorV1

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

def debug(exemples):
	for ex in exemples:
		print(sys.argv[0] + " \"" + ex + "\"")
		ComputorV1(ex)
		print()

if __name__ == "__main__":
	debug(eq)
	debug(bad)
