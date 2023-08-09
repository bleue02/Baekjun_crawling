import numpy as np

print('---AND GATE---')
def AND(x1, x2):
    w1, w2, theta = 0.5, 0.5, 0.7 # w1 = 0.5, w2 = 0.5, theta = 0.7
    tmp = x1 * w1 + x2 * w2 # 1.0
    if tmp <= theta:
        return 0
    elif tmp > theta:
        return 1

output_1 = AND(0,0)
output_2 = AND(1,0)
output_3 = AND(0,1)
output_4 = AND(1,1)
print('AND(0,0) = ',output_1)
print('AND(1,0) = ',output_2)
print('AND(0,1) = ',output_3)
print('AND(1,1) = ',output_4)

print('\n')

print('---Weight Bias "AND" Gate---')
def AND_2(x1,x2):
    x = np.array([x1, x2])
    w = np.array([0.5,0.5])
    b = 0.7
    tmp = np.sum(w * x) + b
    if tmp <= 0:
        return 0
    else:
        return 1
output_bias_1 = AND_2(0,0)
output_bias_2 = AND_2(1,0)
output_bias_3 = AND_2(0,1)
output_bias_4 = AND_2(1,1)
print('Bias AND(0,0) = ', output_bias_1)
print('Bias AND(1,0) = ', output_bias_2)
print('Bias AND(0,1) = ', output_bias_3)
print('Bias AND(1,1) = ', output_bias_4)

print( '\n')

print('---NAND Gate---')
def NAND(x1, x2):
    x = np.array([x1, x2])
    w = np.array([-0.5, -0.5])
    b = 0.7
    tmp = np.sum(w * x) + b
    if tmp <= 0:
        return 0
    else:
        return 1

output_NAND_1 = NAND(0,0)
output_NAND_2 = NAND(1,0)
output_NAND_3 = NAND(0,1)
output_NAND_4 = NAND(1,1)
print('NAND(0,0) = ', output_NAND_1)
print('NAND(1,0) = ', output_NAND_2)
print('NAND(0,1) = ', output_NAND_3)
print('NAND(1,1) = ', output_NAND_4)

print('\n')

print('---OR Gate---')
def OR(x1, x2):
    x = np.array([x1, x2])
    w = np.array([0.5, 0.5])
    b = -0.2 # Bias
    tmp  = np.sum(w * x) + b
    if tmp <= 0:
        return 0
    else:
        return 1
output_OR_1 = OR(0,0)
output_OR_2 = OR(1,0)
output_OR_3 = OR(0,1)
output_OR_4 = OR(1,1)
print('OR(0,0) = ', output_OR_1)
print('OR(1,0) = ', output_OR_1)
print('OR(0,1) = ', output_OR_1)
print('OR(1,1) = ', output_OR_1)

print('\n')

print('---XOR GATE---')
def XOR(x1,x2):
    s1 = NAND(x1,x2)
    s2 = OR(x1, x2)
    y = AND(s1, s2)
    return y

output_XOR_1 = XOR(0,0)
output_XOR_2 = XOR(1,0)
output_XOR_3 = XOR(0,1)
output_XOR_4 = XOR(1,1)

print('XOR(0,0) = ', output_XOR_2)
print('XOR(1,0) = ', output_XOR_1)
print('XOR(0,1) = ', output_XOR_3)
print('XOR(1,1) = ', output_XOR_4)


y = np.array([-1.0, 1.0, 2.0])
y = y.astype(int) # Change to int dtype
print(y)









