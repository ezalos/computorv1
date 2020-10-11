def plot_3d(a , b, c):
	from mpl_toolkits import mplot3d
	import numpy as np
	import matplotlib.pyplot as plt

	def quad_imag(x, y):
		obj = a * (x + (y * 1j)) ** 2 + b * (x + (y * 1j)) + c
		return obj

	def quad(x):
		obj = a * (x) ** 2 + b * (x) + c
		return obj
		
	root = np.roots([a, b, c])
	print(root)
	x = np.linspace(root.real.min() - 10, root.real.max() + 10, 25)
	y = np.linspace(root.imag.min() - 10, root.imag.max() + 10, 25)

	X, Y = np.meshgrid(x, y)
	if root.imag.any():
		Z = quad_imag(X, Y)
	else:
		Z = quad(x)

	fig = plt.figure()
	if root.imag.any():
		ax = plt.axes(projection='3d')
	else:
		ax = plt.axes()
	if root.imag.any():
		ax.plot_wireframe(X, Y, Z, color='blue')
	else:
		ax.plot(x, Z)
	if root.imag.any():
		ax.scatter(root.real, root.imag, np.ndarray(root.shape), c='r', marker='o')
	else:
		ax.scatter(root, np.ndarray(root.shape), c='r', marker='o')

	if root.imag.any():
		ax.set_xlabel('X Real part')
		ax.set_ylabel('X Imag part')
		ax.set_zlabel("f(X)")
	else:
		ax.set_xlabel('X')
		ax.set_ylabel("f(X)")
	ax.set_title(str(a)+"x² + " + str(b)+"x + "+ str(c))
	plt.show()

plot_3d(-9.3, 4, 4)#double
plot_3d(1, 2, 1)#lonely
plot_3d(1, 1, 1)#complex
