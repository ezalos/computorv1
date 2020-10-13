from mpl_toolkits import mplot3d
import numpy as np
import matplotlib.pyplot as plt

class PolGraph():
	def __init__(self, a , b, c, name=""):
		self.root = np.roots([a, b, c])
		self.a = a
		self.b = b
		self.c = c
		self.imag_sol = True if self.root.imag.any() else False
		if len(name):
			self.name = name
		else:
			self.name = str(a)+"x² + " + str(b)+"x + "+ str(c)
		# print("Root: ", self.root)

	def plot(self):
		if len(self.root) == 0:
			self.plot_1d()
		elif self.imag_sol:
			self.plot_3d()
		else:
			self.plot_2d()

	def plot_1d(self, points=25, ctx=5):
		def quad(x):
			obj = self.a * (x) ** 2 + self.b * (x) + self.c
			return obj

		x = np.linspace(-ctx, ctx, points)

		fig = plt.figure()
		ax = plt.axes()

		# Graph Equation
		ax.plot(x, quad(x), label="f(x)=" + self.name)

		# Graph F(x)=0
		ax.plot(x, np.linspace(0, 0, points), c='g', label="f(x)=0")

		ax.set_xlabel('x')
		ax.set_ylabel("f(x)")

		ax.set_title("Solution(s) for " + self.name)
		plt.legend(loc='best')
		plt.show()

	def plot_2d(self, points=25, ctx=5):
		def quad(x):
			obj = self.a * (x) ** 2 + self.b * (x) + self.c
			return obj

		x = np.linspace(self.root.min() - ctx, self.root.max() + ctx, points)

		fig = plt.figure()
		ax = plt.axes()

		# Graph Equation
		ax.plot(x, quad(x), label="f(x)=" + self.name)

		# Graph F(x)=0
		ax.plot(x, np.linspace(0, 0, points), c='g', label="f(x)=0")

		# Graph solutions point(s)
		y = np.zeros(self.root.shape)
		ax.scatter(self.root, y, c='r', marker='o', label="Solution(s)")

		ax.set_xlabel('x')
		ax.set_ylabel("f(x)")

		ax.set_title("Solution(s) for " + self.name)
		plt.legend(loc='best')
		plt.show()


	def plot_3d(self, points=25, ctx=5):

		def quad_imag(x, y):
			obj = self.a * (x + (y * 1j)) ** 2 + self.b * (x + (y * 1j)) + self.c
			return obj.real

		x = np.linspace(self.root.real.min() - ctx,
						self.root.real.max() + ctx, points)
		y = np.linspace(self.root.imag.min() - ctx,
		self.root.imag.max() + ctx, points)

		fig = plt.figure()
		ax = plt.axes(projection='3d')

		# Graph Equation
		x_axe, y_axe = np.meshgrid(x, y)
		z_axe = quad_imag(x_axe, y_axe)
		ax.plot_wireframe(x_axe, y_axe, z_axe,
						color='cyan', alpha=0.5, label="f(x)=" + self.name)

		# Graph F(x)=0
		if False:
			x_axe = np.linspace(self.root.real[0], self.root.real[1], points)
			y_axe = np.linspace(self.root.imag[0] - ctx, self.root.imag[1] + ctx,
								points)
			z_axe = np.linspace(0, 0, points)
			ax.plot(x_axe, y_axe, z_axe, c='g', label="" )

		# Graph F(x,y=0).i == 0
		y_axe = np.linspace(0, 0, points)
		z_axe = quad_imag(x, np.linspace(0, 0, points))
		ax.plot(x, y_axe, z_axe, c='b', label="Real part of " + self.name)

		# Graph solutions point(s)
		y_axe = self.root.imag
		z_axe = quad_imag(self.root.real, self.root.imag)
		ax.scatter(self.root.real, self.root.imag, z_axe,
					c='r', marker='o', label="Solutions")


		ax.set_xlabel('X Real part')
		ax.set_ylabel('X Imag part')
		ax.set_zlabel("f(X) (real part)")
		ax.set_title("Solution(s) for " + self.name)
		plt.legend(loc='best')
		plt.show()

if __name__ == "__main__":
	PolGraph(-9.3, 4, 4).plot()#double
	PolGraph(1, 2, 1).plot()#lonely
	PolGraph(1, 1, 1).plot()#complex
