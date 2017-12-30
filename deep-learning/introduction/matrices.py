import numpy as np

values = [1, 2, 3, 4, 5]
for i in range(len(values)):
    values[i] += 5

print(values)

values = [1, 2, 3, 4, 5]
values = np.array(values) + 5

print(values)

a = np.array([[1, 3], [5, 7]])
print(a)

b = np.array([[2, 4], [6, 8]])
print(b)

c = a + b
print(c)

m = np.array([[1, 2, 3], [4, 5, 6]])
print(m)

n = m * 0.25
print(n)

p = m * n
print(p)

multi = np.multiply(m, n)
print(multi)

f = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
print(f)

g = b = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]])
print(g)
print(g.shape)

h = np.matmul(f, g)
print(h)
print(h.shape)

m = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
print(m)
print(m.shape)

m_t = m.T
print(m_t)
print(m_t.shape)
