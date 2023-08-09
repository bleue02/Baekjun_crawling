import numpy as np
import matplotlib.pylab as plt

# def step_function(x):
#     return np.array(x > 0, dtype=int)
#
# x = np.arange(-5.0, 5.0, 0.1)
# y = step_function(x)
#
# plt.plot(x,y)
# plt.ylim(-0.1, 1.1) # Y축의 범위 지정
# plt.plot(x,y, color='blue',  linestyle = "--")
# plt.title('Step Function')
# plt.show()

# def sig(x):
#  return 1/(1 + np.exp(-x))
#
# x = np.linspace(-10, 10, 50)
# p = sig(x)
# plt.xlabel("x")
# plt.ylabel("Sigmoid(x)")
# plt.plot(x, p)
# plt.show()


# def ReLU(x):
#     return np.maximum(0, x)
#
#
# x = np.array([-1.0, 1.0, 2.0])
# print(ReLU(x))
#
# x = np.arange(-5.0, 5.0, 0.1)
# y = ReLU(x)
# plt.plot(x, y)
# plt.ylim(-0.1, 5.1)
# plt.title('ReLu function')
# plt.show()


# 2차원 배열을 만들어 nidm 사용.
A = np.array([[1,2,3,4], [5,6,7,8]])
print('A = \n', A)
print('\n')
print('Shape of A = ',A.shape)
print('\n')
print('차원의 수 = ',A.ndim) # (2,4)


