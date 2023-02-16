i = 0
nums = []
while i < 4:
    inp = input().split()
    nums.append(inp)
    i += 1
int_nums = []

for i in nums:
    for j in i:
        j = int(j)
        int_nums.append(j)
a, b, c = int_nums[0], int_nums[1], int_nums[2]
fa, sa, sh = int_nums[3:5], int_nums[5:7], int_nums[7:]

t = 1
count_1 = 0
count_2 = 0
count_3 = 0
while t < max(int_nums[3:]):
    if t in range(fa[0], fa[1]) and t in range(sa[0], sa[1]) and t in range(sh[0], sh[1]):
        count_3 += 1
    elif (t in range(fa[0], fa[1]) and t in range(sa[0], sa[1])) or (t in range(fa[0], fa[1]) and t in range(sh[0], sh[1])) or (t in range(fa[0], fa[1]) and t in range(sa[0], sa[1])) :
        count_2+=1
    elif t not in range(fa[0], fa[1]) and t not in range(sa[0], sa[1]) and t not in range(sh[0], sh[1]): 
        pass
    else:
        count_1+=1
    t += 1


s = (1*count_1*a)+(2*count_2*b)+(3*count_3*c)
print(s)

#CHECK LATER 2 failed tests