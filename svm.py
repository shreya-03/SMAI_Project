import numpy as np
from numpy import linalg
import cvxopt
import cvxopt.solvers
import csv,sys
from sklearn.metrics import accuracy_score,precision_score,recall_score,f1_score

def linear_kernel(x1, x2):
	return np.inner(x1, x2)

def polynomial_kernel(x, y, p=3):
	return (1 + np.dot(x, y)) ** p

def gaussian_kernel(x, y, gamma=0.0001):
	return np.exp(-gamma*(linalg.norm(x-y)**2))

class SVM(object):

	def __init__(self, kernel, C):
		self.kernel = kernel
		self.C = C
		if self.C is not None: self.C = float(self.C)

	def fit(self, X, y):
		X=np.array(X)
		y=np.array(y)
		n_samples, n_features = X.shape

		# Gram matrix
		K = np.zeros((n_samples, n_samples))
		for i in range(n_samples):
			for j in range(n_samples):
#					print type(X[i])
				K[i,j] = self.kernel(X[i], X[j])

#		P = cvxopt.matrix(np.outer(y,y) * K)
#		q = cvxopt.matrix(np.ones(n_samples) * -1)
#		A = cvxopt.matrix(y, (1,n_samples))
#		b = cvxopt.matrix(0.0)

#		if self.C is None:
#			G = cvxopt.matrix(np.diag(np.ones(n_samples) * -1))
#			h = cvxopt.matrix(np.zeros(n_samples))
#		else:
#			tmp1 = np.diag(np.ones(n_samples) * -1)
#			tmp2 = np.identity(n_samples)
#			G = cvxopt.matrix(np.vstack((tmp1, tmp2)))
#			tmp1 = np.zeros(n_samples)
#			tmp2 = np.ones(n_samples) * self.C
#			h = cvxopt.matrix(np.hstack((tmp1, tmp2)))

		# solve QP problem
#		solution = cvxopt.solvers.qp(P, q, G, h, A, b)

		# Lagrange multipliers
		P = cvxopt.matrix(np.outer(y, y) * K)
		q = cvxopt.matrix(-1 * np.ones(n_samples))

		# -a_i \leq 0
		# TODO(tulloch) - modify G, h so that we have a soft-margin classifier
		G_std = cvxopt.matrix(np.diag(np.ones(n_samples) * -1))
		h_std = cvxopt.matrix(np.zeros(n_samples))

		# a_i \leq c
		G_slack = cvxopt.matrix(np.diag(np.ones(n_samples)))
		h_slack = cvxopt.matrix(np.ones(n_samples) * self.C)

		G = cvxopt.matrix(np.vstack((G_std, G_slack)))
		h = cvxopt.matrix(np.vstack((h_std, h_slack)))

		A = cvxopt.matrix(y, (1, n_samples))
		b = cvxopt.matrix(0.0)

		solution = cvxopt.solvers.qp(P, q, G, h, A, b)
		a = np.ravel(solution['x'])

		# Support vectors have non zero lagrange multipliers
		sv = a > 1e-5
		ind = np.arange(len(a))[sv]
		self.a = a[sv]
		self.sv = X[sv]
		self.sv_y = y[sv]
		print "%d support vectors out of %d points" % (len(self.a), n_samples)

		# Intercept
		self.b = 0
		for n in range(len(self.a)):
			self.b += self.sv_y[n]
			self.b -= np.sum(self.a * self.sv_y * K[ind[n],sv])
		self.b /= len(self.a)

		# Weight vector
		if self.kernel == linear_kernel:
			self.w = np.zeros(n_features)
			for n in range(len(self.a)):
				self.w += self.a[n] * self.sv_y[n] * self.sv[n]
		else:
			self.w = None

	def project(self, X):
		if self.w is not None:
			return np.dot(X, self.w) + self.b
		else:
			y_predict = np.zeros(len(X))
			for i in range(len(X)):
				s = 0
				for a, sv_y, sv in zip(self.a, self.sv_y, self.sv):
					s += a * sv_y * self.kernel(X[i], sv)
				y_predict[i] = s
			return y_predict + self.b

	def predict(self, X):
		return np.sign(self.project(X))

if __name__ == "__main__":
	f=open(sys.argv[1],'rU')
	T1=csv.reader(f)
	features=[]
	labels=[]
	for data in T1:
		features.append([np.float64(data[i]) for i in range(1,23)])
		labels.append([np.float64(data[0])])
	features=np.array(features)
	labels=np.array(labels)
	print type(features)
	valid_f=open(sys.argv[2],'rU')
	T2=csv.reader(valid_f)
	test_features=[]
	test_labels=[]
	for data in T2:
		test_features.append([np.float64(data[i]) for i in range(1,23)])
		test_labels.append(np.float64(data[0]))
	test_features=np.array(test_features)
	test_labels=np.array(test_labels)
	clf = SVM(linear_kernel,2.0)
	clf.fit(features,labels)
	y_predict = clf.predict(test_features)
#	for label in test_labels:
#		print type(label)
	correct = np.sum(y_predict == test_labels)
	print "%d out of %d predictions correct" % (correct, len(y_predict))
	print 'Accuracy :',accuracy_score(test_labels,y_predict,normalize=True)
	print 'Precision:', precision_score(test_labels,y_predict,average='weighted')
	print 'Recall:', recall_score(test_labels,y_predict,average='weighted')
	print 'F1 score:', f1_score(test_labels,y_predict,average='weighted')
