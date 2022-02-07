# 1
A = int(input())
B = input()

print(A * int(B[2]))
print(A * int(B[1]))
print(A * int(B[0]))
print(A * int(B))

# 2
A = int(input())
b1, b2, b3 = [i for i in input()]

print(A * int(b3))
print(A * int(b2))
print(A * int(b1))
print(A * int(b1 + b2 + b3))

# 3
A = int(input())
b1, b2, b3 = [int(i) for i in input()]

print(A * b3)
print(A * b2)
print(A * b1)
print(A * (100 * b1 + 10 * b2 + b3))
