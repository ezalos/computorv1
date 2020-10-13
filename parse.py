import re
from polynomial_class import PolynomialTerm

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

def update_eq_dic(eq_dic, pol_dic, right=False):
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
	elem = PolynomialTerm(a, n, a_len)
	if n in eq_dic:
		eq_dic[n] = eq_dic[n] + elem
	else:
		eq_dic[n] = elem
	return eq_dic


def parse_equation(str):
	eq_dic = {}
	if '=' in str:
		str = str.split('=')
		regex = re.compile(polynomial_elem_pattern)
		for pol_el in regex.finditer(str[0]):
			pol_dic = pol_el.groupdict()
			eq_dic = update_eq_dic(eq_dic, pol_dic, right=False)
		for pol_el in regex.finditer(str[1]):
			pol_dic = pol_el.groupdict()
			eq_dic = update_eq_dic(eq_dic, pol_dic, right=True)

	equation = list(eq_dic.values())
	equation.sort(key=lambda x: x.n)
	return equation
