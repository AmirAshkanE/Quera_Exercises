init_inputs = input().split()
n, x, k = int(init_inputs[0]), int(init_inputs[1]), int(init_inputs[2])

a = 0
ch_list = []
while a < n:
    ch_list.append(input())
    a += 1

i = x
b = 0
ch = ""
while b < k:
    ch = ch_list[i-1]
    i += 1
    if i == n:
        i = 1
    b += 1

print(ch)
# 2 run time errors at 2 tests, gotta figure out what they are