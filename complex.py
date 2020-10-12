def plot_3d(a , b, c):
	from mpl_toolkits import mplot3d
	import numpy as np
	import matplotlib.pyplot as plt

	def quad_imag(x, y):
		obj = a * (x + (y * 1j)) ** 2 + b * (x + (y * 1j)) + c
		# print(obj)
		return obj.real

	def quad(x):
		obj = a * (x) ** 2 + b * (x) + c
		return obj

	root = np.roots([a, b, c])
	print("Root: ", root)
	x = np.linspace(root.real.min() - 10, root.real.max() + 10, 25)
	y = np.linspace(root.imag.min() - 10, root.imag.max() + 10, 25)

	X, Y = np.meshgrid(x, y)

	fig = plt.figure()
	if root.imag.any():
		Z = quad_imag(X, Y)
		ax = plt.axes(projection='3d')
		xl = root.real
		xl = np.linspace(xl[0], xl[1], 25)
		yl = root.imag
		yl = np.linspace(yl[0] - 10, yl[1] + 10, 25)
		zl = xl
		ax.plot(xl, yl, zl, c='g')
		ax.plot(x, np.linspace(0, 0, 25), quad_imag(x, np.linspace(0, 0, 25)), c='k')
		ax.scatter(root.real, root.imag, quad_imag(root.real, root.imag), c='r', marker='o')
		ax.plot_wireframe(X, Y, Z, color='cyan', alpha=0.5)
		ax.set_xlabel('X Real part')
		ax.set_ylabel('X Imag part')
		ax.set_zlabel("f(X) (real part)")
	else:
		Z = quad(x)
		ax = plt.axes()
		ax.plot(x, Z)
		yl = np.linspace(0, 0, 25)
		ax.plot(x, yl, c='g')
		y_ = np.zeros(root.shape)
		# print(y_)
		ax.scatter(root, y_, c='r', marker='o')
		ax.set_xlabel('X')
		ax.set_ylabel("f(X)")

	ax.set_title(str(a)+"x² + " + str(b)+"x + "+ str(c))
	plt.show()

if __name__ == "__main__":
	plot_3d(-9.3, 4, 4)#double
	plot_3d(1, 2, 1)#lonely
	plot_3d(1, 1, 1)#complex
