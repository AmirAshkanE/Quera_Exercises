number_input = input().split()
r, c = int(number_input[0]), int(number_input[1])
direction=""
a_count = 0
b_count = 0

for a in range(10,r-1,-1):
    a_count+=1

if c >10 :
    c=21-c
    direction="Left"
    print(direction,a_count,c)
elif c < 10:
    direction = "Right"
    print(direction,a_count,c)
else:
    c=0
    print(a_count,c)
    
