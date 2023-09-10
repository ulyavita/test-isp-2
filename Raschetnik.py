import time
a = list(input())
b = int(input())

start_t = time.time()
for i in range(len(a) - 1, - 1, - 1):
    a[i] = int(a[i]) * b
for i in range(len(a) - 1, 0, - 1):
    if a[i] > 9:
        a[i - 1] = a[i - 1] + a[i] // 10
        a[i] = a[i] % 10

print(*a, sep="")
print("Время", time.time() - start_t)

<<<<<<< HEAD
\\for commit test0
\\for commit test
=======

\\for commit test
\\for commit test1
>>>>>>> vita_1
